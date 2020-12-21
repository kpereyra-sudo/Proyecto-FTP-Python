import ftplib  as f
import os
from datetime import datetime, timedelta



def ConeCTOftp(ip):

    try:
        ftp = f.FTP(ip)
        print(ftp.welcome)
        ftp.login()
        return ftp
    except Exception as e:
        print(e)
  
    # try:

    # # Ir al directorio especificado
    #     ftp.cwd('ej/j')
    # # acceder a los archivos del directorio
    #     lista_journal = ftp.nlst()
        
    #     return lista_journal
        
    # except Exception as e:
    #     print(e)
ftp = ConeCTOftp('10.10.19.130')

def ConecTOFTPMicrosoft(ip, directory):

    try:
        ftp = f.FTP(ip)
        print(ftp.welcome)
        ftp.login('unicomer\katherine_pereyra', 'Kper0404')
        ftp.cwd(directory)
    except:
        print("Problemas con la ip o la caja esta apagada")
    return ftp

# ftp = ConeCTOftp('10.10.19.130')
    
def  GotoDirectory(ftp, directorio):
    
    
    
    try:

    # Ir al directorio especificado
        ftp.cwd(directorio)
    # acceder a los archivos del directorio
        lista_journal = ftp.nlst()
        
        return lista_journal
        
    except Exception as e:
        print(e)

 

lista_journal = GotoDirectory( ftp, "ej/j")

    # try:

    # # Ir al directorio especificado
    #     print(ftp.cwd(directorio))
    # # acceder a los archivos del directorio
    #     lista_journal = ftp.nlst()
        


    # except:
    #     print("ESE DIRECTORIO NO EXISTE")

def insertar_ruta_nas(ftp, journal, ruta):

    """ Escribir la ruta que se especifica como parametro en la funcion y guarda los Journal alla"""
    local_filename = os.path.join(ruta, journal)
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR " + journal, lf.write, 8*1024)

def InsertarRutaFTP(journal, servidor, directorio, local_filename):


    ftpj = ConecTOFTPMicrosoft(servidor, directorio)
    
    
   
    try:

    # Ir al directorio especificado
        
    #acceder a los archivos del directorio
        # local_filename = "//10.10.1.67/Volume_1/Journal y Lventas/Journal/2020/516 Galerias 360/%s" %journal
        fp = open(local_filename, 'rb')
        ftpj.storlines('STOR %s' %journal, fp)
        fp.close()


    except Exception as e:
        print(e)
        
# #ir por cada journal y si no esta encriptado enviarlo a las rutas especificadas.
# # journal = (journal for journal in lista_journal if len(journal) == 7

#     # if len(journal) == 7 :
#         #insert NAS
# insertar_ruta_nas(r"\\10.10.1.67\Volume_1\Journal y Lventas\Journal\2020\516 Galerias 360")
#         #Insert on My desk
# InsertarRutaFTP(journal)    
    


if __name__ == "__main__":
    for journal in lista_journal:
        if len(journal) == 7 :
        # insert NAS
            insertar_ruta_nas(r"\\10.10.1.67\Volume_1\Journal y Lventas\Journal\2020\516 Galerias 360")
        #Insert on My desk
            InsertarRutaFTP(journal, 'mlddcdofls01-vm.datacenter.milady.local', '/journal/Journal Generales/516', "//10.10.1.67/Volume_1/Journal y Lventas/Journal/2020/516 Galerias 360/%s" %journal) 
    