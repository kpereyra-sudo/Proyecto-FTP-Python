import ftplib  as f
import os
from datetime import datetime, timedelta


# def ConeCTOftp(ip,directorio):

try:
        ftp = f.FTP('10.10.3.131')
        print(ftp.welcome)
        ftp.login()
except:
        print("Problemas con la ip o la caja esta apagada")

try:

    # Ir al directorio especificado
        print(ftp.cwd('ej/j'))
    # acceder a los archivos del directorio
        lista_journal = ftp.nlst()
        


except:
        print("ESE DIRECTORIO NO EXISTE")

# ConeCTOftp('10.10.19.130', 'ej/j') 

# def ConeCTOftp(ip,directorio):

#     try:
#         ftp = f.FTP(ip)
#         print(ftp.welcome)
#         ftp.login()
#     except:
#         print("Problemas con la ip o la caja esta apagada")

#     return ftp
    
# def  GotoDirectory():

#     try:

#     # Ir al directorio especificado
#         print(ftp.cwd(directorio))
#     # acceder a los archivos del directorio
#         lista_journal = ftp.nlst()
        


#     except:
#         print("ESE DIRECTORIO NO EXISTE")
#     return  lista_journal

# ConeCTOftp('10.10.1.3', '/ej/j') 

def insertar_ruta_nas(ruta):

    """ Escribir la ruta que se especifica como parametro en la funcion y guarda los Journal alla"""
    local_filename = os.path.join(ruta, journal)
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR %s" % journal, lf.write, 8*1024)


def InsertarRutaFTP(journal):

    try:
        ftp = f.FTP('mlddcdofls01-vm.datacenter.milady.local')
        print(ftp.welcome)
        ftp.login('unicomer\katherine_pereyra', 'Kper0404')
    except:
        print("Problemas con la conexion o debe cambiar el password del user")



       

    try:

    # # Ir al directorio especificado
        ftp.cwd('/journal/Journal Generales/573')
    # #acceder a los archivos del directorio
    #     local_filename =  os.path.join(r"\\10.10.1.67\Volume_1\Journal y Lventas\Journal\2020\516 Galerias 360", journal)
    #     #
    #     with open(journal, "rb") as file:
    # # use FTP's STOR command to upload the file
    #         ftp.storbinary("STOR"  + journal, file)
        # local_filename = "C:/Users/katherine_pereyra/Desktop/Prueba ftp/" + journal 
        local_filename = "//10.10.1.67/Volume_1/Journal y Lventas/Journal/2020/573 - Megacentro/%s" %journal
        fp = open(local_filename, 'rb')
        ftp.storlines('STOR %s' %journal, fp)
        fp.close()

        # with open(filename, 'rb') as fp:
            
        #     res = ftp.storlines("STOR " + filename, fp)
            
    except Exception as e:
        print(e)



#ir por cada journal y si no esta encriptado enviarlo a las rutas especificadas.
for journal in lista_journal:

    if len(journal) == 7 :
        #insert NAS
        insertar_ruta_nas(r"\\10.10.1.67\Volume_1\Journal y Lventas\Journal\2020\573 - Megacentro")
        #Insert on My desk
        InsertarRutaFTP(journal)


        
print("Succesfull Upload Files")