import os
import requests

# Function to send GET requests and download video segments
def download_video_segments(base_url, folder_path, start_num, end_num):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    for num in range(start_num, end_num + 1):
        segment_url = base_url.replace("a1.ts", f"a{num}.ts")
        video_filename = os.path.join(folder_path, f'a{num}.ts')

        try:
            # Send a GET request
            response = requests.get(segment_url, stream=True)
            
            # Check if the response is successful
            if response.status_code == 200:
                # Save the video segment
                with open(video_filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                print(f"Segment a{num}.ts downloaded successfully.")
            else:
                print(f"Failed to download segment a{num}.ts. Status code: {response.status_code}")
        
        except requests.RequestException as e:
            print(f"Exception occurred while downloading segment a{num}.ts: {e}")
    
    print("Download process completed.")

# Base URL (without the segment number)
base_url = "https://100x-b-mcdn.akamai.net.in/cohort3/4412213/a1.ts"

# Folder to save the video segments
save_folder = "video_segments"

# Range of segment numbers to download (from a1.ts to aN.ts)
start_segment = 1  # Start from a1.ts
end_segment = 692   # Change this to the desired number of segments

# Calling the function to download video segments
download_video_segments(base_url, save_folder, start_segment, end_segment)
