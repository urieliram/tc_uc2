
## --------------------------------- SOFT-FIXING (deprecared)---------------------------------------------
        
## SOFT-FIXING solution and solve the sub-MILP. (Versión sin actualizar el cut-off)
# if 1 == 0:  # or precargado == False  
#     t_o = time.time() 
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,pc_0,mpc,Pb,C,Cs,Tunder,option='Soft',SB_Uu=SB_Uu,nameins=instancia[0:4])
#     sol_soft = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:4],gap=gap,timelimit=timelimit,
#                           tee=False,emphasize=emph,tofiles=False,option='Soft')
#     z_soft,g_soft = sol_soft.solve_problem() 
#     t_soft        = time.time() - t_o + t_lp
#     print("t_soft= ",round(t_soft,1),"z_soft= ",round(z_soft,1),"g_soft= ",round(g_soft,5))
#     sol_soft.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Soft')

        
## -------------------------------- SOFT FIXING + Pmin (deprecared)------------------------------------
        
## SOFT FIX + Pmin solution and solve the sub-MILP (Versión sin actualizar el cut-off)
## Use 'Soft+pmin' if the lower subset of Uu-Pmin will be considered.
# if 1 == 0:  # or precargado == False  
#     t_o = time.time() 
#     model,xx     = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,pc_0,mpc,Pb,C,Cs,Tunder,option='Soft+pmin',SB_Uu=SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,nameins=instancia[0:4])
#     sol_softpmin = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:4],gap=gap,timelimit=timelimit,
#                              tee=False,emphasize=emph,tofiles=False,option='Soft+pmin')
#     z_softpmin,g_softpmin = sol_softpmin.solve_problem() 
#     t_softpmin            = time.time() - t_o + t_lp
#     print("t_soft+pmin= ",round(t_softpmin,4),"z_soft+pmin= ",round(z_softpmin,1),"g_soft+pmin= ",round(g_softpmin,5))
#     sol_softpmin.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Soft+pmin')
    

## -------------------------------- SOFT FIXING + CUT-OFF (deprecared)------------------------------------
        
## SOFT FIX + CUT-OFF solution and solve the sub-MILP (it is using cutoff ---> z_hard).
# if 1 == 0:  # or precargado == False  
#     t_o = time.time() 
#     model,xx    = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,pc_0,mpc,Pb,C,Cs,Tunder,option='Soft',SB_Uu=SB_Uu,nameins=instancia[0:4])
#     sol_softcut = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:4],gap=gap,cutoff=z_hard,timelimit=timelimit,
#                              tee=False,emphasize=emph,tofiles=False,option='Soft')
#     z_softcut,g_softcut = sol_softcut.solve_problem() 
#     t_softcut           = time.time() - t_o + t_hard ## t_hard (ya incluye el tiempo de lp)
#     print("t_soft+cut= ",round(t_softcut,4),"z_soft+cut= ",round(z_softcut,1),"g_soft+cut= ",round(g_softcut,5))
#     sol_softcut.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Soft+cut')
    
    
## -------------------------------- SOFT FIXING + CUT-OFF + Pmin (deprecared)------------------------------------
        
## SOFT FIX + CUT-OFF + Pmin solution and solve the sub-MILP (it is using cutoff ---> z_hard).
# if 1 == 0:  # or precargado == False  
#     t_o = time.time() 
#     model,xx     = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,pc_0,mpc,Pb,C,Cs,Tunder,option='Soft2',SB_Uu=SB_Uu,nameins=instancia[0:4])
#     sol_softcut2 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:4],gap=gap,cutoff=z_hard,timelimit=timelimit,
#                              tee=False,emphasize=emph,tofiles=False,option='Soft2')
#     z_softcut2,g_softcut2 = sol_softcut2.solve_problem() 
#     t_softcut2            = time.time() - t_o + t_hard ## t_hard (ya incluye el tiempo de lp)
#     print("t_soft+cut+pmin= ",round(t_softcut2,4),"z_soft+cut+pmin= ",round(z_softcut2,1),"g_soft+cut+pmin= ",round(g_softcut2,5))
#     sol_softcut2.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Soft+pmin+cut')   
     
    
## --------------------------- SOFT FIXING + CUT-OFF + Pmin + FIXING_0 (deprecared)------------------------------------
        
## SOFT FIX + CUT-OFF + Pmin + FIXING_0  solution and solve the sub-MILP (it is using cutoff ---> z_hard).
# if 1 == 1:  # or precargado == False  
#     t_o = time.time() 
#     model,xx     = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,pc_0,mpc,Pb,C,Cs,Tunder,option='Soft3',SB_Uu=SB_Uu2,No_SB_Uu=No_SB_Uu2,lower_Pmin_Uu=lower_Pmin_Uu,nameins=instancia[0:4])
#     sol_softcut3 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:4],gap=gap,cutoff=z_hard,timelimit=timelimit,
#                              tee=False,emphasize=emph,tofiles=False,option='Soft3')
#     z_softcut3,g_softcut3 = sol_softcut3.solve_problem() 
#     t_softcut3            = time.time() - t_o + t_hard ## t_hard (ya incluye el tiempo de lp)
#     print("t_soft+cut+pmin+fix0= ",round(t_softcut3,4),"z_soft+cut+pmin+fix0= ",round(z_softcut3,1),"g_soft+cut+pmin+fix0= ",round(g_softcut3,5))
    
#     sol_softcut3.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Soft+pmin+cut+fix0')


## En esta función seleccionamos el conjunto de variables delta que quedarán en uno/cero para ser fijadas posteriormente.
    # def select_fixed_variables_delta(self):    
    #     fixed_delta = []; No_fixed_delta = [] 
        
    #     parameter  = 0.9
    #     total      = 0
    #     nulos      = 0
    #     for g,t,s in self.model.indexGTSg:
    #         if self.model.delta[(g,t,s)].value != None:
                
    #             if self.model.delta[(g,t,s)].value >= parameter:
    #                 fixed_delta.append([g,t,s,1])
    #                 # print(g,t,s)                    
    #                 # print(self.model.delta[(g,t,s)].value)
    #             else:
    #                 No_fixed_delta.append([g,t,s,0])
    #         else: ## Si es None                
    #             fixed_delta.append([g,t,s,0])
    #             nulos = nulos + 1
    #         total = total + 1
                
    #     print('Total delta   =', total)  
    #     print('Nulos delta   =', nulos)  
    #     print('Fixed delta  >=', parameter,len(fixed_delta)-nulos)
        
    #     return fixed_delta, No_fixed_delta
    
    
    ## En esta función seleccionamos el conjunto de variables V,W que quedarán en uno/cero para ser fijadas posteriormente.
    # def select_fixed_variables_VW(self):    
        
    #     fixed_V   = []; No_fixed_V = []; fixed_W = []; No_fixed_W = []
        
    #     parameter = 0.9
    #     total     = 0
    #     for t in range(self.tt):
    #         for g in range(self.gg):
    #             if self.V[g][t] != None:
                
    #                 if self.V[g][t] >= parameter:
    #                     fixed_V.append([g,t,1])
    #                 else:
    #                     No_fixed_V.append([g,t,0])
                    
    #             if self.W[g][t] != None:
                
    #                 if self.W[g][t] >= parameter:
    #                     fixed_W.append([g,t,1])
    #                 else:
    #                     No_fixed_W.append([g,t,0])
    #             total = total + 1
                
    #     print('Total V,W   =',total)  
    #     print('Fixed V    >=', parameter, len(fixed_V)) 
    #     print('Fixed W    >=', parameter, len(fixed_W)) 
           
    #     return fixed_V, No_fixed_V, fixed_W, No_fixed_W


