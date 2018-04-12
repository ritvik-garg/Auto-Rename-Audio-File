import eyed3
import os
import glob

for naam in glob.glob("*.mp3"):
    audio_file = eyed3.load(naam)
    file_name=audio_file.tag.title
    bc=audio_file.tag.title+audio_file.tag.artist
    start=end=0
    while start != -1 and end != -1:
        start = bc.find('(')
        end = bc.find(')')
        if start != -1 and end != -1:
            bc=bc[0:start]+bc[end+1:]
    bc=bc+".mp3"
    os.rename(naam , bc)
