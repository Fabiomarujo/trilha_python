# Sistema de Inventário de Reagentes - Laboratório de Engenharia Química

Este projeto consiste em uma ferramenta de processamento de dados para gestão de frascos de reagentes químicos. O objetivo é transformar listas brutas de inventário em um relatório estruturado, identificar compostos únicos e filtrar lotes que atendam a critérios rigorosos de pureza.

## 🛠️ Tecnologias e Técnicas Utilizadas

O programa foi desenvolvido em **Python 3** utilizando as seguintes técnicas:
- **Set (Conjuntos):** Para identificação imediata de elementos únicos.
- **Zip:** Para a união de múltiplas fontes de dados (listas) em uma única estrutura iterável.
- **Unpacking:** Para extração limpa de dados durante a iteração de listas de tuplas.
- **List Comprehension:** Para filtragem eficiente de dados com sintaxe concisa.
- **Versionamento com Git:** Histórico de desenvolvimento organizado por funcionalidades.

## 🚀 Como executar o programa

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `inventario_lab.py`.
3. Execute o script via terminal:
   ```bash
   python inventario_lab.py
   ```

## 📝 Respostas Teóricas do Desafio

### 1. Por que seria incorreto usar a função `dict()` para transformar o resultado do nosso `zip()` em um dicionário usando o reagente como chave?
Em Python, as chaves de um dicionário devem ser **únicas**. Como o inventário possui múltiplos frascos do mesmo reagente (ex: várias entradas de "Etanol"), ao converter o `zip` diretamente em um dicionário, cada nova ocorrência de um reagente sobrescreveria a anterior. No final, teríamos apenas um lote para cada produto, perdendo todas as outras unidades do estoque.

### 2. O que a função `zip()` gera na memória do Python antes de usarmos a função `list()`?
Ela gera um **objeto iterador** (zip object). Esse objeto utiliza um conceito chamado *lazy evaluation* (avaliação preguiçosa), o que significa que os pares de dados não são criados e armazenados todos de uma vez na memória. Eles são gerados apenas quando solicitados (como em um loop), o que torna o processo muito mais eficiente em termos de consumo de memória, especialmente para grandes bases de dados.

### 3. De que forma o List Comprehension substitui a necessidade de um loop `for` tradicional com `.append()`?
O List Comprehension substitui o processo de três etapas (criação de lista vazia, iteração com `for` e adição manual com `.append()`) por uma única linha de código **declarativa**. Além de ser mais legível, essa técnica é otimizada internamente pelo interpretador Python, resultando em uma execução levemente mais rápida que o método tradicional.


