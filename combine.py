import os
import subprocess

# Function to combine .ts video segments into one video
def combine_video_segments(folder_path, output_filename):
    # Get a list of all .ts files in the folder
    ts_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.ts')])
    
    # Create a file with a list of all .ts files in the correct format for ffmpeg
    with open(os.path.join(folder_path, 'file_list.txt'), 'w') as f:
        for ts_file in ts_files:
            f.write(f"file '{ts_file}'\n")
    
    # Run the ffmpeg command to combine the .ts files
    command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', os.path.join(folder_path, 'file_list.txt'),
        '-c', 'copy',
        output_filename
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Successfully combined video segments into {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during video combination: {e}")

# Folder containing the .ts files
save_folder = "video_segments"

# Output file name (final combined video)
output_video = "final_video.mp4"

# Calling the function to combine .ts video segments
combine_video_segments(save_folder, output_video)
