import eyed3
import os
import re


def update_metadata(mp3_file, title=None, contributing_artists=None, album_artist=None, album=None, genre=None,
                    year=None, track_number=None, album_art_path=None):
    # Load the mp3 file
    audio_file = eyed3.load(mp3_file)

    # Update metadata if provided
    if title:
        audio_file.tag.title = title
    if contributing_artists:
        audio_file.tag.artist = contributing_artists
    else:
        audio_file.tag.artist = "Unknown Artist"

    if album_artist:
        audio_file.tag.album_artist = album_artist
    else:
        audio_file.tag.album_artist = "Unknown Artist"

    if album:
        audio_file.tag.album = album
    if genre:
        audio_file.tag.genre = genre
    if year:
        audio_file.tag.recording_date = eyed3.core.Date(year)
    if track_number:
        audio_file.tag.track_num = track_number

    # Add album art if provided
    if album_art_path and os.path.exists(album_art_path):
        with open(album_art_path, "rb") as img_file:
            album_art_data = img_file.read()
            audio_file.tag.images.set(
                eyed3.id3.frames.ImageFrame.FRONT_COVER, album_art_data, "image/png"
            )
        print(f"Album art added for {mp3_file}")

    # Save changes
    audio_file.tag.save()
    print(f"Metadata updated for {mp3_file}")


def parse_title_and_artist(filename):
    """
    Parses the title and contributing artist from the given filename.
    Format: Title - Artist (Album)
    Example: all 4 the best - PPARTYOF2, Jadagrace & SWIM (FC26 Soundtrack)
    """
    filename = filename.replace('.mp3', '').strip()  # Remove file extension and whitespace

    # Use regex to extract title and artist
    # Pattern: (title) - (artist) (anything in parentheses at the end)
    pattern = r'^(.+?)\s+-\s+(.+?)\s+\(.+?\)$'
    match = re.match(pattern, filename)

    if match:
        title = match.group(1).strip()
        contributing_artist = match.group(2).strip()
        return title, contributing_artist
    else:
        # Fallback: try without parentheses (Title - Artist)
        parts = filename.split(' - ', 1)
        if len(parts) >= 2:
            title = parts[0].strip()
            contributing_artist = parts[1].strip()
            return title, contributing_artist
        else:
            # Default fallback if format is unexpected
            return filename, "Unknown Artist"


def rename_files(folder_path, prefix_to_remove):
    """
    Renames files by removing the specified prefix.
    """
    mp3_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp3')]

    for mp3_file in mp3_files:
        if mp3_file.startswith(prefix_to_remove):
            new_file_name = mp3_file[len(prefix_to_remove):].strip()
            old_file_path = os.path.join(folder_path, mp3_file)
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {mp3_file} -> {new_file_name}")
        else:
            print(f"Skipped: {mp3_file} (does not start with '{prefix_to_remove}')")


def update_folder_metadata(folder_path, album_artist, album, year, genre, album_art_path, prefix_to_remove=None):
    """
    Updates metadata for all MP3 files in the folder after optional renaming.
    """
    # Remove prefix from file names if specified
    if prefix_to_remove:
        rename_files(folder_path, prefix_to_remove)

    # List all MP3 files in the folder
    mp3_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp3')]

    for idx, mp3_file in enumerate(mp3_files, start=1):
        mp3_file_path = os.path.join(folder_path, mp3_file)
        title, contributing_artists = parse_title_and_artist(mp3_file)
        track_number = idx
        update_metadata(mp3_file_path, title=title, contributing_artists=contributing_artists,
                        album_artist=album_artist, album=album, genre=genre, year=year,
                        track_number=track_number, album_art_path=album_art_path)
        print(f"Updated {mp3_file} with track number {track_number}")


if __name__ == "__main__":
    # Define the folder where the MP3 files are stored
    folder_path = r'C:\Users\user\Desktop\FC26\mp3'  # Update folder path as needed

    # Path to the album art
    album_art_path = r'C:\Users\user\Desktop\FC26\mp3\fc26_cover.png'  # Update album art path as needed

    # Define the metadata to update
    album_artist = "EA Trax"  # Common for soundtracks
    album = "FC26"  # Album name
    year = 2026  # Year
    genre = "Game"  # Genre

    # Optional: Remove prefix from filenames (set to None if you don't need to remove any prefix)
    prefix_to_remove = None  # Change this if your files have a prefix like "FC26 - "

    # Call the function to update all MP3 files in the folder
    update_folder_metadata(folder_path, album_artist, album, year, genre, album_art_path, prefix_to_remove)