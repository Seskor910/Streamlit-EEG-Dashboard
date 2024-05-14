import streamlit as st
import os
import sys
import tempfile

# Script alpha filter
sys.path.append(r'E:\Vscode\Tugas Anime\Dashboard\filter_alpha_script')

# Now you can import the modules by their file names without the '.py' extension
from F3alpha import filter_to_alpha_F3
from F4alpha import filter_to_alpha_F4
from FT7alpha import filter_to_alpha_FT7
from FT8alpha import filter_to_alpha_FT8
from T7alpha import filter_to_alpha_T7
from T8alpha import filter_to_alpha_T8
from TP7alpha import filter_to_alpha_TP7
from TP8alpha import filter_to_alpha_TP8

# Script delta filter
sys.path.append(r'E:\Vscode\Tugas Anime\Dashboard\filter_delta_script')

from F3delta import filter_to_delta_F3
from F4delta import filter_to_delta_F4
from FT7delta import filter_to_delta_FT7
from FT8delta import filter_to_delta_FT8
from T7delta import filter_to_delta_T7
from T8delta import filter_to_delta_T8
from TP7delta import filter_to_delta_TP7
from TP8delta import filter_to_delta_TP8

# Script theta filter
sys.path.append(r'E:\Vscode\Tugas Anime\Dashboard\filter_theta_script')

from F3theta import filter_to_theta_F3
from F4theta import filter_to_theta_F4
from FT7theta import filter_to_theta_FT7
from FT8theta import filter_to_theta_FT8
from T7theta import filter_to_theta_T7
from T8theta import filter_to_theta_T8
from TP7theta import filter_to_theta_TP7
from TP8theta import filter_to_theta_TP8

# Script beta filter
sys.path.append(r'E:\Vscode\Tugas Anime\Dashboard\filter_beta_script')

from F3beta import filter_to_beta_F3
from F4beta import filter_to_beta_F4
from FT7beta import filter_to_beta_FT7
from FT8beta import filter_to_beta_FT8
from T7beta import filter_to_beta_T7
from T8beta import filter_to_beta_T8
from TP7beta import filter_to_beta_TP7
from TP8beta import filter_to_beta_TP8

# Script gamma filter
sys.path.append(r'E:\Vscode\Tugas Anime\Dashboard\filter_gamma_script')

from F3gamma import filter_to_gamma_F3
from F4gamma import filter_to_gamma_F4
from FT7gamma import filter_to_gamma_FT7
from FT8gamma import filter_to_gamma_FT8
from T7gamma import filter_to_gamma_T7
from T8gamma import filter_to_gamma_T8
from TP7gamma import filter_to_gamma_TP7
from TP8gamma import filter_to_gamma_TP8

# Script coherence
sys.path.append(r'E:\Vscode\Tugas Anime\Dashboard\coherence')

from coherence_alpha import proses_coherence_alpha
from coherence_beta import proses_coherence_beta
from coherence_delta import proses_coherence_delta
from coherence_gamma import proses_coherence_gamma
from coherence_theta import proses_coherence_theta


st.title('EEG Dashboard')