## ---------------------------- SOFT VARIABLE FIXING ------------------------------------------

    # ## Si se desea usar la solución fix y calcular un sub-MILP.
    # if(option == 'Soft' or option == 'Soft2' or option == 'Soft3'): 

    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval  ## Soft-fixing I                

    #     ## Adding a new restriction.  
    #     ## https://pyomo.readthedocs.io/en/stable/working_models.html
    #     ## Soft-fixing II
    #     model.cuts = pyo.ConstraintList()
    #     n_subset   = math.ceil( (percent_lbc/100) * len(SB_Uu))
    #     expr       = 0
        
    #     for f in SB_Uu:      
    #         expr += model.u[f[0]+1,f[1]+1]
        
    #     if(option == 'Soft2' or option == 'Soft3'):
    #         # \todo{DEMOSTRAR QUE NOS CONVIENE RELAJAR LOS INTENTOS DE ASIGNACIÓN EN EL SOFT-FIXING}
    #         for f in lower_Pmin_Uu: 
    #             model.u[f[0]+1,f[1]+1].domain = UnitInterval ## Soft-fixing
    #         for f in lower_Pmin_Uu:      
    #             expr += model.u[f[0]+1,f[1]+1]               ## New constraint soft.                        
    #     model.cuts.add(expr >= n_subset)                     ## Adding a new restriction.  
    #     #print('Soft: number of variables Uu that could be outside  the n_subset (',100-percent_lbc,'%): ', len(SB_Uu)-n_subset)

    # if(option == 'Soft3'):   
    #     print('Soft3 -estoy fijando a <0>: No_SB_Uu - lower_Pmin_Uu =',len(No_SB_Uu),'-',len(lower_Pmin_Uu))
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)  ## Hard fixing to 0
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].unfix()   ## Unfixing
    
    
    
## --------------------------------- HARD-FIXING U,V,W---------------------------------------------

# HARD-FIXING U,V,W solution and solve the sub-MILP. (deprecared by Uriel)
# if 1 == 0: # or precargado == False
#     t_o = time.time() 
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,pc_0,mpc,Pb,C,Cs,Tunder,option='harduvwdel',SB_Uu=SB_Uu,fixed_V=fixed_V,fixed_W=fixed_W,fixed_delta=[],nameins=instancia[0:4])
#     sol_harduvw = Solution(model=model, env=ambiente, executable=executable, nameins=instancia[0:4], gap=gap, timelimit=timelimit,
#                              tee=False, tofiles=False)
#     z_harduvw = sol_harduvw.solve_problem()
#     t_harduvw = time.time() - t_o + t_lp
#     print("t_hardUVW = ",round(t_harduvw,1),"z_hardUVW = ",round(z_harduvw,1))


## --------------------------------- HARD-FIXING U,V,W y delta---------------------------------------------

# HARD-FIXING U,V,W y delta solution and solve the sub-MILP. (deprecared by Uriel)
# if 1 == 0: # or precargado == False
#     t_o = time.time() 
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,pc_0,mpc,Pb,C,Cs,Tunder,option='harduvwdel',SB_Uu=SB_Uu,fixed_V=fixed_V,fixed_W=fixed_W,fixed_delta=fixed_delta,nameins=instancia[0:4])
#     sol_harduvwdel = Solution(model=model, env=ambiente, executable=executable, nameins=instancia[0:4], gap=gap, timelimit=timelimit,
#                                 tee=False, tofiles=False)
#     z_harduvwdel = sol_harduvwdel.solve_problem()
#     t_harduvwdel = time.time() - t_o + t_lp
#     print("t_hardUVWdel = ",round(t_harduvwdel,1),"z_hardUVWdel = ",round(z_harduvwdel,1))

