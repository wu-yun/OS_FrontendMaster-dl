import os
import os.path
import string
from urllib2 import urlopen, URLError, HTTPError

def format_filename(filename_str):
    s = filename_str
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')
    return filename

def download_file(url, path, self):
    # FIXME(Xinyang): Better exception handling for empty url
    if url is None:
        return
    if len(url) <= 1:
        return

    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        self.browser.get(url)
        temporaryURL = self.browser.current_url
        self.browser.back()
        buff = urlopen(temporaryURL)
        print("Downloading: %s" % (path))

        with open(path, 'wb') as local_file:
            local_file.write(buff.read())


def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)