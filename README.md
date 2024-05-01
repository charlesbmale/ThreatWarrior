# Introduction to ThreatWarrior
- Our Capstone Project, Threat Warrior, is a CNN-Based Objection Detection System implemented on a drone and leveraging a fusion of sensors to provide aerial oversight to object detection systems that are currently implemented. Threat Warrior addresses the following:​
  - A mobile and readily accessible alternative to currently available systems.
  - Utilizing a culmination of sensors to detect both a large array of objects as well as a specified object​.
  - Once detected, the system is designed to properly identify, categorize, and store the perceived object.

## :ledger: Index

- [Usage](#zap-usage)
  - [Installation](#electric_plug-installation)
  - [Commands](#package-commands)
- [Development](#wrench-development)
  - [Pre-Requisites](#notebook-pre-requisites)
  - [Developmen Environment](#nut_and_bolt-development-environment)
  - [File Structure](#file_folder-file-structure)
  - [Build](#hammer-build)  
  - [Deployment](#rocket-deployment)
- [FAQ](#question-faq)
- [Resources](#page_facing_up-resources)
- [Gallery](#camera-gallery)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

## :zap: Usage
This project is to be used in either educational or industrial settings NOT for nefarious use. Threat Warrior was designed to be leveraged for personal, ariculutral, LEO (Law Enforcement Officer), or SAR (Search and Rescue) use.

###  :electric_plug: Installation
For installation:
- You can install by either forking this project off of GitHub or downloading the ZIP.
- Once downloaded, you can pick the IDE or environment of your choice.
- Once your environment is set, make sure to import/install the following dependencies (you may have to use pip3 if using the command line):
  - import pickle
  - import cv2
  - import os
  - import numpy as np
  - import face_recognition
  - import cvzone
  - import sqlite3
  - import json
  - from datetime import datetime
  - import pygame
  - from time import sleep
  - from djitellopy import Tello,
- Once the dependencies are in order, you must load the person you are trying to detect in the "Images" folder. To properly load the person the following conditions must be met:
  - The image must be 32-bit color.
  - The image must be a 220 x 220 square PNG.
  - The image must follow the naming scheme of "00100X.PNG".
- Upon loading the images refer to the "Resources" folder for the "students_data.json" file.
- Ensure that the JSON file reflects the naming scheme of the images in the "Images" folder, as well as any other relevant or necessary information.
- Upon completion of the JSON file run the "SetupStudentsDB.py" file to establish the database (if there is conflict with creating the database, make sure there are no databases in the file path).
- After the aforementioned Python file is ran, the database will be created and the "EncodeGenerator.py" file should be ran as well.
- Last but not least, run the "MainDetectionSystemV2.py" file and you should be well on your way to a functioning system.

###  :package: Commands
- Commands to start the project:
```
$ pip3 install pickle; pip3 install cv2; pip3 install os; pip3 install numpy; pip3 install face_recognition, pip3 install cvzone; pip3 install sqlite3; pip3 install json; pip3 install pygame; and other necesary dependencies.
$ python3 SetupStudentsDB.py
$ python3 EncodeGenerator.py
$ python3 MainDetectionSystemV2.py
```

##  :wrench: Development

### :notebook: Pre-Requisites
List all the pre-requisites the system needs to develop this project.
- DJI Tello Drone
- Laptop or Computer
- YOLOv8 Ultralytics
- OpenCV
- IDE or coding environment

###  :nut_and_bolt: Development Environment
You will need an IDE like Pycharm or a Python-enabled coding editor.


###  :file_folder: File Structure
Add a file structure here with the basic details about files, below is an example.

```
. 
├── FaceRecognitionCheckV2
│   ├── Images
│   │   ├── 001001.PNG
│   │   ├── 001002.PNG
│   │   ├── 001003.PNG
│   │   ├── 001004.PNG
│   │   ├── 001005.PNG
│   │   └── 001006.PNG
│   ├── Resources
│       ├── Modes
│       │   ├── 1.png
│       │   ├── 2.png
│       │   ├── 3.png
│       │   └── 4.png
│       ├── background.png
│       └── students_data.json
│   
└── README.md
```

| No | File Name | Details 
|----|------------|-------|
| 1  | index | Entry point

###  :hammer: Build
Write the build Instruction here.

### :rocket: Deployment
Write the deployment instruction here.

## :question: FAQ
You can optionally add a FAQ section about the project.

##  :page_facing_up: Resources
Add important resources here

##  :camera: Gallery
Pictures of your project.

## :star2: Credit/Acknowledgment
Credit the authors here.

##  :lock: License
Add a license here, or a link to it.
