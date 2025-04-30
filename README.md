# 🧠 Assistant Alfred
Assistant Alfred is a smart assistant powered by voice recognition, speech synthesis, and artificial intelligence. It enables natural voice interactions, allowing users to speak commands and receive spoken responses, all with offline and online support.

## 🚀 Features

🎙️ Voice recognition (online and offline)

🗣️ Text-to-speech audio responses

🤖 Command classification using deep learning (TensorFlow)

🧩 Modular architecture for easy extension

## 🛠️ Technologies Used
### 🎧 Voice Recognition
- Google Speech Recognition (online)
  - Package: SpeechRecognition
- Vosk (offline)
  - Package: vosk
  > Requires configuration of a speech model in the recognizers/model/ folder. Models can be downloaded from: [Vosk Models](https://alphacephei.com/vosk/models)

### 🔊 Speech Synthesis
- pyttsx3 – a cross-platform, offline Text-to-Speech engine
  - Package: pyttsx3

### 🧠 Artificial Intelligence
- TensorFlow – used to build a neural network that classifies spoken commands. The AI model is based on the following architecture:
  - An Embedding layer that converts input characters into dense vector representations.

  - An LSTM (Long Short-Term Memory) layer with 128 units, capable of capturing temporal dependencies in sequences.

  - A Dense output layer with a softmax activation function, used for classifying the input into one of the predefined command labels.

This model is trained to interpret voice commands by converting them into sequences of characters and mapping them to specific intent labels.

## ⚙️ Installation
1. Create a virtual environment (optional, but recommended)
```bash
python -m venv my-virtual-env
```

2. Activate the virtual environment
- Windows
```bash
my-virtual-env\Scripts\activate
```

-Linux/MacOS
```bash
source my-virtual-env/Scripts/activate.bat
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```

> If you don't have a requirements.txt file yet, generate it with:
```bash 
pip freeze > requirements.txt
```

## 🧪 How to Use
1. Make sure your microphone is working properly.
2. Download and place a Vosk offline model (if you prefer offline usage).
3. Run the main script:

```bash
python main.py
```
4. Speak to the assistant and it will respond both in text and with synthesized voice.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License
This project is licensed under the MIT License.