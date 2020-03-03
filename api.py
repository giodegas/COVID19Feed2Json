import feedparser
import requests
from lxml import html
import json
from parseDescription import parseAccertati
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# SUMMARY DATA
@app.route('/')
def retrieve_app_info():
    return jsonify({
        'Author':'Alessio Di Lorenzo','Data Source': 'Ministero della Salute'
    })

@app.route('/data')
def retrieve_data():
    # RSS Protezione Civile
    url = 'http://www.protezionecivile.gov.it/web/guest/dettaglio/-/journal/rss/351561?doAsGroupId=20182&refererPlid=42041&controlPanelCategory=current_site.content&_15_groupId=20182'
    feed = feedparser.parse(url)
    # News con i dettagli sui casi accertati
    data = []
    titles = ['i casi accertati', 'i casi', 'i contagiati', 'i positivi']
    for post in feed.entries:
        #if "casi accertati" in post.title or "i contagiati" in post.title:
        if any(x in post.title for x in titles):
            # Estrazione dati dal link nel feed
            resp = requests.get(post.link)
            tree = html.fromstring(resp.content)
            subs = 'Nel dettaglio:'
            main = tree.xpath("//div[@class='top-content-body']//text()")
            info = [i for i in main]
            if len(info) == 0:
                main = tree.xpath("//div[@class='top-content-body']//p/text()")
                info = [i for i in main]

            details = [d for d in info if subs in d]
            desc = details[0].split('Nel dettaglio:')[1].strip()
            # Organizzazione dei dati del bollettino in un dizionario
            dict = {
                'titolo': post.title,
                'aggiornamento_del': post.published,
                'link': post.link,
                'casi_accertati': parseAccertati(desc)
            }
            data.append(dict)
    # JSON output
    return jsonify(data)

# API END POINTS

# #####################################################################
# SUMMARY DATA
# #####################################################################
@app.route('/summary')
def retrieve_summary_data():
    # Date argument
    data = request.args.get('data')
    # Read data from CSV
    df = pd.read_csv('storico/summary.csv')
    # Apply filter if argument is passed
    if data:
        out_df = df[df.aggiornamento == str(data)]
    else:
        out_df = df
    # Return values
    out_df_sorted = out_df.sort_values(by='aggiornamento', ascending=False)
    values = json.loads(out_df_sorted.to_json(orient='records'))
    return jsonify(values)

# #####################################################################
# SANITARY STATE DATA
# #####################################################################
@app.route('/state')
def retrieve_state_data():
    # Date argument
    data = request.args.get('data')
    # Read data from CSV
    df = pd.read_csv('storico/trattamento.csv')
    # Apply filter if argument is passed
    if data:
        out_df = df[df.aggiornamento == str(data)]
    else:
        out_df = df
    # Return values
    out_df_sorted = out_df.sort_values(by='aggiornamento', ascending=False)
    values = json.loads(out_df_sorted.to_json(orient='records'))
    return jsonify(values)

# #####################################################################
# DISTRIBUTION DATA (BY REGION)
# #####################################################################
@app.route('/distribution/regions')
def retrieve_regions():
    # Date argument
    data = request.args.get('data')
    # Read data from CSV
    df = pd.read_csv('storico/regioni.csv')
    # Apply filter if argument is passed
    if data:
        out_df = df[df.aggiornamento == str(data)]
    else:
        out_df = df
    # Return values
    out_df_sorted = out_df.sort_values(by='aggiornamento', ascending=False)
    # Create GeoJSON output
    geojson = {'type':'FeatureCollection', 'features':[]}
    for index, row in out_df_sorted.iterrows():
        feature = {'type':'Feature','properties':{'aggiornamento':row['aggiornamento'],'numero_casi': row['numero_casi'],'regione': row['nome_regione']},'geometry':{'type':'Point','coordinates':[ row['lng'], row['lat'] ]}}
        geojson['features'].append(feature)
    return geojson

@app.route('/distribution/regions/last')
def retrieve_regions_last():
    # Read data from CSV
    df = pd.read_csv('storico/regioni.csv')
    # Create df using only last day data
    df_last = df.sort_values(['aggiornamento']).drop_duplicates('nome_regione', keep='last')
    # Create GeoJSON output
    geojson = {'type':'FeatureCollection', 'features':[]}
    for index, row in df_last.iterrows():
        feature = {'type':'Feature','properties':{'aggiornamento':row['aggiornamento'],'numero_casi': row['numero_casi'],'regione': row['nome_regione']},'geometry':{'type':'Point','coordinates':[ row['lng'], row['lat'] ]}}
        geojson['features'].append(feature)
    return geojson

if __name__ == '__main__':
    app.run(debug=True)
