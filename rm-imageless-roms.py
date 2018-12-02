#==============================================================================#
# This program is intended to remove any roms from RetroPie that do not
# have any artwork. It will work on a Raspberry Pi or a Linux computer
#==============================================================================#

import os
import os.path
import sys
import string

import rpitools

#==============================================================================#
# It is recommended to change these settings in the rpitools.py file included
# with this program, as it makes it standard across all programs included
# in this package.

# Directory with rom files
rom_dir         = rpitools.rom_dir
# Directory to move games during clean
bak_dir         = rpitools.bak_dir
# Directory that stores image files for RetroPie
img_dir         = rpitools.img_dir

# List of allowed directories to search within roms folder
allowed_systems = rpitools.allowed_systems

# The number of deleted roms
delete_count    = 0
# The total number of roms
total_count     = 0

# Allowed operations in this program
operations = ['DELETE','TEST','CLEAN']

#==============================================================================#

print "This program is intended to remove any roms from RetroPie that \n\
       do not have images for them stored on this device\n\n"
user_input = rpitools.get_user_input(os)

# verify user input
if user_input in operations:

    # for the cleanup process, we need somewhere to put our backups
    if user_input == 'CLEAN':
        if not os.path.isdir(bak_dir):
            os.makedirs(bak_dir)

    # for all the files and directories to said files in the rom directory
    for root, subdirs, files in os.walk(rom_dir):

        list_file_path = os.path.join(root, 'foo.txt')

        with open(list_file_path, 'wb') as list_file:

            os.remove(list_file_path)

            for filename in files:
                file_path = os.path.join(root, filename)

                rom_name = filename.split('.')[0]

                system_name = file_path.split('/')[-2]

                # verify system is allowed (do not want to mess with
                # other folders in the roms directory)
                if system_name in allowed_systems:

                    total_count += 1

                    image_path = img_dir + '/' + system_name + '/' +\
                                    rom_name + '-image.jpg'

                    if not os.path.isfile(image_path):

                        # Calls the function dct (delete clean test)
                        # for the specific rom
                        rpitools.dct_rom(user_input, system_name, rom_name, \
                                        filename, file_path, bak_dir, os)

    remaining_roms = total_count - delete_count

    print "\n" + rpitools.spacer
    print user_input + " COMPLETE: " + str(delete_count) + " of " +\
        str(total_count) + " total (" + str(remaining_roms) + " remain)"
    print rpitools.spacer

else:

    print "INPUT NOT RECOGNIZED, PLEASE TRY AGAIN"
    sys.exit()
