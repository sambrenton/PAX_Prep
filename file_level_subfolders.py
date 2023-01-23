import os, shutil

# Define path of highest level parent folder of collection
root_folder = 'PATH'

# Iterate over entire folder
for root, dirs, files in os.walk(root_folder):

    # Get required names for new sub-folders by stripping file extensions
    new_subfolders = [file.split('.')[0] for file in files]

    # Iterate over new list of required folders (converting to a set removes duplicates)
    for sub_folder in set(new_subfolders):

        # Create new sub-folder in its parent folder
        new_folder_path = os.path.join(root, sub_folder)
        os.mkdir(new_folder_path)

        # Move files in to their new sub-folders
        for file in files:
            file_path = os.path.join(root, file)
            
            if sub_folder in file:
                shutil.move(file_path, new_folder_path)
