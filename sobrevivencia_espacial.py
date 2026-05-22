import random
import sys


def validar_positivo(valor_str):
    """Valida se a entrada é um inteiro maior que zero.

    Caso inválido, encerra o programa.
    """
    try:
        valor = int(valor_str)
        if valor <= 0:
            print("Valor inválido. Reinicie o programa usando valores positivos.")
            sys.exit()
        return valor
    except ValueError:
        print("Valor inválido. Reinicie o programa usando valores positivos.")
        sys.exit()


def exibir_status(ciclo, max_ciclos, oxigenio, energia, alimento):
    """Exibe o painel com as estatísticas atuais da missão."""
    print("\n" + "=" * 40)
    print(f" STATUS DA MISSÃO - CICLO {ciclo}/{max_ciclos}")
    print("=" * 40)
    print(f"💨 Oxigênio: {oxigenio}")
    print(f"⚡ Energia:  {energia}")
    print(f"🍲 Alimento: {alimento}")
    print("=" * 40)


def processar_evento_aleatorio(oxigenio, energia, alimento):
    """Gera um evento automático aleatório impactando os recursos."""
    evento = random.randint(1, 4)
    print("\n⚡ [EVENTO DO PLANETA]")

    if evento == 1:
        print("🚨 Uma tempestade solar atingiu a nave! Perda de 15 de energia.")
        energia -= 15
    elif evento == 2:
        print(
            "🧪 Você encontrou uma fenda de gás respirável! Ganho de 20 de oxigênio."
        )
        oxigenio += 20
    elif evento == 3:
        print(
            "🪳 Criaturas locais invadiram o depósito! Perda de 10 de alimento."
        )
        alimento -= 10
    else:
        print("🌌 O ciclo correu tranquilamente sem anomalias externas.")

    return oxigenio, energia, alimento


def main():
    print("🚀 CONFIGURAÇÃO DO SISTEMA DE SOBREVIVÊNCIA - ORION EXPEDITION 🚀")

    # 1. Entrada de Dados e Tipos
    comandante = input("Digite o nome do comandante: ").strip()

    oxigenio = validar_positivo(
        input("Digite a quantidade inicial de oxigênio: ")
    )
    energia = validar_positivo(input("Digite a quantidade inicial de energia: "))
    alimento = validar_positivo(input("Digite a quantidade inicial de alimento: "))
    max_ciclos = validar_positivo(
        input("Digite a quantidade máxima de ciclos de sobrevivência: ")
    )

    print(f"\nBoa sorte, Comandante {comandante}. O simulador começou!")

    ciclo_atual = 1

    # 3. Estrutura Principal do Sistema (Laço while)
    while ciclo_atual <= max_ciclos:
        # 1. Exibe os recursos atuais
        exibir_status(ciclo_atual, max_ciclos, oxigenio, energia, alimento)

        # 2. Escolha de ação com validação de entrada
        print("Escolha sua ação para este ciclo:")
        print("1 - Explorar região (+Alimento, -Energia)")
        print("2 - Descansar (+Energia, -Alimento)")
        print("3 - Procurar oxigênio (+Oxigênio, -Energia)")
        print("4 - Reparar sistemas de suporte (-Alimento, +Oxigênio/Energia)")

        opcao = input("Digite a opção (1-4): ").strip()

        # 3. Ação altera os recursos
        if opcao == "1":
            print("\n🔍 Explorando a região externa...")
            alimento += 25
            energia -= 15
            oxigenio -= 5
        elif opcao == "2":
            print("\n💤 Tripulação descansando nos alojamentos...")
            energia += 30
            alimento -= 10
        elif opcao == "3":
            print("\n💨 Coletando oxigênio da atmosfera filtrada...")
            oxigenio += 25
            energia -= 15
        elif opcao == "4":
            print("\n🛠️ Efetuando reparos críticos na engenharia...")
            oxigenio += 15
            energia += 10
            alimento -= 15
        else:
            print(
                "\n❌ Comando inválido! A tripulação ficou confusa e perdeu o turno."
            )
            energia -= 5

        # Consumo fixo de sobrevivência por ciclo (Lógica de manutenção)
        oxigenio -= 10
        alimento -= 5

        # 5. Verifica condições de derrota imediata antes do evento
        if oxigenio <= 0 or energia <= 0 or alimento <= 0:
            break

        # 4. Evento automático acontece
        oxigenio, energia, alimento = processar_evento_aleatorio(
            oxigenio, energia, alimento
        )

        # 5. Verifica condições de derrota pós-evento
        if oxigenio <= 0 or energia <= 0 or alimento <= 0:
            break

        # Avança o ciclo se sobreviveu
        ciclo_atual += 1

    # Fim do jogo - 5. Verificação de Vitória ou Derrota
    print("\n" + "=" * 40)
    if oxigenio > 0 and energia > 0 and alimento > 0:
        print("🎉 VITÓRIA! 🎉")
        print(
            f"Parabéns, Comandante {comandante}! A equipe da Orion Expedition sobreviveu até o resgate!"
        )
    else:
        print("💀 DERROTA! 💀")
        print(
            f"O sistema de suporte falhou. A tripulação do Comandante {comandante} não resistiu."
        )
        print(
            f"Recursos finais -> Oxigênio: {oxigenio} | Energia: {energia} | Alimento: {alimento}"
        )
    print("=" * 40)


if __name__ == "__main__":
    main()