## ----------------------------------- HARD-FIXING 2 (only Uu) ---------------------------------------------
## HARD-FIXING (only Uu) solution and solve the sub-MILP. (Require run the LP and HF1)
## FIX-->No_SB_Uu2, UNFIX-->[No_SB_Uu2,lower_Pmin_Uu2]
# if False: 
#     t_o = time.time() 
#     timehard2 = timeheu
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Hard2',SB_Uu=SB_Uu2,No_SB_Uu=No_SB_Uu2,lower_Pmin_Uu=lower_Pmin_Uu2,nameins=instancia[0:5],mode="Tight")
#     sol_hard2 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,timelimit=timehard2,
#                         tee=False,emphasize=emph,tofiles=False,option='Hard2')
#     z_hard2,g_hard2 = sol_hard2.solve_problem()
#     t_hard2         = time.time() - t_o + t_lp
#     print("t_hard2= ",round(t_hard2,1),"z_hard2= ",round(z_hard2,1),"g_hard2= ",round(g_hard2,5) )


    ## --------------------------- HARD VARIABLE FIXING 2 ----------------------------------------

    # ## Si se desea fijar LR->SB y resolver un sub-MILP.
    # if option == 'Hard2':    
    #     for f in No_SB_Uu: 
    #         model.u[f[0]+1,f[1]+1].fix(0) ## Hard fixing
    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #         model.u[f[0]+1,f[1]+1] = 1
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].unfix() ## Unfixing 



    ## ---------------------------- HARD VARIABLE FIXING (deprecared) ------------------------------------------    
    # ## Si se desea usar la solución fix y calcular un sub-MILP.
    # if(option == 'Hard'):    
    #     for f in SB_Uu: 
    #         model.u[f[0]+1,f[1]+1].fix(1)  ## Hard fixing
    # if(option == 'HardUVWdelta'):   (deprecared)         
    #     for f in SB_Uu: 
    #         model.u[f[0]+1,f[1]+1].fix(1)  ## Hard fixing
    #     for f in fixed_V: 
    #         model.v[f[0]+1,f[1]+1].fix(1)  ## Hard fixing
    #     for f in fixed_W: 
    #          model.w[f[0]+1,f[1]+1].fix(1) ## Hard fixing   
    #     for f in fixed_delta: 
    #          model.delta[f[0],f[1],f[2]].fix(0) ## Hard fixing   
    
        ######################################################################
        ## Con este código corren todas las instancias a factibilidad (menos 52)
        ## Se incrementaba la potencia de t_o de los generadores prendidos 
        ## y los que están abajo del mínimo los pone a cero.    
        ## Es decir, no considera la potencia de arranque.
        # if False: ## (Original que está mal)
        #     aux = power_output_t0[i-1] - power_output_minimum[i-1]
        #     if aux<0:
        #         aux=0
        #     p_0_list.append(aux)
        ######################################################################
        
        
        
    ## ---------------------------- SOFT0 FIXING ------------------------------------------
    
    ## Relajamos la restricción de integralidad de las variables 'Uu' candidatas a '1' en la relajación lineal
    ## y fijamos la solución a cero de las variables fuera del Soporte Binario
    ## Liberamos las variables candidatas por LP 'lower_Pmin_Uu'
    ## Sin ninguna restricción de n_subset=90%   
    # if(option == 'Soft0'):    
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)                ## Hard fixing to '0' those elements outside of Sopport Binary      
    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## We remove the integrality constraint of the Binary Support 
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## Soft-fixing I
    #         model.u[f[0]+1,f[1]+1].unfix()               ## Unfixing


    ## ---------------------------- SOFT4 & SOFT7 FIXING ------------------------------------------
    
    # ## Relajamos la restricción de integralidad de las variables 'Uu' candidatas a '1' en la relajación lineal.
    # ## Hacemos que el 90% de las variables del soporte SB_Uu sigan en el.
    # ## Liberamos las variables candidatas por LP 'lower_Pmin_Uu'
    # if(option == 'Soft4' or option == 'Soft7'):    
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)                ## Hard fixing to '0' those elements outside of Sopport Binary      
    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## We remove the integrality constraint of the Binary Support 
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## Soft-fixing I
    #         model.u[f[0]+1,f[1]+1].unfix()               ## Unfixing
    #     ## Adding a new restriction.  
    #     ## https://pyomo.readthedocs.io/en/stable/working_models.html
    #     ## Soft-fixing II
    #     model.cuts = pyo.ConstraintList()
    #     n_subset   = math.ceil((percent_lbc/100) * (len(SB_Uu))) #-len(lower_Pmin_Uu)
    #     expr       = 0        
    #     ## Se hace n_subset = 90% solo a el Soporte Binario
    #     for f in SB_Uu:      
    #         expr += model.u[f[0]+1,f[1]+1]
    #     model.cuts.add(expr >= n_subset)      


    # ## ---------------------------- SOFT5 FIXING ------------------------------------------
    
    # ## Relajamos la restricción de integralidad de las variables 'Uu' candidatas a '1' en la relajación lineal.
    # ## Hacemos que el 90% de las variables del Soporte  Binario 'SB_Uu' sigan en el.Además de los candidatos 'lower_Pmin_Uu' identificados en la LR
    # ## Por último liberamos las variables candidatas por LP 'lower_Pmin_Uu'
    # if(option == 'Soft5'):    
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)                ## Hard fixing to '0' those elements outside of Sopport Binary      
    #     for f in SB_Uu:           ## SB
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## We remove the integrality constraint of the Binary Support 
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #     for f in lower_Pmin_Uu:   ## B
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## Soft-fixing I
    #         model.u[f[0]+1,f[1]+1].unfix()               ## Unfixing
    #     ## Adding a new restriction.  
    #     ## https://pyomo.readthedocs.io/en/stable/working_models.html
    #     ## Soft-fixing II
    #     model.cuts = pyo.ConstraintList()
    #     n_subset   = math.ceil((percent_lbc/100) * len(SB_Uu))
    #     expr       = 0        
    #     ## Se hace n_subset=90% al Soporte Binario 'SB_Uu' y a Candidatos 'lower_Pmin_Uu' identificados en LR
    #     for f in SB_Uu:           ##SB
    #         expr += model.u[f[0]+1,f[1]+1]
    #     for f in lower_Pmin_Uu:   ##B
    #         expr += model.u[f[0]+1,f[1]+1]      
    #     model.cuts.add(expr >= n_subset)        
                        
    # ## ---------------------------- PURE-SOFT FIXING ------------------------------------------
    
    # ## Relajamos la restricción de integralidad de las variables 'Uu' candidatas a '1' en la relajación lineal
    # ## y fijamos la solución a cero de las variables fuera del Soporte Binario
    # ## Liberamos las variables candidatas por LP 'lower_Pmin_Uu'
    # if(option == 'Softp'):    
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)                ## Hard fixing to '0' those elements outside of Sopport Binary      
    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## We remove the integrality constraint of the Binary Support 
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## Soft-fixing I
    #         model.u[f[0]+1,f[1]+1].unfix()               ## Unfixing
    #     ## Adding a new restriction.  
    #     ## https://pyomo.readthedocs.io/en/stable/working_models.html
    #     ## Soft-fixing II
    #     model.cuts = pyo.ConstraintList()
    #     n_subset   = math.ceil((percent_lbc/100) * (len(SB_Uu))) #-len(lower_Pmin_Uu)
    #     expr       = 0        
    #     ## Se hace n_subset=90% solo a el - Soporte Binario -  
    #     for f in SB_Uu:      
    #         expr += model.u[f[0]+1,f[1]+1]
    #     model.cuts.add(expr >= n_subset)      

    ## ---------------------------- LOCAL BRANCHING CONSTRAINT LBC 0------------------------------------------
    
    # ## Define a neighbourhood with LBC0.
    # if(option == 'lbc0'):   
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)                ## Hard fixing to '0' those elements outside of Sopport Binary      
    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## We remove the integrality constraint of the Binary Support 
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].domain = UnitInterval ## Soft-fixing I
    #         model.u[f[0]+1,f[1]+1].unfix()               ## Unfixing
    #     ## Adding a new restriction.  
    #     ## https://pyomo.readthedocs.io/en/stable/working_models.html
    #     ## Soft-fixing II
    #     model.cuts = pyo.ConstraintList()
    #     n_subset   = math.ceil((percent_lbc/100) * (len(SB_Uu))) #-len(lower_Pmin_Uu)
    #     expr       = 0        
    #     ## Se hace n_subset=90% solo a el - Soporte Binario -  
    #     for f in SB_Uu:      
    #         expr += model.u[f[0]+1,f[1]+1]
    #     model.cuts.add(expr >= n_subset)                                         
    #     #print('LBC: number of variables Uu that may be into the n_subset (',percent_lbc,'%): ', n_subset)
    #     outside90 = len(SB_Uu)-n_subset
    #     print(option+' number of variables Uu that may be outside of Binary Support (',100-percent_lbc,'%): ',outside90 )
        
    #     ## Local Branching Cut
    #     expr = 0        
    #     for f in SB_Uu:                         ## Cuenta los cambios de 1 --> 0  
    #         expr += 1 - model.u[f[0]+1,f[1]+1] 
    #     for f in lower_Pmin_Uu:                 ## Cuenta los cambios de 0 --> 1
    #         expr +=     model.u[f[0]+1,f[1]+1]            
    #     model.cuts.add(expr <= k)               ## Adding a new restrictions (lbc0). 
    
    

    ## ---------------------------- LOCAL BRANCHING CONSTRAINT LBC 2------------------------------------------
    
    ## Define a neighbourhood with LBC2.
    # if(option == 'lbc2'):     
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)       ## Hard fixing to '0' those elements outside of Binary Sopport  
    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].domain = Binary
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #         model.u[f[0]+1,f[1]+1] = 1 
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].domain = Binary 
    #         model.u[f[0]+1,f[1]+1].unfix()      ## Unfixing
    #         model.u[f[0]+1,f[1]+1] = 0            
    #     ## Adding a new restriction.  
    #     ## https://pyomo.readthedocs.io/en/stable/working_models.html
    #     ## Soft-fixing II
    #     model.cuts = pyo.ConstraintList()
    #     n_subset   = math.ceil((percent_lbc/100) * (len(SB_Uu))) #-len(lower_Pmin_Uu)
    #     expr       = 0        
    #     ## Se hace n_subset=90% solo a el - Soporte Binario -  
    #     for f in SB_Uu:      
    #         expr += model.u[f[0]+1,f[1]+1]
    #     model.cuts.add(expr >= n_subset)                                         
    #     #print('LBC: number of variables Uu that may be into the n_subset (',percent_lbc,'%): ', n_subset)
    #     outside90 = len(SB_Uu)-n_subset
    #     print(option+' number of variables Uu that may be outside of Binary Support (',100-percent_lbc,'%): ',outside90 )
        
    #     ## Local branching constraint
    #     expr = 0        
    #     for f in SB_Uu:                         ## Cuenta los cambios de 1 --> 0  
    #         expr += 1 - model.u[f[0]+1,f[1]+1] 
    #     for f in lower_Pmin_Uu:                 ## Cuenta los cambios de 0 --> 1
    #         expr +=     model.u[f[0]+1,f[1]+1]            
    #     model.cuts.add(expr <= k)               ## Adding a new restrictions (lbc0).
        
                
        
    ## ---------------------------- LOCAL BRANCHING CONSTRAINT LBC 8------------------------------------------
    
    ## Define a neighbourhood with LBC8.
    # if(option == 'lbc8'):   
    #     for f in No_SB_Uu:
    #         model.u[f[0]+1,f[1]+1].fix(0)          ## Hard fixing to '0' those elements outside of Sopport Binary      
    #     for f in SB_Uu:  
    #         model.u[f[0]+1,f[1]+1].domain = Binary 
    #         model.u[f[0]+1,f[1]+1].unfix() 
    #     for f in lower_Pmin_Uu:
    #         model.u[f[0]+1,f[1]+1].domain = Binary 
    #         model.u[f[0]+1,f[1]+1].unfix()         ## Unfixing
    #     ## Adding a new restriction.  
    #     ## https://pyomo.readthedocs.io/en/stable/working_models.html
    #     ## Soft-fixing II
    #     model.cuts = pyo.ConstraintList()
    #     n_subset   = math.ceil((percent_lbc/100) * (len(SB_Uu))) #-len(lower_Pmin_Uu)
    #     expr       = 0        
    #     ## Se hace n_subset=90% solo a el - Soporte Binario -  
    #     for f in SB_Uu:      
    #         expr += model.u[f[0]+1,f[1]+1]
    #     model.cuts.add(expr >= n_subset)                                         
    #     #print('LBC: number of variables Uu that may be into the n_subset (',percent_lbc,'%): ', n_subset)
    #     outside90 = len(SB_Uu)-n_subset
    #     print(option+' number of variables Uu that may be outside of Binary Support (',100-percent_lbc,'%): ',outside90 )
        
    #     ## Local Branching Cut
    #     expr = 0        
    #     for f in SB_Uu:                         ## Cuenta los cambios de 1 --> 0  
    #         expr += 1 - model.u[f[0]+1,f[1]+1] 
    #     for f in lower_Pmin_Uu:                 ## Cuenta los cambios de 0 --> 1
    #         expr +=     model.u[f[0]+1,f[1]+1]            
    #     model.cuts.add(expr <= k)               ## Adding a new restrictions (lbc8). 
    
    ## --------------------------------------- LOCAL BRANCHING 2 ------------------------------------------
