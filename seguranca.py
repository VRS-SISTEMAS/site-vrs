import hashlib
import platform

SEMENTE_VR = "VR_SOLUCOES_INTEGRACAO_2026_ESTAVEL"

def obter_id_hardware():
    info = platform.processor() + platform.node() + platform.machine()
    return hashlib.md5(info.encode()).hexdigest().upper()[:8]

def gerar_chave_vrs(id_hardware, plano):
    plano_limpo = "".join(filter(str.isalnum, plano.split()[0])).upper()
    bruto = f"{id_hardware}{plano_limpo}{SEMENTE_VR}"
    hash_chave = hashlib.sha256(bruto.encode()).hexdigest().upper()
    return f"VRS-{plano_limpo[0]}-{hash_chave[:8]}"