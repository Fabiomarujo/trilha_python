import random
import sys

def validar_positivo(valor_str):
    """Valida se a entrada é um inteiro maior que zero. Encerra se for inválida."""
    try:
        valor = int(valor_str)
        if valor <= 0:
            print("Valor inválido. Reinicie o programa usando valores positivos.")
            sys.exit()
        return valor
    except ValueError:
        print("Valor inválido. Reinicie o programa usando valores positivos.")
        sys.exit()

def exibir_status(ciclo, comandante, oxigenio, energia, alimento, integridade):
    """Exibe o painel de controle atualizado para o usuário."""
    print("\n" + "="*40)
    print(f" CICLO {ciclo} - PAINEL DA ORION EXPEDITION")
    print(f" Comandante: {comandante}")
    print("="*40)
    print(f" [O2] Oxigênio: {oxigenio}")
    print(f" [⚡] Energia: {energia}")
    print(f" [🍎] Alimento: {alimento}")
    print(f" [🛠️] Integridade da Nave: {integridade}%")
    print("="*40)

def executar_evento_aleatorio(oxigenio, energia, alimento, integridade):
    """Sorteia um evento automático que impacta os recursos ao fim do ciclo."""
    evento = random.randint(1, 4)
    print("\n--- EVENTO DO CICLO ---")
    
    if evento == 1:
        print("💨 Uma microfuga de oxigênio foi detectada no setor B! (-15 O2)")
        oxigenio -= 15
    elif evento == 2:
        print("☀️ Tempestade solar! Os painéis absorveram radiação residual. (+20 Energia)")
        energia += 20
    elif evento == 3:
        print("🦠 Praga espacial contaminou parte da despensa criogênica! (-10 Alimento)")
        alimento -= 10
    elif evento == 4:
        print("☄️ Chuva de micrometeoritos atingiu a fuselagem externa! (-15% Integridade)")
        integridade -= 15
        
    return oxigenio, energia, alimento, integridade

def main():
    print("\n========================================")
    print("    INICIALIZAÇÃO: ORION EXPEDITION     ")
    print("========================================")
    
    comandante = input("Digite o nome do comandante: ").strip()
    if not comandante:
        print("Nome inválido. Reinicie o programa.")
        sys.exit()
        
    oxigenio = validar_positivo(input("Quantidade inicial de oxigênio: "))
    energia = validar_positivo(input("Quantidade inicial de energia: "))
    alimento = validar_positivo(input("Quantidade inicial de alimento: "))
    ciclos_maximos = validar_positivo(input("Quantidade máxima de ciclos para o resgate: "))
    
    # Status inicial extra para a opção 4 (Reparar sistemas)
    integridade_nave = 50 
    ciclo_atual = 1
    
    print("\n🚀 Configuração aceita com sucesso! Iniciando simulação...")

    # Laço principal de sobrevivência
    while ciclo_atual <= ciclos_maximos:
        exibir_status(ciclo_atual, comandante, oxigenio, energia, alimento, integridade_nave)
        
        print("Escolha sua ação para este ciclo:")
        print("1 - Explorar região (Gasta oxigênio e energia, busca suprimentos)")
        print("2 - Descansar (Consome alimento e oxigênio, recupera energia)")
        print("3 - Procurar alimento (Gasta energia, encontra comida)")
        print("4 - Reparar sistemas (Gasta energia, conserta a nave)")
        
        opcao = input("Sua opção (1-4): ").strip()
        
        # 1. Processamento das Escolhas do Usuário
        if opcao == "1":
            print("\n🔍 Explorando os arredores do planeta hostil...")
            oxigenio -= 10
            energia -= 15
            coleta = random.randint(10, 30)
            alimento += coleta
            print(f"Sucesso! Encontrado {coleta} unidades de nutrientes nativos.")
            
        elif opcao == "2":
            print("\n💤 Tripulação em repouso nos alojamentos...")
            alimento -= 10
            oxigenio -= 5
            energia += 25
            print("Energia regenerada substancialmente.")
            
        elif opcao == "3":
            print("\n🌾 Vasculhando compartimentos e estufas internas...")
            energia -= 10
            coleta = random.randint(15, 35)
            alimento += coleta
            print(f"Sucesso! Produzido {coleta} unidades de ração sintética.")
            
        elif opcao == "4":
            print("\n🛠️ Realizando reparos prioritários na estrutura...")
            energia -= 15
            reparo = random.randint(15, 25)
            integridade_nave = min(100, integridade_nave + reparo)
            print(f"Casco reforçado em +{reparo}%.")
            
        else:
            print("\n⚠️ Comando inválido! A tripulação hesitou e perdeu tempo precioso.")
            # Penalidade leve por comando inexistente
            oxigenio -= 5
            energia -= 5

        # 2. Evento Automático de Fim de Turno
        oxigenio, energia, alimento, integridade_nave = executar_evento_aleatorio(
            oxigenio, energia, alimento, integridade_nave
        )

        # 3. Verificação de Condições de Derrota
        if oxigenio <= 0 or energia <= 0 or alimento <= 0 or integridade_nave <= 0:
            print("\n❌" + "!"*38 + "❌")
            print("         CRÍTICO: TRIPULAÇÃO PERDIDA!         ")
            print("!"*40)
            if oxigenio <= 0:
                print("- O sistema de suporte de vida falhou por falta de Oxigênio.")
            if energia <= 0:
                print("- A nave congelou no espaço por falta de Energia.")
            if alimento <= 0:
                print("- A tripulação sucumbiu à inanição por falta de Alimento.")
            if integridade_nave <= 0:
                print("- A estrutura colapsou totalmente sob a pressão atmosférica.")
            print("\nFIM DE JOGO: Você falhou em manter a Orion Expedition viva.")
            break

        # 4. Verificação de Condição de Vitória
        if ciclo_atual == ciclos_maximos:
            print("\n🏆" + "="*38 + "🏆")
            print("          VITÓRIA: O RESGATE CHEGOU!          ")
            print("="*40)
            print(f"Parabéns Comandante {comandante}! Suas decisões salvaram a equipe.")
            print(f"A frota de resgate pousou com sucesso no ciclo {ciclo_atual}.")
            break
            
        ciclo_atual += 1

if __name__ == "__main__":
    main()
