## Pokalert
### Introduction:
This **basic** branch is the core functionality of what's found on **master**. This version searches for and lists any pokemon detected in the vicinity so that you can add your own functionality.

### Installation:
The folowing commands assume you're working on a Raspberry pi running Raspbian.

Download the zip from here:

`wget https://github.com/PangolinPaw/Pokalert/archive/basic.zip`

Unzip it & move into the directory:

`unzip basic.zip`

`cd Pokalert-basic`

Install the requirements using pip:

`sudo pip install -r requirements.txt`

### Usage:
* Open settings.txt with your favourite editor and enter your details:
*`nano settings.txt`
* Run main.py:
*`python main.py`

**main.py** will list all pokemon currently in the area as they are detected. There is no logic to deal with pokemon previously detected that remain in the vicinity.

### Thanks:
Based on [leegao](https://github.com/leegao/pokemongo-api-demo/tree/master)'s work.
