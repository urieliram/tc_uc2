## -------------------  >)|°> UriSoft© <°|(<  -------------------
## File: main.py
## A math-heuristic to Tight and Compact Unit Commitment Problem 
## Developers: Uriel Iram Lezama Lope
## Purpose: Programa principal de un modelo de UC
## Description: Lee una instancia de UCP y la resuelve. 
## Para correr el programa usar el comando 'python3 main.py anjos.json yalma'
## Desde script en linux test.sh 'sh test.sh'
## <º)))>< ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸ ><(((º>
import  gc
import  time
import  sys
import  uc_Co
import  util
import  reading
import  time
import  numpy as np
from    math     import floor, ceil, log
from    copy     import deepcopy 
from    solution import Solution
from    os       import path

nameins = 'uc_03.json'       ## ejemplos dificiles 2,3,4  
nameins = 'uc_06.json'       ## ejemplos regulares 5,6 
nameins = 'uc_21.json'       ## ejemplos dificiles 2,3,4 
nameins = 'uc_22.json'       ## ejemplo dificil  

nameins = 'uc_42.json'       ## ejemplo dificil 
nameins = 'uc_44.json'       ## ejemplo dificil 
#nameins = 'uc_50.json'       ## ejemplo sencillo       [1 abajo,milp factible]   
#nameins = 'uc_51.json'       ## ejemplo sencillo  
#nameins = 'uc_53.json'       ## ejemplo de 'delta' relajado diferente de uno  
#nameins = 'uc_54.json'       ## ejemplo sencillo  
#nameins = 'uc_55.json'       ## ejemplo sencillo  
#nameins = 'uc_56.json'       ## ejemplo sencillo 
#nameins = 'uc_46.json'       ## ejemplo sencillo       [49 abajo,MILP infactible]

nameins = 'uc_02.json'        ## ejemplos dificiles 2,3,4   
nameins = 'mem_01.json'       ## MEM (PENDIENTE)
nameins = 'anjos.json'        ## ejemplo de juguete
nameins = 'morales_ejemplo_III_D.json'  ## 
#nameins = 'dirdat_18.json'   ## analizar infactibilidad 
#nameins = 'dirdat_21.json'   ## analizar infactibilidad 
#nameins = 'dirdat_26.json'   ## analizar infactibilidad 
#nameins = 'dirdat_2.json'    ## analizar infactibilidad
#nameins = 'output.json'      ##     

nameins = 'uc_97.json'       ## 

nameins = 'uc_70.json'       ## 

nameins = 'uc_47.json'       ## ejemplo sencillo  

nameins = 'uc_58.json'       ## prueba demostrativa excelente en mi PC 
nameins = 'uc_58_copy.json'  ## prueba demostrativa excelente en mi PC (cinco dias)


nameins = 'uc_61.json'       ## prueba demostrativa excelente en mi PC 
nameins = 'uc_57_copy.json'  ## prueba demostrativa excelente en mi PC (un dia)

## Cargamos parámetros de configuración desde archivo <config>
## Emphasize balanced=0 (default); feasibility=1; optimality=2;
## symmetry automatic=-1; symmetry low level=1
ambiente, ruta, executable, timeheu, timemilp, emph, symmetry, gap, k, iterstop = util.config_env()
k_original = k  ## Almacenamos el parámetro k de local branching
x          = 1e+75
z_lp=x; z_milp=x; z_hard=x; z_hard3=x; z_ks=x; z_lbc1=x; z_lbc2=x; z_lbc3=x; z_check=x; z_lbc0=x; z_ks=0; z_rks=0; z_=0;
t_lp=0; t_milp=0; t_hard=0; t_hard3=0; t_ks=0; t_lbc1=0; t_lbc2=0; t_lbc3=0; t_check=0; t_lbc0=0; t_ks=0; t_rks=0; t_=0;
g_lp=x; g_milp=x; g_hard=x; g_hard3=x; g_ks=x; g_lbc1=x; g_lbc2=x; g_lbc3=x; g_check=x; g_lbc0=x; g_ks=x; g_rks=x; g_=x;
ns=0; nU_no_int=0; n_Uu_no_int=0; n_Uu_1_0=0;
SB_Uu =[]; No_SB_Uu =[]; lower_Pmin_Uu =[]; Vv =[]; Ww =[]; delta =[];
SB_Uu3=[]; No_SB_Uu3=[]; lower_Pmin_Uu3=[]; Vv3=[]; Ww3=[]; delta3=[];
comment = 'Here it writes a message to the stat.csv results file' 

