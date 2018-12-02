#==============================================================================#
# This program is intended to remove hidden files created by macOS
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

# List of allowed directories to search within roms folder
allowed_systems = rpitools.allowed_systems
# List of macOS hidden file names
macos_hidden = rpitools.macos_hidden

# The number of deleted roms
delete_count    = 0
# The total number of roms
total_count     = 0

# Allowed operations in this program
operations = ['DELETE','TEST','CLEAN']

#==============================================================================#

print "This program is intended to remove any roms from RetroPie that are\n\
       prototypes, demos, betas, kiosks, or debug versions\n\n"
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

        # opens the file path as list_file
        with open(list_file_path, 'wb') as list_file:

            os.remove(list_file_path)

            for filename in files:
                file_path = os.path.join(root, filename)

                # parses the rom file name, not needed for macos hidden files
                rom_name = filename
                # parses the system name
                system_name = file_path.split('/')[-2]

                # verify system is allowed (do not want to mess with
                # other folders in the roms directory)
                if system_name in allowed_systems:

                    # for counting the number of roms looked at
                    total_count += 1

                    # this is the directory the image would be
                    # if the image has been scraped

                    # if no part of any of the incomplete type headers
                    # are in the filename of the rom
                    if any(p in rom_name for p in macos_hidden):

                        # for counting the number of roms that would be deleted
                        delete_count += 1

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
