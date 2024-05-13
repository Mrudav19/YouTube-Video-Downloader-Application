import tkinter as tk
from tkinter import Label, Entry, Button, filedialog, OptionMenu, StringVar
from pytube import YouTube

class YouTubeDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.geometry('450x300')
        master.title("YouTube Video Downloader")

        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text='YouTube Video Downloader', font='Arial 15 bold').pack()

        self.link = tk.StringVar()
        Label(self.master, text='Paste Link Here:', font='Arial 13 bold').place(x=160, y=40)
        self.link_entry = Entry(self.master, width=45, textvariable=self.link)
        self.link_entry.place(x=50, y=90)

        # Video quality options
        self.video_quality = StringVar()
        self.video_quality.set("highest")  # Default selection
        self.quality_options = ["highest", "720p", "480p", "360p", "240p", "144p"]  # Add more options as needed
        Label(self.master, text='Select Quality:', font='Arial 13 bold').place(x=160, y=120)
        self.quality_menu = OptionMenu(self.master, self.video_quality, *self.quality_options)
        self.quality_menu.place(x=50, y=150)

        self.download_button = Button(self.master, text='Download', font='Arial 15 bold', padx=2, command=self.download_video)
        self.download_button.place(x=180, y=200)

    def download_video(self):
        try:
            url = YouTube(str(self.link.get()))
            video_quality = self.video_quality.get()
            if video_quality == "highest":
                video = url.streams.get_highest_resolution()
            else:
                video = url.streams.filter(res=video_quality).first()
            
            # Prompt user to select the directory to save the video
            destination_dir = filedialog.askdirectory()
            if destination_dir:  # If user selects a directory
                video.download(destination_dir)
                self.show_download_success()
        except Exception as e:
            self.show_download_error(str(e))

    def show_download_success(self):
        Label(self.master, text='Downloaded', font='Arial 15').place(x=180, y=250)

    def show_download_error(self, error_message):
        Label(self.master, text=f'Error: {error_message}', font='Arial 15', fg='red').place(x=150, y=250)

def main():
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
