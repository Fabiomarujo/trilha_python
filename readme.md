# ✈️ Sistema de Auxílio ao Orçamento de Viagens

Este é um programa em Python desenvolvido para ajudar nômades digitais e viajantes a planejarem suas finanças internacionais. O sistema consolida orçamentos em Reais (BRL), converte custos diários em Euros (EUR), valida restrições orçamentárias e verifica a viabilidade real da viagem.

## 🚀 Como Executar o Programa

### Pré-requisitos
* Possuir o **Python 3** instalado em sua máquina.

### Passo a Passo
1. Baixe ou clone este repositório para o seu computador.
2. Abra o terminal (ou prompt de comando) na pasta onde o arquivo `calculadora_viagem.py` está salvo.
3. Execute o programa digitando o comando abaixo:
   ```bash
   python calculadora_viagem.py
   ```
4. Digite as informações solicitadas na tela (Orçamento, Destino, Passagem, Hospedagem e Dias) e pressione **Enter** após cada uma.

---

## 🛠️ Regras de Funcionamento e Restrições

* **Cotação Fixa:** O sistema utiliza a cotação padrão de **1 EUR = 6.10 BRL**.
* **Validação de Negativos:** O programa não aceita valores numéricos negativos. Caso você insira um valor inválido (menor que zero), o sistema exibirá uma mensagem de erro e encerrará a execução imediatamente por segurança.
* **Critério de Viabilidade:** A viagem só será considerada **Viável** se o custo total for menor ou igual ao orçamento disponível **E** se a quantidade de dias for maior que zero.

---

## 📚 Respostas das Perguntas Teóricas

### 1. Qual a diferença entre o comando `git add .` e `git commit -m "mensagem"`?
* **`git add .`**: Este comando envia todas as alterações, novos arquivos ou exclusões da pasta atual para a *Staging Area* (área de preparação). Ele funciona como uma seleção prévia, informando ao Git quais modificações devem ser incluídas no próximo "salvamento".
* **`git commit -m "mensagem"`**: Este comando grava permanentemente as alterações que estavam na *Staging Area* no histórico local do repositório. Ele cria um ponto de restauração definitivo (um commit) e anexa uma mensagem explicativa sobre o que foi feito.

### 2. Por que é necessário realizar o casting (conversão de tipo) ao usar a função `input()` em Python para cálculos matemáticos?
Por padrão, tudo o que o usuário digita na função `input()` é capturado pelo Python como uma string (texto), mesmo que sejam digitados apenas números. Como o Python não realiza operações aritméticas (como soma ou divisão) com textos, precisamos fazer o **casting** (usando `int()` para números inteiros ou `float()` para números decimais) para transformar esse texto em um tipo numérico válido antes de fazer qualquer cálculo.

### 3. O que acontece se tentarmos somar uma variável do tipo `str` com uma do tipo `float`?
O Python interrompe o programa imediatamente e exibe um erro de tipo chamado **`TypeError`** (ex: *unsupported operand type(s) for +: 'str' and 'float'*). Isso acontece porque o Python possui **tipagem forte**, o que significa que ele proíbe operações diretas entre tipos de dados incompatíveis sem que haja uma conversão explícita prévia.

---
Desenvolvido como projeto de avaliação prática para controle de orçamento e versionamento com Git.
