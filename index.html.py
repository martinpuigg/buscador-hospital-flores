# backend.py (Python + FastAPI)
from fastapi import FastAPI
import pandas as pd
from fuzzywuzzy import fuzz

app = FastAPI()
df = pd.read_csv('ObjetosGasto.csv')

@app.get("/api/buscar/{query}")
def buscar(query: str):
    resultados = []
    for _, row in df.iterrows():
        score = fuzz.partial_ratio(query.lower(), row['Denominación'].lower())
        if score > 50:
            resultados.append({**row, 'score': score})
    return sorted(resultados, key=lambda x: x['score'], reverse=True)[:50]