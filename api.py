import feedparser
import requests
from lxml import html
import json
from parseDescription import *
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data')
def retrieve_data():
    # RSS Protezione Civile
    url = 'http://www.protezionecivile.gov.it/web/guest/dettaglio/-/journal/rss/351561?doAsGroupId=20182&refererPlid=42041&controlPanelCategory=current_site.content&_15_groupId=20182'
    feed = feedparser.parse(url)
    # News con i dettagli sui casi accertati
    data = []
    for post in feed.entries:
        if "casi accertati" in post.title or "i contagiati" in post.title:
            # Estrazione dati dal link nel feed
            resp = requests.get(post.link)
            tree = html.fromstring(resp.content)
            main = tree.xpath("//div[@class='top-content-body']//p/text()")
            subs = 'Nel dettaglio:'
            info = [i for i in main if subs in i]
            desc = info[0].replace('Nel dettaglio: ','').replace(' Nel dettaglio:','')
            # Organizzazione dei dati del bollettino in un dizionario
            dict = {
                'titolo': post.title,
                'aggiornamento_del': post.published,
                'link': post.link,
                'casi_accertati': parseAccertati(desc),
                # 'ricoverati': parseRicoverati(desc),
                # 'terapia_intensiva':parseTerapiaIntensiva(desc),
                # 'isolamento_domiciliare':parseIsolamentoDomiciliare(desc),
                # 'guariti': parseGuariti(desc),
                # 'deceduti': parseDeceduti(desc)
            }
            data.append(dict)

    # JSON output
    return jsonify(data)

@app.route('/data/it')
def scrape_min_sal():
    # Sito Ministero
    url = 'http://www.protezionecivile.gov.it/web/guest/dettaglio/-/journal/rss/351561?doAsGroupId=20182&refererPlid=42041&controlPanelCategory=current_site.content&_15_groupId=20182'
    return jsonify({'Fonte':'Ministero della Salute'})

if __name__ == '__main__':
    app.run()
