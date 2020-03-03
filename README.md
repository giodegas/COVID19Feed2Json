# COVID19Feed2Json
Python API to returning Civil Protection Department and Italian Ministry of Health official COVID19 data in Italy. It is based on web scraping activity.

## API END POINTS

#### https://covid19-it-api.herokuapp.com/data
Returns **GeoJSON** data from live web scraping of the source. This is no more updated 

#### https://covid19-it-api.herokuapp.com/summary
Returns **JSON** daily data about total infected people, positive, deads, recovered.
Optional parameter:
- data (*type: String*, *example: 2020-02-25 18:00*)

#### https://covid19-it-api.herokuapp.com/state
Returns **JSON** daily data about the sanitary state of infected people
Optional parameter:
- data (*type: String*, *example: 2020-02-25 18:00*)

#### https://covid19-it-api.herokuapp.com/distribution/regions
Returns **GeoJSON** daily data about the outbreaks in each Region
Optional parameter:
- data (*type: String*, *example: 2020-02-25 18:00*)

#### https://covid19-it-api.herokuapp.com/distribution/regions/last
Returns **GeoJSON** data about the last updated outbreaks in each Region 
Optional parameter:
- data (*type: String*, *example: 2020-02-25 18:00*)

## Source
All information comes from <a target="_blank" href="http://www.protezionecivile.gov.it/">Sito del Dipartimento della Protezione Civile - Presidenza del Consiglio dei Ministri</a>

## Thanks...
...to my friend <a href="https://github.com/aborruso">Andrea Borruso</a> for his precious suggestions and encouragement
