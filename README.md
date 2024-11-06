# CVDL-2024-HW1
## Overview
This repository contains code for **CVDL-2024-HW1**, focusing on computer vision and deep learning tasks such as stereo disparity mapping, extrinsic matrix calculation, key point matching, and more. These implementations are developed using Python, OpenCV, and other supporting libraries.

## Features
- **Load Images from Folder:** Load multiple images from a specified folder.
- **Stereo Disparity Map:** Generate and display disparity maps from stereo images.
- **Key Point Detection and Matching:** Detect and match key points between images.
- **Extrinsic Matrix Calculation:** Calculate and display extrinsic matrices for loaded images.
- **Augmented Reality:** Display alphabat on the chest board

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Potassium-chromate/CVDL-2024-HW1.git
   cd CVDL-2024-HW1
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
To start:
```bash
python main.py
```

## Dependencies
- Python 3.10
- **OpenCV:** For computer vision functions and operations
- **NumPy:** For array manipulations
- **Pillow:** For image handling in various formats
- **Tkinter:** For GUI elements and displaying results

## Project Structure
- **main.py:** Main script for running the project.
- **q1.py:** Module for finding Intrinsic matrix and Extrinsic matrix.
- **q2.py:** Module for Augmented Reality, which project words onto the chest board.
- **q3.py:** Module for Stereo Disparity Map.
- **q4.py:** Module for Keypoints processing.

## Troubleshooting
### Original problem 1
In the `cv2.projectPoints function`, the `charPoints` array needs at least four distinct points in three different directions (vectors) to calculate a valid projection. If `charPoints` is used directly, some alphabets with fewer than three points (such as the letter "I", which only has two points) will cause issues.
Example for "I":
```python
newCharPoints = cv2.projectPoints(charPoints, ins, dist, rvec, tvec)
```
The "I" character's data:
```yaml
I: !!opencv-matrix
   rows: 1
   cols: 2
   dt: "3i"
   data: [ 1, 2, 0, 1, 0, 0 ]

```

### Solution
To resolve this, we use the relative coordinates of the corner points (four points in three different directions) to calculate the rotation vector (`rvec`) and translation vector (`tvec`) using `cv2.solvePnPRansac`. Then, we project the character based on the `full_loc` points onto the board. This ensures that the alphabet is properly aligned with the projected points from `full_loc`.

Example:
```python
corner_loc = np.array([[0, 0, 0],
                    [2, 0, 0],
                    [0, 2, 0],
                    [2, 2, 0]])

full_loc = np.array([[0, 0, 0],
                    [1, 0, 0],
                    [2, 0, 0],
                    [0, 1, 0],
                    [1, 1, 0],
                    [2, 1, 0],
                    [0, 2, 0],
                    [1, 2, 0],
                    [2, 2, 0]])

newCharPoints, _ = cv2.projectPoints(full_loc, rvec, tvec, camera_matrix, distortion_coeffs)
```

###  Original problem 2
When projecting 3D points onto a 2D image using `cv2.projectPoints`, you need the camera's rotation and translation vectors (`rvec` and `tvec`). If you directly use the `rvecs[0]` and `tvecs[0]` values from a previous camera calibration, this assumes that the camera's position and orientation are already known. This approach works if the camera has been calibrated, and you have the extrinsic parameters from the calibration process.

However, when working with new images where the camera pose is unknown or the calibration data is unavailable, you cannot rely on `rvecs[0]` and `tvecs[0]` directly. In this case, using the camera calibration results from a single image may lead to incorrect projections.

### Solution:
If you do not have the pre-calibrated camera parameters or need to estimate the camera pose for a specific scene, you should use **`cv2.solvePnPRansac`** to calculate the rotation and translation vectors (`rvec` and `tvec`). This method computes the camera’s position and orientation from the 3D world points and their corresponding 2D image projections. Once the camera pose is estimated, you can use `cv2.projectPoints` to project 3D points onto the 2D image plane accurately.

#### Steps:
1. **Use `cv2.solvePnPRansac`** to calculate the camera pose:
   - `cv2.solvePnPRansac` requires 3D object points and their corresponding 2D image points.
   - It estimates the `rvec` and `tvec` that describe the camera's orientation and position relative to the 3D object.

   ```python
   success, rvec, tvec, inliers = cv2.solvePnPRansac(fullPoints, imgpoints_arr, camera_matrix, distortion_coeffs)
    ```
2. **Use `cv2.projectPoints`** to project 3D points to 2:
   ```python
   newCharPoints = cv2.projectPoints(charPoints, ins, dist, rvec, tvec)
    ```

## License
This project is licensed under the MIT License. See `LICENSE` for details.
