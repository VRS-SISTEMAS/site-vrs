# ==============================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: seguranca.py (Cérebro Unificado de Licenciamento)
# DESCRIÇÃO: Responsável pela criptografia e validação de chaves
# ==============================================================================
import hashlib
import platform
import os
import sys

def obter_caminho_recurso(nome_arquivo):
    """Garante que o sistema encontre o arquivo de licença mesmo após compilado"""
    if getattr(sys, 'frozen', False):
        diretorio_base = os.path.dirname(sys.executable)
    else:
        diretorio_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(diretorio_base, nome_arquivo)

# Semente única para garantir que ninguém descubra como as chaves são geradas
# Esta semente deve ser IDÊNTICA no site e no software de login
SEMENTE_VR = "VR_SOLUCOES_INTEGRACAO_2026_ESTAVEL"

def obter_id_hardware():
    """Captura a identidade única do PC do cliente (ID PARA ATIVAÇÃO)"""
    info = platform.processor() + platform.node() + platform.machine()
    id_curto = hashlib.md5(info.encode()).hexdigest().upper()[:8]
    return id_curto

def gerar_chave_vrs(id_hardware, plano):
    """
    CRIPTOGRAFIA MESTRE: Gera a chave no formato EXATO do ativador.
    Formato Final esperado pelo software: VRS-X-XXXXXXXX
    """
    # Limpeza para garantir que o plano seja sempre lido da mesma forma (ex: BÁSICO -> BASICO)
    plano_limpo = plano.upper().replace("Á", "A").replace("🚀", "").replace("💎", "").strip()
    
    # Combina o ID do PC, o Plano limpo e a Semente secreta da VR Soluções
    bruto = f"{id_hardware}{plano_limpo}{SEMENTE_VR}"
    
    # Gera um hash SHA-256 (Criptografia de alto nível)
    hash_chave = hashlib.sha256(bruto.encode()).hexdigest().upper()
    
    # FORMATO AJUSTADO: VRS + Letra Inicial + 8 caracteres do Hash grudados
    # Removemos o hífen extra que causou a rejeição na imagem anterior
    return f"VRS-{plano_limpo[0]}-{hash_chave[:8]}"

def validar_ativacao(plano_exigido):
    """Verifica se a licença gravada no PC é válida para o hardware atual"""
    arquivo_licenca = obter_caminho_recurso("vrs_config.dat")
    
    if not os.path.exists(arquivo_licenca): 
        return False
        
    try:
        with open(arquivo_licenca, "r") as f:
            chave_gravada = f.read().strip()
            
        id_deste_pc = obter_id_hardware()
        # Gera o que seria a chave correta para este PC e compara com a gravada
        chave_esperada = gerar_chave_vrs(id_deste_pc, plano_exigido)
        
        return chave_gravada == chave_esperada
    except Exception: 
        return False

def salvar_chave(chave):
    """Grava a licença no computador do cliente após a ativação com sucesso"""
    caminho_destino = obter_caminho_recurso("vrs_config.dat")
    with open(caminho_destino, "w") as f:
        f.write(chave.strip())