import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df.reset_index(inplace=True,drop=True)
    
    df.dropna(axis='index',inplace=True)
    df.drop_duplicates(inplace=True)

    df['sexo'] = df['sexo'].str.lower().astype(str).str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['barrio'] = df['barrio'].str.lower().astype(str)
    df['barrio'] = df['barrio'].str.replace('_','-').str.replace('-',' ')
    df['línea_credito'] = df['línea_credito'].str.lower().astype(str)
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],dayfirst=True, format='mixed')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').str.strip().astype(float)   
    
    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)
    
    return df