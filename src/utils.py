import cv2
import numpy as np

def generate_line_art(img, canny_low, canny_high, thickness):

    # Step 1: Detect edges using Canny
    edges = cv2.Canny(img, canny_low, canny_high)

    # Step 2: Thicken edges using dilation
    kernel = np.ones((thickness, thickness), np.uint8)
    thick_edges = cv2.dilate(edges, kernel, iterations=1)

    return thick_edges