## LBC INTEGER VERSION OF Uu without soft-fixing
## Include the LOCAL BRANCHING CUT to the solution and solve the sub-MILP (it is using cutoff=z_hard).
# if False:
#     SB_Uu3 = SB_Uu2.copy()
#     No_SB_Uu3 = No_SB_Uu2.copy()
#     lower_Pmin_Uu3 = lower_Pmin_Uu2.copy()
#     for iter in range(10):
#         t_o = time.time() 
#         model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='lbc2',SB_Uu=SB_Uu3,No_SB_Uu=No_SB_Uu3,lower_Pmin_Uu=lower_Pmin_Uu3,nameins=instancia[0:5],mode="Tight")
#         sol_lbc2 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,cutoff=z_hard,timelimit=timeheu,
#                             tee=False,emphasize=emph,tofiles=False,option='lbc2')
#         z_lbc2,g_lbc2 = sol_lbc2.solve_problem()
#         t_lbc2         = time.time() - t_o + t_hard ## t_hard ya incluye el tiempo de lp
#         print("iter:"+str(iter)+" t_lbc2= ",round(t_lbc2,1),"z_lbc2= ",round(z_lbc2,1),"g_lbc2= ",round(g_lbc2,5) )
        
#         sol_lbc2.cuenta_ceros_a_unos(SB_Uu3, No_SB_Uu3, lower_Pmin_Uu3,'lbc2')
#         SB_Uu3, No_SB_Uu3, xx = sol_hard.select_binary_support_Uu('')    
#         lower_Pmin_Uu3 = sol_lbc2.update_lower_Pmin_Uu(lower_Pmin_Uu3,'lbc2')
        
                    
# ## --------------------------------------- LOCAL BRANCHING 8 ------------------------------------------
# ## Include the LOCAL BRANCHING CUT to the solution and solve the sub-MILP (it is using cutoff=z_hard).
# ## Binary 'Uu'
# if False:
#     SB_Uu3 = SB_Uu2.copy()
#     No_SB_Uu3 = No_SB_Uu2.copy()
#     lower_Pmin_Uu3 = lower_Pmin_Uu2.copy()   
#     t_o = time.time() 
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='lbc8',SB_Uu=SB_Uu3,No_SB_Uu=No_SB_Uu3,lower_Pmin_Uu=lower_Pmin_Uu3,nameins=instancia[0:5],mode="Tight")
#     sol_lbc8 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,cutoff=z_hard,timelimit=timeheu,
#                         tee=False,emphasize=emph,tofiles=False,option='lbc8')
#     z_lbc8,g_lbc8 = sol_lbc8.solve_problem()
#     t_lbc8         = time.time() - t_o + t_hard ## t_hard ya incluye el tiempo de lp
#     print("t_lbc8= ",round(t_lbc8,1),"z_lbc8= ",round(z_lbc8,1),"g_lbc8= ",round(g_lbc8,5) )
    
#     sol_lbc8.update_lower_Pmin_Uu(lower_Pmin_Uu2,'lbc8')
#     sol_lbc8.cuenta_ceros_a_unos(SB_Uu2, No_SB_Uu2, lower_Pmin_Uu2,'lbc8')

## --------------------------------------- LOCAL BRANCHING 0 ------------------------------------------
## Include the LOCAL BRANCHING CUT to the solution and solve the sub-MILP (it is using cutoff=z_hard).
## UnitInterval 'Uu'
## The first iteration of LB 
# if False:
#     SB_Uu3 = SB_Uu2.copy()
#     No_SB_Uu3 = No_SB_Uu2.copy()
#     lower_Pmin_Uu3 = lower_Pmin_Uu2.copy()   
#     t_o = time.time() 
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='lbc0',SB_Uu=SB_Uu3,No_SB_Uu=No_SB_Uu3,lower_Pmin_Uu=lower_Pmin_Uu3,nameins=instancia[0:5],mode="Tight")
#     sol_lbc0 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,cutoff=z_hard,timelimit=timeheu,
#                         tee=False,emphasize=emph,tofiles=False,option='lbc0')
#     z_lbc0,g_lbc0 = sol_lbc0.solve_problem()
#     t_lbc0         = time.time() - t_o + t_hard ## t_hard ya incluye el tiempo de lp
#     print("t_lbc0= ",round(t_lbc0,1),"z_lbc0= ",round(z_lbc0,1),"g_lbc0= ",round(g_lbc0,5) )
    
#     sol_lbc0.update_lower_Pmin_Uu(lower_Pmin_Uu2,'lbc0')
#     sol_lbc0.cuenta_ceros_a_unos(SB_Uu2, No_SB_Uu2, lower_Pmin_Uu2,'lbc0')



