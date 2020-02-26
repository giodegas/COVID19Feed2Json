def parseAccertati(desc):
    accertati = desc.split('. ')[0]
    casi = []
    for caso in accertati.replace('ed',',').split(', '):
        casi.append(caso.replace('i casi accertati di Coronavirus in ','').replace(' sono',':').replace(' in ',': ').replace(' nel ',': ').replace(' nella ',': ').replace(' nelle ',': ').replace('uno','1').replace('una','1').strip() )
    
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
'''
def parsePazienti(desc):
    pazienti = desc.split('. ')[1]
    return pazienti.split(', ')
'''

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

def parseEsiti(desc):
    esiti = desc.split('. ')[2]
    return esiti.split(', ')

def parseGuariti(desc):
    import re
    esiti = desc.split('. ')[2]
    num = re.findall(r'\d+',esiti.split(', ')[0].replace('Una','1'))
    return int(num[0])

def parseDeceduti(desc):
    import re
    esiti = desc.split('. ')[2]
    num = re.findall(r'\d+',esiti.split(', ')[1])
    return int(num[0])