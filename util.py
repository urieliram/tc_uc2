from   math import ceil
from   csv import writer
import numpy as np
import pandas as pd

#https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
    
def sendtofilesolution(U,name):
    N = len(U)
    T = len(U[0])
    file = open(name, "w")
    cadena = ""
    for g in range(N):
        for t in range(T):
            cadena = cadena + str(ceil(U[g][t]))+","
        cadena = cadena + "\n"
        file.write(cadena)
        cadena = ""
    file.close()
    
def sendtofileTUTD(TU,TD,name):
    N = len(TU)
    file = open(name, "w")
    for g in range(N):         
        file.write(str(TU[g])+","+str(TD[g])+ "\n")
    file.close()
    
    
def imprime_sol(model,sol):
    Uu = dict(zip(model.T, sol.getUu()))
    V  = dict(zip(model.T, sol.getV()))
    W  = dict(zip(model.T, sol.getW()))
    P  = dict(zip(model.T, sol.getP()))
    R  = dict(zip(model.T, sol.getR()))    
    # print("u",Uu)
    # print("v",V)
    # print("w",W)
    # print("p",P)
    # print("r",R)
    

def config_env():
    #ambiente='localPC',ruta='instances/',executable='/home/uriel/cplex1210/cplex/bin/x86-64_linux/cplex3'
    df = pd.read_csv('config')    
    if len(df.index) == 1:
        ambiente     = df['ambiente'  ].values[0]
        ruta         = df['ruta'      ].values[0]
        executable   = df['executable'].values[0]
        timeheu      = df['timeheu'   ].values[0]
        timemilp     = df['timemilp'  ].values[0]
        emph         = df['emphasys'  ].values[0]
        symmetry     = df['symmetry'  ].values[0]
        gap          = df['gap'       ].values[0]
        k            = df['k'         ].values[0]
        iterpar      = df['iter'      ].values[0]
    else:
        print('!!! Problema al cargar la configuración. Verifique el ')
        print('formato y rutas del archivo <config>, algo como esto:')
        print('ambiente,ruta,executable,timeheu,timemilp,gap')
        print('localPC,instances/,/home/uriel/cplex1210/cplex/bin/x86-64_linux/cplex,4000,40000,0.001')
                
    return ambiente, ruta, executable, timeheu, timemilp, emph, symmetry, gap, k, iterpar


def trunc(values, decs=1):
    return np.trunc(values*10**decs)/(10**decs)

def getLetter(index):    
    total    = 26
    cociente = int(index / total)-1
    modulo   = int(index % total)    
    if index < total:
        return   '_'+chr(index+97)
    else:
        return   '_'+chr(cociente+97)+chr(modulo+97)

def saveSolution(t_lp,z_lp,t_,z_,SB_Uu,No_SB_Uu,lower_Pmin_Uu,Vv,Ww,delta,option,instance):
    result_ = []
    result_.append((t_lp,z_lp))
    result_.append((t_,z_))
    result_.append((len(SB_Uu)        , len(No_SB_Uu)))
    result_.append((len(lower_Pmin_Uu), len(Vv)))
    result_.append((len(Ww)           , len(delta)))
    result_ = result_ + SB_Uu + No_SB_Uu + lower_Pmin_Uu
    result_ = np.array(result_)    
    np.savetxt('sol'+option+'_a_'+instance+'.csv', result_, delimiter=',')
    result_ = Vv + Ww + delta 
    result_ = np.array(result_)    
    np.savetxt('sol'+option+'_b_'+instance+'.csv', result_, delimiter=',')
    return None

def loadSolution(option,instance):
    array_a = np.loadtxt('sol'+option+'_a_'+instance+'.csv', delimiter=',')
    array_b = np.loadtxt('sol'+option+'_b_'+instance+'.csv', delimiter=',')
    t_lp           = array_a[0][0]
    z_lp           = array_a[0][1]
    t_             = array_a[1][0]
    z_             = array_a[1][1]
    nSB_Uu         = array_a[2][0].astype(int)
    nNo_SB_Uu      = array_a[2][1].astype(int)
    nlower_Pmin_Uu = array_a[3][0].astype(int)
    nVv            = array_a[3][1].astype(int)
    nWw            = array_a[4][0].astype(int)
    ndelta         = array_a[4][1].astype(int)
    array_a        = array_a[5:]
    a = nSB_Uu + nNo_SB_Uu
    SB_Uu         = array_a[:nSB_Uu].astype(int)
    No_SB_Uu      = array_a[nSB_Uu:a].astype(int)
    lower_Pmin_Uu = array_a[a:].astype(int)
    b = nVv + nWw
    Vv            = array_b[:nVv].astype(int)
    Ww            = array_b[nVv:b].astype(int)
    delta         = array_b[b:].astype(int)
    
    #t_,z_,SB_Uu,No_SB_Uu,lower_Pmin_Uu,Vv,Ww,delta,option,instance
    # print(t_,z_,len(SB_Uu),len(No_SB_Uu),len(lower_Pmin_Uu),len(Vv),len(Ww),len(delta))
    return t_lp,z_lp,t_,z_,SB_Uu,No_SB_Uu,lower_Pmin_Uu,Vv,Ww,delta

def igap(LB,UB):
    ## Calcula el integrality gap    
    return abs( LB - UB ) / ( 1e-10 + abs(UB) )    