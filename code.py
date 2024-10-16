import speech_recognition as sr
import os
from langdetect import detect, LangDetectException

# Initialize the recognizer
r = sr.Recognizer()

# Function to detect the language of the text
def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except LangDetectException:
        print("Could not detect language for the given text.")
        return None

# Function to recognize speech from an audio file and detect the language
def recognize_speech_from_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None, None
    
    with sr.AudioFile(file_path) as source:
        total_duration = source.DURATION  # Get the total duration of the audio file
        chunk_duration = 30  # Duration (in seconds) of each chunk to process at once
        start_time = 0
        recognized_text = ""
        language_detected = None
        
        while start_time < total_duration:
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise for each chunk
            # Record a chunk of the audio (30 seconds at a time)
            audio = r.record(source, offset=start_time, duration=chunk_duration)
            
            # Try recognizing speech (defaulting to English, then Tamil if fails)
            try:
                text = r.recognize_google(audio, language='en-US')  # Try English first
                detected_lang = detect_language(text)
                if detected_lang == 'en':
                    print(f"Recognized (EN) from {start_time}s to {start_time + chunk_duration}s: " + text)
                    recognized_text += text + " "
                    language_detected = 'en'
                else:
                    print("Recognized text was not in English, detected language:", detected_lang)
            except sr.UnknownValueError:
                print(f"Could not understand in English from {start_time}s to {start_time + chunk_duration}s.")
            
            # If English fails, try Tamil
            try:
                text = r.recognize_google(audio, language='ta-IN')  # Try Tamil
                detected_lang = detect_language(text)
                if detected_lang == 'ta':
                    print(f"Recognized (TA) from {start_time}s to {start_time + chunk_duration}s: " + text)
                    recognized_text += text + " "
                    language_detected = 'ta'
                else:
                    print("Recognized text was not in Tamil, detected language:", detected_lang)
            except sr.UnknownValueError:
                print(f"Could not understand in Tamil from {start_time}s to {start_time + chunk_duration}s.")
            
            start_time += chunk_duration  # Move to the next chunk
        
        return recognized_text.strip(), language_detected

# Function to write recognized text to a file
def write_to_file(text, language):
    filename = f"output_{language}.txt"
    with open(filename, "a", encoding='utf-8') as file:  # Append to file instead of overwriting
        file.write(text + "\n")
    print(f"Text written to {filename}")

# Main function
def main(file_path):
    recognized_text, language = recognize_speech_from_file(file_path)
    if recognized_text:
        write_to_file(recognized_text, language)

if __name__== "__main__":
    # Provide the path to the audio file you want to recognize
    file_path = "audiodata.wav"  # Replace with your actual audio file path
    main(file_path)
