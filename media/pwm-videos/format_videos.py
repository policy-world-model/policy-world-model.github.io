import os
import subprocess
import sys

def trim_and_compress_video(input_file, output_file, crop_length=None):
    crf_value = '18'  # Fixed CRF value for better quality
    if crop_length and crop_length.lower() != 'none':
        crop_option = ['-t', crop_length]
    else:
        crop_option = []

    command = [
        'ffmpeg', '-i', input_file, *crop_option, '-vf', 'scale=128:-2', '-c:a', 'aac', '-b:a', '192k', '-c:v', 'libx264', '-crf', crf_value, output_file
    ]
    subprocess.run(command, check=True)

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: python3 trim_compress_videos.py input_directory output_directory [crop_length]")
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = sys.argv[2]
crop_length = sys.argv[3] if len(sys.argv) == 4 else None

if not os.path.isdir(input_dir):
    print("Error: Input directory does not exist.")
    sys.exit(1)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

mp4_files = [f for f in os.listdir(input_dir) if f.endswith('.mp4')]

for file in mp4_files:
    input_file = os.path.join(input_dir, file)
    filename = os.path.splitext(file)[0]
    output_file = os.path.join(output_dir, f"{filename}.mp4")
    trim_and_compress_video(input_file, output_file, crop_length)
    print(f"Trimmed and compressed {file} to {output_file}")

print("All videos have been trimmed and compressed.")