# Line Art Generator

This project converts an input image into a clean black-and-white line-art drawing using OpenCV and Python.

## ✨ Features
- **Automatic Line Detection** using Canny edge detection.  
- **Adjustable Line Thickness** using morphological dilation.  
- **Clean, Simple Output** resembling hand-drawn outlines.  
- **Template-Compliant Structure** with organized folders and scripts.  

## 📂 Project Structure

opencv-project-template/
│
├── src/
│ ├── main.py # Main script that controls processing
│ └── utils.py # Helper functions for image operations
│
├── assets/ # Input images for processing
│ └── portrait1.jpg
│
├── results/ # Generated outputs
│ └── line_art1.jpg
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore

## 🔧 Installation
Install the required dependencies:

pip install -r requirements.txt

Make sure your input image is placed in:

assets/portrait1.jpg

## ▶️ Usage
Run the project from the root directory:

python src/main.py

The script will:
- Load the input image  
- Convert it to grayscale  
- Apply Canny edge detection  
- Increase thickness using dilation  
- Save the final output to `results/line_art1.jpg`

## 🧠 How It Works
1. Convert the input image → **Grayscale**  
2. Apply **Edge Detection** using Canny  
3. Apply **Dilation** to thicken edges  
4. Save output → **Clean Line-Art Image**

## 📸 Output
The processed line-art image will be saved in:

results/line_art1.jpg

Made by Jairaj R.
