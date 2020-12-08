import argparse
import scrap
import meta
import hashes
import pickle
import os
import scan
import correo
import socket
import time


def ValidatePath(thePath):
    # Valida que el path existe
    if not os.path.exists(thePath):
        raise argparse.ArgumentTypeError('Path does not exist')

    # Valida que el path es leible
    if os.access(thePath, os.R_OK):
        return thePath
    else:
        raise argparse.ArgumentTypeError('Path is not readable')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-link", dest="link",
                        help="Link a utilizar")
    parser.add_argument('-b', '--baseline',
                        help="Especifica el archivo baseline resultante")
    parser.add_argument('-p', '--Path',
                        type=ValidatePath,
                        help="Especifica el path para el baseline")
    parser.add_argument('-t', '--tmp',
                        help="Especifica el resultado temporal del script de Powershell")
    parser.add_argument('-o', '--output_fp',
                        help="Path hacia el archivo output",
                        default="output.txt")
    parser.add_argument('-r', '--response_fp',
                        help='Path a la respuesta '
                        'archivo que quiere guardar',
                        default="response.txt")
    parser.add_argument('-a', '--api_key',
                        help='virustotal API key')
    parser.add_argument('-u', '--user',
                        help="Su correo")
    parser.add_argument('-w', '--password',
                        help="Contraseña de su correo")
    parser.add_argument('-y', '--destinatary',
                        help="Correo destino")
    parser.add_argument('-s', '--subject',
                        help="Asunto del correo",
                        default='')
    parser.add_argument('-d', '--body',
                        help="Cuerpo del correo",
                        default='')
    args = parser.parse_args()     

    baselineFile = args.baseline
    targetPath = args.Path
    tmpFile = args.tmp
    api_key = args.api_key
    output_fp = args.output_fp
    response_fp = args.response_fp
    link = str(args.link)
    user = args.user
    pwd = args.password
    to = args.destinatary
    subject = args.subject
    body = args.body
    
    if link != ("None"):
        print("\n\tOBTENCION DE SOCKET")
        print(socket.gethostbyname_ex(link))
        scan.main(link, api_key, output_fp, response_fp)
        scrap.scrapingImages(link)
        meta.printMeta()
    else:
        hashes.hash(baselineFile, targetPath, tmpFile)
        correo.sendMail(user,pwd,to,subject,body,tmpFile)
