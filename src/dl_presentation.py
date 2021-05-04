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
    out = str(tmp)

    os.mkdir(out)
    os.mkdir(out + '/svg')
    os.mkdir(out + '/pdf')
    
    # Merge .pdf files to one
    merger = PdfFileMerger()
    
    i = 1
    while True:
        try:
            wget.download('{}/svg/{}'.format(url, i), out='{}/{}/'.format(out, 'svg'))
        except urllib.error.HTTPError:
            break

        print(' ' + str(i))
        # Path to svg and pdf
        form = '{}/{}/{}'
        svgFile = form.format(out, 'svg', i)
        pdfFile = form.format(out, 'pdf', i)
        # Convert svg to pdf
        cairosvg.svg2pdf(url = svgFile, write_to = pdfFile)
        # Merge to final pdf
        merger.append(pdfFile)
        i += 1

    if i != 1:
        merger.write(('{}.pdf').format(tmp))
        print("Final .pdf was created with {} pages.".format(i - 1))
    else:
        print("Download fail.")

    merger.close()
    shutil.rmtree(out)

    return 0