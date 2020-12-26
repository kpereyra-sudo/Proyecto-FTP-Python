import FileFTPFuntions as p
import json


with open('Config.json', 'r') as file:
    config = json.load(file)

# lee la ip desde el config file
IpCaja = config['TiendaFTP156']['ipcaja']
# leer ruta nas y la concatena con cada journal subido.
NasPATHFile = config['TiendaFTP156'][ "pathfile"]
#Lee el servidor especificado en este caso el milady del FTP
ServiDORMilady = config['TiendaFTP156'][ "Servidor"]
# Lee la ruta FTP hacia donde dirigira los Journal
RutaFTP = config['TiendaFTP156']["RutaFTP"]
#Lee ruta NAS
RutaNAS = config['TiendaFTP156']["RutaNAS"]
#Lee la ruta de journal de la caja
JournalDirectoryCaja = config['CajasFTP']["journal"]

def Pantoja():

    """ Lee las funciones que conectan con el FTP, reciben los parametros de conexion
    y extrae cada journal de la caja y los insertar en el nas y el ftp de los journal. """

    ftp = p.ConeCTOftp(IpCaja)
    lista_journal = p.GotoDirectory(ftp, JournalDirectoryCaja)

    for journal in lista_journal:
        if len(journal) == 7 :
        # insert NAS
            nas = p.insertar_ruta_nas(ftp, journal, RutaNAS)
        #Insert on My desk
            InsertFTP = p.InsertarRutaFTP(journal, ServiDORMilady, RutaFTP, NasPATHFile %journal )



if __name__ == "__main__":
  Pantoja = Pantoja()
   
