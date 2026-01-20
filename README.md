# YouTube Converter & Dropbox Uploader

A simple Python GUI application to download audio from YouTube videos, convert it to MP3, and optionally upload it to a Dropbox folder.  

---

## Features

- Download audio from any YouTube video.  
- Convert video audio to MP3.  
- Choose a local folder for downloads (config saved automatically).  
- Optionally upload MP3 files to a specific Dropbox folder.  
- GUI built with Tkinter for easy use.  

---

## Screenshot of GUI


<img width="705" height="231" alt="Yt Converter Gui" src="https://github.com/user-attachments/assets/3dfd6774-1c46-44e9-8005-e4c51b5e9d51" />

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/josh-keilder/song-downloader.git
cd song-downloader
```
2. **Create and activate a Virtual Environment**
```bash
python -m venv .venv
.venv\Scripts\Activate
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
## Optional Dropbox Setup
- Create a .env file in the project root:
```ini
DROPBOX_ACCESS_TOKEN=your_dropbox_access_token_here
```
- You can get an access token for dropbox by creating an app on dropbox.

**IMPORTANT NOTES**
- Make sure to enable "files.content.write" in the permissions tab.
  <img width="662" height="65" alt="Dropbox permissions ss" src="https://github.com/user-attachments/assets/13511807-874e-44dc-ace7-9de4f16eee92" />
- Create a Dropbox folder and set it in config.json.
  <img width="1099" height="79" alt="Folder name ss" src="https://github.com/user-attachments/assets/c3152a77-c740-4ee9-8320-74725da29d5a" />
```json
{
    "local_folder": "",
    "dropbox_folder": "your_dropbox_app_folder_name_here"
}
```

## Usage

1. **Run the program:**

```bash
python yt_converter.py
```
2. **When the GUI opens:**
  - Enter a youtube link
  - Select whether to upload to Dropbox.
  - Click Convert
  - Optionally, change your download folder with the **Change Download Output Folder** button
3. **Your MP3 will be saved locally, and uploaded to Dropbox if selected.**
