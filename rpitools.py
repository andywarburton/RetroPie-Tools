#==============================================================================#
# This is a collection of different tools used by the different programs
# included with RetroPie-tools
# Use at your own risk - changing these variables affects all programs
#==============================================================================#

import os
import os.path
import sys
import string

# config vars, if you are using non-standard stuff change these
# os.environ['HOME'] pulls the users current home directory,
# and changes with the username
# /opt/ does not need to change as this is standard

# Directory with rom files
rom_dir = os.environ['HOME'] + '/RetroPie/roms'
# Directory to move games during clean
bak_dir = os.environ['HOME'] + '/RetroPie/cleaned_up'
# Location of the images for roms
img_dir = '/opt/retropie/configs/all/emulationstation/downloaded_images'

#==============================================================================#

# List of allowed directories to search within roms folder
# If it is not included, it is ignored
# Modify to ignore systems as desired
allowed_systems = [
                  'amiga',          'amstradcpc',   'apple2',
                  'arcade',         'atari800',     'atari2600',
                  'atari5200',      'atari7800',    'atarilynx',
                  'atarist',        'c64',          'coco',
                  'dragon32',       'dreamcast',    'fba',
                  'fds',            'gamegear',     'gb',
                  'gba',            'gbc',          'intellivision',
                  'macintosh',      'mame-advmame', 'mame-libretro',
                  'mame-mame4all',  'mastersystem', 'megadrive',
                  'msx',            'n64',          'neogeo',
                  'nes',            'ngp',          'ngpc',
                  'pc',             'pcengine',     'psp',
                  'psx',            'sega32x',      'segacd',
                  'sg-1000',        'snes',         'vectrex',
                  'videopac',       'wonderswan',   'wonderswancolor',
                  'zmachine',       'zxspectrum'
                  ]

# List of incomplete game filename headers
# Modify to include other headers not included here
incom_types =     [
                  '(Proto)',        '(Demo)',       '(Beta)',
                  '(Kiosk)',        '(Debug ',      '(Rev '
                  ]

# macOS hidden file names
# It is not recommended to modify this
macos_hidden =    ['.DS_Store', '._']

#==============================================================================#

# The warning shown to the user at the start of the program
warning = """
*****************************************************************
      WARNING! THIS SCRIPT WILL PERMANENTLY DELETE FILES!

        ===== PLEASE BACKUP BEFORE RUNNING THIS! =====
       ===== IT IS RECOMMENDED TO DO "TEST" FIRST =====

      TYPE "TEST" TO DO A TEST RUN THAT WILL TELL YOU HOW
          MANY FILES WOULD BE CHANGED BY AN ACTUAL RUN

    TYPE "CLEAN" TO MOVE UNWANTED FILES TO A BACKUP DIRECTORY
                 (/home/pi/RetroPie/cleaned_up)

              TYPE "DELETE" IF YOU ARE SOUND MIND,
           UNDERSTAND THE RISKS, AND WISH TO PROCEED
*****************************************************************
: """

spacer = "*****************************************************************"

#==============================================================================#

def get_user_input(os):
    '''
    Informs the user of the potential consequences of running the
    program, and asks for their input, which will be passed to the program
    '''

    # question.replace() replaces the output text's CLEAN directory (what is
    # presented to the user) with the actual directory

    ui = raw_input(warning.replace('/home/pi',os.environ['HOME'])).upper()

    return ui

#==============================================================================#

def dct_rom(ui, system_name, rom_name, filename, file_path, bak_dir, os):
    '''
    This function deletes, tests, or cleans a rom
    dct_rom(user_input, system_name, rom_name, filename, file_path, bak_dir, os)
    '''

    if ui == 'DELETE':

        print "DELETING: " + system_name + "/" + rom_name +\
                ", (" + filename + ")"
        os.remove(file_path)

    elif ui == 'CLEAN':

        print "CLEANING: " + system_name + "/" + rom_name +\
                ", (" + filename + ")"

        system_bak_dir = bak_dir + '/' + system_name
        bak_file_path = system_bak_dir + '/' + filename

        if not os.path.isdir(system_bak_dir):
            os.makedirs(system_bak_dir)

        os.rename(file_path, bak_file_path)

    else:

        print "TESTING: " + system_name + "/" + rom_name +\
                ", (" + filename + ")"
        ## do nothing

#==============================================================================#
