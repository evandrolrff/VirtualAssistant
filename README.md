# Assistant Alfred

## Technologies
    * Voice recognition:
      * Google - online (package *SpeechRecognition*).
      * Vosk - offline (package *vosk*) and need to configure the model in the `recognizers/model/` folder. The models can be downloaded from [Models](https://alphacephei.com/vosk/models)
    * Speech synthesis.
      * We will use package *pyttsx3*.
    * AI technology.
      * We will use package *tensorflow*.

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
pip install PyYAML
pip install numpy
pip install tensorflow

# To export a list of all installed packages
pip freeze > requirements.txt

# Install packages from requirements
pip install -r requirements. txt

```