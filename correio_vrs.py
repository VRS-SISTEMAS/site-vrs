# ==============================================================================
# NOME DO SISTEMA: VR SOLUÇÕES Sistemas
# MÓDULO: correio_vrs.py (O Carteiro Digital - Versão Final)
# ==============================================================================
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# COMENTÁRIO PARA O VITOR: Esta função é chamada pelo checkout.py
def enviar_email_entrega(destinatario, nome_cliente, id_pc, plano):
    # --- CONFIGURAÇÕES DE ENVIO (Mude aqui) ---
    meu_email = "seu-email@gmail.com"  # Digite seu Gmail aqui
    minha_senha = "sua-senha-de-app"    # Digite sua Senha de App de 16 dígitos aqui
    
    assunto = f"🚀 Confirmação de Pedido - VR Soluções ({plano})"
    
    # Criando a estrutura do e-mail
    msg = MIMEMultipart()
    msg['From'] = meu_email
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Corpo do e-mail em texto simples para garantir entrega
    corpo = f"""
    Olá {nome_cliente}, tudo bem?
    
    Recebemos seu pedido para o Plano {plano} da VR Soluções!
    
    Dados registrados:
    - ID do Computador: {id_pc}
    - Status: Aguardando confirmação de PIX
    
    Assim que o sistema validar seu pagamento, enviaremos sua chave de 
    ativação definitiva por aqui. 
    
    Caso não tenha baixado o instalador, utilize o botão no nosso site.
    
    Atenciosamente,
    Equipe VR Soluções Elite.
    """
    
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        # Configuração do servidor Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Segurança extra
        server.login(meu_email, minha_senha)
        server.sendmail(meu_email, destinatario, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        # Mostra o erro no terminal caso o envio falhe
        print(f"ERRO AO ENVIAR E-MAIL: {e}")
        return False