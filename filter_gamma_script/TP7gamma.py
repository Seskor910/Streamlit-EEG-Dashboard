import mne
import scipy.io as sio
import os
from glob import glob

def filter_to_gamma_TP7(epoch_directory, TP7_gamma_directory):
    # Define the directory containing the source files
    fif_files = glob(os.path.join(epoch_directory, '*.fif'))

    for fif_file_path in fif_files:
        # Load the .fif file
        raw = mne.read_epochs(fif_file_path, preload=True)

        # Select channel and filter for the gamma band (30-45 Hz)
        raw.pick_channels(['TP7']).filter(30, 45)

        # Saving the filtered signal
        filtered_filename = os.path.basename(fif_file_path).replace('.fif', '_TP7_gamma-band.fif')
        filtered_output_path = os.path.join(TP7_gamma_directory, filtered_filename)
        raw.save(filtered_output_path, overwrite=True)
        print(f'Filtered data saved to {filtered_output_path}')