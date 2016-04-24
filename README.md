# Retropie-cleanup

A simple script for cleaning up rom files without artwork from Retropie

To run, simply type:

`sudo python ./cleanup.py`

Then after carefully reading the prompt, type "yes" to proceed. That is your last chance to backout before cleanup.py deletes all your roms without artwork.

### How this works ###

1. Loops through each directory in `/home/pi/RetroPie/roms`
2. Checks if the directory is in the `allowed_systems` array (ports and scummvm are excluded)
3. If it is, we loop through each file in that directory
4. For each file in the directory we check if there is a corrosponding romname-image.jpg in `/opt/retropie/configs/all/emulationstation/downloaded_images/$system
5. If there isn't a matching image file, we delete the rom
6. GOTO 1`
