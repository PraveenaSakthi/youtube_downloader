from pytube import YouTube

def download_video(url):
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        print("Downloading:", video.title)
        stream.download()
        print("Download completed!")
    except Exception as e:
        print("Error:", str(e))
url = input("Enter the URL of the YouTube video: ")
download_video(url)
