# 🚀 Automação de Versionamento de Diretórios Vazios

Este projeto foi desenvolvido para automatizar a gestão de arquivos `.gitkeep` no repositório **"coisas-da-universidade"**. Como o Git não versiona pastas vazias, este script garante que toda a estrutura organizacional acadêmica seja preservada no GitHub.

## 🛠️ Funcionamento

O programa percorre recursivamente o diretório raiz e aplica as seguintes regras:
- **Diretórios Vazios:** Cria um arquivo `.gitkeep` para que a pasta seja rastreada.
- **Diretórios com Conteúdo:** Remove o arquivo `.gitkeep` caso ele exista, mantendo a organização limpa.
- **Exceções:** O diretório `logs/` e a pasta `.git/` são ignorados pelo algoritmo.

## 📋 Instruções de Uso

1. **Pré-requisitos:** Ter o Python 3.x instalado em sua máquina.
2. **Localização:** Certifique-se de que o script `main.py` está na raiz do seu repositório local.
3. **Execução:** Abra o terminal no VS Code e execute:
   ```bash
   python main.py
   ```
4. **Verificação de Logs:** Os resultados de cada execução (data, arquivos criados e removidos) são armazenados em `logs/log.json`.

## 📚 Perguntas Teóricas

### Diferença entre `json.dump()` e `json.dumps()`
- **`json.dump()`**: Utilizado para escrever dados diretamente em um **arquivo** (objeto de arquivo).
- **`json.dumps()`**: O "s" vem de *string*. Ele converte um objeto Python em uma **string JSON**, útil para manipulação em memória ou envio via API.

### Diferença entre `json.load()` e `json.loads()`
- **`json.load()`**: Lê e decodifica dados JSON a partir de um **arquivo** físico aberto.
- **`json.loads()`**: Lê e decodifica dados JSON a partir de uma **string** (texto no formato JSON).

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- Bibliotecas nativas: `os`, `json`, `datetime`.

---
*Projeto desenvolvido como parte do Desafio 4 de Automação.*
