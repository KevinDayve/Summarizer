from pytube import YouTube
def video(path):
    try:
        yt = YouTube(path)
        yt.streams.filter(only_audio=True, file_extension='.mp4').first().download(filename='ytaudio.mp4')
        return "Success"

    except Exception as e:
        print("Please check the link and try again")