if ambiente == 'yalma':
    if len(sys.argv) != 3:
        print('!!! Something went wrong, try write something like: $python3 main.py uc_54.json yalma')
        print('archivo :', sys.argv[1])
        print('ambiente:', sys.argv[2])
        sys.exit()
    nameins  = sys.argv[1]
    ambiente = sys.argv[2]

localtime = time.asctime(time.localtime(time.time()))

scope = 'market'  
scope = ''       ## Unit Commitment Model 

print(localtime,'Solving <'+scope+'> model ---> ---> ---> --->',nameins)

## Lee instancia de archivo .json con formato de [Knueven2020]
instance = reading.reading(ruta+nameins)


## ----------------------------------------- CHECK FEASIBILITY -----------------------------------------------
def checkSol(option,z_,SB_Uux,No_SB_Uux,Vvx,Wwx,deltax,dual=False):
    print('Check the feasibility of solution z_'+option+'=', z_ )
    t_o       = time.time() 
    model,__  = uc_Co.uc(instance,option='Check',SB_Uu=SB_Uux,No_SB_Uu=No_SB_Uux,V=Vvx,W=Wwx,delta=deltax,
                         nameins=nameins[0:5],mode='Tight',scope=scope)
    sol_check = Solution(model=model,nameins=nameins[0:5],env=ambiente,executable=executable,gap=gap,timelimit=timemilp,
                         tee=False,tofiles=False,emphasize=emph,symmetry=symmetry,exportLP=False,option='Check',scope=scope,dual=dual)
    z_check, g_check = sol_check.solve_problem()
    t_check          = time.time() - t_o
    print('t_check= ',round(t_check,1),'z_check= ',round(z_check,4),'g_check= ',round(g_check,4))
    return model

if  False:
    ## --------------------------------------- RECOVERED SOLUTION ---------------------------------------------
    ## Load LR and Hard3 storaged solutions
    if path.exists('solHard3_a_'+nameins[0:5]+'.csv') == True and path.exists('solHard3_b_'+nameins[0:5]+'.csv') == True:
        t_lp,z_lp,t_hard3,z_hard3,SB_Uu3,No_SB_Uu3,lower_Pmin_Uu3,Vv3,Ww3,delta3 = util.loadSolution('Hard3',nameins[0:5]) 
        g_hard3  = util.igap(z_lp,z_hard3) 
        print('Recovered solution ---> ','t_hard3= ',round(t_hard3,1),'z_hard3= ',round(z_hard3,1))
        checkSol('Hard3 (recovered)',z_hard3,SB_Uu3,No_SB_Uu3,Vv3,Ww3,delta3) ## Check feasibility


    ## --------------------------------------- LINEAR RELAXATION ---------------------------------------------
    ## Relax as LP and solve it
    else:
        t_o        = time.time() 
        model,__   = uc_Co.uc(instance,option='LR',nameins=nameins[0:5],mode='Tight',scope=scope)
        sol_lp     = Solution(model=model,env=ambiente,executable=executable,nameins=nameins[0:5],gap=gap,timelimit=timeheu,
                            tee=False,tofiles=False,emphasize=emph,exportLP=False,option='LR',scope=scope)
        z_lp, g_lp = sol_lp.solve_problem() 
        t_lp       = time.time() - t_o
        print('t_lp= ',round(t_lp,1),'z_lp= ',round(z_lp,1))


    ## ------------------------------------ SELECTION VARIABLES TO FIX ---------------------------------------
    ## Seleccionamos las variables que serán fijadas. Es requisito correr antes <linear relaxation>
    ## SB_Uu         variables que SI serán fijadas a 1. (Soporte binario)
    ## No_SB_Uu      variables que NO serán fijadas.
    ## lower_Pmin_Uu variables en las que el producto de Pmin*Uu de [Harjunkoski2021] 
    ##               es menor a la potencia mínima del generador Pmin.
        SB_Uu, No_SB_Uu, lower_Pmin_Uu, Vv, Ww, delta = sol_lp.select_binary_support_Uu('LR')
        del sol_lp
        gc.collect()

    ## ----------------------------------- HARD-FIXING 3 (only Uu) ---------------------------------------------
    ## HARD-FIXING 3 (only Uu) solution and solve the sub-MILP. (Require run the LP)
        t_o       = time.time()
        lbheur    = 'no'
        model,__  = uc_Co.uc(instance,option='Hard3',SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,
                            nameins=nameins[0:5],mode='Tight',scope=scope)
        sol_hard3 = Solution(model=model,env=ambiente,executable=executable,nameins=nameins[0:5],gap=gap,timelimit=timeheu,
                            tee=False,emphasize=emph,lbheur=lbheur,symmetry=symmetry,tofiles=False,option='Hard3',scope=scope)
        z_hard3, g_hard3 = sol_hard3.solve_problem()
        t_hard3  = time.time() - t_o + t_lp   ## <<< --- t_hard3 ** INCLUYE EL TIEMPO DE LP **
        g_hard3  = util.igap(z_lp,z_hard3) 
        print('t_hard3= ',round(t_hard3,1),'z_hard3= ',round(z_hard3,1))
        
        ## ES MUY IMPORTANTE GUARDAR LAS VARIABLES 'Uu=1'(SB_Uu3) DE LA PRIMERA SOLUCIÓN FACTIBLE 'Hard3'.
        ## ASI COMO LAS VARIABLES 'Uu=0' (No_SB_Uu3) 
        ## Este es el primer - Soporte Binario Entero Factible-
        SB_Uu3, No_SB_Uu3, __, Vv3, Ww3, delta3 = sol_hard3.select_binary_support_Uu('Hard3')    
        lower_Pmin_Uu3 = sol_hard3.update_lower_Pmin_Uu(lower_Pmin_Uu,'Hard3')
        #sol_hard3.cuenta_ceros_a_unos( SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Hard3')    

        print('t_hard3= ',round(t_hard3,1),'z_hard3= ',round(z_hard3,1),'g_hard3= ',round(g_hard3,5) )
        del sol_hard3
        gc.collect()
        util.saveSolution(t_lp,z_lp,t_hard3,z_hard3,SB_Uu3,No_SB_Uu3,lower_Pmin_Uu3,Vv3,Ww3,delta3,'Hard3',nameins[0:5])
            

