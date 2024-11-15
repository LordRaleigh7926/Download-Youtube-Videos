# Video Downloader from YouTube

This script provides functionality to download videos from YouTube using a search query. It utilizes the `yt_dlp` library to handle the video extraction and downloading process. The downloaded videos are saved in a specified directory on the user's system (in a folder named auto_downloaded_yt in Videos folder in the user's home directory). 

## Features

- Search for videos on YouTube using a search query.
- Download videos in webm format.
- Automatically generate unique filenames to prevent overwriting existing files.
- Save downloaded videos to a user-specific directory.

## Requirements

- Python 3.9 or greater
- `yt_dlp` library

## Installation

1. Clone the repository or download the script file.
2. Install the required Python packages using pip:

### For Windows
   ```bash
   pip install yt-dlp
   ```

### For Linux/Mac
  ```bash
   pip3 install yt-dlp
   ```

## Usage

### For Windows
1. Ensure that the `yt_dlp` library is installed.
2. Run the script:
   ```bash
   python vid_from_yt.py
   ```
3. Enter the search query when prompted to download the desired video.

   
### For Linux/Mac
1. Ensure that the `yt_dlp` library is installed.
2. Run the script:
   ```bash
   python3 vid_from_yt.py
   ```
3. Enter the search query when prompted to download the desired video.

## Code Structure

- **`baseDIR`**: The directory where downloaded videos are saved. It is set to `Videos/auto_downloaded_yt` under the user's home directory.
- **`generate_unique_filename(search_query: str) -> str`**: A function that generates a unique filename for the video file based on the search query. It ensures that no existing files are overwritten by appending an index to the filename if necessary.

## Logging

The script uses the `logging` module to provide information about the download process and the generated filenames. Ensure that logging is configured appropriately to capture these details.

## Notes

- The script assumes that the user's home directory is accessible and writable.
- Ensure that the `yt_dlp` library is up-to-date to handle any changes in YouTube's video extraction mechanisms.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
