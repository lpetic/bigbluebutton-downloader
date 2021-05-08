#!/usr/bin/env python3

import os
import time
import wget
import validators
import ffmpeg

def playback(url: str, type: str):
    if not validators.url(url):
        print("Not an url.")
        return -1

    # Processing the url
    arr = url.split('/')
    arr = arr[:-2]
    url = '/'.join(arr)

    if type == '--shared-screen':
        return playback_shared_screen(url)

    if type == '--presentation':
        return playback_presentation(url)

    print('Unknow option "{}"'.format(type))

    return -1

def playback_shared_screen(url: str):

    out = '1620473825.322499.tmp'
    # os.mkdir(out)

    l = ['deskshare/deskshare.webm', 'video/webcams.webm']

    for i in l:
        if os.fork() == 0:
            download(url, i, out)
            exit(0)

    for i in l:
        os.wait()

    # Merge video and audio
    video = ffmpeg.input('{}/{}'.format(out, l[0].split('/')[-1]))
    audio = ffmpeg.input('{}/{}'.format(out, l[1].split('/')[-1]))
    out = ffmpeg.output(video, audio, '{}.mp4'.format(out), vcodec='copy', acodec='aac', strict='experimental')
    out.run()

    return 0

def playback_presentation(url: str):
    # TODO ...
    print('TODO...')
    return 0

def download(url: str, extention: str, out: str):
    try:
        wget.download('{}/{}'.format(url, extention), out='{}/'.format(out))
        return 0
    except urllib.error.HTTPError:
        return -1