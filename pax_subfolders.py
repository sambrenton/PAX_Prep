import os, shutil

# Define path of highest level parent folder of collection
root_folder = 'PATH'

# Define names for Preservation and Access folders (Preservica PAX specification)
preservation_dir = 'Representation_Preservation'
access_dir = 'Representation_Access'

# Iterate over entire folder
for root, dirs, files in os.walk(root_folder):

    # Find the directories that contain preservation and access files
    if set(['mp3', 'wav']).issubset(set([file.split('.')[-1] for file in files])):

        # Make the PAX directories
        os.mkdir(os.path.join(root, preservation_dir))
        os.mkdir(os.path.join(root, access_dir))

        # Move the files into the PAX directories
        for file in files:
            file_path = os.path.join(root, file)

            # Move access copy (and checksum if specified for access file)
            if 'mp3' in file: 
                shutil.move(file_path, os.path.join(root, access_dir))

            # Move preservation copy and checksum (assumption checksum is for preservation copy if not specified for access copy)
            if file.endswith('.wav') or file.endswith('.md5'):
                shutil.move(file_path, os.path.join(root, preservation_dir))
