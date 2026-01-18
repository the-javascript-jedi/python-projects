import os
import subprocess
from pydub import AudioSegment


def get_ffmpeg_path():
    """Get FFmpeg path from system"""
    try:
        result = subprocess.run(
            ["where", "ffmpeg"],
            capture_output=True,
            text=True,
            shell=True,
            check=True
        )
        paths = result.stdout.strip().split('\n')
        if paths and paths[0]:
            return paths[0].strip()
    except:
        pass
    return None


def setup_ffmpeg():
    """Setup FFmpeg for pydub"""
    # Try to get FFmpeg path from system
    ffmpeg_path = get_ffmpeg_path()

    if ffmpeg_path:
        print(f"✓ Found FFmpeg at: {ffmpeg_path}")
        # Set the paths for pydub
        AudioSegment.converter = ffmpeg_path
        AudioSegment.ffmpeg = ffmpeg_path
        ffprobe_path = ffmpeg_path.replace("ffmpeg.exe", "ffprobe.exe")
        AudioSegment.ffprobe = ffprobe_path
        return True
    else:
        # If automatic detection fails, try common paths
        common_paths = [
            r"C:\ffmpeg\bin\ffmpeg.exe",
            r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
            r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
        ]

        for path in common_paths:
            if os.path.exists(path):
                print(f"✓ Found FFmpeg at: {path}")
                AudioSegment.converter = path
                AudioSegment.ffmpeg = path
                AudioSegment.ffprobe = path.replace("ffmpeg.exe", "ffprobe.exe")
                return True

        print("❌ Could not find FFmpeg automatically")
        print("\nPlease enter the full path to ffmpeg.exe manually:")
        print("(Run 'where ffmpeg' in CMD to find it)")
        manual_path = input("Path: ").strip().strip('"')

        if manual_path and os.path.exists(manual_path):
            AudioSegment.converter = manual_path
            AudioSegment.ffmpeg = manual_path
            AudioSegment.ffprobe = manual_path.replace("ffmpeg.exe", "ffprobe.exe")
            print(f"✓ FFmpeg set to: {manual_path}")
            return True

        return False


def convert_webm_to_mp3_subprocess(input_path, output_path):
    """Fallback: Convert using subprocess directly"""
    ffmpeg_path = get_ffmpeg_path()
    if not ffmpeg_path:
        ffmpeg_path = "ffmpeg"  # Try using system PATH

    cmd = [
        ffmpeg_path,
        '-i', input_path,
        '-vn',  # No video
        '-ar', '44100',  # Sample rate
        '-ac', '2',  # Stereo
        '-b:a', '192k',  # Bitrate
        '-f', 'mp3',
        output_path,
        '-y'  # Overwrite
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e.stderr[:100]}")
        return False
    except FileNotFoundError:
        return False


def convert_folder(input_folder, output_folder, use_subprocess=False):
    """Main conversion function"""
    print(f"🎵 WebM to MP3 Converter")
    print(f"{'=' * 60}")

    # Setup FFmpeg for pydub (unless using subprocess)
    if not use_subprocess:
        if not setup_ffmpeg():
            print("\n⚠️ Falling back to subprocess method...")
            use_subprocess = True

    # Check input folder
    if not os.path.exists(input_folder):
        print(f"❌ Input folder not found: {input_folder}")
        return

    # Get WebM files
    webm_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.webm')]

    if not webm_files:
        print(f"❌ No .webm files found in {input_folder}")
        return

    print(f"\n📁 Found {len(webm_files)} files to convert")
    print(f"📁 Output: {output_folder}\n")

    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    successful = 0
    failed = []
    skipped = 0

    for i, filename in enumerate(webm_files, 1):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.mp3'
        output_path = os.path.join(output_folder, output_filename)

        # Skip if exists
        if os.path.exists(output_path):
            print(f"[{i}/{len(webm_files)}] ⏭️  Skipping: {filename[:50]}... (exists)")
            skipped += 1
            continue

        print(f"[{i}/{len(webm_files)}] 🔄 Converting: {filename[:50]}...", end=' ')

        try:
            if use_subprocess:
                # Use subprocess method
                if convert_webm_to_mp3_subprocess(input_path, output_path):
                    print("✅")
                    successful += 1
                else:
                    print("❌")
                    failed.append(filename)
            else:
                # Use pydub method
                audio = AudioSegment.from_file(input_path, format="webm")
                audio.export(output_path, format="mp3", bitrate="192k")
                print("✅")
                successful += 1
        except Exception as e:
            print("❌")
            failed.append(filename)
            # Print detailed error for first few failures
            if len(failed) <= 3:
                print(f"     Error: {str(e)[:100]}")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"🎉 Conversion Complete!")
    print(f"✅ Successful: {successful}")
    print(f"⏭️  Skipped: {skipped}")
    print(f"❌ Failed: {len(failed)}")

    if failed:
        print(f"\n❌ Failed files ({len(failed)}):")
        for fname in failed[:5]:
            print(f"   - {fname}")
        if len(failed) > 5:
            print(f"   ... and {len(failed) - 5} more")

    print(f"\n📁 Output: {output_folder}")
    print(f"{'=' * 60}")


# ALTERNATIVE: Simple subprocess-only converter
def simple_convert():
    """Simple converter using only subprocess (no pydub)"""
    input_folder = r'C:\Users\user\Desktop\FC26'
    output_folder = r'C:\Users\user\Desktop\FC26\mp3'

    print("🎵 Simple WebM to MP3 Converter (subprocess method)")
    print(f"{'=' * 60}")

    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Get files
    webm_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.webm')]
    print(f"Found {len(webm_files)} files\n")

    successful = 0
    for i, filename in enumerate(webm_files, 1):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace('.webm', '.mp3'))

        if os.path.exists(output_path):
            print(f"[{i}/{len(webm_files)}] Skipping {filename[:40]}... (exists)")
            continue

        print(f"[{i}/{len(webm_files)}] Converting {filename[:40]}...", end=' ')

        cmd = f'ffmpeg -i "{input_path}" -vn -ar 44100 -ac 2 -b:a 192k -f mp3 "{output_path}" -y'

        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅")
            successful += 1
        else:
            print("❌")

    print(f"\n✅ Converted {successful}/{len(webm_files)} files")
    print(f"📁 Output: {output_folder}")


if __name__ == "__main__":
    # Your paths
    input_folder = r'C:\Users\user\Desktop\FC26'
    output_folder = r'C:\Users\user\Desktop\FC26\mp3'

    # Method 1: Try with pydub first, fallback to subprocess
    # convert_folder(input_folder, output_folder)

    # Method 2: Use only subprocess (more reliable)
    simple_convert()