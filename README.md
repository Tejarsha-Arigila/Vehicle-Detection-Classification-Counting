# Vehicle Detection, Classification and Counting using OpenCV

## Table of Contents
1. [Repository Contents](#repository-contents)
2. [Usage](#usage)
3. [Features](#features)
4. [Configuration Parameters](#configurations-parameters)

## Repository Contents:

1. `main.py`: Main script for running the vehicle counter.
2. `utils.py`: Utility functions and classes aiding in vehicle detection and counting.
3. `config.py`: Stores parameters like model paths, video input, font settings, and thresholds.

## Usage:

1. Clone this repository.
2. Install the necessary libraries using the `requirements.txt` file.

   ```shell 
   pip install -r requirements.txt
   ```

3. Configure video path and other parameters in `config.py` file.
4. Run the `main.py` script:

   ```shell
   python main.py
   ```

5. In the opened window, double-click to set the counting line's position. The script will then count and display vehicles crossing the line in real-time.

## Features:

- Real-time vehicle detection using the **YOLOv4 model**.
- Euclidean distance-based vehicle tracking.
- Interactive counting line positioning with a mouse double-click.
- **Non-Max Suppression (NMS)** for reducing bounding box overlaps.
- Displays categorized vehicle counts: Car, Motorbike, Bus, Truck.

## Configurations Parameters:

- `VIDEO_PATH`: Path to the video file.
- `INPUT_SIZE`: Input size for the YOLO model.
- `CONFIDENCE_THRESHOLD`: Confidence threshold for YOLO detection.
- `NMS_THRESHOLD`: Non-max suppression threshold.
- `FONT_COLOR`, `FONT_SIZE`, `FONT_THICKNESS`: Font settings for the displayed text.
- `CLASSES_FILE`: Path to the classes file for YOLO.
- `REQUIRED_CLASS_INDEX`: Index of required classes from the classes file.
- `MODEL_CONFIG`: Path to the YOLO configuration file.
- `MODEL_WEIGHTS`: Path to the YOLO weights file.

> Adjust these parameters in 'config.py' as per need.   
