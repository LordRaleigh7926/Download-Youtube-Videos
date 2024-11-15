import os
import logging
import yt_dlp

baseDIR = os.path.join(os.path.expanduser('~'), "Videos", "auto_downloaded_yt")
os.makedirs(baseDIR, exist_ok=True)

def generate_unique_filename(search_query:str) -> str:

    """

    Generate a unique filename for a video file based on the search query.

    This function constructs a file path in the specified base directory
    using the given search query. If a file with the same name already
    exists, it appends an index to the filename to ensure uniqueness.

    Args:
        search_query (str): The search query used to generate the base
        filename.

    Returns:
        str: A unique file path for the video file.
    
    """

    tmp_vidfile_path = os.path.join(baseDIR, f"{search_query}.webm")
    file_index = 1

    while os.path.exists(tmp_vidfile_path):
        tmp_vidfile_path = os.path.join(baseDIR, f"{search_query}_{file_index}.webm")
        file_index += 1

    return tmp_vidfile_path

def download_from_youtube(search_query: str) -> None:

    """

    Download a video from YouTube based on a search query.

    This function uses yt_dlp to search for and download a video from YouTube
    matching the given search query. The video is saved to a uniquely named
    file in the specified base directory. Logs are generated to indicate the
    progress and outcome of the download process.

    Args:
        search_query (str): The search query to find and download the video.

    Returns:
        None
        
    """
        

    tmp_vidfile_path = generate_unique_filename(search_query)

    logging.basicConfig(level=logging.INFO)

    try:
        with yt_dlp.YoutubeDL({'outtmpl': tmp_vidfile_path, 'verbose': False}) as video:
            info_dict = video.extract_info(f"ytsearch:{search_query}", download=True)
            video_title = info_dict['title']
            logging.info(f" Downloaded {video_title}")
            logging.info(f" Saved to {tmp_vidfile_path}")
    except Exception as e:
        logging.error(f"An error occurred during the download: {e}")

k = input("Enter video name:  ")

download_from_youtube(k)