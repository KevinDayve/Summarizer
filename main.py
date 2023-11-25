from video import video
from audio import towav
from asr import transcribe
from summary import summarise_text

def main():
    yt_link = input("Enter YouTube video link: ")
    video_download_status = video(yt_link)

    if video_download_status == "Success":
        towav("ytaudio.mp4", "audio.wav")
        transcription = transcribe("audio.wav")
        summary = summarise_text(transcription)
        print("Summary: \n", summary)
    else:
        print("Could not download YouTube video")

if __name__ == "__main__":
    main()