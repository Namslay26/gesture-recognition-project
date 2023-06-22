# Gesture Recognition and Device Control
This project aims to enable gesture recognition using OpenCV and Mediapipe, allowing users to control devices through various hand gestures. The project merges different functionalities such as taking screenshots, point-and-click interaction, and volume control into a single Python script.

## Features
* Gesture recognition using mediapipe and OpenCV.
* Simultaneous recognition of multiple gestures.
* Device control actions:
  *Screenshot capture.
  * Point and click interaction.
  * Volume control.
  * Brightness Control.
  * Scroll Feature

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/Namslay26/gesture-recognition-project.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open the terminal and navigate to the project directory.
2. Run the functionality that you would like to perform. For example,
   ```bash
   python VolumeControl.py
   ```
3. The script will initialize the camera and start capturing frames.
4. Perform various hand gestures in front of the camera to control the devices.

## Project Structure 
.
    ├── BrightnessControl.py                  # File handling Brightness Control
    ├── HandTrackingModule.py                   # File responsible for Hand Detection and tracking 
    ├── MouseControl.py                     # File handling Mouse control functions like pointing and clicking. 
    ├── VolumeControl.py                   # File handling Volume control functions
    ├── screenShot.py                   # File handling screenshot functions 
    ├── scrollFeature.py                   # File handling scroll feature functionality
    └── hands.jpg                         # A picture of a hand to test out the hand detection facility

## Contributing 
Contributions to this project are welcome! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request.

