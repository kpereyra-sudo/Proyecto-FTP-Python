import ftplib  as f
import os
from datetime import datetime, timedelta
import json

with open('Config.json', 'r') as file:
    config = json.load(file)

# lee la ip desde el config file
UserAD = config['userAD']['User']
# leer ruta nas y la concatena con cada journal subido.
Passwd = config['userAD'][ "passwd"]

def ConeCTOftp(ip):

    try:
        ftp = f.FTP(ip)
        print(ftp.welcome)
        ftp.login()
        return ftp
    except Exception as e:
        print(e)
  
    


def ConecTOFTPMicrosoft(ip, directory):

    try:
        ftp = f.FTP(ip)
        print(ftp.welcome)
        ftp.login(UserAD, Passwd)
        ftp.cwd(directory)
    except:
        print("Problemas con la ip o la caja esta apagada")
    return ftp


    
def  GotoDirectory(ftp, directorio):
    
    
    
    try:

    # Ir al directorio especificado
        ftp.cwd(directorio)
    # acceder a los archivos del directorio
        lista_journal = ftp.nlst()
        
        return lista_journal
        
    except Exception as e:
        print(e)

 

    

def insertar_ruta_nas(ftp, journal, ruta):

    """ Escribir la ruta que se especifica como parametro en la funcion y guarda los Journal alla"""
    local_filename = os.path.join(ruta, journal)
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR " + journal, lf.write, 8*1024)
    lf.close()

def InsertarRutaFTP(journal, servidor, directorio, local_filename):


    ftpj = ConecTOFTPMicrosoft(servidor, directorio)
    
    
   
    try:


        fp = open(local_filename, 'rb')
        ftpj.storlines('STOR %s' %journal, fp)
        fp.close()


    except Exception as e:
        print(e)



    