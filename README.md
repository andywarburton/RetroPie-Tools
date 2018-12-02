# RetroPie-Tools

A collection of simple python scripts that I use for cleaning up my RetroPie installation.

* `rm-imageless-roms.py` - (nearly finished) removes roms that do not have any artwork
* `rm-hidden-macos-files.py` - removes annoying macOS hidden files from the roms folder
* `rm-incomplete-roms.py` - removes prototypes, demos, betas, kiosks, or debug roms (by name)

To run, simply copy the above file to any location on your Raspberry Pi and type:

```sudo python ./rm-imageless-roms.py```

Then follow the onscreen instructions!

# TODO:

* `rm-romless-images.py` - (unstarted) removes images that do not have any roms (for instance when rom has been deleted)
* `rm-non-english-roms.py` - (unstarted) removes all roms that are not in English, adaptable to any language!

Got a suggestion for a useful script? Please send suggestions via the issues tab!
