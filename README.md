# RoboGame

<p align="center">
	<img src="images/robot.jpg" width="250" height="250">
</p>

## Overview

RoboGame is a RC robot that can be controlled via Bluetooth on the Raspberry Pi 3 Model B. It uses computer vision to detect if the object that the user has chosen is detected. 

## Webpage

Website is used for object selection. Users have to open the website and choose the object that they want to find. Once the obeject is selected, `app.py` calls object detection algorithm script, `TFLite_detection_webcam.py`, and reads the outputs from the script. Once `app.py` receives the selected object's name and its confidence level higher than 0.60, it will exit the object detection script and redirects to the `success.html`. If `app.py` does not receive the name of the selected obeject (if object detection fails) within 10 seconds, it will redirect to the `fail.html` and gives users an option to try again.

## Robot Movement

### Hardware Used

#### Parts List
* Robot chassis
* Raspberry pi 3b
* Pi camera
* Dual H-bridge motor driver (tb6612fng)
* DC motors (x4)
* Wheel (x4)
* Battery pack
* AAA batteries (x4)
* DC barrel power jack
* Portable rechargeable battery

#### Dual TB6612FNG Motor Driver Pinout Table

| H-bridge Motor Driver  | External Hardware                        | Raspberry Pi 3b  | 
| ---------------------- | ---------------------------------------- |----------------- | 
| VM                     | 6 V battery pack power                   |                  |
| VCC                    |                                          | 5 V              |
| GND                    | Battery pack ground                      |                  |
| A01                    | Front & rear right DC motor, black wire  |                  |
| A02                    | Front & rear right DC motor, red wire    |                  |
| B02                    | Front & rear left DC motor, red wire     |                  |
| B01                    | Front & rear left DC motor, black wire   |                  |
| PWMB                   |                                          | 19               |
| B12                    |                                          | 26               |
| B11                    |                                          | 21               |
| STBY                   | 6 V battery pack power                   |                  |
| A11                    |                                          | 5                |
| A12                    |                                          | 6                |
| PWMA                   |                                          | 13               |

	 	

### Bluetooth Control

The robot is controlled via Bluetooth using an app called Blue Dot - created by Martin O'Hanlon. Blue Dot allows you to control the Raspberry Pi as a "bluetooth remote" by using a simple Python library. The motion of the robot uses an intuitive approach by having the user select top, bottom, left, or right on the blue dot located at the center of the app to move the robot in its respective direction.

The user will first need to correctly set up their phone. They must install the Blue Dot app on their phone, enable Bluetooth, and then connect to the same Wifi used by the Raspberry Pi. Next, the Blue Dot python program can be run. The user will pair their phone with the raspberry pi and connect to it by clicking its icon on the main menu. Shortly after, the big blue dot will appear on their phone to direct the motion of the robot. 

BlueDot Getting Started: https://bluedot.readthedocs.io/en/latest/gettingstarted.html \
BlueDot API Documentation: https://bluedot.readthedocs.io/en/latest/dotapi.html

<p align="center">
	<img src="images/Screenshot_20211214-010031.jpg" width="200" height="300">
</p>

## Computer Vision

Object detection is implemented using open source pre-trained TensorFlow model. The program outputs detected objects with confidence levels.

Run `python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model` to test out objection detection algorithm.

## End Results
Demo Video: https://www.youtube.com/watch?v=3Jn7gxrN-L0
