#!/usr/bin/env python3

import sys
from pathlib import Path
from zipfile import ZipFile

def extract_zipfile(artist, album, path):
    directory = Path("mnt", "jellyfin_data", "media", "Music", artist, album)
    directory.mkdir(parents=True, exist_ok=True)

    with ZipFile(path) as zf:
        zf.extractall(directory)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: import-bandcamp.py "Artist Name" "Album Name" /path/to/some_file.zip')
    else:
        extract_zipfile(sys.argv[1], sys.argv[2], sys.argv[3])
