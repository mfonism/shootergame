# Shooter Game

A tiny game I'm building as a fun project and also a test bed for
[ppb](https://github.com/ppb/pursuedpybear). You can play it by cloning the
repository, creating a virtual environment using the included 
`requirements.txt`, then running with your virtual environment's `python`
command and the `-m` flag.

Sample run script for linux and mac:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python -m shooter

Sample run script for windows:

    python3 -m venv .venv
    .venv/Scripts/activate
    pip install -r requirements.txt
    python -m shooter

Requires Python 3.6 or 3.7.

Now includes the [feet](https://github.com/ironfroggy/feet) runner from
ironyfroggy. If playing on windows, just run `shootergame.exe`.

## Game Control

Use the mouse to select the Start button on the main menu. Control your ship
with the arrow buttons and space bar to shoot.
