from moviepy.editor import VideoFileClip 


def towav(input, output):
    video = VideoFileClip(input)
    audio = video.audio

    #Write the audiofile
    audio.write_audiofile(output, codec = "pcm_s16le")

    #Close the objects
    audio.close()
    video.close()