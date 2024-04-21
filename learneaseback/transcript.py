import assemblyai as aai
from moviepy.editor import VideoFileClip

def give_transscript(video_path):
    # CONVERTING VIDEO TO AUDIO
    # Replace with your API key
    aai.settings.api_key = "e7d8d5a3801f4ceab1b87cc463aae0a8"

    # URL of the file to transcribe
    FILE_URL = video_path#file path

    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)

    if transcript.status == aai.TranscriptStatus.error:
        return transcript.error
    else:

        return transcript.text