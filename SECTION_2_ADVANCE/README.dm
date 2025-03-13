# OpenCV Tutorial - Part 2

## Overview
This repository contains various Python scripts demonstrating key image processing techniques using OpenCV. The scripts are designed to cover fundamental and advanced operations, making it useful for learners and practitioners in computer vision.

## Prerequisites
Ensure you have the following installed before running the scripts:

- Python (>= 3.7)
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)

You can install all dependencies using:
```sh
pip install -r requirements.txt
```

## Folder Structure
```
cv2_part2/
│── 0demo.py                # Basic OpenCV demo
│── 11matlab_cv2_imshow.py  # Comparing OpenCV and MATLAB image display
│── 12split_merge.py        # Splitting and merging color channels
│── 13smoothing.py          # Image smoothing techniques
│── 14bitwise.py            # Bitwise operations on images
│── 15masking.py            # Image masking techniques
│── 16histogram1_gray.py    # Histogram of grayscale images
│── 16histogram2_color.py   # Histogram of color images
│── 17threshold.py          # Image thresholding techniques
│── 18edge.py               # Edge detection methods
│── images/                 # Folder for sample images
│── lecture/                # Lecture materials (if any)
│── videos/                 # Sample videos for processing
│── requirements.txt        # List of dependencies
│── README.md               # Project documentation
```

## Explanation of Scripts

### 1. `0demo.py`
- A basic script to load, display, and save images using OpenCV.

### 2. `11matlab_cv2_imshow.py`
- Demonstrates the difference between displaying images in OpenCV and MATLAB.

### 3. `12split_merge.py`
- Splits an image into its Blue, Green, and Red channels and then merges them back.

### 4. `13smoothing.py`
- Applies different smoothing techniques such as Gaussian blur, median blur, and bilateral filtering.

### 5. `14bitwise.py`
- Demonstrates bitwise operations (AND, OR, XOR, NOT) on images, useful for masking and blending.

### 6. `15masking.py`
- Applies a mask to an image, allowing selective processing of certain regions.

### 7. `16histogram1_gray.py`
- Computes and plots the histogram of a grayscale image.

### 8. `16histogram2_color.py`
- Computes and plots histograms for each color channel in an image.

### 9. `17threshold.py`
- Demonstrates different thresholding techniques such as binary, adaptive, and Otsu’s thresholding.

### 10. `18edge.py`
- Implements edge detection using Sobel, Laplacian, and Canny edge detectors.

## How to Run the Scripts

1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd cv2_part2
   ```

2. Run a specific script:
   ```sh
   python script_name.py
   ```
   Example:
   ```sh
   python 14bitwise.py
   ```

## Future Enhancements
- Add real-time video processing examples.
- Implement feature detection techniques (SIFT, ORB, etc.).
- Include interactive UI elements using OpenCV’s trackbars.

## Contributors
- **Shafqat Ameen Mir** - Developer & Maintainer

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---
Happy Coding! 🎯