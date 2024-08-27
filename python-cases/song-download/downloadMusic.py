from __future__ import unicode_literals
import youtube_dl
from pytube import Playlist

def run(pl):
    links = pl.video_urls
    for link in links:
        
        ydl_opts = {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # ydl.download([link])
            ydl.download(['https://www.youtube.com/watch?v=BGsDSJ7LtAs&list=PLZJmGg18CSg7FHsI_O3vY5-pG4Rtf3mbo'])
    
        print(link)

if __name__ == "__main__":
    url = input("url:")
    pl = Playlist(url)
    run(pl)
    input("Finished...")