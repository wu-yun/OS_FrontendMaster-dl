import os
import os.path
import string
from urllib2 import urlopen, URLError, HTTPError

def format_filename(filename_str):
    s = filename_str
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename

def download_file(url, path):
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        buff = urlopen(url)
        print("Downloading: %s" % (path))

        with open(path, 'wb') as local_file:
            local_file.write(buff.read())

def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
