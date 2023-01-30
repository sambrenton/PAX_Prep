import os

# Root directory containing all the folders to be renamed
root_dir = r'Y:\WTC'

# Iterate over the root directory
for root, dirs, files in os.walk(root_dir):

    # Iterate over directories only
    for dir in dirs:

        # Check if the directory name is ' Preservica_preservation1_lnk' (V5 - Preservation)
        if dir == 'Preservica_preservation1_lnk':

            # Rename the directory to 'Representation_Preservation' (PAX - Preservation)
            os.rename(os.path.join(root, dir), os.path.join(root, 'Representation_Preservation'))

         # Check if the directory name is "Preservica_presentation2_lnk" (V5 - Access)
        elif dir == 'Preservica_presentation2_lnk':

            # Rename the directory to 'Representation_Access' (PAX - Access)
            os.rename(os.path.join(root, dir), os.path.join(root, 'Representation_Access'))
