import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'bv*+ba/b',
            'merge_output_format': 'mp4'
        }

        print(f"Downloading from: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Video downloaded successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory(title="Select folder to save video")
    if folder:
        print(f"Selected folder: {folder}")
    else:
        print("No folder selected.")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # hide the main window

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("❌ Invalid or no save location selected. Download canceled.")
