# Assistant Alfred

## Technologies
    * Voice recognition.
    * Speech synthesis.
    * AI technology.

### Install Virtual Environment

```bash
python -m venv my-virtual-env

source my-virtual-env/Scripts/activate.bat

# always after use the virtual environment
deactivate

pip install SpeechRecognition
pip install pyaudio
pip install vosk
pip install pyttsx3
pip install sounddevice

# To export a list of all installed packages
pip freeze > requirements.txt

```