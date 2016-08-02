## Pokalert
### Introduction:
Email alerts when 'interesting' pokemon are encountered.

(At present emails are sent via Outlook, GMail version pending...)

### Installation:
The folowing commands assume you're working on a Raspberry pi running Raspbian.

Download the zip from here:

`wget https://github.com/PangolinPaw/Pokalert/archive/master.zip`

Unzip it & move into the directory:

`unzip master.zip`

`cd Pokalert-master`

Install the requirements using pip:

`sudo pip install -r requirements.txt`



### Usage:
Note: This stuff is unfinished and untested.
* Open settings.txt with your favourite editor and enter your details:
*`nano settings.txt`
* * List (one per line) the pokedex numbers of any pokemon you're interested in in alertList.txt
* Run main.py:
*`python main.py`

**main.py** will list all pokemon currently in the area and save an account of appearances to the histroy table of **pokedex.db**.

If an interesting pokemon (listed in **alertList.txt**) appears, details are sent to whatever email you included in **settings.txt**, along with a heatmap of all previous encounters and a marker indicating the general area of this latest occurrence.

####Example Heatmap:
Below is a heatmap of all Pidgey appearances in a single day. The latest occurrence is marked by the small blue dot in the centre (the actual output is a zoom-able HTML file, not a PNG like below). This will hopefully let you get to the current Pidgey, but also give you an idea of where to look for others if you don't get there in time.
![heatmap_any](https://cloud.githubusercontent.com/assets/9369383/17296837/06103736-57fb-11e6-8e73-06523d39f598.png)

### Thanks:
Based on [leegao](https://github.com/leegao/pokemongo-api-demo/tree/master)'s work.
