import os
import json
from datetime import datetime

def gerenciar_gitkeep(diretorio_raiz):
    logs_dir = "logs"
    log_file = os.path.join(logs_dir, "log.json")
    
    # Garante a existência do diretório de logs
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    stats = {
        "execucao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "criados": [],
        "removidos": []
    }

    # Percorre o diretório de baixo para cima (topdown=False) 
    # para lidar corretamente com subpastas que ficam vazias
    for root, dirs, files in os.walk(diretorio_raiz, topdown=False):
        # Ignora o diretório de logs e a pasta .git
        if logs_dir in root.split(os.sep) or ".git" in root.split(os.sep):
            continue

        # Verifica se o diretório está vazio (desconsiderando o próprio .gitkeep)
        arquivos_reais = [f for f in files if f != ".gitkeep"]
        esta_vazio = len(arquivos_reais) == 0 and len(dirs) == 0

        caminho_gitkeep = os.path.join(root, ".gitkeep")

        if esta_vazio:
            if not os.path.exists(caminho_gitkeep):
                with open(caminho_gitkeep, 'w') as f:
                    pass
                stats["criados"].append(caminho_gitkeep)
        else:
            if os.path.exists(caminho_gitkeep):
                os.remove(caminho_gitkeep)
                stats["removidos"].append(caminho_gitkeep)

    salvar_logs(log_file, stats)
    print(f"Processamento concluído. Criados: {len(stats['criados'])} | Removidos: {len(stats['removidos'])}")

def salvar_logs(caminho_log, novos_dados):
    historico = []
    if os.path.exists(caminho_log):
        with open(caminho_log, 'r', encoding='utf-8') as f:
            try:
                historico = json.load(f)
                if not isinstance(historico, list): historico = []
            except json.JSONDecodeError:
                historico = []

    historico.append(novos_dados)
    
    with open(caminho_log, 'w', encoding='utf-8') as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    # Executa no diretório atual
    gerenciar_gitkeep(".")
