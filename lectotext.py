import whisper
import yt_dlp

def transcribe_audio_local(audio_file_path, model_name="base"):
    try:
        print(f"Loading Whisper model: {model_name}...")
        model = whisper.load_model(model_name)
        print("Model loaded. Starting transcription...")
        result = model.transcribe(audio_file_path)
        return result["text"]
    
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        return None

if __name__ == "__main__":
    # Replace 'your_audio_file.mp3' with the actual path to your audio file
    audio_file = "goose.mp3"
    model_name = "small"

    # You can choose a different model if needed, e.g., "medium"
    transcription = transcribe_audio_local(audio_file, model_name)

    if transcription:
        print("\n--- Transcription Result ---")
        print(transcription)
    else:
        print("Transcription failed.")