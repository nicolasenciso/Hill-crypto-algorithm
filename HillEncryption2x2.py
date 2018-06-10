import numpy as np
#Autor: Nicolas Ricardo Enciso 
#Dictionary of alphabetic convertion to numbers
letters = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
#Dictionary of numbers convertion to alphabetic
numbers = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',
11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def determinant(mat): #Function to calculate the matrix determinant for a 2x2 dimension
    return  int( (mat.item((0,0)) * mat.item((1,1)) ) - ( mat.item((0,1)) * mat.item((1,0)) ))

def inverse(module,det):#Function to find the inverse of a fraction a * b(mod26) = 1, returning b
    i = 1
    while( ((det*i)%module) != 1 ):
        i+=1
    return i

def adjMatrix(mat): #Function to find the adj matrix
    aux1 = mat.item((0,0))
    aux2 = mat.item((0,1))
    aux3 = mat.item((1,0))
    aux4 = mat.item((1,1))
    auxKey = np.matrix([ [aux4, (-aux2)], [(-aux3), aux1] ])
    return auxKey


def moduleTwo(mat,mod): #Function to do a module 2 to the 2x1 matrix
    aux1 = mat.item((0,0))
    aux3 = mat.item((0,1))
    auxKey = np.matrix([ [aux1%mod],[aux3%mod] ])
    return auxKey

def cypher(key,msg): #Function to cypher the plain text, key as key and msg as the plain message
    cyMsg = ""
    newKey = np.matrix([])
    if len(key) != 4:
        print("Tamano de llave no aceptado: matriz 2x2 unicamente")
    else:
        auxKey = np.matrix([ [key[0],key[1]], [key[2],key[3]] ])#build the matrix of 2x2 of the key
        newKey = auxKey
    msg = msg.replace(" ","")
    if len(msg)%2 == 0:
        msg = msg.upper()#putting on capital letter the message to make sure standarization
        i = 0
        while(i<len(msg)):
            convertion = np.matrix([ [letters[msg[i]], letters[msg[i+1]]] ]) #taking two letters, and teh next 2 and so on
            aux = (convertion*newKey)# doing C = P*K
            aux = moduleTwo(aux,26)#doing module 2 for the C matrix
            cyMsg = cyMsg + str( numbers[aux.item((0,0))] )
            cyMsg = cyMsg + str( numbers[aux.item((1,0))] )# traslating letters to numbers using the dictionary above
            i+=2
    else:
        print("El mensaje debe tener cantidad par de letras")
    return cyMsg
    
def decrypter(key,encryptMsg): #function to decypher the cypher text
    newKey = np.matrix([])
    msgDes = ""
    encryptMsg = encryptMsg.replace(" ","")
    encryptMsg = encryptMsg.upper()#make sure that all the letters come in capital
    if len(key) != 4:
        print("Tamano de llave no aceptado: matriz 2x2 unicamente")
    else:
        auxKey = np.matrix([ [key[0],key[1]], [key[2],key[3]] ]) #building the matrix for the key of 2x2 dimension
        newKey = auxKey
    dett = (determinant(newKey)) #calculate of the determinant for the K^-1 following: 1/|k| * Adj(K^t)
    invKey = inverse(26,dett) #calculate of the inverse for the K matrix, with module 26
    revKey = invKey * adjMatrix(newKey) #complete calculate for the inverse of K, with module include
    if len(encryptMsg)%2 != 0:
        print("Mensaje con longitud de caracteres no par, no ejecutable")
    else:
        i = 0
        while(i<len(encryptMsg)):
            auxToken = np.matrix([ [letters[encryptMsg[i]], letters[encryptMsg[i+1]]] ])#traslating from letters to numbers using the dictionary above
            planeTxt = moduleTwo((auxToken*revKey),26)
            msgDes = msgDes + str( numbers[planeTxt.item((0,0))] )
            msgDes = msgDes + str( numbers[planeTxt.item((1,0))] )#two by two tralating the number to the final plain text
            i+=2
    return msgDes

def menu():
    print("----------BIENVENIDO------------")
    print("------ALGORITMO DE CIFRADO HILL MATRIZ 2X2--------")
    print("> Presione 1 para cifrar")
    print("> Presione 2 para descrifrar")
    print("> Presione cualquier otro numero para salir")
    print("> Luego, presione ENTER")
    inputt = input()
    if int(inputt) == 1:
        print("> -----------------CIFRAMIENTO---------------")
        print("> Ingrese su texto a cifrar, solo letras:  luego presione ENTER")
        message = input()
        print("> Ingrese su llave/matriz 2x2: ")
        print("> Ingrese numero en Posicion a11:  ")
        a11 = int(input())
        print("> Ingrese numero en Posicion a12:  ")
        a12 = int(input())
        print("> Ingrese numero en Posicion a21:  ")
        a21 = int(input())
        print("> Ingrese numero en Posicion a22:  ")
        a22 = int(input())
        line = [a11,a12,a21,a22]
        print("> SU TEXTO CIFRADO ES: ")
        print(cypher(line,message))
    elif int(inputt) == 2:
        print(">-----------------DESCIFRADO--------")
        print("> Ingrese su texto a descifrar, solo letras, luego presione ENTER")
        message = input()
        print("> Ingrese su llav/matriz 2x2: ")
        print("> Ingrese numero en Posicion a11:  ")
        a11 = int(input())
        print("> Ingrese numero en Posicion a12:  ")
        a12 = int(input())
        print("> Ingrese numero en Posicion a21:  ")
        a21 = int(input())
        print("> Ingrese numero en Posicion a22:  ")
        a22 = int(input())
        line = [a11,a12,a21,a22]
        print("> SU TEXTO DESCIFRADO ES: ")
        print(decrypter(line,message))
    else:
        return 0

menu()

