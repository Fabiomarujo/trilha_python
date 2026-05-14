import sys

# COTAÇÃO FIXA CONFORME ENUNCIADO
COTACAO_EUR_BRL = 6.10

def exibir_titulo():
    """Exibe o título principal do sistema."""
    print("\n" + "="*50)
    print("      SISTEMA DE AUXÍLIO AO ORÇAMENTO DE VIAGENS      ")
    print("="*50)

def realizar_calculo():
    """Executa a coleta de dados, validações e exibe o relatório."""
    print("\n--- INICIAR NOVO PLANEJAMENTO ---")
    
    # 1. ENTRADA DE DADOS COM VALIDAÇÃO REPETITIVA
    # Validação do Orçamento
    while True:
        try:
            orcamento_disponivel = float(input("Digite o orçamento disponível (BRL): "))
            if orcamento_disponivel >= 0:
                break
            print("⚠️ O programa não aceita valores negativos. Por favor, digite o valor novamente.")
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número válido.")

    # Entrada do Destino
    destino = input("Digite o destino da viagem: ")

    # Validação do Custo da Passagem
    while True:
        try:
            custo_passagem = float(input("Digite o custo da passagem (BRL): "))
            if custo_passagem >= 0:
                break
            print("⚠️ O programa não aceita valores negativos. Por favor, digite o valor novamente.")
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número válido.")

    # Validação do Custo Diário da Hospedagem
    while True:
        try:
            custo_diario_eur = float(input("Digite o custo diário da hospedagem (EUR): "))
            if custo_diario_eur >= 0:
                break
            print("⚠️ O programa não aceita valores negativos. Por favor, digite o valor novamente.")
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número válido.")

    # Validação da Quantidade de Dias
    while True:
        try:
            quantidade_dias = int(input("Digite a quantidade de dias da viagem: "))
            if quantidade_dias >= 0:
                break
            print("⚠️ O programa não aceita valores negativos. Por favor, digite o valor novamente.")
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número inteiro válido.")

    # 2. CÁLCULOS E LÓGICA
    custo_diario_brl = custo_diario_eur * COTACAO_EUR_BRL
    custo_hospedagem_total_brl = custo_diario_brl * quantidade_dias
    custo_total_viagem = custo_passagem + custo_hospedagem_total_brl

    # Validação de Orçamento
    if custo_total_viagem <= orcamento_disponivel:
        status_orcamento = "Orçamento possível"
    else:
        status_orcamento = "Orçamento não possível"

    # Status Final da Viagem
    viavel = (custo_total_viagem <= orcamento_disponivel) and (quantidade_dias > 0)
    status_final = "Viável" if viavel else "Inviável"

    # Balanço financeiro
    balanco_financeiro = orcamento_disponivel - custo_total_viagem

    # 3. EXIBIÇÃO DE RESULTADOS (f-strings)
    print("\n" + "="*40)
    print(f" RESUMO DA VIAGEM: {destino.upper()} ")
    print("="*40)
    print(f"➞ Custo total da hospedagem em Reais: R$ {custo_hospedagem_total_brl:.2f}")
    print(f"➞ Custo total da viagem em Reais: R$ {custo_total_viagem:.2f}")
    print(f"➞ Validação do orçamento: {status_orcamento}")
    print(f"➞ Status final da viagem: {status_final}")

    if balanco_financeiro >= 0:
        print(f"➞ Saldo final: Sobrará R$ {balanco_financeiro:.2f}")
    else:
        print(f"➞ Saldo final: Faltam R$ {abs(balanco_financeiro):.2f} para atingir o objetivo")
    print("="*40)

# --- FLUXO PRINCIPAL DO MENU ---
exibir_titulo()

while True:
    print("\nEscolha uma das opções abaixo:")
    print("[ 1 ] Calcular Novo Orçamento de Viagem")
    print("[ 2 ] Finalizar o Programa")
    
    opcao = input("Digite sua opção: ").strip()
    
    if opcao == "1":
        realizar_calculo()
    elif opcao == "2":
        print("\n==================================================")
        print(" O sistema foi finalizado. Boa viagem, Mariana! ✈️ ")
        print("==================================================")
        sys.exit()
    else:
        print("⚠️ Opção inválida! Escolha 1 para calcular ou 2 para finalizar.")
