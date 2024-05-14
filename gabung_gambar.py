import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def proses_gabung_gambar(csv_directories_correlation,
                         csv_directories_theta,
                         csv_directories_delta,
                         csv_directories_alpha,
                         csv_directories_beta,
                         csv_directories_gamma,
                         combined_image):
    
    # Folder paths for each type of data
    folders = {
        "Correlation": csv_directories_correlation,
        "Theta": csv_directories_theta,
        "Delta": csv_directories_delta,
        "Alpha": csv_directories_alpha,
        "Beta": csv_directories_beta,
        "Gamma": csv_directories_gamma
    }

    output_dir = combined_image

    def process_files(files_dict):
        matrices = {}
        for key, filepath in files_dict.items():
            matrix = pd.read_csv(filepath, index_col=0).values[:8, :8]
            matrices[key] = matrix
        
        # Membuat matriks
        large_matrix = np.zeros((16, 24))
        positions = [(0, 0), (0, 8), (0, 16), (8, 0), (8, 8), (8, 16)]
        keys = ["Correlation", "Theta", "Delta", "Alpha", "Beta", "Gamma"]

        for key, pos in zip(keys, positions):
            large_matrix[pos[0]:pos[0]+8, pos[1]:pos[1]+8] = matrices[key]
        
        plt.figure(figsize=(12, 8))
        plt.imshow(large_matrix, cmap='viridis', aspect='auto')
        
        save_path = os.path.join(output_dir, f"combined_matrix_{index+1}.png")
        plt.savefig(save_path)
        plt.close()

    file_lists = {key: sorted([os.path.join(path, file) for file in os.listdir(path)]) for key, path in folders.items()}

    for index in range(len(file_lists["Correlation"])):
        files_dict = {key: file_lists[key][index] for key in file_lists}
        process_files(files_dict)
