#!/usr/bin/env python3

import os
import shutil
import time
import cairosvg
import validators
from PyPDF2 import PdfFileMerger

def dl_presentation(url: str):
    if not validators.url(url):
        print("Not an url.")
        return -1

    # Processing the url
    arr = url.split('/')
    if arr[-2] == "svg":
        url = '/'.join(arr)
    else:
        print("Incorrect patern.")
        return -1

    tmp = time.time()
    out = '_output_' + str(tmp)

    os.mkdir(out)
    
    # Merge .pdf files to one
    merger = PdfFileMerger()

    i = 1
    while err := os.system('wget {}/svg/{} -O {}/{}.svg -q -nv'.format(url, i, out, i)) == 0:
        # Path to svg and pdf
        form = '{}/{}.{}'
        svgFile = form.format(out, i, 'svg')
        pdfFile = form.format(out, i, 'pdf')
        # Convert svg to pdf
        cairosvg.svg2pdf(url = svgFile, write_to = pdfFile)
        # Merge to final pdf
        merger.append(pdfFile)
        i += 1

    if i != 1:
        merger.write(('{}.pdf').format(tmp))
        print("Final .pdf was created.")
    else:
        print("Download fail.")

    merger.close()
    shutil.rmtree(out)

    return 0