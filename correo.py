import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass
import ssl

#Scrip para mandar un correo con archivo adjunto
def sendMail(user,pwd,to,subject,body,filename):
    print("\n\tENVIO DE CORREO")
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    adjunto = open(filename, "rb")
    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload((adjunto).read())
    encoders.encode_base64(parte)
    parte.add_header('Content-Disposition', "attachment;filename= %s" % filename)
    msg.attach(parte)
    context = ssl.create_default_context()
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print("[+] Conectando Al Servidor Mail.")
        smtpServer.ehlo()
        print("[+] Empezando Sesión Encriptada.")
        smtpServer.starttls(context=context)
        smtpServer.ehlo()
        print("[+] Logeandose Al Servidor Mail.")
        smtpServer.login(user, pwd)
        print("[+] Mandando Mail.")
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print("[+] Mail Enviado Exitosamente.")
    except:
        print("[-] Enviado De Mail Fallido.")