## --------------------------------- ADICIONALES -------------------------------------------
    ## Compare two solutions 
    # sol_milp.compare(sol_milp2)
    # sol_milp2.send_to_File(letra="a")
            
    
## --------------------------------- SOFT0-FIXING (only Uu) + CUT --------------------------------------------
## SOFT0-FIXING (only Uu) solution and solve the sub-MILP.
## Sin ninguna restricción de del 90%.
# if 1 == 0:
#     t_o = time.time() 
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Soft0',SB_Uu=SB_Uu3,No_SB_Uu=No_SB_Uu3,lower_Pmin_Uu=lower_Pmin_Uu3,nameins=instancia[0:5],mode="Tight")
#     sol_soft0 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,cutoff=z_hard,timelimit=timeheu,
#                         tee=False,emphasize=emph,tofiles=False,option='Soft0')
#     z_soft0,g_soft0 = sol_soft0.solve_problem()
#     t_soft0         = time.time() - t_o + t_hard ## t_hard ya incluye el tiempo de lp
#     print("t_soft0= ",round(t_soft0,1),"z_soft0= ",round(z_soft0,1),"g_soft0= ",round(g_soft0,5) )
    
#     lower_Pmin_Uu0  = sol_soft0.update_lower_Pmin_Uu(lower_Pmin_Uu3,'Soft0')
#     sol_soft0.cuenta_ceros_a_unos(SB_Uu3, No_SB_Uu3, lower_Pmin_Uu3,'Soft0')


## --------------------------------- SOFT5-FIXING (only Uu) + CUT ---------------------------------------------
## SOFT5-FIXING (only Uu) solution and solve the sub-MILP.
## Se aplica la restricción de n_subset=90% al Soporte Binario (Titulares) y a Candidatos (la banca) identificados en LR
# if 1 == 0: 
#     t_o = time.time() 
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Soft5',SB_Uu=SB_Uu3,No_SB_Uu=No_SB_Uu3,lower_Pmin_Uu=lower_Pmin_Uu3,nameins=instancia[0:5],mode="Tight")
#     sol_soft5 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,cutoff=z_hard,timelimit=timeheu,
#                         tee=False,emphasize=emph,tofiles=False,option='Soft5')
#     z_soft5,g_soft5 = sol_soft5.solve_problem()
#     t_soft5         = time.time() - t_o + t_hard ## t_hard ya incluye el tiempo de lp
#     print("t_soft5= ",round(t_soft5,1),"z_soft5= ",round(z_soft5,1),"g_soft5= ",round(g_soft5,5) )
    
#     lower_Pmin_Uu0  = sol_soft5.update_lower_Pmin_Uu(lower_Pmin_Uu3,'Soft5')
#     sol_soft5.cuenta_ceros_a_unos(SB_Uu3, No_SB_Uu3, lower_Pmin_Uu3,'Soft5')
    
#     bb3,vari = Extract().extract('logfile'+'Soft5'+instancia[0:5]+'.log',t_hard=t_hard)

    
## ---------------------------------------- MILP2 with Inequality ------------------------------------------------
## Solve the MILP2 with valid inequality 
# if 1 == 0: 
#     t_o = time.time() 
#     model,xx  = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Milp2',nameins=instancia[0:5],mode="Tight")
#     sol_milp2 = Solution(model=model,nameins=instancia[0:5],env=ambiente,executable=executable,gap=gap,timelimit=timemilp,
#                            tee=False,tofiles=False,emphasize=emph,exportLP=False,option='Milp2')
#     z_milp2,g_milp2 = sol_milp2.solve_problem()
#     t_milp2         = time.time() - t_o
#     print("t_milp2= ",round(t_milp2,1),"z_milp2= ",round(z_milp2,1),"g_milp2= ",round(g_milp2,5)) #"total_costo_arr=",model.total_cSU.value



## ---------------------------------- PURE SOFT-FIXING (only Uu) -----------------------------------------
## SOFTP-FIXING (only Uu) solution and solve the sub-MILP without cut-off and Binary support calculated by Hard-Fix
## Sin cut-off del HF
## Usa el LR->BS y LR->B 
# if 1 == 0:
#     t_o = time.time() 
#     model,xx  = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Softp',SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,nameins=instancia[0:5],mode="Tight")
#     sol_softp = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,timelimit=timeheu,
#                         tee=False,emphasize=emph,tofiles=False,option='Softp')
#     z_softp,g_softp = sol_softp.solve_problem()
#     t_softp         = time.time() - t_o + t_lp
#     print("t_softp= ",round(t_softp,1),"z_softp= ",round(z_softp,1),"g_softp= ",round(g_softp,5))    
#     #sol_softp.update_lower_Pmin_Uu(lower_Pmin_Uu3,'Softp')
#     sol_softp.cuenta_ceros_a_unos(SB_Uu3, No_SB_Uu3,lower_Pmin_Uu3,'Softp')


## ------------------------------- SOFT4-FIXING (only Uu) + CUT ------------------------------------------
## SOFT4-FIXING (only Uu) solution and solve the sub-MILP.
## Se aplica la restricción de n_subset=90% al Soporte Binario (Titulares)
# if 1 == 0:
#     t_o = time.time() 
#     model,xx  = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Soft4',SB_Uu=SB_Uu3,No_SB_Uu=No_SB_Uu3,lower_Pmin_Uu=lower_Pmin_Uu3,nameins=instancia[0:5],mode="Tight")
#     sol_soft4 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,cutoff=z_hard,timelimit=timeheu,
#                         tee=False,emphasize=emph,tofiles=False,option='Soft4')
#     z_soft4,g_soft4 = sol_soft4.solve_problem()
#     t_soft4         = time.time() - t_o + t_hard ## t_hard ya incluye el tiempo de lp
#     print("t_soft4= ",round(t_soft4,1),"z_soft4= ",round(z_soft4,1),"g_soft4= ",round(g_soft4,5) )
    
#     #sol_soft4.update_lower_Pmin_Uu(lower_Pmin_Uu3,'Soft4')
#     sol_soft4.cuenta_ceros_a_unos(SB_Uu3, No_SB_Uu3, lower_Pmin_Uu3,'Soft4')

    
## -------------------------------- SOFT7-FIXING (only Uu) ---------------------------------------------
## SOFT7-FIXING (only Uu) solution and solve the sub-MILP.
## Se aplica la restricción de n_subset=90% al Soporte Binario obtenido por el Hard Fixing
## Sin cut-off del HF
# if 1 == 0:
#     t_o = time.time() 
#     model,xx  = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Soft7',SB_Uu=SB_Uu3,No_SB_Uu=No_SB_Uu3,lower_Pmin_Uu=lower_Pmin_Uu3,nameins=instancia[0:5],mode="Tight")
#     sol_soft7 = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,timelimit=timeheu,
#                         tee=False,emphasize=emph,tofiles=False,option='Soft7')
#     z_soft7,g_soft7 = sol_soft7.solve_problem()
#     t_soft7         = time.time() - t_o + t_hard ## t_hard ya incluye el tiempo de lp
#     print("t_soft7= ",round(t_soft7,1),"z_soft7= ",round(z_soft7,1),"g_soft7= ",round(g_soft7,5) )
    
#     #sol_soft7.update_lower_Pmin_Uu(lower_Pmin_Uu,'Soft7')
#     sol_soft7.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Soft7')


 # KS (EN DESARROLLO)
