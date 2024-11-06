from Load import Load_Data
import numpy as np
import cv2

class SIFT:
    def __init__(self, Load_Data):
        self.Image_1 = None
        self.Load_Data = Load_Data
        self.Image_1 = None
        self.screen_width = 1024  
        self.screen_height = 1024
        self.sift = cv2.SIFT_create()
        
    def Keypoints(self):
        # Load image from the Load_Data instance
        self.Image_1 =  self.Load_Data.Image_L
        if self.Image_1 is None:
            print("Image_1 not loaded.")
            return
        
        # Detect keypoints and compute descriptors
        keypoints, descriptors = self.sift.detectAndCompute(self.Image_1, None)
        # Draw keypoints on the image
        key_img = cv2.drawKeypoints(self.Image_1, keypoints, None, color=(0,255,0))
        
        # Resize the image for display
        self.screen_width = int(np.shape(key_img)[1]/4)
        self.screen_height = int(np.shape(key_img)[0]/4)
        key_img = cv2.resize(key_img, (self.screen_width, self.screen_height))
        
        # Display the image with keypoints
        cv2.imshow('key_img', key_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def MatchKeypoints(self):
        # Load image from the Load_Data instance
        self.Image_1 =  self.Load_Data.Image_L
        self.Image_2 =  self.Load_Data.Image_R
        if self.Image_1 is None:
            print("Image_1 not loaded.")
            return
        if self.Image_2 is None:
            print("Image_2 not loaded.")    
            return
        
        # Detect keypoints and compute descriptors
        keypoints1, descriptors1 = self.sift.detectAndCompute(self.Image_1, None)
        keypoints2, descriptors2 = self.sift.detectAndCompute(self.Image_2, None)
        
        # Use BFMatcher to match keypoints
        matches = cv2.BFMatcher().knnMatch(descriptors1, descriptors2, k=2)


        # Apply the ratio test
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:  # Adjust ratio as needed
                good_matches.append([m])

        print(f"Number of good matches: {len(good_matches)}")

        # Draw matches
        matched_image = cv2.drawMatchesKnn(self.Image_1, keypoints1, self.Image_2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        
        # Adjust image size
        self.screen_width = int(np.shape(matched_image)[1]/4)
        self.screen_height = int(np.shape(matched_image)[0]/4)
        matched_image = cv2.resize(matched_image, (self.screen_width, self.screen_height))
        
        # Display the matched image
        cv2.imshow('matched_image', matched_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    LD = Load_Data()
    SIFT = SIFT(LD)
    LD.LoadSingleImage(left_side = True)
    LD.LoadSingleImage(left_side = False)
    SIFT.MatchKeypoints()
    