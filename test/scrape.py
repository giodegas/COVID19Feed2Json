import feedparser
import requests
from lxml import html

url = 'http://www.protezionecivile.gov.it/web/guest/dettaglio/-/journal/rss/351561?doAsGroupId=20182&refererPlid=42041&controlPanelCategory=current_site.content&_15_groupId=20182'
feed = feedparser.parse(url)

data = []
titles = ['i casi accertati', 'i casi', 'i contagiati', 'i positivi']
for post in feed.entries:
    if any(x in post.title for x in titles):
        resp = requests.get(post.link)
        tree = html.fromstring(resp.content)
        subs = 'Nel dettaglio:'

        main = tree.xpath("//div[@class='top-content-body']//text()")
        # info = [i for i in main if subs in i]
        info = [i for i in main]
        if len(info) == 0:
            main = tree.xpath("//div[@class='top-content-body']//p/text()")
            # info = [i for i in main if subs in i]
            info = [i for i in main]

        details = [d for d in info if subs in d]
        # print(details)
        desc = details[0].split('Nel dettaglio:')[1].strip()

        print(post.link)

        '''
        # Seleziona come descrizione la parte della string successiva allo split 'Nel dettaglio:'
        desc = info[0].split('Nel dettaglio:')[1].strip()
        # Organizzazione dei dati del bollettino in un dizionario
        dict = {
            'titolo': post.title,
            'aggiornamento_del': post.published,
            'link': post.link
        }
        data.append(dict)

        print(dict)
        '''