import sys
CSV = sys.argv[1]
DNI = int(sys.argv[2])
SALIDA = sys.argv[3]
TIPO = sys.argv[4]

def buscarChequesPorCliente(dni):
    cheques =[]
    registro = open(CSV,'r')
    
    for linea in registro:
        linea = linea.rstrip("\n").split(",")
        if int(linea[8]) == dni:
            cheques.append(linea)
    registro.close()
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
            
            p=chequesDepositados(DNI)
            print(p)
    
elif SALIDA=="csv":
    chequesCliente = open("DNI.csv", 'w')
    if TIPO=="EMITIDO":
        for cheque in chequesEmitidos(DNI):
            
            chequesCliente.write(str(cheque))
         
        
    if TIPO=="DEPOSITADO":
        for cheque in chequesDepositados(DNI):
            print(cheque)
            chequesCliente.write(str(cheque))

    chequesCliente.close()
    


        
        
#print("registro de cheques del cliente",buscarChequesPorCliente(DNI),"<<<<<<<<<<<<")

