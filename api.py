import feedparser
import requests
from lxml import html
import json
from parseDescription import parseAccertati
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
                # 'ricoverati': parseRicoverati(desc),
                # 'isolamento_domiciliare':parseIsolamentoDomiciliare(desc),
                # 'guariti': parseGuariti(desc),
                # 'deceduti': parseDeceduti(desc)
            }
            data.append(dict)

    # JSON output
    return jsonify(data)

if __name__ == '__main__':
    app.run()
