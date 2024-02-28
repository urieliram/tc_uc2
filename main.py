# -------------------  >)|°> UriSoft© <°|(<  -------------------
# File: main.py
# A math-heuristic to Tight and Compact Unit Commitment Problem 
# Developers: Uriel Iram Lezama Lope
# Purpose: Programa principal de un modelo de UC
# Description: Lee una instancia de UCP y la resuelve. 
# Para correr el programa usar el comando 'python3 main.py anjos.json yalma'
# Desde script en linux test.sh 'sh test.sh'
# <º)))>< ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸ ><(((º>
import time
import sys
import uc_Co
import util
import reading
from solution import Solution

nameins = 'uc_03.json'       # ejemplos dificiles 2,3,4  
nameins = 'uc_06.json'       # ejemplos regulares 5,6 
nameins = 'uc_21.json'       # ejemplos dificiles 2,3,4 
nameins = 'uc_22.json'       # ejemplo dificil  
nameins = 'uc_42.json'       # ejemplo dificil 
nameins = 'uc_44.json'       # ejemplo dificil 
#nameins = 'uc_50.json'       # ejemplo sencillo       [1 abajo,milp factible]   
#nameins = 'uc_51.json'       # ejemplo sencillo
#nameins = 'uc_53.json'       # ejemplo de 'delta' relajado diferente de uno  
#nameins = 'uc_54.json'       # ejemplo sencillo
#nameins = 'uc_55.json'       # ejemplo sencillo 
#nameins = 'uc_56.json'       # ejemplo sencillo
#nameins = 'uc_46.json'       # ejemplo sencillo       [49 abajo,MILP infactible]
nameins = 'uc_02.json'        # ejemplos dificiles 2,3,4
nameins = 'mem_01.json'       # MEM (PENDIENTE)
nameins = 'anjos.json'        # ejemplo de juguete
nameins = 'morales_ejemplo_III_D.json'  #
nameins = 'uc_97.json'       #
nameins = 'uc_70.json'       #
nameins = 'uc_47.json'       # ejemplo sencillo
nameins = 'uc_58.json'       # prueba demostrativa excelente en mi PC 
nameins = 'uc_58_copy.json'  # prueba demostrativa excelente en mi PC (cinco dias) parA mtheuristics
nameins = 'uc_61.json'       # prueba demostrativa excelente en mi PC 
nameins = 'uc_57_copy.json'  # prueba demostrativa excelente en mi PC (un dia)

# Cargamos parámetros de configuración desde archivo <config>
# Emphasize balanced=0 (default); feasibility=1; optimality=2;
# symmetry automatic=-1; symmetry low level=1
ambiente, ruta, executable, timeheu, timemilp, emph, symmetry, gap, k, iterstop = util.config_env()
k_original = k  # Almacenamos el parámetro k de local branching
x = 1e+75
z_milp = x
z_ = 0
t_milp = 0
t_ = 0
g_milp = x
g_ = x
SB_Uu =[]; No_SB_Uu =[]; lower_Pmin_Uu =[]; Vv =[]; Ww =[]; delta =[];
SB_Uu3=[]; No_SB_Uu3=[]; lower_Pmin_Uu3=[]; Vv3=[]; Ww3=[]; delta3=[];
comment = 'Here it writes a message to the stat.csv results file'

if ambiente == 'yalma':
    if len(sys.argv) != 3:
        print('!!! Something went wrong, try write something like: $python3 main.py uc_54.json yalma')
        print('archivo :', sys.argv[1])
        print('ambiente:', sys.argv[2])
        sys.exit()
    nameins = sys.argv[1]
    ambiente = sys.argv[2]

localtime = time.asctime(time.localtime(time.time()))


print(localtime,'Solving < UCP based on power> model ---> ---> ---> --->', nameins)

# Lee instancia de archivo .json con formato de [Knueven2020]
instance = reading.reading(ruta+nameins)


# NO OLVIDES COMENTAR TUS PRUEBAS ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
comment    = 'Leyendo zonas prohibidas'

  
# ---------------------------------------------- MILP ----------------------------------------------------------
# Solve as a MILP

if  True: 
    strategy = 3
    symmetrydefault = 0 # symmetry breaking: Automatic =-1 Turn off=0 ; moderade=1 ; extremely aggressive=5
    cutoff   = 1e+75 
    lbheur   = 'yes'  
    emph     = 1          # feasibility=1 ; balanced=0
    t_o      = time.time() 
    model,__ = uc_Co.uc(instance,option='MilpTest',nameins=nameins[0:5],mode='Tight')
    sol_milp = Solution(model=model,nameins=nameins[0:5],env=ambiente,executable=executable,
                        gap=gap,cutoff=cutoff,symmetry=symmetrydefault,strategy=strategy,timelimit=timemilp,
                        tee=False,tofiles=True,emphasize=emph,lbheur=lbheur,
                        exportLP=False,option='MilpTest')
    z_milp, g_milp = sol_milp.solve_problem()
    t_milp         = time.time() - t_o
    print('t_milp= ',round(t_milp,1),'z_milp= ',round(z_milp,1),'g_milp= ',round(g_milp,5))
    
    
    
    # ----------------------------- DUAL COST ----------------------------------------------
    
    # SB_Uu, No_SB_Uu, __, Vv, Ww, delta = sol_milp.select_binary_support_Uu('Milp0') 
    # model,__  = uc_Co.uc(instance,option='FixSol',SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,V=Vv,W=Ww,delta=delta,
    #                      nameins=nameins[0:5],mode='Tight')
    # sol_fix   = Solution(model=model,env=ambiente,executable=executable,nameins=nameins[0:5],gap=gap,timelimit=timeheu,
    #                       tee=False,tofiles=False,emphasize=emph,exportLP=False,option='FixSol',dual=True)
    # z_fix, g_fix = sol_fix.solve_problem() 
    # print('z_fix= ',round(z_fix,4))
    
    # for t in model.T:
    #     print(model.dual[ model.demand_rule65[t] ],model.dual[ model.demand_rule67[t] ])


# --------------------------------- RESULTS -------------------------------------------
# Append a list as new line to an old csv file using as log, the first line of the file as shown.
# 'ambiente,localtime,nameins,T,G,gap,emphasize,timelimit,z_lp,z_hard,z_milp,z_milp2,z_soft,z_softpmin,z_softcut,z_softcut2,z_softcut3,z_lbc,
#                                                       t_lp,t_hard,t_milp,t_milp2,t_soft,t_softpmin,t_softcut,t_softcut2,t_softcut3,t_lbc,
#                                                       n_fixU,nU_no_int,n_Uu_no_int,n_Uu_1_0,k,bin_sup,comment'

#ambiente,localtime,nameins,instance[1],instance[0],gap,emph,timeheu,timemilp,z_lp,z_milp,z_hard,z_hard3,z_lbc1,z_lbc2,z_lbc3,z_ks,z_rks,t_lp,t_milp,t_hard,t_hard3,t_lbc1,t_lbc2,t_lbc3,t_ks,t_rks,g_milp,g_hard,g_hard3,g_lbc1,g_lbc2,g_lbc3,g_ks,g_rks,k,ns,comment
row = [ambiente,localtime,nameins,instance[1],instance[0],gap,emph,timeheu,timemilp,
    round(z_milp,1),round(t_milp,1),round(g_milp,8),k,comment] #round(((z_milp-z_milp2)/z_milp)*100,6)
util.append_list_as_row('stat.csv', row)

print(localtime,'terminé instancia ...´¯`·...·´¯`·.. ><(((º> ',nameins)

exit()

