# 🚗 Vehicle Detection, Classification, and Counting using OpenCV

📌 Jump straight to:
- [Repository Contents](#repository-contents)
- [Usage](#usage)
- [Features](#features)
- [Configuration Parameters](#configurations-parameters)

---

## 📁 Repository Contents

- 📜 `main.py`: Launches the vehicle counter.
- 🛠 `utils.py`: Houses utility functions and classes for vehicle operations.
- ⚙️ `config.py`: Manages parameters such as model paths, video input, and display settings.

- 📦 `MODEL/`: (`yolov4.weights` missing in this repo - [download](https://drive.google.com/file/d/1qTdvxKKP4K9u5GJrffufSx6cpR1AmLoz/view?usp=sharing))
  - 🧠 `yolov4.cfg`: YOLO model config.
  - 🔖 `coco.names`: Recognizable classes by the model.

- 🎥 `VIDEO/`:
  - 📹 `video2.mp4`: A test sample.

---

## 🚀 Usage

1. 🔗 Clone this repository.
2. 📦 Install dependencies:

   ```shell 
   pip install -r requirements.txt
   ```
   
3. ⚙️ Adjust paths and parameters in config.py.
4. 🏃‍♂️ Execute:
   ```shell
   python main.py
   ```
5. 🖱 In the new window, double-click to position the counting line. Watch as vehicle stats get tallied in real-time!

---

## 🌟 Features
- 🕐 Real-time detection via YOLOv4.
- 📏 Uses Euclidean distance for tracking.
- 🖱 Set counting line with a double-click.
- 📦 Non-Max Suppression (NMS) to declutter overlapping boxes.
- 📊 Classifies and displays counts: Car 🚗, Motorbike 🏍, Bus 🚌, Truck 🚛.

---

## ⚙️ Configurations Parameters
- `VIDEO_PATH`: Pathway to your footage.
- `INPUT_SIZE`: YOLO model's desired input dimensions.
- `CONFIDENCE_THRESHOLD`: Desired confidence level for detections.
- `NMS_THRESHOLD`: Non-max suppression's threshold.
- `FONT_COLOR`, `FONT_SIZE`, `FONT_THICKNESS`: Style the on-screen text.
- `CLASSES_FILE`: YOLO's class definitions file path.
- `REQUIRED_CLASS_INDEX`: Indices of classes you wish to monitor.
- `MODEL_CONFIG`: YOLO's config file path.
- `MODEL_WEIGHTS`: YOLO's weight file path (download separately).

> 🛠 Tweak these in config.py to fit your scenario.
