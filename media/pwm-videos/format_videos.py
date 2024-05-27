import os
import subprocess
import argparse

def process_videos(input_dir, output_dir, crop_time):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Construct the ffmpeg command
            command = [
                'ffmpeg',
                '-i', input_path,
                '-t', str(crop_time),
                '-c:v', 'libx264',
                '-crf', '18',  # 18 is generally considered visually lossless
                '-preset', 'slow',
                output_path
            ]
            
            print(f"Processing {filename}")
            subprocess.run(command, check=True)

def main():
    parser = argparse.ArgumentParser(description="Crop and compress videos.")
    parser.add_argument('y', type=str, help="Directory containing the input videos.")
    parser.add_argument('z', type=str, help="Directory to save the processed videos.")
    parser.add_argument('x', type=int, help="Number of seconds to crop from the start of the video.")
    
    args = parser.parse_args()
    
    input_dir = args.y
    output_dir = args.z
    crop_time = args.x
    
    process_videos(input_dir, output_dir, crop_time)

if __name__ == "__main__":
    main()