import cv2
import numpy as np
import tkinter as tk
from tkinter import scrolledtext


class CameraCalibration:
    def __init__(self, Load_Data):
        self.ret = None
        self.camera_matrix = None
        self.distortion_coeffs = None
        self.rvecs = None
        self.tvecs = None
        self.q1_renew_tag = -1
        self.obj_points = []
        self.img_points = []
        self.square_size = 0.02
        self.screen_width = 1024  
        self.screen_height = 1024
        self.pattern_size = (11, 8) 
        self.object_points = np.zeros((self.pattern_size[0] * self.pattern_size[1], 3), np.float32)
        self.object_points[:, :2] = np.mgrid[0:self.pattern_size[0], 0:self.pattern_size[1]].T.reshape(-1, 2) * self.square_size
        self.corner = None
        self.load_renew_tag = Load_Data.load_renew_tag
        self.folder_images = Load_Data.folder_images
        
    def Find_corner(self):
        if not self.folder_images:
            print("No images loaded.")
            return
        
        else:
            for img in self.folder_images:
                
                grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                # Define the number of inner corners in the chessboard
                pattern_size = (11, 8)
                
                # Find chessboard corners
                ret, self.corners = cv2.findChessboardCorners(grayimg, pattern_size)           
                if ret:
                    print("Chessboard corners detected!")
                    # Draw the corners on the image
                    cv2.drawChessboardCorners(grayimg, pattern_size, self.corners, ret)
                    
                    resized_img = cv2.resize(grayimg, (self.screen_width, self.screen_height))
                    
                    cv2.imshow('Corners', resized_img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    print("Chessboard corners not found.")
                    
    def Find_Intrinsic(self):
        if not self.folder_images:
            print("No images loaded.")
            return
        
        else:
            self.calibrate()
            
            # Output the intrinsic matrix
            print("Intrinsic matrix:")
            print(self.camera_matrix)
            
            self.display_window("Intrinsic matrix", self.camera_matrix)
    
    def Find_Extrinsic(self,value):  
        if value <= 0 or value > len(self.folder_images):
            print("Index out of range")
            return
        if not self.folder_images:
            print("No images loaded.")
            return
        
        else:
            self.calibrate()
                
            rotation_vector = self.rvecs[value - 1]
            translation_vector = self.tvecs[value - 1]
            rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
        
            # Create the extrinsic matrix
            extrinsic_matrix = np.hstack((rotation_matrix, translation_vector.reshape(-1, 1)))
            print(f"Extrinsic matrix of {value}.bmp.")
            print(extrinsic_matrix)
            
            title = "Extrinsic matrix of " + str(value) +" .bmp."
            self.display_window(title, extrinsic_matrix)
    
    def Find_Distortion(self,value):
        if not self.folder_images:
            print("No images loaded.")
            return
        
        else:
            self.calibrate()
                
            print(f"Distortion matrix of {value}.bmp.")
            print(self.distortion_coeffs)
            
            self.display_window("Distortion matrix", self.distortion_coeffs)
            
    def Show_Result(self,value):
        if value <= 0 or value > 15:
            print("Index out of range")
            return
        
        if not self.folder_images:
            print("No images loaded.")
            return
        
        else:
            self.calibrate()
            result_img = cv2.undistort(self.folder_images[value-1], self.camera_matrix, self.distortion_coeffs)
            
            distorted_img = cv2.resize(self.folder_images[value-1], (self.screen_width, self.screen_height))
            undistorted_img = cv2.resize(result_img, (self.screen_width, self.screen_height))
            
            # Display the original and undistorted images
            cv2.imshow('Distorted Image', distorted_img)
            cv2.imshow('Undistorted Image', undistorted_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            
    def calibrate(self):
        if not self.folder_images:
            print("No images loaded.")
            return
        if (self.q1_renew_tag != self.load_renew_tag):
            # Initialize
            self.obj_points.clear()
            self.img_points.clear()
                        
            for img in self.folder_images:
                grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
                # Find the chessboard corners
                ret, self.corners = cv2.findChessboardCorners(grayimg, self.pattern_size)
                
                if ret:
                    self.obj_points.append( self.object_points)
                    self.img_points.append(self.corners)
                    
            # Calibrate the camera
            self.ret, self.camera_matrix, self.distortion_coeffs, self.rvecs, self.tvecs = cv2.calibrateCamera(self.obj_points, self.img_points, grayimg.shape[::-1], None, None)
           
            self.q1_renew_tag = self.load_renew_tag
    
    def display_window(self,title,text):
        window = tk.Tk()
        window.title(title)
     
        # Add a scrolled text widget to display the matrix
        text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=10, font=("Helvetica", 10))
        text_area.pack(pady=10, padx=10)
     
        # Insert the extrinsic matrix into the text widget
        text_area.insert(tk.END, f"{text}")
        text_area.config(state=tk.DISABLED)  # Make the text read-only
     
        window.mainloop()