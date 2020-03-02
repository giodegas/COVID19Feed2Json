def saveSummary(data, positivi, deceduti, guariti, tot_casi):
    import csv
    import pandas as pd
    # Caricamento del sommario storico CSV in pandas
    df = pd.read_csv('storico/summary.csv')
    # Aggiunta del nuovo record allo storico se non è già presente
    if str(data) in df.aggiornamento.values:
        print('tutti i dati sono aggiornati')
    else:
        print('inserimento dei nuovi dati')
        df_updated = df.append(pd.DataFrame([[str(data),tot_casi,positivi,deceduti,guariti]], columns=df.columns))
        df_updated.to_csv('storico/summary.csv',index=False)
    

def saveTreatments(data, num_isolamento, num_ricoverati, num_tintensiva):
    import csv
    import pandas as pd
    # Caricamento dello storico CSV dei trattamenti in pandas
    df = pd.read_csv('storico/trattamento.csv')
    # Aggiunta del nuovo record allo storico se non è già presente
    if str(data) in df.aggiornamento.values:
        print('tutti i dati sono aggiornati')
    else:
        print('inserimento dei nuovi dati')
        df_updated = df.append(pd.DataFrame([[str(data),num_isolamento,num_ricoverati,num_tintensiva]], columns=df.columns))
        df_updated.to_csv('storico/trattamento.csv',index=False)

def saveRegions():
    print('salvo le regioni...')