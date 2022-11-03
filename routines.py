## -------------------  >)|°> UriSoft© <°|(<  -------------------
# File: routines.py
# Developers: Uriel Iram Lezama Lope
# Purpose: Various functions 
## <º)))>< ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸ ><(((º>

# Esta funcion recibe una potencia (pow) y regresa el costo de acuerdo a una función piecewise (list)
# function to calculate the cost segment from his power
def Fo(list, pow):
    cost = 0
    min = list[0][0]
    if len(list) == 1:
        max = list[0][0]     
    else:
        max = list[len(list)-1][0]

    # print("min=",min,"pow", pow,"max=",max)   
    if min <= pow <= max:
        for obj in reversed(list):
            if pow <= obj[0]:
                cost = obj[1]
            # print("cost", cost)
    else:        
        cost=list[0][1]
        print(">>>undefined energy cost, verify that the power is within the piecewise cost; cost= $",cost)

    return cost
 

# account times on
def time_on(T, N, U, account):
    Ton = [[0 for x in range(T)] for y in range(N)]
    for t in range(T):
        for i in range(N):
            if U[i][t] == 1:
                if t == 0:
                    Ton[i][t] = account[i] + 1
                else:
                    Ton[i][t] = Ton[i][t-1] + 1
            else:
                Ton[i][t] = 0
    return(Ton)

# account times off
def time_off(T, N, U, account):
    Toff = [[0 for x in range(T)] for y in range(N)]
    for t in range(T):
        for i in range(N):
            if U[i][t] == 0:
                if t == 0:
                    Toff[i][t] = account[i] + 1
                else:
                    Toff[i][t] = Toff[i][t-1] + 1
            else:
                Toff[i][t] = 0
    return(Toff)


# Validate that the unit can be decommitment without violations
# row = es la columna de la solución que corresponde al generador
# TU = Minimum up time
# TD = Minimum down time
# account = time periods keep in the start (t=-1)
def feasiblerow(row, TU, TD, account):
    feasible = True 
    status = row[0]

    # print("TU =",TU,", TD =",TD)
    
    Tio = code(row, account) #Code the solution in number on, number off,..., and so on.
    for t in range(len(Tio)-1):
        if status == 1:
            if Tio[t] < TU:
                print("infeasibleTU,t=",t,Tio[t])
                feasible=False
        else:
            if Tio[t] < TD:
                print("infeasibleTD,t=",t,Tio[t])
                feasible=False
        if status == 1: 
            status = 0
        else:
            status = 1
    return (feasible)

#  Account times ON for a simple row time
def time_on_row(row, account):
    Ton = [0 for x in range(len(row))]
    
    for t in range(len(Ton)):
        if row[t] == 1:
            if  t == 0:
                Ton[t] = account + 1
            else:
                Ton[t] = Ton[t-1] + 1
    return(Ton)

#  Account times OFF for a simple row time
def time_off_row(row, account):
    Toff = [0 for x in range(len(row))]
    for t in range(len(Toff)):
        if row[t] == 0:
            if  t == 0:
                Toff[t] = account + 1
            else:
                Toff[t] = Toff[t-1] + 1
    return(Toff)


#  Account times ON and OFF (1/0) for a simple row time
#  row: serie de 1/0 del generador  
#  account: cantidad de periodos al inicio que lleva encendido/apagado el generador
def code(row, account):  
    Tio = []
    Tio.append(account)
    Tio[0] = Tio[0] + 1
    k=0    
    for t in range(1,len(row)):
        if row[t-1] == row[t]:
            Tio[k] = Tio[k] + 1
        else:
            Tio.append(1)
            k=k+1
    return(Tio)

#  Secuence of times on/off from generator  
#  account: cantidad de periodos al inicio que lleva encendido/apagado el generador
def decode(secuence, account, status):
    row = []
    secuence[0] = secuence[0] - account
  
    for i in range(len(secuence)):
        for j in range(secuence[i]):
            #print("",status)
            row.append(status)
        if status == 1: 
            status = 0
        else:
            status = 1
    return(row)



