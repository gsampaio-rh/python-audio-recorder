# Audio Recorder

This Python script records audio from the specified input device until it is stopped by the user. The recorded audio is saved as a WAV file.

## Requirements

- Python 3
- PyAudio library

## Usage

1. To install the required dependencies from the requirements.txt file, run the following command in your terminal:

```pip install -r requirements.txt```

2. Run the `audio_recorder.py` script:

```python audio_recorder.py```

3. Select the input device to record from by entering its ID when prompted.

4. The script will start recording and display a volume bar that shows the current input level. To stop recording, press `Ctrl+C`.

5. The recorded audio will be saved as a WAV file in the current directory. The file name will include the date and time of the recording.

## Notes

- If you have trouble recording from a specific input device, try changing the `CHANNELS`, `RATE`, or `FORMAT` constants in the script.
- The volume bar shows the input level in decibels relative to full scale (dBFS). A value of 0 dBFS represents the maximum possible input level.
