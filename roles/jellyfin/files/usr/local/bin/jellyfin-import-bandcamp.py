#!/usr/bin/env python3

import sys
from pathlib import Path
from zipfile import ZipFile

def extract_zipfile(artist, album, path):
    if Path("/mnt/jellyfin_data").exists():
        base = Path("/mnt/jellyfin_data/media/Music")
    else:
        base = Path.cwd()
    directory = Path(base, artist, album)
    directory.mkdir(parents=True, exist_ok=True)

    with ZipFile(path) as zf:
        zf.extractall(directory)

if __name__ == '__main__':
    if len(sys.argv) != 4 and len(sys.argv) != 2:
        print('Usage: import-bandcamp.py "Artist Name" "Album Name" /path/to/some_file.zip')
        print('   or: import-bandcamp.py /path/to/some_file.zip')
        print('Where the latter has a filename of the format "Artist Name - Album Name.zip"')
    elif len(sys.argv) == 2:
        filename = Path(sys.argv[1]).resolve()
        parts = filename.with_suffix('').name.split(' - ')
        extract_zipfile(parts[0], parts[1], filename)
    else:
        extract_zipfile(sys.argv[1], sys.argv[2], sys.argv[3])
