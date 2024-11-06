from q1 import CameraCalibration
from Load import Load_Data

import cv2
import numpy as np

class Argumented_Reality:
    def __init__(self, Load_Data, vertical_mode = False):
        self.alph_loc = np.array([[7, 5, 0],
                    [4, 5, 0],
                    [1, 5, 0],
                    [7, 2, 0],
                    [4, 2, 0],
                    [1, 2, 0]])
        self.full_loc = np.array([[0, 0, 0],
                    [1, 0, 0],
                    [2, 0, 0],
                    [0, 1, 0],
                    [1, 1, 0],
                    [2, 1, 0],
                    [0, 2, 0],
                    [1, 2, 0],
                    [2, 2, 0]])
        self.full_ver_loc = np.array([[0, 0, 0],
                    [1, 0, 0],
                    [2, 0, 0],
                    [0, 1, -1],
                    [1, 1, -1],
                    [2, 1, -1],
                    [0, 2, -2],
                    [1, 2, -2],
                    [2, 2, -2]])
        self.corner_loc = np.array([[0, 0, 0],
                    [2, 0, 0],
                    [0, 2, 0],
                    [2, 2, 0]])
        self.CB = None
        self.vertical_mode = vertical_mode
        self.folder_images = Load_Data.folder_images
        self.Load_Data = Load_Data
        
    def Show_on_board(self,words):
        # Load images and calibrate the camera
        self.CB = CameraCalibration(self.Load_Data)
        self.CB.calibrate()
        
        # Open the alphabet data
        fs = cv2.FileStorage('alphabet_db_onboard.txt', cv2.FILE_STORAGE_READ)
        
        img_counter = 0
        imgpoints = []
        
        for img in self.folder_images:
            img = img.copy()
            word_counter = 0
            for char in words:
                #Make sure less than 6 alphabets
                if(word_counter >= 6):
                    break
                #Prevent non-uppercase letter
                if not char.isupper():
                    continue
                
                charPoints = fs.getNode(char).mat()  
                
                cornerPoints = self.corner_loc + self.alph_loc[word_counter]
                fullPoints = self.full_loc + self.alph_loc[word_counter]
                fullVerPoints = self.full_ver_loc + self.alph_loc[word_counter]  
                
                # Ensure calibration values are available
                if self.CB.ret and self.CB.camera_matrix is not None and self.CB.distortion_coeffs is not None:
                    # Prepare object points (3D) and image points (2D)
                    objpoints = cornerPoints.reshape(-1, 3)
                    imgpoints.clear()
                    #find the imgpoints of full points in chest board
                    for points in objpoints:
                        index = points[0] + points[1]*11 
                        imgpoints.append(self.CB.img_points[img_counter][index])
                        
                    imgpoints_arr = np.array(imgpoints)
                    imgpoints_arr = imgpoints_arr.reshape(-1, 2)
                    
                    # use four points from corner to estimate rotation and translation by solvePnPRansac
                    success, rvec, tvec, inliers = cv2.solvePnPRansac(objpoints.astype(np.float32), imgpoints_arr, self.CB.camera_matrix, self.CB.distortion_coeffs)
                
                    
                    
                    # check the mode
                    if self.vertical_mode:
                        re_charPoints = fullVerPoints.reshape(-1, 1, 3).astype(np.float32)
                    else:
                        re_charPoints = fullPoints.reshape(-1, 1, 3).astype(np.float32)
                    
                    # project character points onto the image plane
                    newCharPoints, _ = cv2.projectPoints(re_charPoints, rvec, tvec, self.CB.camera_matrix, self.CB.distortion_coeffs)
                
                    # Display setting
                    color = (0, 255, 0)
                    thickness = 9

                    # Draw lines
                    for i in range(charPoints.shape[0]):  
                        #find start and end point in from full points
                        pt1_idx = charPoints[i, 0, 0] + charPoints[i, 0, 1] * 3
                        pt2_idx = charPoints[i, 1, 0] + charPoints[i, 1, 1] * 3

                        pt1 = tuple(newCharPoints[pt1_idx, 0, :].astype(np.int32))
                        pt2 = tuple(newCharPoints[pt2_idx, 0, :].astype(np.int32))
                        cv2.line(img, pt1, pt2, color, thickness)        
                else:
                    print("Calibration failed. Camera matrix or distortion coefficients are not set.")
                
                word_counter += 1
                
            resized_img = cv2.resize(img, (self.CB.screen_width, self.CB.screen_height))
            # Show the result
            cv2.imshow("Projected Letter", resized_img)
            cv2.waitKey(1500)
            img_counter += 1
            
        cv2.destroyAllWindows()
            
if __name__ == "__main__":
    LD = Load_Data()
    LD.Loadfolder()
    AR = Argumented_Reality(LD, vertical_mode = True)
    words = "TEST"
    AR.Show_on_board(words)