## --------------------------------------- LOCAL BRANCHING 1 ------------------------------------------
## LBC COUNTINOUS VERSION without soft-fixing
## Include the LOCAL BRANCHING CUT to the solution and solve the sub-MILP (it is using cutoff=z_hard).

if  False:    
    t_o            = time.time() 
    Vv             = deepcopy(Vv3)
    Ww             = deepcopy(Ww3)
    delta          = deepcopy(delta3)
    SB_Uu          = deepcopy(SB_Uu3)
    No_SB_Uu       = deepcopy(No_SB_Uu3)
    lower_Pmin_Uu  = deepcopy(lower_Pmin_Uu3)
    t_net          = timemilp - t_hard3
    t_res          = timemilp - t_hard3
    cutoff         = z_hard3
    incumbent      = z_hard3
    z_old          = z_hard3
    improve        = True    
    timeover       = False
    iter           = 1
    saved          = [SB_Uu,No_SB_Uu,Vv,Ww,delta]
    rightbranches  = []
    char           = ''
    fish           = ')'
    result_iter    = []
    result_iter.append((t_hard3,z_hard3))
    print('\t')
        
    while True:
        if (iter==iterstop) or (time.time() - t_o >= t_net):
            break
        lbheur   = 'no'
        char     = ''
        
        if improve == False:
            cutoff=1e+75
                 
        timeheu1  = min(t_res,timeheu)
        model, __ = uc_Co.uc(instance,option='lbc1',SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,V=Vv,W=Ww,delta=delta,
                            percent_soft=90,k=k,nameins=nameins[0:5],mode='Tight',scope=scope,improve=improve,timeover=timeover,rightbranches=rightbranches)
        sol_lbc1  = Solution(model=model,env=ambiente,executable=executable,nameins=nameins[0:5],letter=util.getLetter(iter-1),gap=gap,cutoff=cutoff,timelimit=timeheu1,
                            tee=False,emphasize=emph,lbheur=lbheur,symmetry=symmetry,tofiles=False,option='lbc1',scope=scope)
        z_lbc1,g_lbc1 = sol_lbc1.solve_problem()
        
        #sol_lbc1.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'lbc1') ## Compara contra la última solución
        
        gap_iter = abs((z_lbc1 - z_old) / z_old) * 100 ## Percentage
        improve = False
        if z_lbc1 < incumbent :                        ## Update solution
            incumbent  = z_lbc1
            cutoff     = z_lbc1
            # saved      = [SB_Uu,No_SB_Uu,Vv,Ww,delta]
            char       = '***'
            g_lbc1     = util.igap(z_lp,z_lbc1)
            if gap_iter > gap:
                improve = True

        result_iter.append((round(time.time() - t_o + t_hard3,1),z_lbc1))
        z_old = z_lbc1 ## Guardamos la z de la solución anterior
          
        print('<°|'+fish+'>< iter:'+str(iter)+' t_lbc1= ',round(time.time()-t_o+t_hard3,1),'z_lbc1= ',round(z_lbc1,1),char ) #,'g_lbc1= ',round(g_lbc1,5)
        print('\t')       
        fish = fish + ')'  
        
        ## Aqui se prepara la nueva iteracion ...  
        timeover == False       
        if improve == False:   
            if sol_lbc1.timeover == True or sol_lbc1.nosoluti == True or sol_lbc1.infeasib == True:                     
                if sol_lbc1.timeover == True:   
                    print('k=[k/2] Time limit reach without improve: shrinking the neighborhood  ...  >(°> . o O')
                else:
                    print('k=[k/2] No solution/infeasible: shrinking the neighborhood  ...  >(°> . o O')
                k = floor(k/2)  
                timeover == True         
            else:              
                print('Leaving a local optimum ...  >>+*+*+*+*+*+|°>')
                SB_Uu, No_SB_Uu, __, Vv, Ww, delta = sol_lbc1.select_binary_support_Uu('lbc1')  
                lower_Pmin_Uu = sol_lbc1.update_lower_Pmin_Uu(lower_Pmin_Uu,'lbc1') 
                rightbranches.append([SB_Uu,No_SB_Uu,lower_Pmin_Uu])
                fish = ')'
        else: ## Mejora la solución
            SB_Uu, No_SB_Uu, __, Vv, Ww, delta = sol_lbc1.select_binary_support_Uu('lbc1')  
            lower_Pmin_Uu = sol_lbc1.update_lower_Pmin_Uu(lower_Pmin_Uu,'lbc1')
            saved         = [SB_Uu,No_SB_Uu,Vv,Ww,delta] ## Update solution
                    
        t_res = t_net - time.time() + t_o 
        print('lbc1','tiempo restante:',t_res)
        
        del sol_lbc1
        gc.collect()
        iter  = iter + 1
         
    t_lbc1 = time.time() - t_o + t_hard3  
    z_lbc1 = incumbent    
    for item in result_iter:
        print(item[0],',',item[1])    
    result_iter = np.array(result_iter)
    np.savetxt('iterLBC1'+nameins[0:5]+'.csv', result_iter, delimiter=',')
    
    checkSol('z_lbc1',z_lbc1,SB_Uu,No_SB_Uu,Vv,Ww,delta) ## Check feasibility (LB1)
        
    k = k_original  ## Si es que LBC cambió el parámetro k

        
