# Vehicle Detection, Classification and Counting using OpenCV

## Table of Contents
1. [Files in the Repository](#files-in-the-repository)
2. [How to Use](#how-to-use)
3. [Features](#features)
4. [Configurations](#configurations)

## Files in the Repository:

1. `main.py`: The primary script to run the vehicle counter.
2. `utils.py`: Contains utility functions and classes that help in the vehicle detection and counting process.
3. `config.py`: Configuration file that houses parameters such as paths to models, video input, font settings, and thresholds.

## How to Run:

1. Clone this repository.
2. Install the necessary libraries using the `requirements.txt` file.

```shell pip install -r requirements.txt```

3. Set your video path and other configurations in the `config.py` file.
4. Run the `main.py` script:

   ```shell python main.py```

5. In the displayed window, double-click to set the position of the middle line. The script will count the vehicles crossing the set lines and display the count in real-time.

## Features:

- Real-time vehicle detection using the **YOLOv4 model**.
- Uses the Euclidean distance to track vehicles.
- Ability to set the counting line's position with a double click.
- **Non-Max Suppression (NMS)** to ensure accurate detection by reducing overlapping bounding boxes.
- Displays vehicle counts categorized as Car, Motorbike, Bus, and Truck.

## Configurations:

- `VIDEO_PATH`: Path to the video file.
- `INPUT_SIZE`: Input size for the YOLO model.
- `CONFIDENCE_THRESHOLD`: Confidence threshold for YOLO detection.
- `NMS_THRESHOLD`: Non-max suppression threshold.
- `FONT_COLOR`, `FONT_SIZE`, `FONT_THICKNESS`: Font settings for the displayed text.
- `CLASSES_FILE`: Path to the classes file for YOLO.
- `REQUIRED_CLASS_INDEX`: Index of required classes from the classes file.
- `MODEL_CONFIG`: Path to the YOLO configuration file.
- `MODEL_WEIGHTS`: Path to the YOLO weights file.

Make sure to configure these appropriately in the `config.py` file to suit your requirements.   
