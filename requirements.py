#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Validação e Instalação de Dependências
Autor: Antigravity AI
Descrição: Verifica se o ambiente possui todas as bibliotecas necessárias para o TCC.
           Caso faltem pacotes, realiza a instalação automática via pip.
Uso:
    python requirements.py
"""

import sys
import subprocess
import importlib.metadata
from pathlib import Path

# Mapeamento de nomes de pacotes do pip para os nomes usados em importações Python
PACKAGE_MAPPING = {
    "scikit-learn": "sklearn",
    "tensorflow-intel": "tensorflow",
}

def carregar_requirements(caminho_req: Path) -> list[str]:
    """Lê o arquivo requirements.txt e extrai as linhas de pacotes válidos."""
    if not caminho_req.exists():
        print(f"[-] Erro: Arquivo {caminho_req.name} não foi encontrado!")
        sys.exit(1)
        
    pacotes = []
    with open(caminho_req, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            # Ignora comentários e linhas vazias
            if not linha or linha.startswith("#"):
                continue
            # Remove comentários inline
            if " #" in linha:
                linha = linha.split(" #")[0].strip()
            pacotes.append(linha)
    return pacotes

def separar_nome_versao(pacote_str: str) -> tuple[str, str, str]:
    """Separa o nome do pacote do operador de versão (ex: >=, ==) e da versão desejada."""
    for op in (">=", "==", "<=", "~=", ">", "<"):
        if op in pacote_str:
            parts = pacote_str.split(op)
            return parts[0].strip(), op, parts[1].strip()
    return pacote_str.strip(), "", ""

def verificar_dependencias(pacotes: list[str]) -> tuple[list[str], list[str]]:
    """Verifica quais dependências estão faltando ou desatualizadas no ambiente atual."""
    ausentes = []
    desatualizadas = []
    
    for pct in pacotes:
        nome_pip, op, versao_req = separar_nome_versao(pct)
        nome_import = PACKAGE_MAPPING.get(nome_pip, nome_pip)
        
        try:
            # Tenta obter a versão instalada via metadata
            versao_instalada = importlib.metadata.version(nome_pip)
        except importlib.metadata.PackageNotFoundError:
            # Fallback secundário para ver se o módulo é importável
            try:
                importlib.import_module(nome_import)
                versao_instalada = "Desconhecida (Módulo importável)"
            except ImportError:
                ausentes.append(pct)
                continue
                
        if op and versao_req and versao_instalada != "Desconhecida (Módulo importável)":
            # Comparação simples de versão
            # Em ambientes produtivos usa-se packaging.version, mas para evitar dependências adicionais
            # fazemos uma comparação base simples por tuplas de inteiros
            try:
                instalada_parts = [int(x) for x in versao_instalada.split(".")[:3] if x.isdigit()]
                requerida_parts = [int(x) for x in versao_req.split(".")[:3] if x.isdigit()]
                
                if op == ">=" and instalada_parts < requerida_parts:
                    desatualizadas.append(f"{nome_pip} (Instalada: {versao_instalada} | Requerida: {pct})")
                elif op == "==" and instalada_parts != requerida_parts:
                    desatualizadas.append(f"{nome_pip} (Instalada: {versao_instalada} | Requerida: {pct})")
            except Exception:
                # Se falhar o parsing de versão (ex: versão com alfa/beta), assume que está ok
                pass
                
    return ausentes, desatualizadas

def instalar_pacotes(pacotes_para_instalar: list[str]):
    """Chama o instalador pip no subprocesso para instalar as dependências."""
    print(f"\n[+] Iniciando a instalação de {len(pacotes_para_instalar)} dependência(s)...")
    cmd = [sys.executable, "-m", "pip", "install"] + pacotes_para_instalar
    try:
        res = subprocess.run(cmd, check=True)
        if res.returncode == 0:
            print("[OK] Instalação concluída com sucesso!")
        else:
            print(f"[-] Falha na instalação. Código de retorno: {res.returncode}")
    except Exception as e:
        print(f"[-] Ocorreu um erro crítico durante a instalação: {e}")

def main():
    print("=" * 65)
    print("        VERIFICADOR DE DEPENDÊNCIAS DO PIPELINE DO TCC          ")
    print("=" * 65)
    
    caminho_req = Path(__file__).resolve().parent / "requirements.txt"
    pacotes = carregar_requirements(caminho_req)
    
    print(f"Carregados {len(pacotes)} pacotes requeridos de '{caminho_req.name}'.")
    print("[*] Analisando ambiente Python atual...")
    
    ausentes, desatualizadas = verificar_dependencias(pacotes)
    
    if not ausentes and not desatualizadas:
        print("\n[OK] Tudo pronto! Todas as dependências necessárias estão instaladas e atualizadas.")
        sys.exit(0)
        
    if ausentes:
        print("\n[-] Dependências FALTANTES encontradas:")
        for a in ausentes:
            print(f"    • {a}")
            
    if desatualizadas:
        print("\n[!] Dependências DESATUALIZADAS encontradas:")
        for d in desatualizadas:
            print(f"    • {d}")
            
    total_instalar = ausentes + [d.split(" (")[0] for d in desatualizadas]
    
    print("\n" + "-" * 65)
    pergunta = f"Deseja instalar/atualizar esses {len(total_instalar)} pacotes automaticamente agora? [S/n]: "
    
    # Execução automática se não for terminal interativo ou se passado argumento '-y'
    executar_auto = "-y" in sys.argv
    
    if executar_auto:
        instalar_pacotes(total_instalar)
    else:
        opcao = input(pergunta).strip().lower()
        if opcao in ("", "s", "sim", "y", "yes"):
            instalar_pacotes(total_instalar)
        else:
            print("[!] Instalação cancelada. Por favor, instale manualmente usando:")
            print(f"    pip install -r {caminho_req.name}")

if __name__ == "__main__":
    main()
