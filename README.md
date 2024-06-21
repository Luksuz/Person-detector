# Face Detection with Haar Cascades

## Overview

This project utilizes computer vision techniques, specifically Haar cascades, for detecting faces in images and video streams. Haar cascades are efficient classifiers commonly used for object detection tasks.

### Key Features:

- **Face Detection**: Detects human faces in images and real-time video streams.
  
- **Real-time Processing**: Utilizes Haar cascades for efficient face detection in live video.

## Technologies Used:

- Python
- OpenCV (Open Source Computer Vision Library)
- Haar Cascades: Pre-trained XML files for detecting faces

## Project Structure:

1. **haar_face.xml**: Directory containing Haar cascade classifiers in XML format.

2. **trainingData/**: Sample images or videos for testing.

3. **face_train.py**:  A training script that uses trainingData and haar_face.xml to tailor the detector to your data.

## Getting Started

To run face detection:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/person-detector.git
   cd face-detection
   pip install -r requirements.txt
   python face_train.py
