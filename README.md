## Pokalert
### Introduction:
Email alerts when 'interesting' pokemon are encountered.

(At present emails are sent via Outlook, GMail version pending...)

### Installation:
pip install -r requirements.txt

### Usage:
Note: This stuff is unfinished and untested.
* Enter Pokemon Trainer Club login details and a location to settings.txt
* Add recipient email to alert.py
* Run main.py
* List (one per line) the pokedex numbers of any pokemon you're interested in in alertList.txt

**main.py** will list all pokemon currently in the area and save an account of appearances to the histroy table of **pokedex.db**.

If an interesting pokemon (listed in **alertList.txt**) appears, details are sent to the recipient, along with a heatmap of all previous encounters and a marker indicating the general area of this latest occurrence.

####Example Heatmap:
![heatmap_any](https://cloud.githubusercontent.com/assets/9369383/17296837/06103736-57fb-11e6-8e73-06523d39f598.png)

### Thanks:
Based on [leegao](https://github.com/leegao/pokemongo-api-demo/tree/master)'s work
