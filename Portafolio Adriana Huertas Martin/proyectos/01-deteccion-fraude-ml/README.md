# Detección de Fraude en Transacciones Financieras (Machine Learning)

## Problema de Negocio
Las pérdidas por transacciones fraudulentas representan un alto impacto financiero. El reto principal es el extremo desbalance de clases (menos del 1% de transacciones son fraude).

## Solución Aplicada
1. Tratamiento de datos con **SMOTE** para balanceo de clases.
2. Entrenamiento con **Random Forest / XGBoost** optimizando métricas como *Recall* y *AUC-ROC*.
3. Definición de umbrales dinámicos de riesgo para minimizar bloqueos a usuarios legítimos.
