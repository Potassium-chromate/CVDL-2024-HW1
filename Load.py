import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import numpy as np
import cv2
import random



class Load_Data:
    def __init__(self):
        self.folder_images = []
        self.Image_L = None
        self.Image_R = None
        self.load_renew_tag = 0

    def Loadfolder(self):   
        self.folder_images.clear()
        # Initialize the root window
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        
        # Open the file dialog to select a folder
    
        folder_path = filedialog.askdirectory(title="Select Folder")
            
        if not folder_path:
            print("No folder selected.")
            return
        print("Selected Folder Path:", folder_path)
    
        for filename in os.listdir(folder_path):
            if filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):  
                img_path = os.path.join(folder_path, filename)  
                img = Image.open(img_path) 
                img_cv = np.array(img)
                img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
                self.folder_images.append(img_cv)
    
        # Now images contains all loaded image objects
        print(f"Loaded {len(self.folder_images)} images.")
        self.load_renew_tag = random.randint(1, 10000000)
        return
    
    def LoadSingleImage(self, left_side = True):
        global Image_L, Image_R
        
        root = tk.Tk()
        root.withdraw()
        img_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
        )
        if img_path:
            print("Selected image:", img_path)
        else:
            print("No image selected.")
        
        img = Image.open(img_path) 
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        
        if left_side:
            self.Image_L = img_cv
        else:
            self.Image_R = img_cv
        return
        
if __name__ == "__main__":
   FD = Load_Data()