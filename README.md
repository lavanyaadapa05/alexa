content = """# Alexa Clone with SoundDevice Integration

This project is a simple voice assistant (like Alexa) built using Python. It listens for commands using the microphone, processes the audio, and responds using text-to-speech. The assistant can play songs, tell the time, give jokes, and search Wikipedia, among other functionalities.

The project uses the following libraries:
- `speech_recognition`: For converting speech into text.
- `pyttsx3`: For text-to-speech conversion.
- `pywhatkit`: For playing songs on YouTube.
- `datetime`: For getting the current time.
- `wikipedia`: For fetching information from Wikipedia.
- `pyjokes`: For telling jokes.
- `sounddevice`: For capturing audio from the microphone.

## Installation

### Prerequisites
Ensure you have Python 3.6 or higher installed on your machine. You can check this by running:

```bash
python --version
```

### Setup Instructions

1. Clone the repository: If you haven't already cloned the repository, run the following command:

```bash
git clone https://github.com/your-username/alexa-clone.git
```

2. Install the required dependencies:
   - Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

   - Activate the virtual environment:
     - On Windows:

```bash
.\venv\Scripts\activate
```
     - On macOS/Linux:

```bash
source venv/bin/activate
```

   - Install dependencies:

```bash
pip install -r requirements.txt
```

   Or install each dependency individually:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes sounddevice scipy
```

3. Microphone Setup: Make sure you have a working microphone connected to your system. The script uses sounddevice to capture audio from the microphone.

4. Run the Application: Run the script by executing:

```bash
python run.py
```

The program will continuously listen for the keyword "alexa" and process your voice commands.

## Code Explanation

### Main Components:
- `talk(text)`: This function takes a string of text as input and uses pyttsx3 to convert it into speech. The assistant speaks the text out loud.
- `record_audio()`: This function uses the sounddevice library to record audio from the microphone. The recorded audio is saved as a WAV file, which is later used for speech recognition.
- `take_command()`: This function listens for audio commands. It:
  - Uses the `record_audio()` function to capture the audio.
  - Converts the audio into text using the `speech_recognition` library.
  - Filters out the keyword "alexa" from the command if present.
  - Returns the recognized command as text.
- `run_alexa()`: This function runs the logic for different commands. It:
  - Calls `take_command()` to get the user's speech.
  - Processes the command and takes appropriate action, such as:
    - Playing a song on YouTube.
    - Telling the current time.
    - Giving information about a person (via Wikipedia).
    - Telling a joke.
  - If the command is not recognized, it prompts the user to say the command again.

### Functionalities:
- **Play songs**: The assistant can play songs on YouTube using the pywhatkit library by saying "play [song name]".
- **Tell time**: The assistant can tell the current time by saying "time".
- **Wikipedia search**: The assistant can fetch a summary of a person or topic from Wikipedia by saying "who the heck is [person]" or similar commands.
- **Tell jokes**: The assistant can tell random jokes using the pyjokes library.
- **Handle unknown commands**: If the command is not recognized, the assistant prompts the user to repeat the command.
