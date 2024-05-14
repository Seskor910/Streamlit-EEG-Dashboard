import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io
import seaborn as sns
import os
import glob
import mne
import copy
import logging
from scipy.signal import coherence
from scipy.signal import csd, welch
from matplotlib import cm
from scipy.signal import hilbert
from matplotlib.colors import LogNorm
from mne_connectivity import spectral_connectivity_epochs

def proses_correlation(epoch_directory, csv_directory_correlation):
    directory_path = epoch_directory
    selected_electrodes_names = ['FT7', 'T7', 'TP7', 'TP8', 'T8', 'FT8', 'F3', 'F4']
    file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".fif")]
    save_csv_path = csv_directory_correlation
    total_epochs = 0
    for file_path in file_paths:
        epochs = mne.read_epochs(file_path, preload=True)
        num_epochs = len(epochs)
        total_epochs += num_epochs
        file_basename = os.path.basename(file_path).split('.')[0]
        print(f"{os.path.basename(file_path)}: {num_epochs} epochs")

        for epoch_idx, epoch_data in enumerate(epochs.get_data()):
            selected_indices = [epochs.ch_names.index(name) for name in selected_electrodes_names if name in epochs.ch_names]
            selected_data = epoch_data[selected_indices]
            column_labels = [epochs.ch_names[idx] for idx in selected_indices]
            df = pd.DataFrame(selected_data.T, columns=column_labels)
            correlation_matrix = df.corr()
            
            csv_filename = f"{file_basename}_correlation_matrix_epoch_{epoch_idx + 1}.csv"
            csv_file_path = os.path.join(save_csv_path, csv_filename)
            correlation_matrix.to_csv(csv_file_path)
    print(f"Total epochs loaded: {total_epochs}")