## --------------------------------------- LOCAL BRANCHING 2 ------------------------------------------
## LBC COUNTINOUS VERSION without soft-fixing
## Include the LOCAL BRANCHING CUT to the solution and solve the sub-MILP (it is using cutoff=z_hard).

if  False:    
    t_o            = time.time() 
    Vv             = deepcopy(Vv3)
    Ww             = deepcopy(Ww3)
    delta          = deepcopy(delta3)
    SB_Uu          = deepcopy(SB_Uu3)
    No_SB_Uu       = deepcopy(No_SB_Uu3)
    lower_Pmin_Uu  = deepcopy(lower_Pmin_Uu3)
    t_net          = timemilp - t_hard3
    t_res          = timemilp - t_hard3
    cutoff         = z_hard3
    incumbent      = z_hard3
    z_old          = z_hard3
    improve        = True    
    timeover       = False
    iter           = 1
    saved          = [SB_Uu,No_SB_Uu,Vv,Ww,delta]
    rightbranches  = []
    char           = ''
    fish           = ')'
    result_iter    = []
    result_iter.append((t_hard3,z_hard3))
    print('\t')
        
    while True:
        if (iter==iterstop) or (time.time()-t_o >= t_net):
            break
        lbheur   = 'no'
        char     = ''
        
        if improve == False:
            cutoff=1e+75
        
        timeheu1  = min(t_res,timeheu)      
        model, __ = uc_Co.uc(instance,option='lbc2',SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,V=Vv,W=Ww,delta=delta,
                            percent_soft=90,k=k,nameins=nameins[0:5],mode='Tight',scope=scope,improve=improve,timeover=timeover,rightbranches=rightbranches)
        sol_lbc2  = Solution(model=model,env=ambiente,executable=executable,nameins=nameins[0:5],letter=util.getLetter(iter-1),gap=gap,cutoff=cutoff,timelimit=timeheu1,
                            tee=False,emphasize=emph,lbheur=lbheur,symmetry=symmetry,tofiles=False,option='lbc2',scope=scope)
        z_lbc2,g_lbc2 = sol_lbc2.solve_problem()
        
        #sol_lbc2.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'lbc2') ## Compara contra la última solución
        
        gap_iter = abs((z_lbc2 - z_old)/z_old) * 100 ## Percentage
        improve = False
        if z_lbc2 < incumbent :                      ## Update solution
            incumbent  = z_lbc2
            cutoff     = z_lbc2
            #saved      = [SB_Uu,No_SB_Uu,Vv,Ww,delta]
            char       = '***'
            g_lbc2     = util.igap(z_lp,z_lbc2)
            if gap_iter > gap:
                improve = True
            
        result_iter.append((round(time.time()-t_o+t_hard3,1),z_lbc2))
        z_old = z_lbc2 ## Guardamos la solución anterior
          
        print('<°|'+fish+'>< iter:'+str(iter)+' t_lbc2= ',round(time.time()-t_o+t_hard3,1),'z_lbc2= ',round(z_lbc2,1),char ) #,'g_lbc2= ',round(g_lbc2,5)
        print('\t')       
        fish = fish + ')'  
        
        ## Aquí se prepara la nueva iteracion ...  
        timeover == False       
        if improve == False:   
            if sol_lbc2.timeover == True or sol_lbc2.nosoluti == True or sol_lbc2.infeasib == True:                     
                if sol_lbc2.timeover == True:   
                    print('k=[k/2] Time limit reach without improve: shrinking the neighborhood  ...  >(°> . o O')
                else:
                    print('k=[k/2] No solution/infeasible: shrinking the neighborhood  ...  >(°> . o O')
                k = floor(k/2)  
                timeover == True         
            else:              
                print('Leaving a local optimum     ...    >>+*+*+*+*+*+|°>')
                SB_Uu, No_SB_Uu, __, Vv, Ww, delta = sol_lbc2.select_binary_support_Uu('lbc2')  
                lower_Pmin_Uu = sol_lbc2.update_lower_Pmin_Uu(lower_Pmin_Uu,'lbc2') 
                rightbranches.append([SB_Uu,No_SB_Uu,lower_Pmin_Uu])
                fish = ')'
        else: ## Mejora la solución
            SB_Uu, No_SB_Uu, __, Vv, Ww, delta = sol_lbc2.select_binary_support_Uu('lbc2')  
            lower_Pmin_Uu = sol_lbc2.update_lower_Pmin_Uu(lower_Pmin_Uu,'lbc2') 
            saved         = [SB_Uu,No_SB_Uu,Vv,Ww,delta] ## Update solution

        t_res = t_net - time.time() + t_o 
        print('lbc2 ','tiempo restante:',t_res)
        
        del sol_lbc2
        gc.collect()
        iter = iter + 1

    t_lbc2 = time.time() - t_o + t_hard3  
    z_lbc2 = incumbent    
    for item in result_iter:
        print(item[0],',',item[1])    
    result_iter = np.array(result_iter)
    np.savetxt('iterLBC2'+nameins[0:5]+'.csv', result_iter, delimiter=',')
    
    checkSol('z_lbc2',z_lbc2,SB_Uu,No_SB_Uu,Vv,Ww,delta) ## Check feasibility (LBC2)
    
    k = k_original  ## Si es que LBC cambió el parámetro k


