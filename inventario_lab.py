# Dados do inventário físico
reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 'Ácido Acético', 'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol', 'Acetona', 'Metanol', 'Ácido Sulfúrico', 'Acetona', 'Ácido Acético', 'Etanol']
lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01', '2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01', '2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02', '2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01', '2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01', '2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01', '2023-ETA-02']
purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0, 99.2, 96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0, 98.5, 95.0, 96.0]

# 1. Identificação dos Tipos de Reagentes (Set)
reagentes_unicos = set(reagentes)
print(f"Total de reagentes diferentes: {len(reagentes_unicos)}")
print(f"Compostos únicos: {reagentes_unicos}\n")

# 2. Estruturação do Inventário, unindo lista com ZIP
inventario = list(zip(reagentes, lotes, purezas))

# 3. Geração de Relatório 
print("--- RELATÓRIO DE INVENTÁRIO ---")
for nome, lote, valor in inventario:
    print(f"Frasco do Lote: {lote} | Reagente: {nome:15} | Pureza: {valor}%")

# 4. Filtragem 
lotes_aprovados = [lote for nome, lote, valor in inventario if valor >= 98.0]

print(f"\n--- LOTES APROVADOS (PUREZA >= 98%) ---")
print(lotes_aprovados)
