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

    print("Extracting: {}/{}".format(artist, album))
    with ZipFile(path) as zf:
        zf.extractall(directory)

def extract_zipfile_infer(path):
    filename = Path(path).resolve()
    parts = filename.with_suffix('').name.split(' - ')
    extract_zipfile(parts[0], parts[1], filename)

if __name__ == '__main__':
    if len(sys.argv) == 5 and sys.argv[1] == '--metadata':
        extract_zipfile(sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            extract_zipfile_infer(arg)
    else:
        print('Usage: import-bandcamp.py --metadata "Artist Name" "Album Name" /path/to/some_file.zip')
        print('   or: import-bandcamp.py /path/to/some_file.zip /path/to/some_other_file.zip')
        print('Where the latter has filenames of the format "Artist Name - Album Name.zip"')
