import os
import csv
import soundfile as sf
import numpy as np

# Define the directories
directories = {
    '64': 'BongoCompressed64k',
    '128': 'BongoCompressed128k',
    '256': 'BongoCompressed256k'
}

# Open the CSV file
with open('Bongoresults.csv', 'w', newline='') as csvfile:
    fieldnames = ['filename', 'bitrate', 'snr', 'psnr', 'ssim']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Loop over the directories
    for bitrate, directory in directories.items():
        # Get all files in the directory
        files = os.listdir(directory)

        # Loop over the files
        for file in files:
            # Read the original and degraded audio files
            original_audio, fs = sf.read('Bongo//{file}')
            degraded_audio, fs = sf.read('{directory}//{file}')

            # Handle potential multi-channel audio
            if len(original_audio.shape) > 1:
                original_audio = original_audio[:, 0]  # Use the first channel
            if len(degraded_audio.shape) > 1:
                degraded_audio = degraded_audio[:, 0]  # Use the first channel

            # Calculate metrics
            snr_value = snr(original_audio, degraded_audio)
            psnr_value = psnr(original_audio, degraded_audio)
            ssim_value = ssim(original_audio, degraded_audio)

            # Write the results to the CSV file
            writer.writerow({
                'filename': file,
                'bitrate': bitrate,
                'snr': snr_value,
                'psnr': psnr_value,
                'ssim': ssim_value
            })