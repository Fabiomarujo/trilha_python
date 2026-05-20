# ⚔️ Simulador de Batalha TCG (Trading Card Game)

Este projeto foi desenvolvido como parte do **Desafio 2 da for_code**. O objetivo é simular um duelo de turnos entre dois monstros, validando lógica de programação, manipulação de estados (HP) e controle de fluxo em Python.

## 🚀 Como Funciona
O programa solicita o nome, vida e ataque de dois monstros. A batalha ocorre em turnos:
1. O Monstro 1 ataca primeiro.
2. Se o Monstro 2 sobreviver, ele contra-ataca.
3. O placar é atualizado e o ciclo se repete até que o HP de alguém chegue a 0.

### Regras Aplicadas:
- **Validação:** Não são aceitos valores de HP ou Ataque menores ou iguais a zero.
- **Saúde:** O HP nunca é exibido como número negativo (mínimo de 0).
- **Interface:** Narrativa de batalha utilizando formatadores de texto (f-strings).

## 🛠️ Como Executar
1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone este repositório ou baixe o arquivo `simulador_tcg.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python simulador_tcg.py

## 🧠 Perguntas Teóricas

### 1. Qual é a principal diferença prática entre usar um laço `for` e um laço `while`? Por que o `while` foi a melhor escolha para este duelo?
**Resposta:** O laço `for` é geralmente utilizado quando sabemos de antemão quantas vezes o código deve ser repetido (iteração sobre uma sequência definida). O `while` é baseado em uma condição lógica que pode ser alterada dinamicamente. No duelo, o `while` é a melhor escolha porque não sabemos quantos turnos a luta vai durar; ela deve continuar apenas **enquanto** ambos os monstros tiverem vida.

### 2. Para que serve a palavra-chave `return` dentro de uma função? O que acontece se uma função fizer um cálculo mas não possuir o `return`?
**Resposta:** O `return` serve para enviar o resultado de uma operação interna da função para o escopo que a chamou, permitindo que esse valor seja armazenado em variáveis. Se uma função realiza um cálculo mas não possui `return`, ela retorna `None` por padrão, e o resultado do cálculo é "perdido" para o restante do programa.

### 3. O que é um "Loop Infinito" e como podemos evitá-lo ao construir uma estrutura `while`?
**Resposta:** Um loop infinito ocorre quando a condição do `while` nunca se torna falsa, fazendo o programa rodar para sempre ou travar. Para evitá-lo, devemos garantir que, dentro do corpo do loop, ocorra uma alteração nas variáveis de controle (ex: diminuir o HP do defensor) que leve a condição de parada a ser atingida.

## 🧑‍💻 Autor
Desenvolvido por Fábio Gonçalves.