uploaded_file = st.file_uploader("Upload a .mat file", type=['mat'])
if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # Use a temporary file to avoid conflicts
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mat") as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_path = tmp.name

    # Directory paths
    base_directory = r'E:\Vscode\Tugas Anime\Dashboard'
    fif_directory = os.path.join(base_directory, 'fif_directory')
    epoch_directory = os.path.join(base_directory, 'epoch_directory')
    combined_image_directory = os.path.join(base_directory, 'combined_image')
    channel_directoriesalpha = {
        'F3': os.path.join(base_directory, 'channel_directory', 'filter_channel_F3', 'alpha_band'),
        'F4': os.path.join(base_directory, 'channel_directory', 'filter_channel_F4', 'alpha_band'),
        'FT7': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT7', 'alpha_band'),
        'FT8': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT8', 'alpha_band'),
        'T7': os.path.join(base_directory, 'channel_directory', 'filter_channel_T7', 'alpha_band'),
        'T8': os.path.join(base_directory, 'channel_directory', 'filter_channel_T8', 'alpha_band'),
        'TP7': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP7', 'alpha_band'),
        'TP8': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP8', 'alpha_band'),
        # Define other channels similarly...
    }
    channel_directoriesdelta = {
        'F3': os.path.join(base_directory, 'channel_directory', 'filter_channel_F3', 'delta_band'),
        'F4': os.path.join(base_directory, 'channel_directory', 'filter_channel_F4', 'delta_band'),
        'FT7': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT7', 'delta_band'),
        'FT8': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT8', 'delta_band'),
        'T7': os.path.join(base_directory, 'channel_directory', 'filter_channel_T7', 'delta_band'),
        'T8': os.path.join(base_directory, 'channel_directory', 'filter_channel_T8', 'delta_band'),
        'TP7': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP7', 'delta_band'),
        'TP8': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP8', 'delta_band'),
        # Define other channels similarly...
    }
    channel_directoriestheta = {
        'F3': os.path.join(base_directory, 'channel_directory', 'filter_channel_F3', 'theta_band'),
        'F4': os.path.join(base_directory, 'channel_directory', 'filter_channel_F4', 'theta_band'),
        'FT7': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT7', 'theta_band'),
        'FT8': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT8', 'theta_band'),
        'T7': os.path.join(base_directory, 'channel_directory', 'filter_channel_T7', 'theta_band'),
        'T8': os.path.join(base_directory, 'channel_directory', 'filter_channel_T8', 'theta_band'),
        'TP7': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP7', 'theta_band'),
        'TP8': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP8', 'theta_band'),
        # Define other channels similarly...
    }
    channel_directoriesbeta = {
        'F3': os.path.join(base_directory, 'channel_directory', 'filter_channel_F3', 'beta_band'),
        'F4': os.path.join(base_directory, 'channel_directory', 'filter_channel_F4', 'beta_band'),
        'FT7': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT7', 'beta_band'),
        'FT8': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT8', 'beta_band'),
        'T7': os.path.join(base_directory, 'channel_directory', 'filter_channel_T7', 'beta_band'),
        'T8': os.path.join(base_directory, 'channel_directory', 'filter_channel_T8', 'beta_band'),
        'TP7': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP7', 'beta_band'),
        'TP8': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP8', 'beta_band'),
        # Define other channels similarly...
    }
    channel_directoriesgamma = {
        'F3': os.path.join(base_directory, 'channel_directory', 'filter_channel_F3', 'gamma_band'),
        'F4': os.path.join(base_directory, 'channel_directory', 'filter_channel_F4', 'gamma_band'),
        'FT7': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT7', 'gamma_band'),
        'FT8': os.path.join(base_directory, 'channel_directory', 'filter_channel_FT8', 'gamma_band'),
        'T7': os.path.join(base_directory, 'channel_directory', 'filter_channel_T7', 'gamma_band'),
        'T8': os.path.join(base_directory, 'channel_directory', 'filter_channel_T8', 'gamma_band'),
        'TP7': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP7', 'gamma_band'),
        'TP8': os.path.join(base_directory, 'channel_directory', 'filter_channel_TP8', 'gamma_band'),
        # Define other channels similarly...
    }
    csv_directories = {
        'alpha': os.path.join(base_directory, 'csv_data', 'alpha_band'),
        'beta': os.path.join(base_directory, 'csv_data', 'beta_band'),
        'delta': os.path.join(base_directory, 'csv_data',  'delta_band'),
        'theta': os.path.join(base_directory, 'csv_data',  'theta_band'),
        'gamma': os.path.join(base_directory, 'csv_data', 'gamma_band'),
        'correlation': os.path.join(base_directory, 'csv_data', 'correlation'),
        # Define other channels similarly...
    }
    
    try:
        from konversi_ke_fif import konversi_ke_fif
        from segmentasi_6s import process_fif_to_epochs
        
        konversi_ke_fif(temp_path, fif_directory)
        st.success(f"File '{uploaded_file.name}' converted successfully!")

        os.makedirs(fif_directory, exist_ok=True)
        os.makedirs(epoch_directory, exist_ok=True)

        process_fif_to_epochs(fif_directory, epoch_directory)
        st.success("Epochs created successfully.")

        # Filter to alpha band per channel
        filter_to_alpha_F3(epoch_directory, channel_directoriesalpha['F3'])
        filter_to_alpha_F4(epoch_directory, channel_directoriesalpha['F4'])
        filter_to_alpha_FT7(epoch_directory, channel_directoriesalpha['FT7'])
        filter_to_alpha_FT8(epoch_directory, channel_directoriesalpha['FT8'])
        filter_to_alpha_T7(epoch_directory, channel_directoriesalpha['T7'])
        filter_to_alpha_T8(epoch_directory, channel_directoriesalpha['T8'])
        filter_to_alpha_TP7(epoch_directory, channel_directoriesalpha['TP7'])
        filter_to_alpha_TP8(epoch_directory, channel_directoriesalpha['TP8'])
        # Add calls to other channel-specific functions similarly...

        st.success("Alpha band filtering completed successfully.")

        # Filter delta band per channel
        filter_to_delta_F3(epoch_directory, channel_directoriesdelta['F3'])
        filter_to_delta_F4(epoch_directory, channel_directoriesdelta['F4'])
        filter_to_delta_FT7(epoch_directory, channel_directoriesdelta['FT7'])
        filter_to_delta_FT8(epoch_directory, channel_directoriesdelta['FT8'])
        filter_to_delta_T7(epoch_directory, channel_directoriesdelta['T7'])
        filter_to_delta_T8(epoch_directory, channel_directoriesdelta['T8'])
        filter_to_delta_TP7(epoch_directory, channel_directoriesdelta['TP7'])
        filter_to_delta_TP8(epoch_directory, channel_directoriesdelta['TP8'])

        st.success("Delta band filtering completed successfully.")

        # Filter theta band per channel
        filter_to_theta_F3(epoch_directory, channel_directoriestheta['F3'])
        filter_to_theta_F4(epoch_directory, channel_directoriestheta['F4'])
        filter_to_theta_FT7(epoch_directory, channel_directoriestheta['FT7'])
        filter_to_theta_FT8(epoch_directory, channel_directoriestheta['FT8'])
        filter_to_theta_T7(epoch_directory, channel_directoriestheta['T7'])
        filter_to_theta_T8(epoch_directory, channel_directoriestheta['T8'])
        filter_to_theta_TP7(epoch_directory, channel_directoriestheta['TP7'])
        filter_to_theta_TP8(epoch_directory, channel_directoriestheta['TP8'])

        st.success("Theta band filtering completed successfully.")

        # Filter beta band per channel
        filter_to_beta_F3(epoch_directory, channel_directoriesbeta['F3'])
        filter_to_beta_F4(epoch_directory, channel_directoriesbeta['F4'])
        filter_to_beta_FT7(epoch_directory, channel_directoriesbeta['FT7'])
        filter_to_beta_FT8(epoch_directory, channel_directoriesbeta['FT8'])
        filter_to_beta_T7(epoch_directory, channel_directoriesbeta['T7'])
        filter_to_beta_T8(epoch_directory, channel_directoriesbeta['T8'])
        filter_to_beta_TP7(epoch_directory, channel_directoriesbeta['TP7'])
        filter_to_beta_TP8(epoch_directory, channel_directoriesbeta['TP8'])

        st.success("Beta band filtering completed successfully.")

        # Filcorrelation per channel
        filter_to_gamma_F3(epoch_directory, channel_directoriesgamma['F3'])
        filter_to_gamma_F4(epoch_directory, channel_directoriesgamma['F4'])
        filter_to_gamma_FT7(epoch_directory, channel_directoriesgamma['FT7'])
        filter_to_gamma_FT8(epoch_directory, channel_directoriesgamma['FT8'])
        filter_to_gamma_T7(epoch_directory, channel_directoriesgamma['T7'])
        filter_to_gamma_T8(epoch_directory, channel_directoriesgamma['T8'])
        filter_to_gamma_TP7(epoch_directory, channel_directoriesgamma['TP7'])
        filter_to_gamma_TP8(epoch_directory, channel_directoriesgamma['TP8'])

        st.success("Gamma band filtering completed successfully.")

        # Coherence alpha band
        proses_coherence_alpha(channel_directoriesalpha['F3'],
                               channel_directoriesalpha['F4'],
                               channel_directoriesalpha['FT7'],
                               channel_directoriesalpha['FT8'],
                               channel_directoriesalpha['T7'],
                               channel_directoriesalpha['T8'],
                               channel_directoriesalpha['TP7'],
                               channel_directoriesalpha['TP8'],
                               csv_directories['alpha'])
        
        st.success("Alpha band coherence completed successfully.")

        # Coherence beta band
        proses_coherence_beta(channel_directoriesbeta['F3'],
                               channel_directoriesbeta['F4'],
                               channel_directoriesbeta['FT7'],
                               channel_directoriesbeta['FT8'],
                               channel_directoriesbeta['T7'],
                               channel_directoriesbeta['T8'],
                               channel_directoriesbeta['TP7'],
                               channel_directoriesbeta['TP8'],
                               csv_directories['beta'])
        
        st.success("Beta band coherence completed successfully.")

        # Coherence delta band
        proses_coherence_delta(channel_directoriesdelta['F3'],
                               channel_directoriesdelta['F4'],
                               channel_directoriesdelta['FT7'],
                               channel_directoriesdelta['FT8'],
                               channel_directoriesdelta['T7'],
                               channel_directoriesdelta['T8'],
                               channel_directoriesdelta['TP7'],
                               channel_directoriesdelta['TP8'],
                               csv_directories['delta'])
        
        st.success("Delta band coherence completed successfully.")

        # Coherence gamma band
        proses_coherence_gamma(channel_directoriesgamma['F3'],
                               channel_directoriesgamma['F4'],
                               channel_directoriesgamma['FT7'],
                               channel_directoriesgamma['FT8'],
                               channel_directoriesgamma['T7'],
                               channel_directoriesgamma['T8'],
                               channel_directoriesgamma['TP7'],
                               channel_directoriesgamma['TP8'],
                               csv_directories['gamma'])
        
        st.success("Gamma band coherence completed successfully.")

        # Coherence theta band
        proses_coherence_theta(channel_directoriestheta['F3'],
                               channel_directoriestheta['F4'],
                               channel_directoriestheta['FT7'],
                               channel_directoriestheta['FT8'],
                               channel_directoriestheta['T7'],
                               channel_directoriestheta['T8'],
                               channel_directoriestheta['TP7'],
                               channel_directoriestheta['TP8'],
                               csv_directories['theta'])
        
        st.success("Theta band coherence completed successfully.")

        # Correlation
        from correlation import proses_correlation
        proses_correlation(epoch_directory, csv_directories['correlation'])

        st.success("Correlation completed successfully.")

        # Penggabungan gambar
        from gabung_gambar import proses_gabung_gambar
        proses_gabung_gambar(csv_directories['correlation'],
                             csv_directories['theta'],
                             csv_directories['delta'],
                             csv_directories['alpha'],
                             csv_directories['beta'],
                             csv_directories['gamma'],
                             combined_image_directory)
        
        st.success("Combining images completed successfully.")

        # Testing kelas
        from test import proses_testing
        majority_class, class_count = proses_testing(combined_image_directory)
        st.success(f"Majority class detected: {majority_class}")
        st.write("Class counts:")
        st.write(class_count)
        
    except Exception as e:
        st.error(f"Failed to convert or process the file: {str(e)}")
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

else:
    st.info("Please upload a file.")
