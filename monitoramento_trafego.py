# Dados do monitoriamento via câmera
avenidas = ['Av. Central', 'Av. Brasil', 'Av. Central', 'Linha Verde', 'Linha Amarela', 'Linha Vermelha', 'BR 101', 'BR 40', 'BR 115', 'Est. Magé', 'Av. Maricá', 'Av. Paulista', 'Av. Suburbana', 'Est. Timdiba', 'Av. Mananciais', 'Av. Brasil', 'Av. Paulista']
horarios = ['07:00', '07:05', '07:10', '07:15', '07:20', '07:25', '07:30', '07:35', '07:40', '07:45', '07:50', '08:00', '08:05', '08:10', '08:15', '08:20', '08:25']
veiculos = [120, 340, 150, 500, 290, 110, 100, 90, 100, 95, 120, 125, 360, 320, 340, 200, 105]
cogestionamento = [35, 80, 40, 92, 75, 34, 32, 30, 32, 31, 35, 36, 84, 78, 80, 65, 33]

# 1. Identificação dos Tipos de veículos (Set)
avenidas_unicas = set(avenidas)
print(f"Total de avenidas diferentes: {len(avenidas_unicas)}")
print(f"CompAvenidas únicas: {avenidas_unicas}\n")

# 2. Estruturação do Monitoramento, unindo lista com ZIP
monitoramento = list(zip(avenidas, horarios, veiculos, cogestionamento))

# 3. Geração de Relatório (Unpacking)
print("--- RELATÓRIO DE MONITORAMENTO ---")
for local, horario, veiculo, trafego in monitoramento:
    print(f"Local: {local} | Horário: {horario} | Veículo: {veiculo} | Congestionamento: {trafego}")

# 4. Filtragem inteligente de horários críticos (List Comprehension)
horario_pico = [horario for local, horario, veiculo, trafego in monitoramento if trafego >= 40]
locais_horario_pico = [horario and local for local, horario, veiculo, trafego in monitoramento if trafego >= 40]

print(f"\n--- HORARIO(S) DE PICO ---\n")
print(f"Horários de pico de trafego com maior volume de carro: {horario_pico}\n")

# 5. Geração de ranking utilizando (dict comprehension)
ranking = dict([(avenidas[i], cogestionamento[i]) for i in range(len(avenidas_unicas))])

print(f"\n--- RANKING  ---\n")
print(ranking)

# 6. Sistemas de Alertas (if, elif e else)
print(f"\n--- ALERTA DAS VIAS ---\n")
for local, horario, veiculo, trafego in monitoramento:
    if trafego >= 40:
        print(f"Evite estes Locais: {local}\n")
    elif trafego < 40:
        print(f"Vias com melhor fluxo de veículos:{local}")