# if False:
#     SB_Uu = SB_Uu3.copy()                 ## ESTE SERÁ EL KERNEL
#     No_SB_Uu = No_SB_Uu3.copy()
#     lower_Pmin_Uu = lower_Pmin_Uu3.copy() ## ESTE LO DIVIDIREMOS EN BUCKETS
#     t_o = time.time()    
#     iter  = 0
#     escape  = 1
#     result_iter   = []
#     result_iter.append((t_hard,z_hard)) 
#     result_iter = []
#     cutoff=z_hard
#     while 1==1:
#         model,xx    = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='KS',
#                                SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,nameins=instancia[0:5],mode="Tight")
#         sol_ks = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,cutoff=cutoff,timelimit=timeheu,
#                             tee=False,emphasize=emph,tofiles=False)
#         z_ks,g_ks = sol_ks.solve_problem()    
#         cutoff         = z_ks
#         result_iter.append((round(time.time()-t_o,1),z_ks)) 
#         print("iter:"+str(iter)+" t_ks= ",round(time.time()-t_o+t_hard,1),"z_ks= ",round(z_ks,1),"g_ks= ",round(g_ks,5) )
        
#         escape = sol_ks.cuenta_ceros_a_unos(SB_Uu, No_SB_Uu, lower_Pmin_Uu,'ks')
#         SB_Uu, No_SB_Uu, xx = sol_lbc1.select_binary_support_Uu('ks')    
#         result_iter.append((round(time.time()-t_o+t_hard,1),z_lbc1)) 
#         char = ''
#         if z_lbc1 <= incumbent:
#             incumbent = z_lbc1
#             cutoff    = z_lbc1
#             savedsol  = [SB_Uu,No_SB_Uu,lower_Pmin_Uu]
#             char = '**'
#         if escape == 0:
#             print(' + * + * + * + Escapando de un óptimo local ...')
#             rightbranches.append([SB_Uu,No_SB_Uu,lower_Pmin_Uu])
            
#         iter = iter + 1
        
#     t_ks = time.time() - t_o + t_hard ## t_hard (ya incluye el tiempo de LP)
#     print("t_ks= ", round(t_ks,4), "z_ks= ", round(z_ks,1), "n_SB_Uu= ", len(SB_Uu))

 
## ----------------------------------- HARD-FIXING (only Uu) ---------------------------------------------
## HARD-FIXING (only Uu) solution and solve the sub-MILP. (Require run the LP)

# if False: 
#     t_o      = time.time()
#     lbheur   = 'yes'
#     model,xx = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='Hard',
#                         SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,nameins=instancia[0:5],mode='Tight')
#     sol_hard = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],gap=gap,timelimit=timeheu,
#                         tee=False,emphasize=emph,lbheur=lbheur,symmetry=symmetry,tofiles=False,option='Hard')
#     z_hard,g_hard = sol_hard.solve_problem()
#     t_hard                 = time.time() - t_o + t_lp
#     print('t_hard= ',round(t_hard,1),'z_hard= ',round(z_hard,1),'g_hard= ',round(g_hard,5) )
    
#     ## ES MUY IMPORTANTE GUARDAR LAS VARIABLES 'Uu=1'(SB_Uu3) DE LA PRIMERA SOLUCIÓN FACTIBLE 'Hard'.
#     ## ASI COMO LAS VARIABLES 'Uu=0' (No_SB_Uu3) 
#     ## Este es el primer - Soporte Binario Entero Factible-
#     SB_Uu3, No_SB_Uu3, xx, Vv, Ww, delta = sol_hard.select_binary_support_Uu('')    
#     lower_Pmin_Uu3 = sol_hard.update_lower_Pmin_Uu(lower_Pmin_Uu,'Hard')
#     sol_hard.cuenta_ceros_a_unos( SB_Uu, No_SB_Uu, lower_Pmin_Uu,'Hard')

# def resultados_lp_milp(instance,ambiente,gap,timelimit):
    
#     z_milp = 0; z_hard = 0; t_milp = 0; t_hard = 0; precargado = False
#     df = pd.read_csv('resultados_previos.csv')
#     df = df.loc[(df['instancia'] == instance) & (df['ambiente'] == ambiente) & (df['gap'] == gap) & (df['timelimit'] == timelimit)]
    
#     if len(df.index) != 0:
#         z_milp = df['z_milp'].values[0]
#         z_hard = df['z_hard'].values[0]
#         t_milp = df['t_milp'].values[0]
#         t_hard = df['t_hard'].values[0]
#         precargado = True
#         print('Resultados de <milp> y <hard-fixing> pre-cargados y asignados.')
         
#     return precargado, z_milp, z_hard, t_milp, t_hard



## ---------------------------------  ITERATIVE  VARIABLE  FIXING  --------------------------------------
## La versión básica de IVF consiste en relajar la formulacion y a partir de ello sacar 
## el soporte binario SB_Uu y una lista de candidatos lower_Pmin_Uu, después de manera iterativa se resulven los 
## SUB-MILP´S 'restringidos' mas pequeños usando el paradigna de KS.
## IVF solution and solve the sub-MILP (it is using cutoff = z_hard).
## Use 'Soft+pmin' (lower subset of Uu-Pmin)  as the first and unique bucket to consider
## Use relax the integrality variable Uu.

# if True:
#     Vv             = deepcopy(Vv3)
#     Ww             = deepcopy(Ww3)
#     delta          = deepcopy(delta3)
#     SB_Uu          = deepcopy(SB_Uu3)
#     No_SB_Uu       = deepcopy(No_SB_Uu3)
#     lower_Pmin_Uu  = deepcopy(lower_Pmin_Uu3)
#     saved          = [SB_Uu,No_SB_Uu,Vv,Ww,delta]

#     t_o         = time.time() 
#     incumbent   =  z_hard3
#     cutoff      =  z_hard3 # 1e+75 
#     iter        =  0  
#     sol_ivf     =  []
#     result_iter =  []
#     result_iter.append((t_hard3 + time.time() - t_o, z_hard3))

#     while True:
        
#         t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
#         if t_res <= 0:
#             break

#         t_1 = time.time()
#         model,__  = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='LR',
#                              SB_Uu=saved[0],No_SB_Uu=saved[1],V=saved[2],W=saved[3],delta=saved[4],nameins=instancia[0:5],mode='Tight')
#         sol_rc    = Solution(model=model,nameins=instancia[0:5],env=ambiente,executable=executable,gap=gap,timelimit=timemilp,
#                              tee=False,tofiles=False,emphasize=emph,symmetry=symmetry,exportLP=False,option='RC')
#         z_rc,g_rc = sol_rc.solve_problem() 
#         t_rc      = time.time() - t_1
#         print('t_rc= ',round(t_rc,1),'z_rc= ',round(z_rc,4))      
                    
#         ## ------------------------------------ Selection variables to fix ---------------------------------------
#         ## lower_Pmin_Uu  >>> Este valor podría ser usado para definir el parámetro k en el LBC o buckets en un KS <<<  
#         SB_Uu, No_SB_Uu, lower_Pmin_Uu, Vv, Ww, delta = sol_rc.select_binary_support_Uu('LR')
        
#         del sol_rc
#         gc.collect()
        
#         if len(lower_Pmin_Uu) == 0:
#             break
           
