"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
from pathlib import Path

solicitudes_de_credito = pd.read_csv(Path("files/input/solicitudes_de_credito.csv"), sep=';', index_col=0)


solicitudes_de_credito['sexo'] = solicitudes_de_credito['sexo'].str.lower().str.replace('_', ' ').str.replace('-', ' ')
solicitudes_de_credito['tipo_de_emprendimiento'] = solicitudes_de_credito['tipo_de_emprendimiento'].str.lower().str.replace('_', ' ').str.replace('-', ' ')
solicitudes_de_credito['idea_negocio'] = solicitudes_de_credito['idea_negocio'].str.lower().str.replace('_', ' ').str.replace('-', ' ')
solicitudes_de_credito['barrio'] = solicitudes_de_credito['barrio'].str.lower().str.replace('_', ' ').str.replace('-', ' ')
solicitudes_de_credito['línea_credito'] = solicitudes_de_credito['línea_credito'].str.lower().str.replace('_', ' ').str.replace('-', ' ')


solicitudes_de_credito['estrato'] = solicitudes_de_credito['estrato'].astype(int)
solicitudes_de_credito['comuna_ciudadano'] = solicitudes_de_credito['comuna_ciudadano'].astype(float)


def parse_date(date_str):
        if pd.isna(date_str):
            return pd.NaT
        try:
            parts = date_str.split("/")
            if len(parts) == 3:
                if len(parts[0]) == 4:
                    return pd.to_datetime(date_str, format="%Y/%m/%d")
                else:
                    return pd.to_datetime(date_str, format="%d/%m/%Y")
            parts = date_str.split("-")
            if len(parts) == 3:
                if len(parts[0]) == 4:
                    return pd.to_datetime(date_str, format="%Y-%m-%d")
                else:
                    return pd.to_datetime(date_str, format="%d-%m-%Y")
        except:
            return pd.NaT

solicitudes_de_credito["fecha_de_beneficio"] = solicitudes_de_credito["fecha_de_beneficio"].apply(parse_date).dt.strftime("%Y-%m-%d")

solicitudes_de_credito['monto_del_credito'] = solicitudes_de_credito['monto_del_credito'].str.replace('$', '').str.replace(',', '').str.strip().astype(float).astype(int)

solicitudes_de_credito = solicitudes_de_credito.dropna()

solicitudes_de_credito = solicitudes_de_credito.drop_duplicates()

to_csv_path = Path("files/output/solicitudes_de_credito.csv")
to_csv_path.parent.mkdir(parents=True, exist_ok=True)

solicitudes_de_credito.to_csv(to_csv_path, index=False, sep=';')

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    solicitudes_de_credito.to_csv("files/output/solicitudes_de_credito.csv", index=False, sep=';')
    print("Limpieza realizada y archivo guardado")
