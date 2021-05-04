#!/usr/bin/env python3

import os
import shutil
import time
import cairosvg
import validators
import wget
import urllib

from PyPDF2 import PdfFileMerger

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

    tmp = time.time()
    out = str(tmp) + '.tmp'

    os.mkdir(out)
    os.mkdir(out + '/svg')
    os.mkdir(out + '/pdf')
    
    # Merge .pdf files to one
    merger = PdfFileMerger()
    
    i = 0
    while True:
        try:
            i += 1
            wget.download('{}/svg/{}'.format(url, i), out='{}/{}/'.format(out, 'svg'))
        except urllib.error.HTTPError:
            break
        
        print(' ' + str(i))
        # Path to svg and pdf
        form = '{}/{}/{}'
        svg = form.format(out, 'svg', i)
        pdf = form.format(out, 'pdf', i)
        # Convert svg to pdf
        cairosvg.svg2pdf(url = svg, write_to = pdf)
        # Merge to final pdf
        merger.append(pdf)

    if i != 0:
        merger.write(('{}.pdf').format(tmp))
        print("Final .pdf was created with {} pages.".format(i))
    else:
        print("Download fail.")

    merger.close()
    shutil.rmtree(out)

    return 0