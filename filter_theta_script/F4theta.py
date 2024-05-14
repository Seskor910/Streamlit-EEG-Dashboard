import mne
import scipy.io as sio
import os
from glob import glob

def filter_to_theta_F4(epoch_directory, F4_theta_directory):
    # Define the directory containing the source files
    fif_files = glob(os.path.join(epoch_directory, '*.fif'))

    for fif_file_path in fif_files:
        # Load the .fif file
        raw = mne.read_epochs(fif_file_path, preload=True)

        # Select channel and filter for the theta band (4-7 Hz)
        raw.pick_channels(['F4']).filter(4, 7)

        # Saving the filtered signal
        filtered_filename = os.path.basename(fif_file_path).replace('.fif', '_F4_theta-band.fif')
        filtered_output_path = os.path.join(F4_theta_directory, filtered_filename)
        raw.save(filtered_output_path, overwrite=True)
        print(f'Filtered data saved to {filtered_output_path}')