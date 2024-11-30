import eyed3
import os


def update_track_numbers(folder_path):
    """
    Updates the track number field in the metadata of MP3 files
    to be sequential, starting from 1, without renaming the files.

    Args:
        folder_path (str): Path to the folder containing MP3 files.
    """
    # List all MP3 files in the folder
    mp3_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp3')]

    # Sort the MP3 files by name to ensure consistent ordering
    mp3_files.sort()

    # Update the track number field in metadata
    for idx, mp3_file in enumerate(mp3_files, start=1):
        file_path = os.path.join(folder_path, mp3_file)

        # Load the MP3 file
        audio_file = eyed3.load(file_path)
        if audio_file and audio_file.tag:
            # Update the track number field
            audio_file.tag.track_num = idx
            audio_file.tag.save()
            print(f"Updated track number for {mp3_file} to {idx}")
        else:
            print(f"Skipped {mp3_file}: Unable to load metadata.")


if __name__ == "__main__":
    # Define the folder where the MP3 files are stored
    folder_path = r'C:\Users\user\Desktop\FC25\mp3'  # Update this path as needed

    # Call the function to update track numbers in metadata
    update_track_numbers(folder_path)
