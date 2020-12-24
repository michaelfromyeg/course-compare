# Course Compare

Compare what courses you're taking with your friends, through the upload of a .ical file.

## Usage

TODO

## Setup

Set up the virtual environment.

### Linux

```sh
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Windows

TODO

## Dependencies

This software relies heavily on `ics.py`, a severely underrated Python package for interacting with `.ics` files. Go check it out!

## Known Issues

- Reading in .ics files directly from UBC's SSC causes the Python ics package to throw an error, that uploading to Google Calendar fixes

## Contributing

TODO
