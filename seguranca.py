# ==============================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: seguranca.py (Cérebro Unificado de Licenciamento)
# FUNÇÃO: Validar Hardware, Gerar Chaves e Travar Planos
# DESENVOLVEDOR: Iara & Vitor
# ==============================================================================

import hashlib
import platform
import os
import sys

# ==============================================================================
# FUNÇÃO GPS: LOCALIZAÇÃO DE CAMINHOS PARA EXECUTÁVEL
# ==============================================================================
def obter_caminho_recurso(nome_arquivo):
    """ 
    Retorna o caminho correto para arquivos de configuração e banco de dados.
    Esta função é vital para que o executável (.exe) não procure o arquivo 
    dentro da pasta temporária do Windows, mas sim na pasta onde o programa está instalado.
    """
    if getattr(sys, 'frozen', False):
        # Se estiver rodando como executável compilado (.exe)
        diretorio_base = os.path.dirname(sys.executable)
    else:
        # Se estiver rodando como script Python (.py) em desenvolvimento
        diretorio_base = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(diretorio_base, nome_arquivo)

# CHAVE MESTRA: Esta semente é o segredo do algoritmo da VR Soluções. 
# Importante: Esta string deve ser IGUAL no gerador de chaves e no software.
SEMENTE_VR = "VR_SOLUCOES_INTEGRACAO_2026_ESTAVEL"

def obter_id_hardware():
    """ 
    Gera uma assinatura única (Fingerprint) do computador do cliente.
    Captura dados do processador, nome da rede e arquitetura.
    Retorna: Uma string de 8 caracteres (Ex: A1B2C3D4).
    """
    # Coleta informações únicas da máquina física
    info = platform.processor() + platform.node() + platform.machine()
    # Transforma em um hash MD5 para criar um identificador curto e fixo
    id_curto = hashlib.md5(info.encode()).hexdigest().upper()[:8]
    return id_curto

def gerar_chave_final(id_hardware, plano):
    """ 
    Algoritmo mestre de geração de licença.
    id_hardware: O ID de 8 dígitos capturado no PC do cliente.
    plano: 'BASICO', 'JUNIOR' ou 'SENIOR'.
    Retorna: Uma chave formatada (Ex: VRS-B-ABCD-1234).
    """
    # Cria a string bruta combinando o hardware, o plano e a semente secreta
    bruto = f"{id_hardware}{plano.upper()}{SEMENTE_VR}"
    # Gera o Hash SHA256 para máxima segurança contra ataques
    hash_chave = hashlib.sha256(bruto.encode()).hexdigest().upper()
    
    # Formatação Profissional: Identificador-Plano-Trechos do Hash
    return f"VRS-{plano[0].upper()}-{hash_chave[:4]}-{hash_chave[8:12]}"

def validar_ativacao(plano_exigido):
    """ 
    Verifica se o software possui uma licença válida para rodar.
    Lê o arquivo 'vrs_config.dat' e compara com a assinatura da máquina atual.
    """
    # Localiza o arquivo de licença usando o caminho absoluto (GPS)
    arquivo_licenca = obter_caminho_recurso("vrs_config.dat")
    
    # Se o arquivo não existir, o sistema permanece bloqueado
    if not os.path.exists(arquivo_licenca):
        return False
    
    try:
        # Abre o arquivo e lê a chave que o cliente colou
        with open(arquivo_licenca, "r") as f:
            chave_gravada = f.read().strip()
        
        # Reconstrói qual seria a chave CORRETA para este hardware específico
        id_deste_pc = obter_id_hardware()
        chave_esperada = gerar_chave_final(id_deste_pc, plano_exigido)
        
        # Se a chave gravada for idêntica à esperada, acesso liberado
        return chave_gravada == chave_esperada
    except Exception:
        # Proteção contra arquivos corrompidos ou editados manualmente
        return False

def salvar_chave(chave):
    """ 
    Grava a chave de ativação no arquivo vrs_config.dat.
    Garante que o arquivo seja criado na mesma pasta do executável.
    """
    caminho_destino = obter_caminho_recurso("vrs_config.dat")
    with open(caminho_destino, "w") as f:
        f.write(chave.strip())