import os

def media_folder():
    # Get the current directory
    current_dir = os.getcwd()

    # Move one level up from the current directory
    return os.path.abspath(os.path.join(current_dir, os.pardir))

def rafael_wav_folder():
    # Specify the folder containing your sound files
    current_dir = os.getcwd()

    # Move one level up from the current directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # choose your directory
    folder_path = os.path.join(parent_dir, 'wav')
    return os.path.join(folder_path, 'rafael-pseudowords')


def giulia_wav_folder():
    # Specify the folder containing your sound files
    current_dir = os.getcwd()

    # Move one level up from the current directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # choose your directory
    folder_path = os.path.join(parent_dir, 'wav')
    return os.path.join(folder_path, 'giulia-pseudowords')

# def rafael_wav_folder():
#     # Specify the folder containing your sound files
#     current_dir = os.getcwd()

#     # Move one level up from the current directory
#     parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

#     # choose your directory
#     folder_path = os.path.join(parent_dir, 'wav')
#     return os.path.join(folder_path, 'microsoft-maria')

def dapa_ap_wav_folder():
    # choose your directory
    folder_path = os.path.join(media_folder(), 'wav')
    return os.path.join(folder_path, 'giulia-dapa-ap')