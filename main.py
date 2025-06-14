from pytubefix import YouTube

def download(link):
    youtube = YouTube(link)
    youtube = youtube.streams.filter(progressive=True, file_extension="mp4").first()
    try:
        youtube.download()
    except:
        print("Error")
    print("Download Success!")

link = input("Enter youtube url: ")
download(link)