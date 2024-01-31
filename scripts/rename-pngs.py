import os

def rename_files():
    folder_path = os.getcwd()  # Get the current working directory

    # List all files in the current folder
    files = os.listdir(folder_path)
    files = [file for file in files if file.lower().endswith('.png')]

    # Iterate through each file and rename it
    for index, file_name in enumerate(files):
        # Generate the new file name with the "4xxx" prefix
        new_name = f"4{index + 1:03d}.png"

        # Construct the full paths for old and new names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")

if __name__ == "__main__":
    rename_files()