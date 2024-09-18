import os
from PIL import Image
import requests
from io import BytesIO
import google.generativeai as genai
from dotenv import load_dotenv
from scripts.frames import extract_and_save_frames

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is missing. Please set it in the .env file.")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

prompt_text = """
Analyze the image and provide only the likelihood percentage indicating the risk of future escalation or threat. The output should be a percentage (e.g., 70%) without any additional description or text.
"""

def load_image(image_path):
    try:
        if image_path.startswith("http"):
            response = requests.get(image_path)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def analyze_image(image_path, prompt=prompt_text):
    try:
        img = load_image(image_path)
        if img is not None:
            response = model.generate_content([prompt, img])
            return response.text
        else:
            return "Failed to load image."
    except Exception as e:
        print(f"Error analyzing image {image_path}: {e}")
        return None

def analyze_images_in_folder(folder_path):
    results = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            result = analyze_image(image_path)
            if result:
                print(f"The risk of escalation or future threat for **{filename}** is: {result}")
                results.append({"filename": filename, "result": result})
    return results

def main():
    VIDEO_PATH = './videos/v1.mp4'
    CAMERA_FOLDER = './camera'
    IMAGE_FOLDER = './images'
    
    def video():
        print("\nStarting frame extraction from video...\n")
        extract_and_save_frames(video_path=VIDEO_PATH, frame_interval=10, output_folder=CAMERA_FOLDER)
        print("\nStarting video analysis...\n")
        analyze_images_in_folder(CAMERA_FOLDER)

    def image():
        print("\nStarting image analysis...\n")
        analyze_images_in_folder(CAMERA_FOLDER)
        print("\n")
        analyze_images_in_folder(IMAGE_FOLDER)
        
    ask_user = input("What analysis do you want: video/image/all? ").strip().lower()
    
    if ask_user == 'video':
        video()
    elif ask_user == 'image':
        image()
    elif ask_user == 'all':
        video()
        image()
    else:
        print("Invalid input. Please enter 'video', 'image', or 'all'.")

    print("\nAnalysis complete.\n")

if __name__ == '__main__':
    main()
