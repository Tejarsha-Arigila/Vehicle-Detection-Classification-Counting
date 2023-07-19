import cv2
import numpy as np
import config
from utils import EuclideanDistTracker, postProcess, count_vehicle

class VehicleCounter:
    def __init__(self):
        self.tracker = EuclideanDistTracker()
        self.cap = cv2.VideoCapture(config.VIDEO_PATH)
        self.input_size = config.INPUT_SIZE
        self.confThreshold = config.CONFIDENCE_THRESHOLD
        self.nmsThreshold = config.NMS_THRESHOLD
        self.font_color = config.FONT_COLOR
        self.font_size = config.FONT_SIZE
        self.font_thickness = config.FONT_THICKNESS
        self.middle_line_position = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2
        self.up_line_position = self.middle_line_position - 30
        self.down_line_position = self.middle_line_position + 30
        self.is_double_clicked = False
        self.classNames = open(config.CLASSES_FILE).read().strip().split('\n')
        self.required_class_index = config.REQUIRED_CLASS_INDEX
        modelConfiguration = config.MODEL_CONFIG
        modelWeigheights = config.MODEL_WEIGHTS
        self.net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeigheights)
        np.random.seed(42)
        self.colors = np.random.randint(0, 255, size=(len(self.classNames), 3), dtype='uint8')
        self.temp_up_list = []
        self.temp_down_list = []
        self.up_list = [0, 0, 0, 0]
        self.down_list = [0, 0, 0, 0]
        cv2.namedWindow("Output")
        cv2.setMouseCallback("Output", self.set_line_position)

    def set_line_position(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            self.middle_line_position = y   
            self.up_line_position = self.middle_line_position - 15
            self.down_line_position = self.middle_line_position + 15
            self.is_double_clicked = True
            self.down_list = [0, 0, 0, 0]

    def realTime(self):
        while True:
            success, img = self.cap.read()
            img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
            ih, iw, channels = img.shape
            blob = cv2.dnn.blobFromImage(img, 1 / 255, (self.input_size, self.input_size), [0, 0, 0], 1, crop=False)

            self.net.setInput(blob)
            layersNames = self.net.getLayerNames()
            outputNames = [(layersNames[i[0] - 1]) for i in self.net.getUnconnectedOutLayers()]

            outputs = self.net.forward(outputNames)
            postProcess(outputs, img, self.colors, self.classNames, self.confThreshold, self.nmsThreshold,
                        self.required_class_index, self.tracker, self.up_list, self.down_list, self.up_line_position,
                        self.middle_line_position, self.down_line_position, self.temp_up_list, self.temp_down_list,
                        self.is_double_clicked, self.font_color, self.font_size, self.font_thickness)

            if self.is_double_clicked:
                cv2.line(img, (0, self.up_line_position), (iw, self.up_line_position), (0, 0, 255), 1)
                cv2.line(img, (0, self.middle_line_position), (iw, self.middle_line_position), (255, 255, 255), 2)
                cv2.line(img, (0, self.down_line_position), (iw, self.down_line_position), (0, 0, 255), 1)

                cv2.putText(img, "Up", (110, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(img, "Down", (160, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(img, "Car:        " + str(self.up_list[0]) + "     " + str(self.down_list[0]), (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(img, "Motorbike:  " + str(self.up_list[1]) + "     " + str(self.down_list[1]), (20, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(img, "Bus:        " + str(self.up_list[2]) + "     " + str(self.down_list[2]), (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(img, "Truck:      " + str(self.up_list[3]) + "     " + str(self.down_list[3]), (20, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            cv2.imshow('Output', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    vc = VehicleCounter()
    vc.realTime()
