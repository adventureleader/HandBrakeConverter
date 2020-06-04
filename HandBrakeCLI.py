#!/usr/bin/env python3

import os
from pathlib import Path

mediaType=['/media/content/movies', '/media/content/tv', '/media/content/exercise']
source =[]
target=[]

for type in mediaType:
    #get all .mkv files to be converted and set .m4v target
    for path in Path(type).rglob('*.mkv'):
      source.append(path)
      target.append((path.name).replace('.mkv', '.m4v'))

    #send each file to handbrake to be converted
    for i in range(len(source)):
      os.chdir(source[i].parent)
      hbCommand='HandBrakeCLI -i "{}" -o "{}"'.format(source[i].name, target[i])
      os.system(hbCommand)

sysexit()
