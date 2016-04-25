import os
import os.path
import sys
import string

# config vars, if you are using non-standard stuff change these
rom_dir         = '/home/pi/RetroPie/roms'
bak_dir         = '/home/pi/RetoPie/cleaned_up'
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

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)

if user_input == 'DELETE' or user_input == 'delete' or user_input == 'test' or user_input == 'TEST' or user_input == 'clean' or user_input == 'CLEAN' :

    # check if bak_dir exists
    # if not, make it

    for root, subdirs, files in os.walk(rom_dir):
    
        list_file_path = os.path.join(root, 'foo.txt')

        with open(list_file_path, 'wb') as list_file:
        
            for filename in files:
                file_path = os.path.join(root, filename)
            
                rom_name = filename.split('.')[0]
            
                system_name = file_path.split('/')[-2] 

                if system_name in allowed_systems:

                    total_count += 1

                    image_path = img_dir + '/' + system_name + '/' + rom_name + '-image.jpg'

                    #print image_path

                    if not os.path.isfile(image_path):
                        ## no image found, we should delete the rom!
                        print "DELETING: " + system_name + "/" + rom_name + " (" + filename + ")"
                        if user_input == 'delete' or user_input == 'DELETE':
                            ## os.remove(file_path)
                            delete_count += 1
                        elif user_input == 'clean' or user_input == 'CLEAN':
                            ## check if bak_dir/system_name does NOT exist
                            ## if so, create it
                            ## then move file to bak_dir/system_name
                            delete_count += 1
                        else:
                            ## do nothing
                            delete_count += 1
                    
    if user_input == 'delete' or user_input == 'DELETE':
        print "\n--------------------------------------------------------------------"
        print " CLEANUP COMPLETE: " + str(delete_count) + " of " + str(total_count) + " files have been deleted! SHINY!"
        print "--------------------------------------------------------------------"
    elif user_input == 'clean' or user_input == 'CLEAN':
        print "\n--------------------------------------------------------------------"
        print " CLEAN COMPLETE: " + str(delete_count) + " of " + str(total_count) + " files have been moved! SHINY!"
        print "--------------------------------------------------------------------"
    else:
        print "\n--------------------------------------------------------------------"
        print " CLEANUP COMPLETE: " + str(delete_count) + " of " + str(total_count) + " are ripe to be tidied!"
        print "--------------------------------------------------------------------"
    
else :
    
    print "SCRIPT ABORTED (GOOD CHOICE!)"
