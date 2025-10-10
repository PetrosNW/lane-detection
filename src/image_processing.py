import cv2
import numpy as np
import os

def preprocess_image(image_path):
    """Convert image to grayscale and apply Gaussian blur, display all in one resizable window."""

    # 1️⃣ Load the image
    if not os.path.exists(image_path):
        print(f"❌ Image not found at: {image_path}")
        return

    image = cv2.imread(image_path)
    if image is None:
        print("❌ Failed to load image. Check the path or file integrity.")
        return

    print(f"✅ Original image loaded: {image.shape}")

    # 2️⃣ Resize to fit your screen (keep proportions)
    max_width = 1000
    scale = max_width / image.shape[1]
    image = cv2.resize(image, (int(image.shape[1] * scale), int(image.shape[0] * scale)))
    print(f"📏 Resized image shape: {image.shape}")

    # 3️⃣ Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 4️⃣ Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 5️⃣ Stack horizontally
    gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    blur_rgb = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)
    stacked = np.hstack((image, gray_rgb, blur_rgb))

    print("🖼️ Displaying processed image...")
    cv2.namedWindow("Original | Grayscale | Blurred", cv2.WINDOW_NORMAL)
    cv2.imshow("Original | Grayscale | Blurred", stacked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = r"C:\Users\Administrator\Documents\lane_detection_project\test_images\road1.jpg"
    preprocess_image(image_path)
