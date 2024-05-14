import mne
import scipy.io as sio
import os
from glob import glob

def filter_to_beta_FT8(epoch_directory, FT8_beta_directory):
    # Define the directory containing the source files
    fif_files = glob(os.path.join(epoch_directory, '*.fif'))

    for fif_file_path in fif_files:
        # Load the .fif file
        raw = mne.read_epochs(fif_file_path, preload=True)

        # Select channel and filter for the beta band (12-30 Hz)
        raw.pick_channels(['FT8']).filter(12, 30)

        # Saving the filtered signal
        filtered_filename = os.path.basename(fif_file_path).replace('.fif', '_FT8_beta-band.fif')
        filtered_output_path = os.path.join(FT8_beta_directory, filtered_filename)
        raw.save(filtered_output_path, overwrite=True)
        print(f'Filtered data saved to {filtered_output_path}')