import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.reset_index(inplace=True,drop=True)
    
    df.drop(columns=['Unnamed: 0'],inplace=True)

    df["sexo"] = df["sexo"].str.upper().astype(str).str.strip()
    df["sexo"] = df["sexo"].str[0]
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['barrio'] = df['barrio'].str.lower().astype(str)
    df['barrio'] = df['barrio'].str.replace('_','-').str.replace('-',' ')
    df['estrato'] = df['estrato'].astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],dayfirst=True, format='mixed')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').str.strip().astype(float)   
    df['línea_credito'] = df['línea_credito'].str.lower().astype(str)
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ').str.replace('-',' ').str.strip()
    
    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)
    
    return df
