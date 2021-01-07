import FileFTPFuntions as p
import json


with open('Config.json', 'r') as file:
    config = json.load(file)

# lee la ip desde el config file
IpCaja = config['TiendaFTP510']['ipcaja']
# leer ruta nas y la concatena con cada journal subido.
NasPATHFile = config['TiendaFTP510'][ "pathfile"]
#Lee el servidor especificado en este caso el milady del FTP
ServiDORMilady = config['TiendaFTP510'][ "Servidor"]
# Lee la ruta FTP hacia donde dirigira los Journal
RutaFTP = config['TiendaFTP510']["RutaFTP"]
#Lee ruta NAS
RutaNAS = config['TiendaFTP510']["RutaNAS"]
#Lee la ruta de journal de la caja
JournalDirectoryCaja = config['CajasFTP']["journal"]

def Whatsapp():

    """ Lee las funciones que conectan con el FTP, reciben los parametros de conexion
    y extrae cada journal de la caja y los insertar en el nas y el ftp de los journal. """

    ftp = p.ConeCTOftp(IpCaja)
    lista_journal = p.GotoDirectory(ftp, JournalDirectoryCaja)

    for journal in lista_journal:
        if journal.startswith('JC') and len(journal) == 7:
        # if len(journal) == 7 :
        # insert NAS
            nas = p.insertar_ruta_nas(ftp, journal, RutaNAS)
        #Insert on My desk
            InsertFTP = p.InsertarRutaFTP(journal, ServiDORMilady, RutaFTP, NasPATHFile %journal )



if __name__ == "__main__":
  Whatsapp = Whatsapp()
   
