import speech_recognition as sr

def main():
    print("Welcome! I'm Alfred your assistant virtual!")

    # Create a recognizer instance
    r = sr.Recognizer()

    while True:
        try:
            # Capture audio from the microphone
            with sr.Microphone() as source:
                print("Say something...")
                audio = r.listen(source)

            # Convert speech to text
            text = r.recognize_google(audio)
            print(f"You said: {text}")

            # Process the text (e.g., respond to commands)
            if "hello" in text.lower():
                print("Hello! How can I assist you today?")
            elif "goodbye" in text.lower():
                print("Goodbye! Have a great day.")
                break
        except sr.UnknownValueError:
            print("I didn't understand that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")



if __name__ == "__main__":
    main()