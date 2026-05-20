def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    """
    Realiza o ataque, subtrai o HP e garante que não seja negativo.
    Retorna o novo valor de HP do defensor.
    """
    hp_atualizado = hp_defensor - ataque
    
    # Restrição: HP nunca deve ser menor que zero
    if hp_atualizado < 0:
        hp_atualizado = 0
        
    print(f"{nome_atacante} atacou {nome_defensor} causando {ataque} de dano!")
    return hp_atualizado

def exibir_placar(nome1, hp1, nome2, hp2):
    """Exibe o HP atual de ambos os monstros."""
    print(f"\n--- PLACAR ---")
    print(f"{nome1}: {hp1} HP")
    print(f"{nome2}: {hp2} HP")
    print("-" * 14 + "\n")

def main():
    print("\n⚔️  SIMULADOR DE BATALHA TCG  ⚔️\n")

    # 1. Entrada de Dados
    nome_monstro1 = input("Digite o nome do Monstro 1: ")
    hp_monstro1 = int(input(f"Digite os Pontos de Vida (HP) de {nome_monstro1}: "))
    ataque_monstro1 = int(input(f"Digite os Pontos de Ataque de {nome_monstro1}: "))

    nome_monstro2 = input("Digite o nome do Monstro 2: ")
    hp_monstro2 = int(input(f"Digite os Pontos de Vida (HP) de {nome_monstro2}: "))
    ataque_monstro2 = int(input(f"Digite os Pontos de Ataque de {nome_monstro2}: "))

    # Validação de Entrada
    if hp_monstro1 <= 0 or ataque_monstro1 <= 0 or hp_monstro2 <= 0 or ataque_monstro2 <= 0:
        print("\n❌ VALOR INVÁLIDO: Vida e Ataque devem ser maiores que zero. O programa será encerrado.")
        return

    print(f"\n🔥 O DUELO COMEÇOU: {nome_monstro1} vs {nome_monstro2}! 🔥\n")

    # 3. Lógica de Turnos (Loop While) loop principal
    while hp_monstro1 > 0 and hp_monstro2 > 0:
        # Monstro 1 ataca o Monstro 2
        hp_monstro2 = atacar(nome_monstro1, ataque_monstro1, nome_monstro2, hp_monstro2)
        
        # O Monstro 2 só contra-ataca se sobreviver
        if hp_monstro2 > 0:
            hp_monstro1 = atacar(nome_monstro2, ataque_monstro2, nome_monstro1, hp_monstro1)
        
        # Exibe o placar após cada rodada de ataques
        exibir_placar(nome_monstro1, hp_monstro1, nome_monstro2, hp_monstro2)

    # 4. Condição de Vitória
    if hp_monstro1 > 0:
        print(f"🏆 O grande vencedor é: {nome_monstro1}!")
    else:
        print(f"🏆 O grande vencedor é: {nome_monstro2}!")

if __name__ == "__main__":
    main()
