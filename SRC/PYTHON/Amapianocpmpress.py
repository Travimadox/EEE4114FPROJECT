import tempfile
import os
from pydub import AudioSegment 

def compress_mp3_return_wav(original_audio_file, bitrate="128k"):
    audio = AudioSegment.from_file(original_audio_file, format="wav")

    # Temporary MP3 Conversion
    with tempfile.NamedTemporaryFile(suffix='.mp3') as temp_mp3:
        audio.export(temp_mp3.name, format="mp3", bitrate=bitrate)

        # Load back from the temporary MP3 file
        temp_audio = AudioSegment.from_mp3(temp_mp3.name)

        # Construct the output WAV filename 
        original_filename = os.path.splitext(os.path.basename(original_audio_file))[0] 
        output_folder = "AmapianoCompressed" + bitrate  # Dynamic output folder
        output_wav_filename = os.path.join(output_folder, original_filename + ".wav")

        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True) 

        # Export and save as WAV 
        temp_audio.export(output_wav_filename, format="wav") 



# Main Processing Logic
audio_folder = "Amapiano"
bitrates = ["64k", "128k", "256k"]

for filename in os.listdir(audio_folder):
    if filename.endswith(".wav"):
        filepath = os.path.join(audio_folder, filename)
        for bitrate in bitrates:
            compress_mp3_return_wav(filepath, bitrate)  