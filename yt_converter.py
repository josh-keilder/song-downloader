import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube
import os, json, dropbox
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.environ.get("DROPBOX_ACCESS_TOKEN")

CONFIG_FILE = "config.json"

class YTConverter:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Youtube to MP3 Converter")
        self.main_window.geometry("700x200")

        self.config = self.load_config()

        if not self.config["local_folder"]:
            self.config["local_folder"] = filedialog.askdirectory(
                title="Choose a folder to save songs"
            )

        self.save_config()

        self.link_label = tk.Label(self.main_window, text="Insert Link:")
        self.link_label.pack()
        self.link_entry = tk.Entry(self.main_window, width=50)
        self.link_entry.pack()

        tk.Button(
            self.main_window,
            text="Change Download Output Folder",
            command=self.change_folders
            ).pack()
        
        self.dropbox_var = tk.BooleanVar()

        dropbox_frame = tk.Frame(self.main_window)
        dropbox_frame.pack()
        self.dropbox_check_label = tk.Label(dropbox_frame, text="Upload to dropbox?")
        self.dropbox_check = tk.Checkbutton(dropbox_frame, variable=self.dropbox_var)
        self.dropbox_check_label.pack(side="left")
        self.dropbox_check.pack(side="left")

        self.convert_button = tk.Button(self.main_window, text="Convert", command=self.convert_Video)
        self.convert_button.pack(pady=5)
        self.converted_output = tk.Label(self.main_window, text="---------")
        self.converted_output.pack()


        self.quit_button = tk.Button(self.main_window, text="Quit", command=self.main_window.destroy).pack(side='bottom')

        tk.mainloop()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        return {"local_folder": "", "dropbox_folder": ""}

    def save_config(self):
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=4)

    def change_folders(self):
        self.config["local_folder"] = filedialog.askdirectory(title="Choose a folder to save songs.")

        self.save_config()
        self.converted_output.config(text="Folder updated!")

    def convert_Video(self):
        try:
            url = self.link_entry.get().strip()
            yt = YouTube(url)
            audio = yt.streams.filter(only_audio=True).first()

            if audio is None:
                self.converted_output.config(text="No audio stream found.")
                return

            downloaded_file = audio.download(output_path=self.config["local_folder"])

            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            print("Done")

            self.converted_output.config(text="Conversion to mp3 success! Downloading file...")

            if self.dropbox_var.get():
                dropbox_path = f"{self.config["dropbox_folder"]}/{os.path.basename(new_file)}"

                self.upload_to_dropbox(
                    local_file_path=new_file,
                    dropbox_path=dropbox_path
                )

        except Exception as e:
            print(f"Error occurred: {e}")
            self.converted_output.config(text=f"Error occurred: {e}")


    def upload_to_dropbox(self, local_file_path, dropbox_path):
        if not ACCESS_TOKEN:
            self.converted_output.config(text="Dropbox token not found.")
            return
        
        try:
            dbx = dropbox.Dropbox(ACCESS_TOKEN)

            with open(local_file_path, "rb") as f:
                dbx.files_upload(
                    f.read(),
                    dropbox_path,
                    mode=dropbox.files.WriteMode.overwrite
                )

            self.converted_output.config(text="Conversion to MP3 success and uploaded to Dropbox!")

        except Exception as e:
            print(f"Error occurred: {e}")
            self.converted_output.config(text=f"Error occurred: {e}")

if __name__ == '__main__':
    yt_gui = YTConverter()