#         char  = ''
#         t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
#         if t_res <= 0:
#             break

#         timeheu1  = min(t_res,timeheu)    
                
#         try:
#         ##  Resolvemos el MILP con SB_Uu=1 (hints) y lower_Pmin_Uu=0 (no fijas) y con No_SB_Uu=0 (fijas)
#             lbheur       = 'yes'
#             emph         = 1     ## feasiability
#             model,__     = uc_Co.uc(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,mpc,Pb,Cb,C,Cs,Tunder,names,option='IVF',
#                                         SB_Uu=SB_Uu,No_SB_Uu=No_SB_Uu,lower_Pmin_Uu=lower_Pmin_Uu,nameins=instancia[0:5],mode='Tight')
#             sol_ivf      = Solution(model=model,env=ambiente,executable=executable,nameins=instancia[0:5],letter=util.getLetter(iter),gap=gap,cutoff=cutoff,timelimit=timeheu1,
#                                         tee=False,emphasize=emph,lbheur=lbheur,symmetry=symmetry,tofiles=False,option='IVF')
#             z_ivf, g_ivf = sol_ivf.solve_problem()
#             t_ivf        = time.time() - t_o + t_hard3
#             SB_Uu, No_SB_Uu, __, Vv, Ww, delta = sol_ivf.select_binary_support_Uu('IVF') 
                        
#             if z_ivf < incumbent :                      ## Update solution
#                 incumbent  = z_ivf
#                 cutoff     = z_ivf
#                 saved      = [SB_Uu,No_SB_Uu,Vv,Ww,delta]
#                 g_ivf      = util.igap(z_lp,z_ivf)
#                 char       = '***'
                        
#             result_iter.append((round(time.time()-t_o+t_hard3,1), z_ivf))
#             print('<°|>< iter:'+str(iter)+' t_ivf= ',round(time.time()-t_o+t_hard3,1),'z_ivf= ',round(z_ivf,1),char) #,'g_ivf= ',round(g_ivf,5)
#         except:
#             print('>>> Iteración sin solución')
#             result_iter.append((round(time.time()-t_o+t_hard3,1), 1e+75))
                    
#         print('\t')       
                    
#         t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
#         print('ivf ','tiempo restante:',t_res)

#         iter = iter + 1
                
#     t_ivf = (time.time() - t_o) + t_hard3  ## t_hard3 ya incluye el tiempo de LP
#     z_ivf = incumbent    
#     for item in result_iter:
#         print(item[0],',',item[1])
#     result_iter = np.array(result_iter)
#     np.savetxt('iterIVF'+instancia[0:5]+'.csv', result_iter, delimiter=',')
        
#     checkSol('z_ivf',z_ivf) ## Check feasibility (IVF)
             
             
                    
# # (EN PROCESO ...)
# def validation(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,TD_0,SU,SD,RU,RD,p_0,Pb,Cb,C,mpc,Cs,Tunder,names,abajo_min): 
        
#     print('>>> generadores abajo del límite mínimo:',abajo_min)  
       
#     print('*** Capacidades totales de los generadores en el tiempo cero ***')
#     gen0=0
#     for i in p_0:
#         gen0 = p_0[i] + gen0 
#     print('potencia p_0            =',gen0)
#     maxi=0
#     for i in Pmax:
#         if u_0[i]==1:
#           maxi = Pmax[i] + maxi
#     maxi = maxi - gen0
#     print('capacidad subir gen_0   =',maxi)    
#     mini=0
#     for i in Pmin:
#         if u_0[i]==1:
#           mini = Pmin[i] + mini
#     mini = gen0 - mini
#     print('capacidad bajar gen_0   =',mini)
     
#     rampUp=0
#     for i in RU:
#         if u_0[i]==1:
#           rampUp = util.trunc(RU[i] + rampUp,1)
#     print('rampUp_0                =',rampUp)    
#     rampDown=0
#     for i in RD:
#         if u_0[i]==1:
#           rampDown = util.trunc(RD[i] + rampDown,1)
#     print('rampDown_0              =',rampDown)
#     startUp=0
#     for i in SU:
#         if u_0[i]==0:
#           startUp = SU[i] + startUp
#     print('startUp_0               =',startUp)
#     shutDown=0
#     for i in SD:
#         if u_0[i]==1:
#           shutDown = SD[i] + shutDown
#     print('shutDown_0              =',shutDown)    
        
#     print('Delta demanda  De_0     =',De[1]-gen0)
#     print('Reserve  R_0            =',R[1])    
    
#     lista1 = []
#     for i in range(2,len(De)):
#         lista1.append(De[i-1]-De[i])
#     print('máx demanda subida      =',abs(util.trunc(min(lista1),1)) )
#     print('máx demanda bajada      =',abs(util.trunc(max(lista1),1) ))
        
#     lista2 = []
#     for i in range(2,len(R)):
#         lista2.append(R[i-1]-R[i])
#     print('máx reserva subida      =',util.trunc(max(lista2),1) )
#     print('máx reserva bajada      =',util.trunc(min(lista2),1) )
    
#     #print(gen0,maxi,mini,startUp,shutDown,rampUp,rampDown,De[1],R[1],
#           #util.trunc(max(lista1)),util.trunc(min(lista1)),util.trunc(max(lista2)),util.trunc(min(lista2)))
        
#     return 0

# # (EN PROCESO ...)
# def to_dirdat(G,T,L,S,Pmax,Pmin,TU,TD,De,R,u_0,U,D,SU,SD,RU,RD,p_0,Pb,C,mpc,Cs,Tunder,names):    
#     print('Exporting instance data to dirdat csv files...')
    
# ## Deleting an non-empty folder dirdat
#     shutil.rmtree('dirdat', ignore_errors=True)
#     os.mkdir('dirdat')    
# ##  Escribiendo HORIZOMDA.csv
#     data = {'periodos': [len(T)],'duracion': [60],'bandera': [0],'dias': [1]}
#     df = pd.DataFrame(data)
#     df.to_csv('dirdat/HORIZOMDA.csv',header=False, index=False)
    
# ##  Escribiendo PRODEM.csv
#     index = list(range(len(De)))
#     my_list = list(De.values())
#     df = pd.DataFrame(columns = index)  
#     df_length = len(df)
#     df.loc[df_length] = my_list
#     df.to_csv('dirdat/PRODEM.csv',header=False, index=False)
    
# ##  Escribiendo RRESUS.csv
#     index = list(range(len(R)))
#     my_list = list(R.values())
#     df = pd.DataFrame(columns = index)  
#     df_length = len(df)
#     df.loc[df_length] = my_list
#     df.to_csv('dirdat/RRESUS.csv',header=False, index=False)

# ##  Escribiendo UNITRC.csv
# ##  Escribiendo ASIGNRC.csv
# ##  Escribiendo LIUNITRC.csv
# ##  Escribiendo LSUNITRC.csv
# ##  Escribiendo RAMPASRC.csv
# ##  Escribiendo ARRARC.csv
# ##  Escribiendo OPPARORC.csv
# ##  Escribiendo UNITRCCI.csv
# ##  Escribiendo CGMRC.csv
# ##  Escribiendo COVAARRC.csv
# ##  Escribiendo POTVERC.csv
# ##  Escribiendo PREVERC.csv
# ##  Escribiendo UNIHMDA.csv



    
## ---------------------------------  REDUCED KERNEL SEARCH --------------------------------------
## 
## La versión básica de RKS consiste en relajar la formulacion fijando el soporte binario y a partir de ello sacar 
## el kernel SB_Uu y un conjunto de buckets a partir de lower_Pmin_Uu, después de manera 
## iterativa se resuelven los SUB-MILP´S 'restringidos' mas pequeños. Este proceso se repite hasta terminar el tiempo.
## RKS solution and solve the sub-MILP (it is using cutoff = z_hard).
## Use 'Soft+pmin' (lower subset of Uu-Pmin) as the first and unique bucket to consider

