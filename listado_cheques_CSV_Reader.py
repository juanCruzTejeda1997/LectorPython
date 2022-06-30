import sys
import csv
CSV = sys.argv[1]
DNI = int(sys.argv[2])
SALIDA = sys.argv[3]
TIPO = sys.argv[4]

def buscarChequesPorCliente(dni):
    cheques =[]
    archivo = open(CSV,'r')
    registro = csv.reader(archivo)
    for linea in registro:
        linea = linea
        if int(linea[8]) == dni:
            cheques.append(linea)
    archivo.close()
    return cheques

def chequesEmitidos(dni):
    emitidos=[]
    cheques = buscarChequesPorCliente(dni)
    for cheque in cheques:
        if cheque[9]  == "EMITIDO":
            emitidos.append(cheque)
    if len(emitidos) == 0:
        return "El usuario no tiene cheques emitidos"
    else:
        return emitidos
    
def chequesDepositados(dni):
    depositados=[]
    cheques = buscarChequesPorCliente(dni)
    for cheque in cheques:
        if cheque[9]  == "DEPOSITADO":
            depositados.append(cheque)
    if len(depositados) == 0:
        return "El usuario no tiene cheques depositados"
    else:
        return depositados

def escribirCSV(tipo,dni):
    with open("DNI.csv", 'w') as chequesCliente:
                writer = csv.writer(chequesCliente)
                if tipo=="EMITIDO":
                    for cheque in chequesEmitidos(dni):
                        writer.writerow(cheque)
                if tipo=="DEPOSITADO":
                    for cheque in chequesDepositados(dni):
                        writer.writerow(cheque)
                chequesCliente.close()

def printCheques(dni,tipo):
    if(tipo=="EMITIDO"):
        print(chequesEmitidos(dni))
    else:
        if (tipo=="DEPOSITADO"):
            print(chequesDepositados(dni))

def filtrarChequesPorEntrada(salida,tipo,dni):
        if salida=="pantalla":
            printCheques(dni,tipo)
        elif salida=="csv":
            escribirCSV(tipo,dni)

 ################################################
                
filtrarChequesPorEntrada(SALIDA,TIPO,DNI)