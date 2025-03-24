# Face Detection Project

This project is a Python-based face detection system that identifies and classifies faces of well-known individuals such as Elon Musk, Mark Zuckerberg, and others. The model leverages deep learning techniques to detect and recognize faces in images and videos.

## Features
- Detect and classify faces of specific individuals.
- Uses OpenCV and deep learning models for face recognition.
- Supports real-time face detection using a webcam.
- Works with both images and video files.

## Technologies Used
- Python
- OpenCV
- dlib (for face detection and recognition)
- NumPy
- TensorFlow/Keras (if using deep learning models)

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/face-detection.git
cd face-detection

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
### Detect Faces in an Image
```bash
python detect_faces.py --image path/to/image.jpg
```

### Detect Faces in a Video
```bash
python detect_faces.py --video path/to/video.mp4
```

### Real-time Face Detection
```bash
python detect_faces.py --webcam
```

## Dataset
This project uses a dataset of facial images of well-known individuals. You can extend it by adding more labeled images in the `dataset/` directory.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
[Kaushal Yadav](https://github.com/Kaushal-dev-ai)
