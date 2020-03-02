# Estrae data e ora dal titolo della pagina
def formatDate(titolo):
    from datetime import datetime
    data = titolo.split(":")[1].strip()
    if 'Gennaio'.casefold() in data:
        monthNum = "1"
        data_e_ora = data.replace('Gennaio'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')
        
    if 'Febbraio'.casefold() in data:
        monthNum = "2"
        data_e_ora = data.replace('Febbraio'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Marzo'.casefold() in data:
        monthNum = "3"
        data_e_ora = data.replace('Marzo'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')
        
    if 'Aprile'.casefold() in data:
        monthNum = "4"
        data_e_ora = data.replace('Aprile'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Maggio'.casefold() in data:
        monthNum = "5"
        data_e_ora = data.replace('Maggio'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Giugno'.casefold() in data:
        monthNum = "6"
        data_e_ora = data.replace('Giugno'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Luglio'.casefold() in data:
        monthNum = "7"
        data_e_ora = data.replace('Luglio'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Agosto'.casefold() in data:
        monthNum = "8"
        data_e_ora = data.replace('Agosto'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Settembre'.casefold() in titolo:
        monthNum = "9"
        data_e_ora = data.replace('Settembre'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Ottobre'.casefold() in data:
        monthNum = "10"
        data_e_ora = data.replace('Ottobre'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Novembre'.casefold() in data:
        monthNum = "11"
        data_e_ora = data.replace('Novembre'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    if 'Dicembre'.casefold() in data:
        monthNum = "12"
        data_e_ora = data.replace('Dicembre'.casefold(),monthNum).replace(', ore ','T').replace(' ','-').replace('.',':')

    format_date = datetime.strptime(data_e_ora, '%d-%m-%YT%H:%M')
    return format_date