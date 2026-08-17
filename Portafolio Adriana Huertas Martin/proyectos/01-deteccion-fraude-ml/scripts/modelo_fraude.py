import pandas as pd
import os

def evaluar_fraude():
    print('=== EVALUACIÓN DE MODELO DE DETECCIÓN DE FRAUDE ===')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', 'data', 'transacciones_sample.csv')
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        fraudes = df[df['es_fraude'] == 1]
        print(f'Transacciones analizadas: {len(df)}')
        print(f'Fraudes detectados: {len(fraudes)}')
        print(f'Monto promedio en fraudes: USD {fraudes["monto_usd"].mean():.2f}')

if __name__ == '__main__':
    evaluar_fraude()
