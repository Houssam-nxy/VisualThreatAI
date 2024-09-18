import os
from moviepy.editor import VideoFileClip
from PIL import Image
import numpy as np

def extract_and_save_frames(video_path, frame_interval=1, output_folder='./camera/'):
    try:
        clip = VideoFileClip(video_path)
        duration = clip.duration

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        saved_image_paths = []

        for time in range(0, int(duration), frame_interval):
            print(f"\nExtracting frame at time {time} seconds...\n")
            frame = clip.get_frame(time)

            save_path = os.path.join(output_folder, f'frame_at_{time}_seconds.jpg')
            img = Image.fromarray(np.array(frame))
            img.save(save_path)

            saved_image_paths.append(save_path)
            print(f"Frame saved at {save_path}")

        return saved_image_paths

    except Exception as e:
        print(f"Error during frame extraction and saving: {e}")
        return []
