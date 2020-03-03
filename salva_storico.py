def saveSummary(data, positivi, deceduti, guariti, tot_casi, csv_path):
    import csv
    import pandas as pd
    # Caricamento del sommario storico CSV in pandas
    df = pd.read_csv(csv_path)
    # Aggiunta del nuovo record allo storico se non è già presente
    if str(data) in df.aggiornamento.values:
        print('tutti i dati epidemiologici sono aggiornati')
    else:
        print('inserimento dei nuovi dati epidemiologici')
        df_updated = df.append(pd.DataFrame([[str(data),tot_casi,positivi,deceduti,guariti]], columns=df.columns))
        df_updated.to_csv(csv_path,index=False)
    
def saveTreatments(data, num_isolamento, num_ricoverati, num_tintensiva, csv_path):
    import csv
    import pandas as pd
    # Caricamento dello storico CSV dei trattamenti in pandas
    df = pd.read_csv(csv_path)
    # Aggiunta del nuovo record allo storico se non è già presente
    if str(data) in df.aggiornamento.values:
        print('tutti i dati sullo stato sanitario dei casi sono aggiornati')
    else:
        print('inserimento dei nuovi dati sullo stato sanitario dei casi')
        df_updated = df.append(pd.DataFrame([[str(data),num_isolamento,num_ricoverati,num_tintensiva]], columns=df.columns))
        df_updated.to_csv(csv_path,index=False)

def saveRegions(list_regioni,data,csv_path):
    import csv
    import pandas as pd
    # Caricamento dello storico CSV dei trattamenti in pandas
    df = pd.read_csv(csv_path)
    # Aggiunta del nuovo record allo storico se non è già presente
    if str(data) in df.aggiornamento.values:
        print('tutti i dati sulla distribuzione dei casi sono aggiornati')
    else:
        print('inserimento dei nuovi dati sulla distribuzione dei casi')
        df_updated = df.append(list_regioni , ignore_index=True)
        df_updated.to_csv(csv_path,index=False)