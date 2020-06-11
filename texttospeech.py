import pyttsx3

def text_to_speech(user_text):
    """
    Parameters:
    user_text (str): string message to be converted to audio and output using speakers available
    """
    try:
        engine = pyttsx3.init()
        engine.say(user_text)
        engine.runAndWait()
    except:
        print("ERROR: unknown error in text to speech")

if __name__ == "__main__":
    print('Welcome to Text to Speech')
    text_to_speech('This is the demo to Python Text to Speech')
    text_to_speech('Pretty exciting isnt it?')
    text_to_speech('Welcome')
