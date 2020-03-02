def geocodeRegione(regione):
    coordinates = ""
    if regione == 'Lombardia':
        coordinates = [9.227828979492188,45.57463894211682]
    elif regione == 'Veneto':
        coordinates = [11.854319842000052,45.65492501300008]
    elif regione == 'Emilia-Romagna':
        coordinates = [11.039213647000054,44.52591084900007]
    elif regione == 'Liguria':
        coordinates = [9.427370000000053,44.415350258000046]
    elif regione == 'Sicilia':
        coordinates = [14.000000000000057,37.50000000000006]
    elif regione == 'Marche':
        coordinates = [13.137824067000054,43.34820017700008]
    elif regione == 'Lazio':
        coordinates = [12.772626321000075,41.97568188900004]
    elif regione == 'Campania':
        coordinates = [14.840115810000043,40.85973483500004]
    elif regione == 'Piemonte':
        coordinates = [7.92049247500006,45.05730108000006]
    elif regione == 'Toscana':
        coordinates = [11.126187689000062,43.45082948600003]
    elif regione == 'Abruzzo':
        coordinates = [13.855048784000076,42.22755568500003]
    elif regione == 'Puglia':
        coordinates = [16.618785484000057,40.98504106300004]
    elif regione == 'Molise':
        coordinates = [14.6337890625,41.6154423246811]
    elif regione == 'Basilicata':
        coordinates = [16.083984375,40.51379915504413]
    elif regione == 'Umbria':
        coordinates = [12.436523437499998,43.13306116240612]
    elif regione == 'Sardegna':
        coordinates = [7.8576966,40.0562185]
    elif regione == 'Friuli':
        coordinates = [12.5594548,46.1129993]
    elif regione == 'Trentino':
        coordinates = [10.6469911,46.1015475]
    elif regione == 'Calabria':
        coordinates = [16.446533203125,38.976492485539396]
    elif regione == 'Valle d\'Aosta':
        coordinates = [6.8099952,45.7259823]
    elif regione.find('Bolzano'):
        coordinates = [11.121170080500887,46.072160043857124]
    else:
        coordinates = [13.6614,41.9186]

    return coordinates