## ---------------------------------  KERNEL SEARCH I ---------------------------------
##
## La versión básica de KS consiste en relajar la formulacion y a partir de ello sacar 
## las variables del kernel y de los buckets, después de manera iterativa se resulven los 
## SUB-MILP´S 'restringidos' mas pequeños.
## KS solution and solve the sub-MILP (it is using cutoff = z_hard).
## Use 'Soft+pmin' (lower subset of Uu-Pmin)  as the first and unique bucket to consider
## Use relax the integrality variable Uu.

if  False:
    Vv          = deepcopy(Vv3)
    Ww          = deepcopy(Ww3)
    delta       = deepcopy(delta3)
    SB_Uu       = deepcopy(SB_Uu3)
    No_SB_Uu    = deepcopy(No_SB_Uu3)
    saved       = [SB_Uu,No_SB_Uu,Vv,Ww,delta]

    t_o         = time.time() 
    incumbent   =  z_hard3
    cutoff      =  z_hard3 # 1e+75 
    iter        =  0  
    sol_ks      =  []
    result_iter =  []
    result_iter.append((t_hard3 + time.time() - t_o, z_hard3))

    while True:
        ## --------------------------------------- CALCULATE REDUCED COSTS Uu ------------------------------------
        t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
        if t_res <= 0:
            print('KS Salí ciclo externo')
            break
        
        if  True:
            t_1 = time.time()
            model,__  = uc_Co.uc(instance,option='RC',SB_Uu=saved[0],No_SB_Uu=saved[1],V=saved[2],W=saved[3],delta=saved[4],
                                 nameins=nameins[0:5],mode='Tight',scope=scope)
            sol_rc    = Solution(model=model,nameins=nameins[0:5],env=ambiente,executable=executable,gap=gap,timelimit=timemilp,
                                tee=False,tofiles=False,emphasize=emph,symmetry=symmetry,exportLP=False,rc=True,option='RC',scope=scope)
            z_rc,g_rc = sol_rc.solve_problem() 
            t_rc      = time.time() - t_1
            print('KS t_rc= ',round(t_rc,1),'z_rc= ',round(z_rc,4))      
            
            ## ----------------------------- SECOND PHASE ----------------------------------------------
            ##  Defining buckets 
            rc   = []
            i    = 0                    
            for f in No_SB_Uu: 
                rc.append(( i, model.rc[model.u[f[0]+1,f[1]+1]],f[0],f[1] ))
                i = i + 1    
            rc.sort(key=lambda tup:tup[1], reverse=False) ## Ordenamos las variables No_SB_Uu de acuerdo a sus costos reducidos 
            
            ##  Definimos el número de buckets 
            K = floor(1 + 3.322 * log(len(No_SB_Uu)))  ## Sturges rule
            print('KS Number of buckets K =', K)    
            len_i  = ceil(len(No_SB_Uu) / K)
            pos_i  = 0
            k_     = [0]    
            for i in range(len_i,len(No_SB_Uu),len_i+1):
                k_.append( i )
            k_[-1] = len(No_SB_Uu)
            print( k_ )
            
            cutoff      = incumbent # 1e+75 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            iter_bk     = 0
            iterstop    = K - 2
            char        = ''
            kernel      = deepcopy(SB_Uu)
            
            ## Recontabilizamos el tiempo
            t_res   = max(0,( timemilp - t_hard3) - (time.time() - t_o))
            timeheu = t_res / K
            
            while True: 
                t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
                if iter_bk >= iterstop or t_res <= 0:
                    print('KS Salí ciclo interno')
                    break

                timeheu1  = min(t_res,timeheu)      
                bucket    = rc[k_[iter_bk]:k_[iter_bk + 1]] 
                print('bucket',util.getLetter(iter),'[',k_[iter_bk],':',k_[iter_bk + 1],']' )      
                
                try:
                    ##  Resolvemos el kernel con cada uno de los buckets
                    lbheur     = 'yes'
                    emph       = 0     ## feasibility =1
                    model,__   = uc_Co.uc(instance,option='KS',kernel=kernel,bucket=bucket,nameins=nameins[0:5],mode='Tight',scope=scope)
                    sol_ks     = Solution(model=model,env=ambiente,executable=executable,nameins=nameins[0:5],letter=util.getLetter(iter),gap=gap,cutoff=cutoff,timelimit=timeheu1,
                                        tee=False,emphasize=emph,lbheur=lbheur,symmetry=symmetry,tofiles=False,option='KS',scope=scope)
                    z_ks, g_ks = sol_ks.solve_problem()
                    t_ks       = time.time() - t_o + t_hard3
                    kernel, No_SB_Uu, __, Vv, Ww, delta = sol_ks.select_binary_support_Uu('KS') 
                    
                    if z_ks < incumbent :                      ## Update solution
                        incumbent  = z_ks
                        cutoff     = z_ks
                        saved      = [kernel,No_SB_Uu,Vv,Ww,delta]
                        g_ks       = util.igap(z_lp,z_ks)
                        char       = '***'
                        
                    result_iter.append((round(time.time()-t_o+t_hard3,1), z_ks))
                    print('<°|>< iter:'+str(iter)+' t_ks= ',round(time.time()-t_o+t_hard3,1),'z_ks= ',round(z_ks,1),char) #,'g_ks= ',round(g_ks,5)
                except:
                    # print('>>> Iteración sin solución')
                    result_iter.append((round(time.time()-t_o+t_hard3,1), 1e+75))
                finally:    
                    iter_bk = iter_bk + 1
                    
                print('\t')       
                    
                t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
                print('KS ','tiempo restante:',t_res)
                
                del sol_ks
                gc.collect()
                iter = iter + 1
                                
        Vv       = deepcopy(saved[2])
        Ww       = deepcopy(saved[3])
        delta    = deepcopy(saved[4])
        SB_Uu    = deepcopy(saved[0])
        No_SB_Uu = deepcopy(saved[1])

    t_ks = (time.time() - t_o) + t_hard3  
    z_ks = incumbent    
    for item in result_iter:
        print(item[0],',',item[1])
    result_iter = np.array(result_iter)
    np.savetxt('iterKS'+nameins[0:5]+'.csv', result_iter, delimiter=',')
    
    checkSol('z_ks',z_ks,SB_Uu,No_SB_Uu,Vv,Ww,delta) ## Check feasibility (KS)
            
        
    ## PENDIENTES    
    # \todo{Exportar los Costos reducidos ordenados de LR y comparar contra los lower_Pmin_Uu, se esperan coincidencias}
    # \todo{Curar instancias Morales y Knueven (cambiar limites pegados y agregar piecewise cost)}
    # \todo{Incluir datos hidro de instancias en México} 
    # \todo{Incluir restricciones de generadores hidro}  
    # \todo{Verificar por qué la instancia mem_01.json es infactible}
    
    ## PRUEBAS                    
    # \todo{Probar experimentalmente que fijar otras variables enteras además de Uu no impacta mucho}         
    # \todo{Probar modificar el tamaño de las variables soft-fix de 90% al 95%}
    # \todo{Probar configuración enfasis feasibility vs optimality en el Solver )} 

    ## IDEAS    
    # \todo{Un KS relajando y fijando grupos de variables a manera de buckets}

    ## DESCARTES         
    # \todo{Un movimiento en la búsqueda local puede ser cambiar la asignación del costo de arranque en un periodo adelante o atras para algunos generadores} 
    # \todo{Hacer un VNS o un VND con movimientos definidos con las variables}
    # \todo{Podrian fijarse todas las variables (u,v,w y delta) relacionadas con los generadores que se escogen para ser fijados}
    # \todo{Podríamos usar reglas parecidas al paper de Todosijevic para fijar V,W a partir de Uu}
    # \todo{probar que SI conviene incluir los intentos de asignación en las variables soft-fix }
    # \todo{Calcular el tamaño del slack del subset Sbarra -Soporte binario-}
    # \todo{Probar tamaños del n_kernel (!!! al parecer influye mucho en el tiempo de búsqueda)} 
    # \todo{Agregar must-run} 
    # \todo{Encontrar la primer solución factible del CPLEX}
    
    ## TERMINADAS
    # \todo{Considerar no usar nada de Hard, ni cut-off, ni Soporte Binario.}
    # \todo{Probar cambiar el valor de k en nuevas iteraciones con una búsqueda local (un LBC completo de A.Lodi)}    
    # \todo{Usar la solución factible hard como warm-start} 
    # \todo{Probar el efecto de la cota obtenida del hard-fix} 
    # \todo{Probar con diferentes calidades de primera solución factible,(podríamos usar Pure Variable-fixing)}
    # \todo{Revisar la desigualdad válida. El numero de 1´s de las variables de arranque 'V' en un horizonte deben ser igual al número de 1's en la variable delta}
    # \todo{Comparar soluciones entre si en variables u,v,w y delta}
    # \todo{Verificar que las restricciones de arranque que usan delta en la formulación, se encontraron variables con valor None en la solución}
    # \todo{Fijar la solución entera y probar factibilidad} 
    # \todo{Crear instancias sintéticas a partir de morales-españa2013} 
    
