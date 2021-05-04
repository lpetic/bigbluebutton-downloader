#!/usr/bin/env python3

import os
import shutil
import time
import cairosvg
import validators
import wget
import urllib
import threading
from PyPDF2 import PdfFileMerger

def download_and_convert(url: str, i: int, out: str):
    try:
        wget.download('{}/svg/{}'.format(url, i), out='{}/{}/'.format(out, 'svg'))
    except urllib.error.HTTPError:
        return -1
    print(' ' + str(i))
    # Path to svg and pdf
    svg = '{}/{}/{}'.format(out, 'svg', i)
    pdf = '{}/{}/{}'.format(out, 'pdf', i)
    # Convert svg to pdf
    cairosvg.svg2pdf(url = svg, write_to = pdf)
    return 0

def dl_presentation(url: str):
    if not validators.url(url):
        print("Not an url.")
        return -1

    # Processing the url
    arr = url.split('/')
    if arr[-2] == "svg":
        arr = arr[:-2]
        url = '/'.join(arr)
    else:
        print("Incorrect patern.")
        return -1

    out = str(time.time()) + '.tmp'

    os.mkdir(out)
    os.mkdir(out + '/svg')
    os.mkdir(out + '/pdf')

    # Found the size of the presentation
    slides = []
    i = 0
    total = 0
    found = True
    while found:
        i += 8
        slides.append(i)
        if download_and_convert(url, i, out) == -1:
            while download_and_convert(url, i, out) == -1:
                slides.append(i)
                i -= 1
                total = i
            found = False
    
    # Install thread on other slides to download
    threads = []
    for i in range(1, total):
        if i not in slides:
            t = threading.Thread(target=download_and_convert, args=(url, i, out))
            t.start()
            threads.append(t)

    lock = threading.Lock()
    for i in threads:
        with lock:
            i.join()
    
    # Merge .pdf files to one
    if total != 0:
        merger = PdfFileMerger()
        for i in range(1, total + 1):
            merger.append('{}/pdf/{}'.format(out, i))
        merger.write(('{}.pdf').format(out))
        merger.close()
        print("Final .pdf was created with {} slides.".format(total))
    else:
        print("Download fail.")

    shutil.rmtree(out)

    return 0