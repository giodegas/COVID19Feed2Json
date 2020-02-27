def parseAccertati(desc):
    accertati = desc.split('. ')[0]
    casi = []
    for caso in accertati.replace('ed',',').split(', '):
        casi.append(caso.replace('i casi accertati di Coronavirus in ','').replace(' sono',':').replace(' in ',': ').replace(' nel ',': ').replace(' nella ',': ').replace(' nelle ',': ').replace(' e ','').replace(' a ',': ').replace('uno','1').replace('una','1').strip() )
    
    data = []
    for i,val in enumerate(casi):
        if i > 0:
            # print(val.split(': ')[::-1])
            dict = { val.split(': ')[::-1][0] :  int(val.split(': ')[::-1][1]) }
        else: 
            # print(val.split(': '))
            dict = { val.split(': ')[::-1][1] : int(val.split(': ')[::-1][0]) }   
        data.append(dict)
    
    #print(data)   
    return data

def parseRicoverati(desc):
    import re
    pazienti = desc.split('. ')[1]
    num = re.findall(r'\d+',pazienti.split(', ')[0])
    return int(num[0])

def parseTerapiaIntensiva(desc):
    import re
    pazienti = desc.split('. ')[1]
    num = re.findall(r'\d+',pazienti.split(', ')[1])
    return int(num[0])

def parseIsolamentoDomiciliare(desc):
    import re
    pazienti = desc.split('. ')[1]
    num = re.findall(r'\d+',pazienti.split(', ')[2])
    return int(num[0])

def parseGuariti(desc):
    from word2number import w2n
    from googletrans import Translator
    esiti = desc.split('. ')[2]
    guariti = esiti.split(', ')[0]
    word_num = guariti.split(' ')[0]
    if word_num == 'Una':
        word_num_en = 'One'
    else: 
        translator = Translator()
        word_num_en = translator.translate(word_num, src='it', dest='en').text

    num_guariti = w2n.word_to_num(word_num_en)
    return num_guariti

def parseDeceduti(desc):
    import re
    esiti = desc.split('. ')[2]
    num = re.findall(r'\d+',esiti.split(', ')[1])
    return int(num[0])