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


    

    


if SALIDA=="pantalla":
    if(TIPO=="EMITIDO"):
                print(chequesEmitidos(DNI))
else:
    if (TIPO=="DEPOSITADO"):
        print(chequesDepositados(DNI))
    elif SALIDA=="csv":
        with open("DNI.csv", 'w') as chequesCliente:
            writer = csv.writer(chequesCliente)
            if TIPO=="EMITIDO":
                for cheque in chequesEmitidos(DNI):
                    writer.writerow(cheque)
            if TIPO=="DEPOSITADO":
                for cheque in chequesDepositados(DNI):
                    writer.writerow(cheque)
        chequesCliente.close()


                
