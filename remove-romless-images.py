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

print "sorry, nothing going on here so far!"
