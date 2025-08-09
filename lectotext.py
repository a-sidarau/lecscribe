import time
import whisper
import yt_dlp
from datetime import datetime

# Replace 'file.mp3' with the actual path to your audio file
audio_file = "goose.mp3"
# Whisper model name. More on https://github.com/openai/whisper/blob/main/model-card.md
model_name = "small"

def transcribe_audio_local(audio_file_path, model_name="base"):
    '''
    Main function for audio-text trancription
    Get audio file and model name and convert audio into text using Whisper
    '''
    print("-" * 30)
    print(f"Loading Whisper model: {model_name}...")
    model = whisper.load_model(model_name)
    print("Model loaded. Starting transcription...")
    print("-" * 30)

    try:
        result = model.transcribe(audio_file_path)
        return result["text"]
    
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        return False


def write_to_file(text):
    # Writing transcribed text into file with timestamp in it's name
    # Get timestamp using built-in datetime module
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # creating filename from with timestamp
    filename = f"transcription_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Transcription succesfully written into file:")
    print(f"{filename}")


if __name__ == "__main__":

    transcription = transcribe_audio_local(audio_file, model_name)

    print("-" * 30)
    if transcription:
        print("Transcription Result:")
        print("-" * 30)
        print(transcription)
        print("-" * 30)
        write_to_file(transcription)
    else:
        print("--- Transcription failed.")
    print("-" * 30)