# if  False:
#     Vv          = deepcopy(Vv3)
#     Ww          = deepcopy(Ww3)
#     delta       = deepcopy(delta3)
#     SB_Uu       = deepcopy(SB_Uu3)
#     No_SB_Uu    = deepcopy(No_SB_Uu3)
#     saved       = [SB_Uu,No_SB_Uu,Vv,Ww,delta]

#     t_o         = time.time() 
#     incumbent   =  z_hard3
#     cutoff      =  z_hard3 # 1e+75 
#     iter        =  0  
#     sol_rks     =  []
#     result_iter =  []
#     result_iter.append((t_hard3 + time.time() - t_o, z_hard3))

#     while True:
#         ## --------------------------------------- CALCULATE REDUCED COSTS Uu ------------------------------------
#         t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
#         if t_res <= 0:
#             print('RKS Salí ciclo externo')
#             break
        
#         if  True:
#             t_1 = time.time()
#             model,__  = uc_Co.uc(instance,option='RC',
#                                 SB_Uu=saved[0],No_SB_Uu=saved[1],V=saved[2],W=saved[3],delta=saved[4],nameins=nameins[0:5],mode='Tight',scope=scope)
#             sol_rc    = Solution(model=model,nameins=nameins[0:5],env=ambiente,executable=executable,gap=gap,timelimit=timemilp,
#                                 tee=False,tofiles=False,emphasize=emph,symmetry=symmetry,exportLP=False,option='RC')
#             z_rc,g_rc = sol_rc.solve_problem() 
#             t_rc      = time.time() - t_1
#             print('RKS t_rc= ',round(t_rc,1),'z_rc= ',round(z_rc,4))      
            
#             ## ----------------------------- SECOND PHASE ----------------------------------------------
#             ##  Defining buckets 
#             rc   = []
#             i    = 0                    
#             for f in No_SB_Uu: 
#                 rc.append(( i, model.rc[model.u[f[0]+1,f[1]+1]],f[0],f[1] ))
#                 i = i + 1    
#             rc.sort(key=lambda tup:tup[1], reverse=False) ## Ordenamos las variables No_SB_Uu de acuerdo a sus costos reducidos 
            
#             ##  Definimos el número de buckets 
#             K = floor(1 + 3.322 * log(len(No_SB_Uu)))  ## Sturges rule
#             print('RKS Number of buckets K =', K)    
#             len_i  = ceil(len(No_SB_Uu) / K)
#             pos_i  = 0
#             k_     = [0]    
#             for i in range(len_i,len(No_SB_Uu),len_i+1):
#                 k_.append( i )
#             k_[-1] = len(No_SB_Uu)
#             print( k_ )
            
#             cutoff      = incumbent # 1e+75 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             iter_bk     = 0
#             iterstop    = 3 #K - 2  #  
#             char        = ''
#             kernel      = deepcopy(SB_Uu)
            
#             ## Recontabilizamos el tiempo
#             t_res   = max(0,( timemilp - t_hard3) - (time.time() - t_o))
#             timeheu = t_res / K
            
#             while True: 
#                 t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
#                 if iter_bk >= iterstop or t_res <= 0:
#                     print('RKS Salí ciclo interno')
#                     break

#                 timeheu1  = min(t_res,timeheu)      
#                 bucket    = rc[k_[iter_bk]:k_[iter_bk + 1]] 
#                 print('bucket',util.getLetter(iter),'[',k_[iter_bk],':',k_[iter_bk + 1],']' )      
                
#                 try:
#                     ##  Resolvemos el kernel con cada uno de los buckets
#                     lbheur     = 'yes'
#                     emph       = 0     ## feasibility =1
#                     model,__   = uc_Co.uc(instance,option='RKS',
#                                           kernel=kernel,bucket=bucket,
#                                           nameins=nameins[0:5],mode='Tight',scope=scope)
#                     sol_rks     = Solution(model=model,env=ambiente,executable=executable,
#                                            nameins=nameins[0:5],letter=util.getLetter(iter),
#                                            gap=gap,cutoff=cutoff,timelimit=timeheu1,
#                                            tee=False,emphasize=emph,lbheur=lbheur,symmetry=symmetry,tofiles=False,option='RKS')
#                     z_rks, g_rks = sol_rks.solve_problem()
#                     t_rks       = time.time() - t_o + t_hard3
#                     kernel, No_SB_Uu, __, Vv, Ww, delta = sol_rks.select_binary_support_Uu('RKS') 
                    
#                     if z_rks < incumbent :                      ## Update solution
#                         incumbent  = z_rks
#                         cutoff     = z_rks
#                         saved      = [kernel,No_SB_Uu,Vv,Ww,delta]
#                         g_rks       = util.igap(z_lp,z_rks)
#                         char       = '***'
                        
#                     result_iter.append((round(time.time()-t_o+t_hard3,1), z_rks))
#                     print('<°|>< iter:'+str(iter)+' t_rks= ',round(time.time()-t_o+t_hard3,1),'z_rks= ',round(z_rks,1),char) #,'g_rks= ',round(g_rks,5)
#                 except:
#                     # print('>>> Iteración sin solución')
#                     result_iter.append((round(time.time()-t_o+t_hard3,1), 1e+75))
#                 finally:    
#                     iter_bk = iter_bk + 1
                    
#                 print('\t')       
                    
#                 t_res = max(0,( timemilp - t_hard3 ) - (time.time() - t_o))
#                 print('RKS ','tiempo restante:',t_res)
                
#                 del sol_rks
#                 gc.collect()
#                 iter = iter + 1
                                
#         Vv       = deepcopy(saved[2])
#         Ww       = deepcopy(saved[3])
#         delta    = deepcopy(saved[4])
#         SB_Uu    = deepcopy(saved[0])
#         No_SB_Uu = deepcopy(saved[1])

#     t_rks = (time.time() - t_o) + t_hard3  
#     z_rks = incumbent    
#     for item in result_iter:
#         print(item[0],',',item[1])
#     result_iter = np.array(result_iter)
#     np.savetxt('iterRKS'+nameins[0:5]+'.csv', result_iter, delimiter=',')
    
#     checkSol('z_rks',z_rks,SB_Uu,No_SB_Uu,Vv,Ww,delta) ## Check feasibility (RKS)
             
           
           
           
    # ## ---------------------------- Inequality related with 'delta' and 'v' ------------------------------------------
    # if option == 'Milp2':
    #     def Start_up_cost_desigualdad_Uriel(m,g):  ##  start-up cost eq.(54)(s < value(len(m.S[g])) and t >= m.Tunder[g,s+1]):
    #         return sum(m.v[g,t] for t in m.T) == sum(m.delta[g,t,s] for s in range(1,value(len(m.S[g]))+1) for t in m.T)  
    #     model.Start_up_cost_desigualdad_Uriel = Constraint(model.G,rule = Start_up_cost_desigualdad_Uriel)
        