# execute the code step by step
## download the songs
 first use the 1_DownlodYoutubeAudio.py file and download the songs from youtube
 private videos cannot be downloaded so once we encounter a private video in playlist we need to skip it only
 change the start_index value to the number after the  private video
download_playlist(playlist_url, output_directory, start_index=0, cookies_file="cookies.txt")

## convert to mp3
the downloaded files are in webm - run the second script to convert webm to mp3 files

## add meta data
run the third script to add the meta data


