import os

from folders import rafael_wav_folder

# Read the list of words from your text file
with open('words.txt', 'r') as file:
    word_list = file.read().splitlines()

folder_path = rafael_wav_folder()

# Use glob to get a list of all WAV files in the folder
file_list = os.listdir(folder_path)

# Iterate through the files and rename them
for index, filename in enumerate(file_list):
    if filename.startswith('word-'):
        # Extract the number from the filename
        number = int(filename.split('-')[1].split('.')[0])
        if 1 <= number <= len(word_list):
            new_name = word_list[number - 1] + '.wav'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
            print(f'Renamed {filename} to {new_name}')
        else:
            print(f'File {filename} does not have a corresponding word in the list.')

print('Rename process completed.')