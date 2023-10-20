"""
Select jpg files from a (base) source directory and copy them to destination folders
corresponding to cycles.

Author: Carlos Rafael Fernandes Picanço
Date: August 24, 2023
License: GPL-3.0
"""

import os
import random
import shutil
from audio_synthetizer import synthetize

def get_random_word(words):
    '''Returns a random word from the given list of words.'''
    return words[random.randrange(len(words))]

def get_words_from_letter(letter, index, words):
    '''Returns a list of words that has letter at index position'''
    return [word for word in words if word[index] == letter]

def get_negative_comparisons(word, words):
    '''Returns a string with the negative comparisons for the given word.'''
    negative_comparisons = []
    for index, letter in enumerate(word):
        negative_comparisons.append(get_random_word(get_words_from_letter(letter, index, words)))
    return ' '.join(negative_comparisons)

def get_jpg_files(source_dir):
    '''Returns a list of jpg files in the source directory.'''
    return [file for file in os.listdir(source_dir) if file.endswith('.jpg')]

def select_files(files_list, alphanumeric_codes):
    '''Selects files from the files list based on the size of the alphanumeric_codes list and
    returns them as a dictionary with 'filename' and 'alphanumeric_code' keys.'''
    num_files = len(alphanumeric_codes)
    selected_files = [files_list.pop(random.randrange(len(files_list))) for _ in range(num_files)]
    selected_files_dict = [{'filename': file, 'alphanumeric_code': code} for file, code in zip(selected_files, alphanumeric_codes)]
    return selected_files_dict

def copy_files_to_folders(files, destination_dirs):
    '''Copies the given files to the specified destination folders using the
    alphanumeric_code as the filename.'''
    for folder_name in destination_dirs:
        os.makedirs(folder_name, exist_ok=True)
        for file_data in files:
            alphanumeric_code = file_data['alphanumeric_code']
            source_path = os.path.join(source_dir, file_data['filename'])
            destination_path = os.path.join(folder_name, alphanumeric_code + '.jpg')
            print('Copying Image from ', source_path, 'to ', destination_path)
            shutil.copy(source_path, destination_path)

def synthetize_files(destination_dirs, words_said, alphanumeric_codes):
    '''Synthetizes the given words_said and copies the resulting audio files to the
    specified destination folders using the alphanumeric_code as the filename.'''
    for folder_name in destination_dirs:
        os.makedirs(folder_name, exist_ok=True)
        for word, alphanumeric_code in zip(words_said, alphanumeric_codes):
            output_file = os.path.join(folder_name, alphanumeric_code + '.wav')
            print('Synthetizing', word, 'to', output_file)
            synthetize(word, output_file)

def save_printed_files(destination_dirs, words_printed, alphanumeric_codes):
    '''Saves the given words_printed to text files and copies them to the
    specified destination folders using the alphanumeric_code as the filename.'''
    for folder_name in destination_dirs:
        os.makedirs(folder_name, exist_ok=True)
        for word, alphanumeric_code in zip(words_printed, alphanumeric_codes):
            output_file = os.path.join(folder_name, alphanumeric_code + '.txt')
            print('Saving', word, 'to', output_file)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(word)

            output_file = os.path.join(folder_name, alphanumeric_code + 'negative.txt')
            print('Saving negative comparisons for', word, 'to', output_file)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(get_negative_comparisons(word))

if __name__ == '__main__':
    # Set the source directory containing the jpg files
    source_dir = 'base'

    # Create the destination folders if they don't exist
    destination_dirs = ['01', '02', '03', '04', '05', '06']

    # Get the list of jpg files
    jpg_files = get_jpg_files(source_dir)

    # Fixed alphanumeric codes throughout cycles
    alphanumeric_codes = ['B3', 'B4']

    # Select files and copy them to folders
    selected_files = select_files(jpg_files, alphanumeric_codes)
    copy_files_to_folders(selected_files, destination_dirs)

    # variable alphanumeric codes throughout cycles
    alphanumeric_codes = ['B1', 'B2']
    for directory in destination_dirs:
        os.makedirs(directory, exist_ok=True)
        selected_files = select_files(jpg_files, alphanumeric_codes)
        copy_files_to_folders(selected_files, [directory])

    # Save spoken words to text files
    alphanumeric_codes = ['A3', 'A4']
    words_said = ['FALÓ', 'BENÁ']
    synthetize_files(destination_dirs, words_said, alphanumeric_codes)

    alphanumeric_codes = ['A1', 'A2']
    selected_words_said = [
        ['NIBÓ', 'FALÉ'], ['BOFÁ', 'LENÍ'], ['LEBÓ', 'FANÍ'],
        ['BONÍ', 'LEFÁ'], ['FABÓ', 'NILÉ'], ['BOLÉ', 'NIFÁ']]

    for words, directory in zip(selected_words_said, destination_dirs):
        synthetize_files([directory], words, alphanumeric_codes)

    #save printed words to text files
    alphanumeric_codes = ['C3', 'C4']
    words_printed = ['FALÓ', 'BENÁ']
    save_printed_files(destination_dirs, words_printed, alphanumeric_codes)

    alphanumeric_codes = ['C1', 'C2']
    selected_words_printed = [
        ['NIBÓ', 'FALÉ'], ['BOFÁ', 'LENÍ'], ['LEBÓ', 'FANÍ'],
        ['BONÍ', 'LEFÁ'], ['FABÓ', 'NILÉ'], ['BOLÉ', 'NIFÁ']]
    for words, directory in zip(selected_words_printed, destination_dirs):
        save_printed_files([directory], words, alphanumeric_codes)