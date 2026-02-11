# =================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: servico_email.py (Motor de Disparo Automático)
# =================================================================
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_chave_vrs(destinatario, nome_cliente, plano):
    """Tenta enviar o e-mail, mas não trava o sistema se falhar"""
    # IMPORTANTE: Para funcionar, você precisará configurar estas 2 linhas depois
    remetente = "seu-email@gmail.com" 
    senha_app = "sua-senha-aqui" 

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = f"🚀 Sua Licença VR Soluções - {plano}"

    corpo = f"Olá {nome_cliente},\n\nUma chave de acesso com validade de 30 dias foi gerada no seu e-mail para o plano {plano}."
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha_app)
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False # Se der erro no e-mail, o sistema continua vivo