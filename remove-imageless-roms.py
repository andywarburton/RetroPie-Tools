import os
import os.path
import sys
import string

# config vars, if you are using non-standard stuff change these
rom_dir         = '/home/pi/RetroPie/roms'
bak_dir         = '/home/pi/RetroPie/cleaned_up'
img_dir         = '/opt/retropie/configs/all/emulationstation/downloaded_images'
allowed_systems = ['amiga','amstradcpc','apple2','arcade','atari800','atari2600','atari5200','atari7800','atarilynx','atarist','c64','coco','dragon32','dreamcast','fba','fds','gamegear','gb','gba','gbc','intellivision','macintosh','mame-advmame','mame-libretro','mame-mame4all','mastersystem','megadrive','msx','n64','neogeo','nes','ngp','ngpc','pc','pcengine','psp','psx','sega32x','segacd','sg-1000','snes','vectrex','videopac','wonderswan','wonderswancolor','zmachine','zxspectrum']
delete_count    = 0
total_count     = 0

question = """  
*****************************************************************
      WARNING! THIS SCRIPT WILL PERMANENTLY DELETE FILES!
         AND IS WRITTEN BY AN AMATEUR PYTHON DEVELOPER

        =====   THIS COULD GO VERY VERY WRONG!   =====        
        ===== PLEASE BACKUP BEFORE RUNNING THIS! =====
        
        ARE YOU SURE YOU WANT TO PROCEED? (YES/TEST/NO)
        
      TYPE "TEST" TO DO A TEST RUN THAT (HOPEFULLY) WON'T 
              ACTUALLY DELETE ANY FILES (MAYBE)
              
    TYPE "CLEAN" TO MOVE UNWANTED FILES TO A BACKUP DIRECTORY
                 (/home/pi/RetroPie/cleaned_up)
        
    TYPE "DELETE" IF YOU ARE SOUND MIND, UNDERSTAND THE RISKS
       AND WISH TO PROCEED WITH PERMANENTLY DELETING STUFF!
*****************************************************************
: """

user_input = raw_input(question)

if user_input == 'DELETE' or user_input == 'delete' or user_input == 'test' or user_input == 'TEST' or user_input == 'clean' or user_input == 'CLEAN' :

    # for the cleanup process, we need somewhere to put our backups
    if user_input == 'clean' or user_input == 'CLEAN':
        if not os.path.isdir(bak_dir):
            os.makedirs(bak_dir)

    for root, subdirs, files in os.walk(rom_dir):
    
        list_file_path = os.path.join(root, 'foo.txt')

        with open(list_file_path, 'wb') as list_file:
        
            os.remove(list_file_path)
                    
            for filename in files:
                file_path = os.path.join(root, filename)
            
                rom_name = filename.split('.')[0]
            
                system_name = file_path.split('/')[-2] 

                if system_name in allowed_systems:

                    total_count += 1

                    image_path = img_dir + '/' + system_name + '/' + rom_name + '-image.jpg'

                    if not os.path.isfile(image_path):
                        ## no image found, we should delete the rom!
                        
                        if user_input == 'delete' or user_input == 'DELETE':

                            print "DELETING: " + system_name + "/" + rom_name + " (" + filename + ")"
                            os.remove(file_path)
                            delete_count += 1

                        elif user_input == 'clean' or user_input == 'CLEAN':

                            print "CLEANING: " + system_name + "/" + rom_name + " (" + filename + ")"
                            system_bak_dir = bak_dir + '/' + system_name
                            bak_file_path = system_bak_dir + '/' + filename
                                                        
                            if not os.path.isdir(system_bak_dir):
                                os.makedirs(system_bak_dir)

                            os.rename(file_path, bak_file_path)
                            delete_count += 1

                        else:

                            print "TESTING: " + system_name + "/" + rom_name + " (" + filename + ")"
                            ## do nothing
                            delete_count += 1

    remaining_roms = total_count - delete_count
    
    if user_input == 'delete' or user_input == 'DELETE':
        print "\n--------------------------------------------------------------------"
        print "CLEANUP COMPLETE: " + str(delete_count) + " of " + str(total_count) + " files have been deleted! (" + str(remaining_roms) + " remain)"
        print "--------------------------------------------------------------------"
    elif user_input == 'clean' or user_input == 'CLEAN':
        print "\n--------------------------------------------------------------------"
        print "CLEAN COMPLETE: " + str(delete_count) + " of " + str(total_count) + " files have been moved!  (" + str(remaining_roms) + " remain)"
        print "--------------------------------------------------------------------"
    else:
        print "\n--------------------------------------------------------------------"
        print "TEST COMPLETE: " + str(delete_count) + " of " + str(total_count) + " are ripe to be tidied!  (" + str(remaining_roms) + " remain)"
        print "--------------------------------------------------------------------"
    
else :
    
    print "SCRIPT ABORTED (GOOD CHOICE!)"
