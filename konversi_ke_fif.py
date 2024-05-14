import os
import mne
import scipy.io as sio
import logging

def konversi_ke_fif(file, fif_directory):
    # Set logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Define the path to the .mat file
    mat_file_path = file

    try:
        # load mat file
        mat = sio.loadmat(mat_file_path)

        # Function to extract the key for EEG data from the .mat file
        def get_eeg_key(mat):
            for key in mat.keys():
                if key.startswith('a') and key.endswith('mat'):
                    return key
            return None
        
        # Ekstraksi data key EEG
        eeg_key = get_eeg_key(mat)
        if eeg_key is None:
            logging.warning(f"EEG data key not found in {mat_file_path}. Skipping file.")
            return

        # Load the EEG data, sampling rate, and define channel names
        data = mat[eeg_key]
        sampling_rate = mat['samplingRate'][0, 0]
        channel_names = ['EEG%03d' % (i + 1) for i in range(data.shape[0])]

        # Create MNE info object
        info = mne.create_info(ch_names=channel_names, sfreq=sampling_rate, ch_types='eeg')
        
        # Transpose data if necessary
        if data.shape[0] != len(channel_names):
            data = data.T
        
        # Create RawArray
        raw = mne.io.RawArray(data, info)

        # Rename Channels
        channels_to_plot = {
            'EEG039': 'FT7', 'EEG045': 'T7', 'EEG050': 'TP7',
            'EEG101': 'TP8', 'EEG108': 'T8', 'EEG115': 'FT8',
            'EEG024': 'F3', 'EEG124': 'F4'
        }
        mne.rename_channels(raw.info, channels_to_plot)

        # Output fif file name
        fif_filename = os.path.splitext(os.path.basename(mat_file_path))[0] + '.fif'
        output_path = os.path.join(fif_directory, fif_filename)

        # save data
        raw.save(output_path, overwrite=True)
        logging.info(f'Converted {mat_file_path} to {output_path}')

    except Exception as e:
        logging.error(f"Error processing {mat_file_path}: {e}")
