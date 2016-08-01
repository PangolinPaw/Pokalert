import gmplot
import sqlite3

dbFile = 'pokedex.db'
db = ''
c =''

def initialise():
	"Initialise database"
	global dbFile, c, db
	db = sqlite3.connect(dbFile) # Open database (create it if it does't exist)
	db.text_factory = str
	c = db.cursor()



def readPoints(category, place):
	if c == '':
		initialise()
	
	#c.execute("SELECT NAME, LAT, LNG FROM {table} WHERE LOCATION=?".format(table=category),(place.upper(),))

	c.execute("SELECT NAME, LAT, LNG FROM {table}".format(table=category))
	coords = c.fetchall()

	return coords

def filterPoke(appearances, pokemon="ANY"):
	filteredList = []
	for appearance in appearances:
		if pokemon.upper() != "ANY":
			if appearance[0] == pokemon:
				#print "{pkmn}\t\t {lat}, {lng}".format(pkmn=appearance[0], lat=appearance[1], lng=appearance[2])
				filteredList.append([appearance[1], appearance[2]])
		else:
			filteredList.append([appearance[1], appearance[2]])
			#print "{pkmn}\t\t {lat}, {lng}".format(pkmn=appearance[0], lat=appearance[1], lng=appearance[2])
	return filteredList

def formatCoord(appearances):
	latList = []
	lngList = []

	for appearance in appearances:
		lat = float(appearance[0])
		lng = float(appearance[1])
		latList.append(lat)
		lngList.append(lng)

	return latList, lngList

def addPoints(startLat, startLng, latList, lngList, pkmn):
	gmap = gmplot.GoogleMapPlotter(startLat, startLng, 16)
	gmap.heatmap(latList, lngList, 10, 30, None, 0.8)
	gmap.scatter([startLat], [startLng], '#00129D', size=10, marker=False)
	mapname = "maps/heatmap_{0}.html".format(pkmn)
	gmap.draw(mapname)
	return mapname

def makeMap(pkmn, startLat, startLng):
	"Produce heatmap of specified pokemon."
	appearances = readPoints("history", "")
	filtAppearances = filterPoke(appearances, pokemon=pkmn)
	latList, lngList = formatCoord(filtAppearances)
	mapname = addPoints(startLat, startLng, latList, lngList, pkmn)
	return mapname

def main():
	appearances = readPoints("history", "MASSEY CLOSE, CHIPPENHAM, WILTSHIRE")
	filtAppearances = filterPoke(appearances)
	latList, lngList = formatCoord(filtAppearances)
	print latList
	print lngList
	addPoints(latList[0], lngList[1], latList, lngList)

if __name__ == "__main__":
	#main()
	latList = [51.5927253232909, 51.5951882786809, 51.5941185409947]
	lngList = [-2.09981378520729, -2.10469812300322, -2.10471326294716]
	startLat = 51.5957719419205
	startLng = -2.10426268353617
	makeMap("Weedle", startLat, startLng)
