# BigBlueButton Downloader
A simple script to download users' presentations during a session.
This project is working fine with BigBlueButton 2.7.2 version.

# Installation
```sh
# Install the requirements
$ python3 -m pip install -r requirements.txt
```

# Usage
```sh
$ ./main.py help
Usage: [COMMAND] [OPTION]

=====================================================

NAME
    presentation [URL]

DESCRIPTION
    Download a presentation from BigBlueButton server.
    The URL to provide is the current URL of the slide.

=====================================================

NAME
    playback [URL] [TYPE]

DESCRIPTION
    Download a playback from BigBlueButton server.
    The URL to provide is the URL of the video or audio.

    --shared-screen     Type of the video is a deskshare.
    --presentation      Tyoe of the video is presentation with slides.

=====================================================
```