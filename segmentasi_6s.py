import mne
import scipy.io as sio
import os
from glob import glob

def process_fif_to_epochs(fif_directory, epoch_directory):
    # Load file .fif nya
    fif_files = glob(os.path.join(fif_directory, '*.fif'))

    # Memilih channel
    selected_channels = ['FT7', 'T7', 'TP7', 'TP8', 'T8', 'FT8', 'F3', 'F4']

    # Proses segmentasi
    for fif_file_path in fif_files:
        raw = mne.io.read_raw_fif(fif_file_path, preload=True)

        # Membuat epoch-epochnya
        events = mne.make_fixed_length_events(raw, start=0, duration=6)
        epochs = mne.Epochs(raw, events, tmin=0, tmax=5.999, baseline=None, preload=True, picks=selected_channels)

        # Menyimpan epoch-epochnya
        epoch_filename = os.path.splitext(os.path.basename(fif_file_path))[0] + '-epo.fif'
        epochs.save(os.path.join(epoch_directory, epoch_filename), overwrite=True)
        print(f"Saved epochs to {epoch_filename}")