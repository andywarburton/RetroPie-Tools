# This program is intended to remove any roms from RetroPie that do not
# have any artwork. It will work on a Raspberry Pi or a Linux computer


import os
import os.path
import sys
import string

# config vars, if you are using non-standard stuff change these
# os.environ['HOME'] pulls the users current home directory, wherever
# that is, and changes with the username
# /opt/ does not need to change as this is standard across RetroPie and
# linux distros
rom_dir         = os.environ['HOME'] + '/RetroPie/roms'
bak_dir         = os.environ['HOME'] + '/RetroPie/cleaned_up'
img_dir         = '/opt/retropie/configs/all/emulationstation/downloaded_images'
allowed_systems = [
                  'amiga','amstradcpc','apple2',
                  'arcade','atari800','atari2600',
                  'atari5200', 'atari7800','atarilynx',
                  'atarist','c64','coco',
                  'dragon32','dreamcast','fba',
                  'fds','gamegear','gb',
                  'gba','gbc','intellivision',
                  'macintosh','mame-advmame', 'mame-libretro',
                  'mame-mame4all','mastersystem','megadrive',
                  'msx','n64', 'neogeo',
                  'nes','ngp','ngpc',
                  'pc','pcengine','psp',
                  'psx','sega32x','segacd',
                  'sg-1000','snes','vectrex',
                  'videopac','wonderswan','wonderswancolor',
                  'zmachine','zxspectrum'
                  ]

# The number of deleted roms
delete_count    = 0
# The total number of roms
total_count     = 0

question = """
*****************************************************************
      WARNING! THIS SCRIPT WILL PERMANENTLY DELETE FILES!

        ===== PLEASE BACKUP BEFORE RUNNING THIS! =====
      ===== IT IS RECOMMENDED TO DO "TEST" FIRST! =====

      TYPE "TEST" TO DO A TEST RUN THAT WILL TELL YOU HOW
          MANY FILES WOULD BE CHANGED BY AN ACTUAL RUN

    TYPE "CLEAN" TO MOVE UNWANTED FILES TO A BACKUP DIRECTORY
                 (/home/pi/RetroPie/cleaned_up)

              TYPE "DELETE" IF YOU ARE SOUND MIND,
           UNDERSTAND THE RISKS, AND WISH TO PROCEED
*****************************************************************
: """

spacer = "*****************************************************************"

# question.replace() replaces the output text's CLEAN directory (what is
# presented to the user) with the actual directory
user_input = raw_input(question.replace('/home/pi',os.environ['HOME'])).upper()

# verify user input
if user_input in ['DELETE','TEST','CLEAN']:

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
                        ## no image found, we should delete the rom!

                        if user_input == 'DELETE':

                            print "DELETING: " + system_name + "/" + rom_name +\
                                    " (" + filename + ")"
                            os.remove(file_path)
                            delete_count += 1

                        elif user_input == 'CLEAN':

                            print "CLEANING: " + system_name + "/" + rom_name +\
                                    " (" + filename + ")"
                            system_bak_dir = bak_dir + '/' + system_name
                            bak_file_path = system_bak_dir + '/' + filename

                            if not os.path.isdir(system_bak_dir):
                                os.makedirs(system_bak_dir)

                            os.rename(file_path, bak_file_path)
                            delete_count += 1

                        else:

                            print "TESTING: " + system_name + "/" + rom_name +\
                                    " (" + filename + ")"
                            ## do nothing
                            delete_count += 1

    remaining_roms = total_count - delete_count

    print "\n" + spacer
    print user_input + " COMPLETE: " + str(delete_count) + " of " +\
        str(total_count) + " total (" + str(remaining_roms) + " remain)"
    print spacer

else:
  
    print "INPUT NOT RECOGNIZED, PLEASE TRY AGAIN"
    sys.exit()

