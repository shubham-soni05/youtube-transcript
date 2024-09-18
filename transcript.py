from youtube_transcript_api import YouTubeTranscriptApi as yta
import pytube
import moviepy.editor as mp
import speech_recognition as sr

api_key = 'AIzaSyCrUgIJak68cYM4AEA-O3JB-Yz-9pDwhfw'

# Function to download the video using pytube
def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()
    return video.default_filename

# Function to convert video to audio using moviepy
def convert_video_to_audio(video_path, output_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path, codec='pcm_s16le')
    video_clip.close()
    audio_clip.close()

# Function to convert audio to text using speech_recognition
def convert_audio_to_text(audio_file):
    r = sr.Recognizer()
    r.energy_threshold = 400
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

# Specify the video URL
vid_url = "https://youtu.be/_ey_1I1aJ5w?si=QR1Li2i2wlbeTCSy"

# Extract the video ID from the URL
vid_id = vid_url.split("/")[-1]

try:
    # First code: Extract transcript from YouTube video
    data = yta.get_transcript(vid_id)
    transcript = ''
    for value in data:
        for key, val in value.items():
            if key == 'text':
                transcript += val

    lines = transcript.splitlines()
    final_tra = "".join(lines)

    with open("xyz.txt", "w") as file:
        file.write(final_tra)

    print("Transcript extraction complete!")

except Exception as e:
    

    # Second code: Download video, convert to audio, and convert audio to text
    video_path = download_video(vid_url)
    audio_file = "C://Users//shubh//OneDrive//Desktop//shubham//acadmics//project//youtube//audio_file//npt.wav"
    output_text_file = "output_text.txt"

    convert_video_to_audio(video_path, audio_file)
    converted_text = convert_audio_to_text(audio_file)

    with open(output_text_file, "w") as file:
        file.write(converted_text)

    print("Video to audio conversion complete!")
    print("Converted Text:")
    print(converted_text)