## NO OLVIDES COMENTAR TUS PRUEBAS ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
comment    = 'Leyendo zonas prohibidas'

  
## ---------------------------------------------- MILP ----------------------------------------------------------
## Solve as a MILP

if  True: 
    strategy = 3
    symmetrydefault = 0 ## symmetry breaking: Automatic =-1 Turn off=0 ; moderade=1 ; extremely aggressive=5
    cutoff   = 1e+75 
    lbheur   = 'yes'  
    emph     = 1          ## feasibility=1 ; balanced=0
    t_o      = time.time() 
    model,__ = uc_Co.uc(instance,option='MilpTest',nameins=nameins[0:5],mode='Tight',scope=scope)
    sol_milp = Solution(model=model,nameins=nameins[0:5],env=ambiente,executable=executable,
                        gap=gap,cutoff=cutoff,symmetry=symmetrydefault,strategy=strategy,timelimit=timemilp,
                        tee=False,tofiles=False,emphasize=emph,lbheur=lbheur,
                        exportLP=False,option='MilpTest',scope=scope)
    z_milp, g_milp = sol_milp.solve_problem()
    t_milp         = time.time() - t_o
    print('t_milp= ',round(t_milp,1),'z_milp= ',round(z_milp,1),'g_milp= ',round(g_milp,5))
    
    
    
    ## ----------------------------- DUAL COST ----------------------------------------------
    
    SB_Uu, No_SB_Uu, __, Vv, Ww, delta = sol_milp.select_binary_support_Uu('Milp0') 
    model,__  = uc_Co.uc(instance,option='FixSol',SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,V=Vv,W=Ww,delta=delta,
                         nameins=nameins[0:5],mode='Tight',scope=scope)
    sol_fix   = Solution(model=model,env=ambiente,executable=executable,nameins=nameins[0:5],gap=gap,timelimit=timeheu,
                          tee=False,tofiles=False,emphasize=emph,exportLP=False,option='FixSol',scope=scope,dual=True)
    z_fix, g_fix = sol_fix.solve_problem() 
    print('z_fix= ',round(z_fix,4))
    
    # for t in model.T:
    #     print(model.dual[ model.demand_rule65[t] ],model.dual[ model.demand_rule67[t] ])


