# import yt_dlp
#
# def download_playlist(playlist_url, output_directory, start_index=30):
#     # Define download options
#     ydl_opts = {
#         'format': 'bestaudio/best',  # Download best audio quality
#         'extractaudio': True,  # Extract audio only
#         'audioquality': 1,  # Highest audio quality
#         'audioformat': 'mp3',  # Output format as MP3
#         'outtmpl': f'{output_directory}/%(title)s.%(ext)s',  # Save the audio in the given directory
#         'noplaylist': False,  # Ensure playlist is processed
#         'playlist_items': f'{start_index}-',  # Download from the 30th item onward
#     }
#
#     # Create a YouTubeDL object with the given options
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         # Download the playlist starting from the 30th file
#         ydl.download([playlist_url])
#         print(f"Playlist from the {start_index}th item onward downloaded successfully!")
#
# if __name__ == "__main__":
#     # Enter the playlist URL and the directory where you want to save the MP3 files
#     playlist_url = 'https://www.youtube.com/playlist?list=PLP_LcnuF3YFmwCOh9yIr8OCH5hXg8m-7L'
#     output_directory = r'C:\Users\user\Desktop\FC25'  # Specify the path where you want the files
#
#     # Call the download function, starting from the 30th file
#     download_playlist(playlist_url, output_directory, start_index=30)
#############################################################################################
#############################################################################################
#############################################################################################
# skip songs
#############################################################################################
#############################################################################################
#############################################################################################
import yt_dlp

def download_playlist(playlist_url, output_directory, start_index=30, cookies_file="cookies.txt"):
    # Define download options
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best audio quality
        'extractaudio': True,  # Extract audio only
        'audioquality': 1,  # Highest audio quality
        'audioformat': 'mp3',  # Output format as MP3
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',  # Save the audio in the given directory
        'noplaylist': False,  # Ensure playlist is processed
        'playlist_items': f'{start_index}-',  # Download from the 30th item onward
        'cookies': cookies_file,  # Path to the cookies file
        'quiet': True,  # Suppress unnecessary output
    }

    # Create a YouTubeDL object with the given options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Download the playlist
            ydl.download([playlist_url])
            print(f"Playlist from the {start_index}th item onward downloaded successfully!")
        except yt_dlp.utils.DownloadError as e:
            # Check for private video error
            if "Private video" in str(e):
                print(f"Skipping private video: {e}")
            else:
                # Raise other errors
                raise

if __name__ == "__main__":
    # Enter the playlist URL and the directory where you want to save the MP3 files
    playlist_url = 'https://www.youtube.com/playlist?list=PLP_LcnuF3YFmwCOh9yIr8OCH5hXg8m-7L'
    output_directory = r'C:\Users\user\Desktop\FC25'  # Specify the path where you want the files

    # Call the download function, starting from the 30th file
    download_playlist(playlist_url, output_directory, start_index=0, cookies_file="cookies.txt")
