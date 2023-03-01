import os, shutil

# Code to change an individual folder into a PAX

# Define the path of the directory
SOURCE_DIR = 'PATH'

# Change the current working directory
os.chdir(SOURCE_DIR)

# Make the new PAX subfolder - takes the name of the folder, and appends '.pax'
PAX_fldr = os.path.basename(SOURCE_DIR)+ '.pax'
os.mkdir(PAX_fldr)

# Move the files in to the PAX folder
for file in os.listdir():
    shutil.move(file, PAX_fldr)

# Change the current working directory to the PAX folder
os.chdir(PAX_fldr)

# Define the folders for PAX representations
PRESERVATION_DIR = 'Representation_Preservation'
ACCESS_DIR = 'Representation_Access'

# Make the folders for PAX representations
os.mkdir(PRESERVATION_DIR)
os.mkdir(ACCESS_DIR)

# Move files into their respective representation folders
for file in os.listdir():
    if file.endswith('.tif'):
        shutil.move(file, PRESERVATION_DIR)
    if file.endswith('.jpg'):
        shutil.move(file, ACCESS_DIR)

