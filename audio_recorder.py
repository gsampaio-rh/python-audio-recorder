import pyaudio
import wave
import datetime

# constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".wav"

# get list of available input devices and their indices
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
print("Available input devices:")
for i in range(numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

# set input device index to record from the sound card output
input_device_index = int(input("Enter the device ID to record: "))

# get the device name
device_name = p.get_device_info_by_index(input_device_index)['name']

# start recording
print(f"Starting to record device {device_name} ...")
frames = []
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=input_device_index,
                frames_per_buffer=CHUNK)
try:
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        # print volume bar
        volume = max(data)
        bars = "#" * int(50 * volume / 32768)
        print(f"\r[{bars:50}] {volume:.2f} dBFS", end='', flush=True)
except KeyboardInterrupt:
    # save recording to WAV file
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # print recording length and filename
    print("\nRecording stopped")
    recording_length = datetime.timedelta(seconds=len(frames) / RATE)
    print("Recording length:", recording_length)
    print("Recording saved as:", WAVE_OUTPUT_FILENAME)
