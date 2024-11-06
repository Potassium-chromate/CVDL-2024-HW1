import cv2
import numpy as np

class Stereo_Disparity_Map:
    def __init__(self, Load_Data):
        self.numDisparities = 432
        self.blockSize = 25
        self.Image_L = None
        self.Image_R = None
        self.Load_Data = Load_Data
        self.screen_width = 1024  
        self.screen_height = 1024
        
    def Show_map(self):

        if self.Load_Data.Image_L is None:
            print("Image_L not loaded!")
            return
        
        if self.Load_Data.Image_R is None:
            print("Image_R not loaded!")
            return
        
        self.Image_L = self.Load_Data.Image_L
        self.Image_R = self.Load_Data.Image_R
        
        stereo = cv2.StereoBM.create(self.numDisparities, self.blockSize)
        disparity = stereo.compute(self.Image_L, self.Image_R)
        #disparity_normalized = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        #disparity_normalized = np.uint8(disparity_normalized)
        
        self.screen_width = int(np.shape(self.Image_R)[1]/4)
        self.screen_height = int(np.shape(self.Image_R)[0]/4)
        
        resized_disparity = cv2.resize(disparity, (self.screen_width, self.screen_height))
        resized_Image_L = cv2.resize(self.Image_L, (self.screen_width, self.screen_height))
        resized_Image_R = cv2.resize(self.Image_R, (self.screen_width, self.screen_height))
        
        cv2.imshow('ImgL', resized_Image_L)
        cv2.imshow('ImgR', resized_Image_R)
        cv2.imshow('Disparity Map', resized_disparity)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
