import eyed3
import os


def update_metadata(mp3_file, title=None, contributing_artists=None, album_artist=None, album=None, genre=None,
                    year=None, track_number=None):
    # Load the mp3 file
    audio_file = eyed3.load(mp3_file)

    # Update metadata if provided
    if title:
        audio_file.tag.title = title
    if contributing_artists:
        audio_file.tag.artist = contributing_artists
    if album_artist:
        audio_file.tag.album_artist = album_artist
    if album:
        audio_file.tag.album = album
    if genre:
        audio_file.tag.genre = genre
    if year:
        audio_file.tag.recording_date = eyed3.core.Date(year)
    if track_number:
        audio_file.tag.track_num = track_number

    # Save changes
    audio_file.tag.save()
    print(f"Metadata updated for {mp3_file}")


def parse_title_and_artist(filename):
    # Extract the title and contributing artist
    # Format: Title - Contributing Artist (FC25 SOUNDTRACK)

    filename = filename.replace('.mp3', '')

    # Find the position of the dash and the (FC25 SOUNDTRACK)
    if ' - ' in filename:
        title_part = filename.split(' - ')[0]  # Before the dash
        artist_part = filename.split(' - ')[1]  # After the dash

        # Remove "(FC25 SOUNDTRACK)" from the artist part
        contributing_artists = artist_part.split(' (')[0].strip()  # Take everything before "(FC25 SOUNDTRACK)"

        return title_part, contributing_artists
    else:
        return filename, ""  # If no dash, use filename as title and no contributing artist


def update_folder_metadata(folder_path, album_artist, album, year, genre):
    # List all MP3 files in the folder
    mp3_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp3')]

    # Loop through each MP3 file
    for idx, mp3_file in enumerate(mp3_files, start=1):
        mp3_file_path = os.path.join(folder_path, mp3_file)

        # Parse title and contributing artist from filename
        title, contributing_artists = parse_title_and_artist(mp3_file)

        # Set other metadata values
        track_number = idx

        # Update metadata for each file
        update_metadata(mp3_file_path, title=title,
                        contributing_artists=contributing_artists,
                        album_artist=album_artist,
                        album=album,
                        genre=genre,
                        year=year,
                        track_number=track_number)
        print(f"Updated {mp3_file} with track number {track_number}")


if __name__ == "__main__":
    # Define the folder where the MP3 files are stored
    folder_path = r'C:\Users\user\Desktop\FC25\mp3'  # Use the provided folder path

    # Define the metadata to update
    album_artist = "EA Trax"
    album = "FC25"
    year = 2025
    genre = "Game"  # Updated Genre to "Game"

    # Call the function to update all MP3 files in the folder
    update_folder_metadata(folder_path, album_artist, album, year, genre)
