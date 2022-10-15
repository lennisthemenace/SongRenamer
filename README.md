# SongRenamer

Tool for Renaming Song files to reflect their attributes

This is useful if you have a folder full of MP3's and M4A's with randon file names (Like when you copy them from an old
iPod)

A simple tool for copying files from your iPod is [this](https://github.com/tylern4/CopyiPod), it will copy all your
songs from your iPod, but leaves then named how the iPod sorted them (useless to a human). So run Renamer.py in the
directory you have the songs you want automatically renamed. then it will create 2 directories "Processed" and "Renamed"
.

/Processed
This contains all the original files that were successfully processed, but left intact here.

/Renamed
This contains copies of the original files with their nice new name.

Anything files left in the root directory are ones that the tool couldn't process. (sometimes the tracks dont have the
attributes this tool needs for it to run) 