## --------------------------------- RESULTS -------------------------------------------
## Append a list as new line to an old csv file using as log, the first line of the file as shown.
## 'ambiente,localtime,nameins,T,G,gap,emphasize,timelimit,z_lp,z_hard,z_milp,z_milp2,z_soft,z_softpmin,z_softcut,z_softcut2,z_softcut3,z_lbc,
#                                                       t_lp,t_hard,t_milp,t_milp2,t_soft,t_softpmin,t_softcut,t_softcut2,t_softcut3,t_lbc,
#                                                       n_fixU,nU_no_int,n_Uu_no_int,n_Uu_1_0,k,bin_sup,comment'

#ambiente,localtime,nameins,instance[1],instance[0],gap,emph,timeheu,timemilp,z_lp,z_milp,z_hard,z_hard3,z_lbc1,z_lbc2,z_lbc3,z_ks,z_rks,t_lp,t_milp,t_hard,t_hard3,t_lbc1,t_lbc2,t_lbc3,t_ks,t_rks,g_milp,g_hard,g_hard3,g_lbc1,g_lbc2,g_lbc3,g_ks,g_rks,k,ns,comment
row = [ambiente,localtime,nameins,instance[1],instance[0],gap,emph,timeheu,timemilp,
    round(z_lp,1),round(z_milp,1),round(z_hard,1),round(z_hard3,1),round(z_lbc1,1),round(z_lbc2,1),round(z_lbc3,1),round(z_ks,1),round(z_rks,1),
    round(t_lp,1),round(t_milp,1),round(t_hard,1),round(t_hard3,1),round(t_lbc1,1),round(t_lbc2,1),round(t_lbc3,1),round(t_ks,1),round(t_rks,1),
                  round(g_milp,8),round(g_hard,8),round(g_hard3,8),round(g_lbc1,8),round(g_lbc2,8),round(g_lbc3,8),round(g_ks,8),round(g_rks,8),
                  k,ns,comment] #round(((z_milp-z_milp2)/z_milp)*100,6)
util.append_list_as_row('stat.csv',row)

print(localtime,'terminé instancia ...´¯`·...·´¯`·.. ><(((º> ',nameins)

exit()

