import cv2
import os
from utils import generate_line_art

ASSET_PATH = "assets/portrait1.jpg"
RESULTS_DIR = "results"
OUTPUT_FILE = "results/line_art1.jpg"

def main():

    # To ensure wether results/ exists or not
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    # Load image
    img = cv2.imread(ASSET_PATH)
    if img is None:
        print("❌ ERROR: portrait.jpg not found in assets/")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Fixed parameters
    CANNY_LOW = 50
    CANNY_HIGH = 150
    THICKNESS = 3

    # Generate output
    result = generate_line_art(gray, CANNY_LOW, CANNY_HIGH, THICKNESS)

    # Save image directly
    cv2.imwrite(OUTPUT_FILE, result)
    print(f"✔ Output saved to {OUTPUT_FILE}")
    print("✔ No windows opened. Program finished.")

if __name__ == "__main__":
    main()
