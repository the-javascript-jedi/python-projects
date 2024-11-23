import os
from pydub import AudioSegment


def convert_webm_to_mp3(input_folder, output_folder):
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.webm'):
            input_path = os.path.join(input_folder, filename)
            output_filename = filename.replace('.webm', '.mp3')
            output_path = os.path.join(output_folder, output_filename)

            try:
                # Load the .webm file using AudioSegment
                audio = AudioSegment.from_file(input_path, format="webm")
                # Export the file as .mp3
                audio.export(output_path, format="mp3")
                print(f"Converted {filename} to MP3")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")


if __name__ == "__main__":
    input_folder = r'C:\Users\user\Desktop\FC25'  # Folder where your .webm files are
    output_folder = r'C:\Users\user\Desktop\FC25\mp3'  # Folder to save the .mp3 files

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert .webm files to .mp3
    convert_webm_to_mp3(input_folder, output_folder)
