## -------------------  >)|°> UriSoft© <°|(<  -------------------
## File: uc_Co.py
## Developers: Uriel Iram Lezama Lope
## Purpose: UC 'Compact' model introduced by Knueven2020b
## Description:
## Objetive               (69)
## Up-time/down-time      (2), (3), (4), (5)       'garver_3bin_vars',
##                                                 'rajan_takriti_UT_DT',
## Generation limits      (17), (20), (21)         'MLR_generation_limits',
##                                                 'garver_power_vars',
##                                                 'garver_power_avail_vars',
## Ramp limits            (35), (36)               'damcikurt_ramping',
## Piecewise production   (50)                     'Hua and Baldick 2017',
## Start-up cost          (54), (55), (56)         'MLR_startup_costs',
## System constraints     (67)
##  
## (Alternative) Piecewise production   (42), (43), (44)         'Garver1962',
## An example: https://pascua.iit.comillas.edu/aramos/openSDUC.py
## <º)))>< ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸ ><(((º>

# import pyomo.environ as pyo
# from   pyomo.environ import *
from  pyomo.environ import Set, ConcreteModel, Param, Var, Objective, minimize, ConstraintList, Constraint, Any, value, UnitInterval, Binary
from  math import floor ,ceil
import threading
      
def uc(instance,option='None',
       kernel=[],bucket=[],SB_Uu=[],No_SB_Uu=[],lower_Pmin_Uu=[],V=[],W=[],delta=[],
       percent_soft=90,k=20,nameins='ml',mode='Tight',improve=True,timeover=False,rightbranches=[]):      
       
    G       = instance[0]
    T       = instance[1]
    L       = instance[2]
    S       = instance[3]
    Pmax    = instance[4]
    Pmin    = instance[5]
    UT      = instance[6] 
    DT      = instance[7] 
    De      = instance[8]
    R       = instance[9]
    u_0     = instance[10]
    U       = instance[11]
    D       = instance[12]
    TD_0    = instance[13]
    SU      = instance[14] 
    SUD     = instance[15]
    PSD     = instance[16]
    SD      = instance[17]
    SDD     = instance[18]
    PSU     = instance[19]
    RU      = instance[20]
    RD      = instance[21]
    p_0     = instance[22]
    Pb      = instance[23]
    Cb      = instance[24]
    C       = instance[25] 
    CR      = instance[26] ## Minimum production cost
    Cs      = instance[27]
    Tunder  = instance[28]
    names   = instance[29]
    LOAD    = instance[30]
    Ld      = instance[31]
    Pd      = instance[32]
    Cd      = instance[33]
    GRO     = instance[34]
    RO      = instance[35]
    ROmin   = instance[36]
    ROmax   = instance[37]
    Crr     = instance[38]
    Cs10    = instance[39]
    Cs30    = instance[40]
    Cns10   = instance[41]
    Cns30   = instance[42]
    RRe     = instance[43]
    RR10    = instance[44]
    RR30    = instance[45]
    RN10    = instance[46]
    RN30    = instance[47]        
    ORDC    = instance[48]
    Cordc   = instance[49]
    RCO     = instance[50] 
    TSg     = instance[51]  
    TDg     = instance[52]
    
    model      = ConcreteModel(nameins)    
    model.G    = Set(          initialize = G)
    model.T    = Set(          initialize = T)  
    model.L    = Set(model.G , initialize = L) 
    model.S    = Set(model.G , initialize = S) 
    
    model.ORDC  = Set(               initialize = ORDC)
    model.LOAD  = Set(               initialize = LOAD)  
    model.Ld    = Set(  model.LOAD , initialize = Ld) ## Set of segments of purchase bid of elastic load
    model.TSg   = Set(  model.G    , initialize = TSg) ## Set of segments of TRAJECTORY STARTUP
    model.TDg   = Set(  model.G    , initialize = TDg) ## Set of segments of TRAJECTORY SHUTDOWN
    model.GRO   = Set(               initialize = GRO) 
    model.RO    = Set(  model.GRO  , initialize = RO)     
    model.Crr   = Param(model.G    , initialize = Crr   , within = Any) #
    model.Cs10  = Param(model.G    , initialize = Cs10  , within = Any) #
    model.Cs30  = Param(model.G    , initialize = Cs30  , within = Any) #
    model.Cns10 = Param(model.G    , initialize = Cns10 , within = Any) #
    model.Cns30 = Param(model.G    , initialize = Cns30 , within = Any) #
    model.RRe   = Param(model.G    , initialize = RRe   , within = Any) #
    model.RR10  = Param(model.G    , initialize = RR10  , within = Any) #
    model.RR30  = Param(model.G    , initialize = RR30  , within = Any) #
    model.RN10  = Param(model.G    , initialize = RN10  , within = Any) #
    model.RN30  = Param(model.G    , initialize = RN30  , within = Any) #
    model.Cordc = Param(model.ORDC , initialize = Cordc , within = Any) #
    model.RCO   = Param(model.ORDC , initialize = RCO   , within = Any) #
    
    model.Pmax  = Param(model.G    , initialize = Pmax  , within = Any)
    model.Pmin  = Param(model.G    , initialize = Pmin  , within = Any)
    model.UT    = Param(model.G    , initialize = UT    , within = Any)
    model.DT    = Param(model.G    , initialize = DT    , within = Any)
    model.De    = Param(model.T    , initialize = De    , within = Any)
    model.R     = Param(model.T    , initialize = R     , within = Any)
    model.u_0   = Param(model.G    , initialize = u_0   , within = Any)
    model.D     = Param(model.G    , initialize = D     , within = Any)
    model.U     = Param(model.G    , initialize = U     , within = Any)
    model.SU    = Param(model.G    , initialize = SU    , within = Any)
    model.SD    = Param(model.G    , initialize = SD    , within = Any)
    
    ## Trayectorias de arranque y apagado
    model.SUD   = Param(model.G    , initialize = SUD    , within = Any) 
    model.SDD   = Param(model.G    , initialize = SDD    , within = Any) 
    
    model.RU    = Param(model.G    , initialize = RU    , within = Any)
    model.RD    = Param(model.G    , initialize = RD    , within = Any)
    model.p_0   = Param(model.G    , initialize = p_0   , within = Any) 
    model.CR    = Param(model.G    , initialize = CR    , within = Any) #cost of generator g running and operating at minimum production

    
    # model.c    = Param(model.G , initialize = {1:5,2:15,3:30}    ,within =Any)
    # model.cU   = Param(model.G , initialize = {1:800,2:500,3:250},within = Any)
    
    inside90 = 0              ## default
    CLP      = 1000.0         ## penalty cost for failing to meet or exceeding load ($/megawatt-hour (MWh)).
    CRP      = 999999999999.0 ## penalty cost for failing to meet reserve requirement
    
    ##  Defined index to compute the per-generator, per-time, and segment period production costs.
    def index_G_T_Lg(m):
        return ((g,t,l) for g in m.G for t in m.T for l in range(1,len(m.L[g])+1))    
    model.indexGTLg = Set(initialize=index_G_T_Lg, dimen=3)     
    
    ##  Defined index to compute the per-generator, and segment period production costs.
    def index_G_Lg(m):
        return ((g,l) for g in m.G for l in range(1,len(m.L[g])+1))     
    model.indexGLg  = Set(initialize=index_G_Lg, dimen=2)    
    
    ##  Defined index to compute the per-generator, per-time, and  start-up segment cost variable.
    def index_G_T_Sg(m):
        return ((g,t,s) for g in m.G for t in m.T for s in range(1,len(m.S[g])+1))        
    model.indexGTSg = Set(initialize=index_G_T_Sg, dimen=3) 
    
    ##  Defined index to compute the per-generator, and start-up segment cost variable.
    def index_G_Sg(m):
        return ((g,s) for g in m.G for s in range(1,len(m.S[g])+1))     
    model.indexGSg  = Set(initialize=index_G_Sg, dimen=2)
    

    ## Prohibid operating zones index
    
    ##  Defined index to compute the per-load, and segment energy purchase.
    def index_LOAD_Ld(m):
        return ((d,i)  for d in m.LOAD                for i in range(1,len(m.Ld[d])+1))
    model.indexLoadLd = Set(initialize=index_LOAD_Ld, dimen=2)
        
    ##  Defined index to compute the per-load, per-time, and segment energy purchase.
    def index_LOAD_T_Ld(m):
        return ((d,t,i) for d in m.LOAD for t in m.T for i in range(1,len(m.Ld[d])+1))
    model.indexLoadTLd = Set(initialize=index_LOAD_T_Ld, dimen=3)        
        
    ##  Defined index to prohibed operative zone (POZ).
    def index_GRO_RO(m):
        return ((g,ro) for g in m.GRO                for ro in m.RO[g])
    model.indexGRO_RO = Set(initialize=index_GRO_RO, dimen=2)        
        
    def indexGRO_T_RO(m):
        return ((g,t,ro) for g in m.GRO for t in m.T for ro in m.RO[g])
    model.indexGRO_T_RO = Set(initialize=indexGRO_T_RO, dimen=3)
        
    def index_GRO_T(m):
        return ((g,t) for g in m.GRO                 for t in m.T)
    model.indexGRO_T = Set(initialize=index_GRO_T, dimen=2)     
                    
    ##  Defined index to compute the per-generator, and segments of TRAJECTORY START-UP.
    def index_G_TSg(m):
        return ((g,tr) for g in m.G for tr in range(1,len(m.TSg[g])+1))     
    model.index_G_TSg  = Set(initialize=index_G_TSg, dimen=2) 
      
    ##  Defined index to compute the per-generator, and segments of TRAJECTORY SHUT-DOWN.
    def index_G_TDg(m):
        return ((g,tr) for g in m.G for tr in range(1,len(m.TDg[g])+1))     
    model.index_G_TDg  = Set(initialize=index_G_TDg, dimen=2)           
    
    model.PSU   = Param(model.index_G_TSg , initialize = PSU  , within = Any)
    model.PSD   = Param(model.index_G_TDg , initialize = PSD  , within = Any) 
    
    
    if(option == 'LR' or option == 'RC' or option == 'FixSol'): #Si se desea relajar las variables enteras como continuas
        model.u     = Var( model.G , model.T , within = UnitInterval)   ## UnitInterval: floating point values in the interval [0,1]
        model.v     = Var( model.G , model.T , within = UnitInterval)   
        model.w     = Var( model.G , model.T , within = UnitInterval)   
        model.delta = Var( model.indexGTSg,    within = UnitInterval)   
    else:        
        model.u     = Var( model.G , model.T , within = Binary)
        model.v     = Var( model.G , model.T , within = Binary)
        model.w     = Var( model.G , model.T , within = Binary)
        model.delta = Var( model.indexGTSg,    within = Binary) 

    model.e         = Var( model.G , model.T , bounds = (0.0,99999.0))
    model.eg        = Var( model.G , model.T , bounds = (0.0,99999.0))
    model.pg        = Var( model.G , model.T , bounds = (0.0,99999.0))
    model.p         = Var( model.G , model.T , bounds = (0.0,99999.0))
    model.eb        = Var( model.G , model.T , bounds = (0.0,99999.0))
    model.ebc       = Var( model.G , model.T , bounds = (0.0,99999.0))  ## pbarra' (capacidad máxima de salida con reserva arriba del m.Pmin)
    model.ec        = Var( model.G , model.T , bounds = (0.0,99999.0))  ## p' (potencia de salida arriba del m.Pmin)
    model.r         = Var( model.G , model.T , bounds = (0.0,99999.0))  ## reserve in general without specific timing
    model.cp        = Var( model.G , model.T , bounds = (0.0,9999999.0))
    
    ## Variables de reserva
    model.rco  = Var( model.ORDC  , model.T  , bounds = (0.0,9999999.0))  ## reserva comprada del sistema
    model.rre  = Var( model.G     , model.T  , bounds = (0.0,9999999.0))  ## reserva de regulacion
    model.rs10 = Var( model.G     , model.T  , bounds = (0.0,9999999.0))   ## reserva rodante de 10
    model.rs30 = Var( model.G     , model.T  , bounds = (0.0,9999999.0))   ## reserva rodante de 30
    model.rn10 = Var( model.G     , model.T  , bounds = (0.0,9999999.0))   ## reserva no rodante de 10
    model.rn30 = Var( model.G     , model.T  , bounds = (0.0,9999999.0))   ## reserva no rodante de 30
        
    model.rrep  = Var( model.G    , model.T  , bounds = (0.0,9999999.0))  ## reserva de regulacion para subir +
    model.rrem  = Var( model.G    , model.T  , bounds = (0.0,9999999.0))  ## reserva de regulacion para bajar -
    model.rs10p = Var( model.G    , model.T  , bounds = (0.0,9999999.0))   ## reserva rodante de 10 para subir +
    model.rs30p = Var( model.G    , model.T  , bounds = (0.0,9999999.0))   ## reserva rodante de 30 para subir +
    model.rs10m = Var( model.G    , model.T  , bounds = (0.0,9999999.0))   ## reserva rodante de 10 para bajar -
    model.rs30m = Var( model.G    , model.T  , bounds = (0.0,9999999.0))   ## reserva rodante de 30 para bajar -
        
    model.cSU       = Var( model.G    , model.T  , bounds = (0.0,9999999.0))  ## total cost start-up
    model.cSD       = Var( model.G    , model.T  , bounds = (0.0,9999999.0))  ## total cost shut-down
    model.mcp       = Var( model.G    , model.T  , bounds = (0.0,9999999.0))  ## minimum cost production
    # model.snplus    = Var( model.T ,           bounds = (0.0,9999999.0))    ##surplus demand
    # model.snminus   = Var( model.T ,           bounds = (0.0,9999999.0))    ##surplus demand
    model.sn        = Var(model.T               , bounds = (0.0,9999999.0))       ##surplus demand
    model.sR        = Var(model.T               , bounds = (0.0,9999999.0))       ##surplus reserve         
    model.el        = Var(model.indexGTLg       , bounds = (0.0,99999.0))         ## within=UnitInterval UnitInterval == [0,1]   
    model.total_cSU = Var(                       bounds = (0.0,999999999999.0))  ## Acumula total prendidos
    # model.total_cSD = Var( bounds = (0.0,999999999999.0))              ## Acumula total costos de apagados
    model.total_cEN = Var( bounds = (0.0,999999999999.0))                ## Acumula total costos de energia
    model.total_cMP = Var( bounds = (0.0,999999999999.0))                ## Acumula total CR
    model.total_MPC = Var( bounds = (0.0,999999999999.0))                ## Acumula total MPC
    model.total_cDE = Var( bounds = (0.0,999999999999.0))                ## Acumula total compra de ENERGIA de demandas elasticas 'd'
    model.total_cRE = Var( bounds = (0.0,999999999999.0))                ## Acumula total compra de ENERGIA de demandas elasticas 'd'
    model.total_cPR = Var( bounds = (0.0,999999999999.0))                ## Acumula total compra de RESERVAS de generadores 'd'
    model.allLOAD   = Var( model.T ,bounds = (0.0,999999999999.0))       ## Cuenta el total de demanda elástica asignada
    
    model.Pb     = Param(model.indexGLg, initialize = Pb,     within = Any)
    model.Cb     = Param(model.indexGLg, initialize = Cb,     within = Any)
    model.C      = Param(model.indexGLg, initialize = C,      within = Any)
    model.Cs     = Param(model.indexGSg, initialize = Cs,     within = Any)
    model.Tunder = Param(model.indexGSg, initialize = Tunder, within = Any)
    
    ## Elastic load demand variables and Prohibed zone minimum
    model.l  = Var(  model.LOAD,     model.T, bounds = (0.0,9999999999.0))   ## Elastic demand commit
    model.cd = Var(  model.LOAD,     model.T, bounds = (0.0,9999999999.0))   ## Partial load cost        
    model.ld = Var(  model.indexLoadTLd,      bounds = (0.0,99999.0))        ## Stairwise segments
    model.Pd = Param(model.indexLoadLd,   initialize = Pd, within = Any)     ## Stairwise energy
    model.Cd = Param(model.indexLoadLd,   initialize = Cd, within = Any)     ## Stairwise cost
        
    model.ROmin = Param(model.indexGRO_RO , initialize = ROmin)              ## Prohibed zone minimum
    model.ROmax = Param(model.indexGRO_RO , initialize = ROmax)              ## Prohided zone maximum
    model.pc_RO = Var(  model.indexGRO_T_RO, bounds = (0.0,99999.0))      
        
    if option == 'LR' or option == 'RC' or option == 'FixSol':
        model.u_RO  = Var(  model.indexGRO_T_RO, within = UnitInterval)        
    else:
        model.u_RO  = Var(  model.indexGRO_T_RO, within = Binary)        
            
       
    ## model.mut2.pprint()        ## For entire Constraint List
    ## print(model.mut2[1].expr)  ## For only one index of Constraint List
    ## print(model.mdt2[3].expr)  ## For only one index of Constraint List
    ## model.u.set_values(dict)
    ## model.u.set_values({(1,3): 1}) ## OJO este no sirve , no fija !!!
    ## https://pyomo.readthedocs.io/en/stable/working_models.html
    ## model.u[3,1].fix(0)
    ## model.u.fix(0)       
    
    def obj_rule(m): 
        return  + m.total_cSU \
                + m.total_cEN \
                + m.total_cMP \
                + m.total_MPC 
                #- m.total_cDE \
                #+ m.total_cRE \
                #- m.total_cPR \
                #   + sum(m.sn[t]   * CLP                    for t in m.T) 
                #   + sum(m.sR[t]   * CRP                    for t in m.T) \
                #   + m.total_cSD\
    model.obj = Objective(rule = obj_rule,sense=minimize)
    

    ## -----------------------------TOTAL COSTOS VACIO------------------------------------------  
    def total_cMP_rule(m):  ## to account CR cost
        return m.total_cMP == sum( m.CR[g] * m.u[g,t] for g in m.G for t in m.T)
    model.total_cMP_ = Constraint(rule = total_cMP_rule)  
    
    ## -----------------------------TOTAL COSTOS ENERGIA------------------------------------------  
    def total_cEN_rule(m):  ## to account energy cost
        return m.total_cEN == sum( m.cp[g,t] for g in m.G for t in m.T)    
    model.total_cEN_ = Constraint(rule = total_cEN_rule)
        
    ## -----------------------------TOTAL COSTOS ARRANQUE------------------------------------------  
    def total_cSU_rule(m):  ## to account starts cost
        return m.total_cSU == sum( m.cSU[g,t] * 1 for g in m.G for t in m.T)
    model.total_cSU_ = Constraint(rule = total_cSU_rule)  
    
    ## -----------------------------TOTAL MINIMUM PRODUCTION COST------------------------------------------  
    def total_MPC_rule(m):  ## to account minumum production cost
        return m.total_MPC == sum( m.mcp[g,t] * 1 for g in m.G for t in m.T)
    model.total_MPC_ = Constraint(rule = total_MPC_rule) 
    
    
    def merge1():  
        a=1            
           
    ## --------------------------------------- TOTAL OFERTAS DE COMPRA DEMANDA ------------------------------------------------  
    if False:
        if True:
            def total_cDE_rule(m):  ## to account purchase of energy of elastic loads
                return m.total_cDE == sum( m.cd[d,t] for d in m.LOAD for t in m.T)
            model.total_cDE_rule = Constraint(rule = total_cDE_rule)   
        
        ## --------------------------- TOTAL OFERTAS DE COMPRA DE RESERVA -------------------------------------
        if False: 
            def total_cRE_rule(m):  ## to account sales of reserve of generators
                return m.total_cRE == sum((  m.rre[g,t] * m.Crr[g]   + 
                                            m.rs10[g,t] * m.Cs10[g]  + 
                                            m.rs30[g,t] * m.Cs30[g]  + 
                                            m.rn10[g,t] * m.Cns10[g] + 
                                            m.rn30[g,t] * m.Cns30[g]) for g in m.G for t in m.T)
            model.total_cRE_rule = Constraint(rule = total_cRE_rule)    
            
        ## ------------------------- TOTAL COMPRAS DE RESERVA (PURCHASE BID)---------------------------------
        if False: 
            def total_PR_rule(m):  ## to account purchase RESERVE of the generators
                return m.total_cPR == sum( m.Cordc[b]*m.rco[b,t] for b in m.ORDC for t in m.T)
            model.total_PR_rule = Constraint(rule = total_PR_rule) 
       
    ## -----------------------------TOTAL COSTOS APAGADO------------------------------------------  
    # def total_cSD_rule(m):  ## to account for stoppages cost
    #     return m.total_cSD == sum( m.cSD[g,t] * 1 for g in m.G for t in m.T)
    # model.total_cSD_ = Constraint(rule = total_cSD_rule)
        
    
    ## -----------------------------GARVER------------------------------------------  
    def logical_rule(m,g,t):    ## logical Knueven eq.(2)   ## Nycander eq.(5) 
        if t == 1:
            return m.u[g,t] - m.u_0[g]   == m.v[g,t] - m.w[g,t]
        else:
            return m.u[g,t] - m.u[g,t-1] == m.v[g,t] - m.w[g,t]
    model.logical    = Constraint(model.G,model.T,rule = logical_rule)

    
    ## ----------------------------POWER EQUALS------------------------------------
      
    def energy_igual_rule(m,g,t):  ## iguala e a ec   eq.(12)
        return m.e[g,t] == m.ec[g,t] + m.Pmin[g] * m.u[g,t]
    model.energy_igual_rule  = Constraint(model.G,model.T, rule = energy_igual_rule)    
    
    # *** PODRIA AYUDAR A HACER MAS TIGHT ***
    # def Piecewise_offer44b(m,g,t):  ## piecewise offer eq.(44b)
    #     return m.ec[g,t] <= ( m.Pmax[g] - m.Pmin[g] ) * m.u[g,t]               
    # model.Piecewise_offer44b = Constraint(model.G,model.T, rule = Piecewise_offer44b)       
    
    def merge2():     
        a=1       
        
    ## --------------------------------------- ENERGY AND TOTAL POWER ------------------------------------------------  
    def total_energy1(m,g,t):                     ## Nycander eq.(24), (25) 
        if m.SU[g] >= m.Pmin[g] :                 ## :g ∈ Gfast units
            if t == 1:
                return m.eg[g,t] == (1/2)*(m.Pmin[g])*(m.u_0[g]   - m.u[g,t]) + (1/2)*(m.p_0[g]   + m.p[g,t])
            else:
                return m.eg[g,t] == (1/2)*(m.Pmin[g])*(m.u[g,t-1] - m.u[g,t]) + (1/2)*(m.p[g,t-1] + m.p[g,t])
        else:                                     ## :g ∈ Gslow units
            if t == 1:
                return m.eg[g,t] == (m.Pmin[g])*(m.u[g,t]) + (1/2)*(m.p_0[g]   + m.p[g,t])
            else:
                return m.eg[g,t] == (m.Pmin[g])*(m.u[g,t]) + (1/2)*(m.p[g,t-1] + m.p[g,t])
    model.total_energy1 = Constraint(model.G,model.T, rule = total_energy1)
    
    def power_igual_rule(m,g,t):  ## iguala pg a p  Nycander eq.(26)
        if m.SU[g] >= m.Pmin[g] :                   ## :g ∈ Gfast
            return m.pg[g,t] == m.Pmin[g] * m.u[g,t] + m.p[g,t]
        else:                                   ## :g ∈ Gslow 
                                                ## :g ∈ Gslow 
            if  t < max(len(m.T)-m.SUD[g],0): # t < len(m.T)
                return m.pg[g,t] == m.Pmin[g] * m.u[g,t] + m.p[g,t]                  + \
                sum(m.PSU[g,i]*m.v[g,t-i+m.SUD[g]+2] for i in range(1,m.SUD[g]+1)) #+ \
                #sum(m.PSD[g,i]*m.w[g,t-i         +2] for i in range(2,m.SDD[g]+1))            
            else:
                return Constraint.Skip
    model.power_igual_rule  = Constraint(model.G,model.T, rule = power_igual_rule) 
    
    def total_energy2(m,g,t):         ## Uriel Constraint 
        return m.eg[g,t] == m.e[g,t]  ## Igual la "e_gorro" de Nycander con la "e=p" de Knueven
    model.total_energy2 = Constraint(model.G,model.T, rule = total_energy2)
     

    ## ------------------------------START-UP AND SHUT-DOWN RAMPS---------------------------------   

    def sdsu_ramp_rule20(m,g,t):          ## eq.(20) 
        if m.UT[g] > 1 and t < len(m.T):  ## :g ∈ G>1
            return m.ec[g,t] + m.r[g,t] <= (m.Pmax[g]-m.Pmin[g])*m.u[g,t] \
                - (m.Pmax[g]-m.SU[g])*m.v[g,t] - (m.Pmax[g]-m.SD[g])*m.w[g,t+1]
        else:
            return Constraint.Skip    
    model.sdsu_ramp_rule20 = Constraint(model.G,model.T, rule = sdsu_ramp_rule20)

    def su_ramp_rule21a(m,g,t):           ## eq.(21a)
        if m.UT[g] == 1:                  ## :g ∈ G1
            return m.ec[g,t] + m.r[g,t] <= (m.Pmax[g]-m.Pmin[g])*m.u[g,t] - (m.Pmax[g]-m.SU[g])*m.v[g,t]
        else:
            return Constraint.Skip    
    model.su_ramp_rule21a = Constraint(model.G,model.T, rule = su_ramp_rule21a) 
           
    def sd_ramp_rule21b(m,g,t):           # eq.(21b)
        if m.UT[g] == 1 and t < len(m.T): # :g ∈ G>1
            return m.ec[g,t] + m.r[g,t] <= (m.Pmax[g]-m.Pmin[g])*m.u[g,t] - (m.Pmax[g]-m.SD[g])*m.w[g,t+1]
        else:
            return Constraint.Skip    
    model.sd_ramp_rule21b = Constraint(model.G,model.T, rule = sd_ramp_rule21b)
    
    def merge3():  
        a=1
        
    ## -------------------------------GENERATION LIMITS (Tight)------------------------------------------ 

    if mode == 'Tight':
        TRU = []; TRD = []; TRU.append(-1); TRD.append(-1)
        for g in G:
            TRU.append(floor((model.Pmax[g]-model.SU[g])/model.RU[g]))
            TRD.append(floor((model.Pmax[g]-model.SU[g])/model.RD[g]))                

        def su_sd_rule23a(m,g,t):                      ## eq.(23a)
            if m.UT[g] == 1 and m.SU[g] != m.SD[g] and t<len(m.T):    ## :g ∈ G1
                return m.ec[g,t] + m.r[g,t] <= (m.Pmax[g]-m.Pmin[g])*m.u[g,t] - (m.Pmax[g]-m.SU[g])*m.v[g,t] \
                    -max(0,m.SU[g]-m.SD[g])*m.w[g,t+1] 
            else:
                return Constraint.Skip     
        model.su_sd_rule23a  = Constraint(model.G,model.T, rule = su_sd_rule23a)  
         
        def su_sd_rule23b(m,g,t):                      ## eq.(23b)
            if m.UT[g] == 1 and m.SU[g] != m.SD[g] and t<len(m.T):    ## :g ∈ G1
                return m.ec[g,t] + m.r[g,t] <= (m.Pmax[g]-m.Pmin[g])*m.u[g,t] - (m.Pmax[g]-m.SD[g])*m.w[g,t+1] \
                    -max(0,m.SD[g]-m.SU[g])*m.v[g,t] 
            else:
                return Constraint.Skip    
        model.su_sd_rule23b  = Constraint(model.G,model.T, rule = su_sd_rule23b) 
        
        def up_ramp_rule38(m,g,t):  ## eq.(38) upper bounds based on the ramp-up and shutdown trajectory of the generator: Pan and Guan (2016)
            if t < len(m.T):
                expr = 0
                for i in range(0,min(m.UT[g]-2+1,TRU[g]+1)):
                    if t-i > 0:
                        expr += (m.Pmax[g]-m.SU[g]-i*m.RU[g])*m.v[g,t-i]                    
                ## expr=sum((m.Pmax[g]-m.SU[g]-i*m.RU[g])*m.v[g,t-i] for i in range(0,min(m.UT[g]-2+1,TRU[g]+1)))                
                return m.eb[g,t] <= m.Pmax[g]*m.u[g,t] - (m.Pmax[g]-m.SD[g])*m.w[g,t+1] - expr
            else:
                return Constraint.Skip
        model.up_ramp_rule38 = Constraint(model.G,model.T, rule = up_ramp_rule38)   
        
        #Trajectory pending 
        ##40 pending
        ##41 pending
    
    def merge4():
        a=1
    
    ## -------------------------------LIMITS & RAMPS------------------------------------------   
        
    def up_ramp_rule35(m,g,t):          ## ramp-up eq.(35)
        if t == 1:
            return m.ebc[g,t] - max(0,m.p_0[g]-m.Pmin[g]) <= (m.SU[g]-m.Pmin[g]-m.RU[g])*m.v[g,t] + m.RU[g]*m.u[g,t]
        else:
            return m.ebc[g,t] - m.ec[g,t-1]  <= (m.SU[g]-m.Pmin[g]-m.RU[g])*m.v[g,t] + m.RU[g]*m.u[g,t]
    model.up_ramp_rule35   = Constraint(model.G,model.T, rule = up_ramp_rule35)   

    def down_ramp_rule36(m,g,t):        ## ramp-down eq.(36) 
        if t == 1:
            return max(0,m.p_0[g]-Pmin[g])   - m.ec[g,t] <= (m.SD[g]-m.Pmin[g]-m.RD[g])*m.w[g,t] + m.RD[g]*m.u_0[g]
        else:
            return m.ec[g,t-1] - m.ec[g,t] <= (m.SD[g]-m.Pmin[g]-m.RD[g])*m.w[g,t] + m.RD[g]*m.u[g,t-1]
    
    model.down_ramp_rule36 = Constraint(model.G,model.T, rule = down_ramp_rule36)
    
    def merge5():
        a=1

    ## -------------------------------DEMAND & RESERVE----------------------------------------   
 
    def demand_rule_market1(m,t):                        ## demand Nycander eq.(4) + m.LOAD 
        return sum( m.pg[g,t] for g in m.G )   == m.De[t] + sum( m.l[d,t] for d in m.LOAD )
    model.demand_rule_market1 = Constraint(model.T, rule = demand_rule_market1)
                                
    def merge6():
        a=1

    ## --------------------------------MINIMUM UP/DOWN TIME---------------------------------------

    def mut_rule(m,g,t):  ## minimum-up time eq.(4)
        if t >= m.UT[g]:
            return sum( m.v[g,i] for i in range(t-value(m.UT[g])+1,t+1)) <= m.u[g,t]        
        else:
            return Constraint.Skip
    model.mut = Constraint(model.G, model.T, rule = mut_rule)    

    def mdt_rule(m,g,t): ## minimum-down time eq.(5)
        if t >= m.DT[g]:
            return sum( m.w[g,i] for i in range(t-value(m.DT[g])+1,t+1)) <= 1 - m.u[g,t] 
        else:
            return Constraint.Skip
    model.mdt = Constraint(model.G, model.T, rule = mdt_rule)
        
    def mdt_rule2(m,g): ## enforce the minimum-down time eq.(3b)
        minimo = min( value(D[g]),len(m.T) )
        if minimo > 0:
            return sum( m.u[g,i] for i in range(1,minimo+1)) == 0
        else: 
            return Constraint.Skip
    model.mdt2 = Constraint(model.G, rule = mdt_rule2)
    
    def mut_rule2(m,g):  ## enforce the minimum-up time eq.(3a)
        minimo = min( value(m.U[g]) , len(m.T) )
        if minimo > 0:
            return sum( m.u[g,i] for i in range(1,minimo+1) ) == int(minimo)
        else: 
            return Constraint.Skip    
    model.mut2 = Constraint(model.G, rule = mut_rule2)
        
    ## (Enforce) the initial Minimum Up/Down Times fixing the initial periods U[g] and D[g] 
    ## Tight and Compact MILP Formulation for the Thermal Unit Commitment Problem
    ## Germán Morales-España, Jesus M. Latorre, and Andrés Ramos
    def enforce():
        for g in model.G: 
            for t in model.T: 
                if t <= U[g]+D[g]:
                    model.u[g,t].fix(model.u_0[g])

    #enforce()
    def merge7():
        a=1
        
    ## ----------------------------PIECEWISE OFFER-------------------------------------------   
    
    if mode == 'Tight':  ##  Garver 1962
        def Piecewise_offer42(m,g,t,l):  ## piecewise offer eq.(42)
            if l == 1:
                return m.el[g,t,l] <= (m.Pb[g,l]-m.Pmin[g] ) * m.u[g,t]
            if l > 1:
                return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1] ) * m.u[g,t]
        model.Piecewise_offer42  = Constraint(model.indexGTLg, rule = Piecewise_offer42)  
        
        def Piecewise_offer43(m,g,t):   ## piecewise offer eq.(43)
            return sum(m.el[g,t,l] for l in range(1,value(len(m.L[g]))+1)) == m.ec[g,t] 
        model.Piecewise_offer43  = Constraint(model.G,model.T, rule = Piecewise_offer43)       
        
        def Piecewise_offer44(m,g,t):   ## piecewise offer eq.(44)
            return sum(m.C[g,l] * m.el[g,t,l] for l in range(1,value(len(m.L[g]))+1)) == m.cp[g,t] 
        model.Piecewise_offer44  = Constraint(model.G,model.T, rule = Piecewise_offer44) 
        
        def Piecewise_mcp(m,g,t):   ## minimum production cost
            try:
                return m.C[g,1] * m.Pmin[g] * m.u[g,t] == m.mcp[g,t]          
            except:
                if t==1:
                    print('<Piecewise_mcp> name...',names[g]) 
                return Constraint.Skip
        model.Piecewise_mcp = Constraint(model.G,model.T, rule = Piecewise_mcp)
        
        
    # *** PODRIA AYUDAR A HACER MAS TIGHT ***
    if mode == 'Tight' and False:  ##  Knueven et al. (2018b)          
        ## Tightened the bounds on pl(t)->(43),(44) with the start-up 
        ## and shutdown variables using the start-up and shutdown ramp:
        Cv = []
        Cw = []
        for g in G:
            auxv=[]
            auxw=[]
            for l in L[g]:
                a=0       
                if Pb[g,l] <= SU[g]:
                       a=0     
                if l==1 : ## Case Pb[g,l=0] = Pmin[g]
                    if Pmin[g] < SU[g] and SU[g] < Pb[g,l]:
                        a=Pb[g,l]-SU[g]   
                    if Pmin[g] >= SU[g]:
                        a=Pb[g,l]-Pmin[g]  
                if l!=1:
                    if Pb[g,l-1] < SU[g] and SU[g] < Pb[g,l]:
                        a=Pb[g,l]-SU[g]   
                    if Pb[g,l-1] >= SU[g]:
                        a=Pb[g,l]-Pb[g,l-1]  
                auxv.append(a)
                b=0 
                if Pb[g,l] <= SD[g]:
                   b=0    
                if l==1: ## Case Pb[g,0] = Pmin[g]
                    if Pmin[g] < SD[g] and SD[g] < Pb[g,l]:
                        b=Pb[g,l]-SD[g]   
                    if Pmin[g] >= SD[g]:
                        b=Pb[g,l]-Pmin[g]  
                if l!=1: 
                    if  Pb[g,l-1] < SD[g] and SD[g] < Pb[g,l]:
                        b=Pb[g,l]-SD[g]   
                    if  Pb[g,l-1] >= SD[g]:
                        b=Pb[g,l]-Pb[g,l-1]  
                auxw.append(b)
                #print('g,l',g,l)
            Cv.append(auxv)
            Cw.append(auxw)
            
        def Piecewise_offer46(m,g,t,l):  ## piecewise offer eq.(46)  Knueven et al. (2018b)      
            if m.UT[g] > 1:
                if l == 1:  ## Case Pb[g,l=0] = Pmin[g]
                    if t < len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]- m.Pmin[g] )*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t] - Cw[g-1][l-1]*m.w[g,t+1]
                    if t == len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]- m.Pmin[g] )*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t] - 0
                if l > 1:
                    if t < len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1])*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t] - Cw[g-1][l-1]*m.w[g,t+1]
                    if t == len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1])*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t] - 0
            else: ## UT[g] == 1
                return Constraint.Skip         
        model.Piecewise_offer46  = Constraint(model.indexGTLg, rule = Piecewise_offer46)
        
        def Piecewise_offer47a(m,g,t,l):  ## piecewise offer eq.(47a)  Knueven et al. (2018b)     
            if m.UT[g]==1:
                if l == 1:  ## Case Pb[g,0] = Pmin[g]
                    return m.el[g,t,l] <= (m.Pb[g,l]-m.Pmin[g]  )*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t] 
                if l > 1:
                    return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1])*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t]
            else:
                return Constraint.Skip                    
        model.Piecewise_offer47a = Constraint(model.indexGTLg, rule = Piecewise_offer47a)
        
        def Piecewise_offer47b(m,g,t,l):  ## piecewise offer eq.(47b)  Knueven et al. (2018b)     
            if m.UT[g]==1:
                if l == 1:  ## Case Pb[g,0] = Pmin[g]
                    if t < len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pmin[g]  )*m.u[g,t] - Cw[g-1][l-1]*m.w[g,t+1]
                    if t == len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pmin[g]  )*m.u[g,t] - 0
                if l > 1:
                    if t < len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1])*m.u[g,t] - Cw[g-1][l-1]*m.w[g,t+1]
                    if t == len(m.T):
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1])*m.u[g,t] - 0                       
            else:
                return Constraint.Skip                 
        model.Piecewise_offer47b = Constraint(model.indexGTLg, rule = Piecewise_offer47b)
        
        def Piecewise_offer48a(m,g,t,l):  ## piecewise offer eq.(48a)  Knueven et al. (2018b)     
            if m.UT[g]==1 and SU[g]!=SD[g]:
                posit = max(0,Cv[g-1][l-1] - Cw[g-1][l-1])      
                if l == 1:  ## Case Pb[g,l=0] = Pmin[g]
                    if t < len(m.T):         
                        return m.el[g,t,l] <= (m.Pb[g,l]- m.Pmin[g] )*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t] - posit*m.w[g,t+1]
                    if t == len(m.T):  
                        return Constraint.Skip                   
                if l > 1:  ## Caso general 
                    if t < len(m.T):   
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1])*m.u[g,t] - Cv[g-1][l-1]*m.v[g,t] - posit*m.w[g,t+1]
                    if t == len(m.T):    
                        return Constraint.Skip  
            else:
                return Constraint.Skip                       
        model.Piecewise_offer48a = Constraint(model.indexGTLg, rule = Piecewise_offer48a) 
                        
        # VALIDAR EXPERIMENTALMENTE
        def Piecewise_offer48b(m,g,t,l):  ## piecewise offer eq.(48b)  Knueven et al. (2018b)     
            if m.UT[g]==1 and SU[g]!=SD[g]:
                posit = max(0,Cw[g-1][l-1] - Cv[g-1][l-1]) 
                if l == 1:  ## Case Pb[g,l=0] = Pmin[g]
                    if t < len(m.T):              
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pmin[g]  )*m.u[g,t] - Cw[g-1][l-1]*m.w[g,t+1] - posit*m.v[g,t]
                    if t == len(m.T):
                        return Constraint.Skip                     
                if l > 1: ## Caso general 
                    if t < len(m.T):             
                        return m.el[g,t,l] <= (m.Pb[g,l]-m.Pb[g,l-1])*m.u[g,t] - Cw[g-1][l-1]*m.w[g,t+1] - posit*m.v[g,t]
                    if t == len(m.T):   
                        return Constraint.Skip                                 
            else:
                return Constraint.Skip                            
        model.Piecewise_offer48b = Constraint(model.indexGTLg, rule = Piecewise_offer48b)    
    
    def merge8(): 
        a=1         
    def merge8b():   
        a=1
        
    ## ----------------------------SIMPLE COST PRODUCTION (HYDRO)-------------------------------------------  
    # Pending ...    
    if False:
        def simple_cost_hydro(m,g,t):   
            return m.C[g,1] * m.e[g,t] == m.cp[g,t]                                            
        model.simple_cost_hydro = Constraint(model.G,model.T, rule = simple_cost_hydro)
        
    
    ## ----------------------------VARIABLE START-UP COST-------------------------------------------     
    if True: ## Morales-España et al. (2013a):
         
        def Start_up_cost54(m,g,t,s):  ##  start-up cost eq.(54)   Checar and t >= m.Tunder[g,s+1]:----- 
            if s != len(m.S[g]) and t >= m.Tunder[g,s+1]:  
                return m.delta[g,t,s] <= sum(m.w[g,t-i] for i in range(m.Tunder[g,s],m.Tunder[g,s+1])) 
            else:
                return Constraint.Skip                                   
        model.Start_up_cost54 = Constraint(model.indexGTSg, rule = Start_up_cost54)
       
        def Start_up_cost55(m,g,t):  ##  start-up cost eq.(55)
            return m.v[g,t] == sum(m.delta[g,t,s] for s in range(1,len(m.S[g])+1))
        model.Start_up_cost55 = Constraint(model.G,model.T, rule = Start_up_cost55) 
         
        def Start_up_cost56(m,g,t):  ##  start-up cost eq.(56)
            return m.cSU[g,t] == sum((m.Cs[g,s]*m.delta[g,t,s]) for s in range(1,len(m.S[g])+1))
        model.Start_up_cost56 = Constraint(model.G,model.T, rule = Start_up_cost56)    
        
    
    ## Initial Startup (t=0) Type required by MLR and Knueven from
    ## 'Tight and Compact MILP Formulation for the Thermal Unit Commitment Problem',
    ## Germán Morales-España, Jesus M. Latorre, and Andrés Ramos.  
    def enforce2():   
        for g in range(1,len(G)+1): 
            for t in range(1,len(T)+1): 
                for s in range(1,len(S[g])): 
                    if TD_0[g]>=2:
                        if t < model.Tunder[g,s+1]:
                            if t > max(model.Tunder[g,s+1]-TD_0[g],1):
                                model.delta[g,t,s].fix(0)
                                # print('fix delta:',g,t,s)  
                      
    #enforce2()                 
    def merge9():
        a=1
                                
    if  False:   
        ## ----------------------- ELASTIC LOADS (PURCHASE BID) ----------------------------   
        ## My version of stairwise of purchase bid based on garver eq.(42), (43) y (44)
        def Piecewise_load_bid1(m,d,t,i):  ## based on eq.(42) Knueven
            if i != 1:
                return m.ld[d,t,i-1] <= (m.Pd[d,i-1]-m.Pd[d,i] )
            else:
                return Constraint.Skip 
        model.Piecewise_load_bid1 = Constraint(model.indexLoadTLd , rule = Piecewise_load_bid1)    
            
        def Piecewise_load_bid2(m,d,t):   ## based on eq.(43)
            return sum(m.ld[d,t,i] for i in range(1,value(len(m.Ld[d]))+1)) == m.l[d,t]                       
        model.Piecewise_load_bid2 = Constraint(model.LOAD, model.T, rule = Piecewise_load_bid2)           
            
        def Piecewise_load_bid3(m,d,t):   ## based on eq.(44)
            return sum(m.Cd[d,i] * m.ld[d,t,i] for i in range(1,value(len(m.Ld[d]))+1)) == m.cd[d,t]    
        model.Piecewise_load_bid3 = Constraint(model.LOAD, model.T, rule = Piecewise_load_bid3) 
                    
        def Piecewise_load_bid4(m,t):   ## sub-total commited load
            return sum( m.l[d,t]  for d in m.LOAD)  ==      m.allLOAD[t]                
        model.Piecewise_load_bid4 = Constraint(            model.T, rule = Piecewise_load_bid4)
            
        def load_bid_min(m,d,t):   
            # print('Pd_min',m.Pd[d,len(m.Ld[d])]) 
            return m.l[d,t] >= m.Pd[d,len(m.Ld[d])]                                  
        model.load_bid_min        = Constraint(model.LOAD, model.T, rule = load_bid_min)   
            
        def load_bid_max(m,d,t):  
            # print('Pd_max',m.Pd[d,1]) 
            return m.l[d,t] <= m.Pd[d,1]       
        model.load_bid_max        = Constraint(model.LOAD, model.T, rule = load_bid_max)
                                            
        def merge10():
            a=1                                                                       

    if False:
        ## ----------------------- PROHIBID OPERATING ZONES ----------------------------  
        def prohibid_operative_zones_min(m,g,t,ro):  
            return  m.ec_RO[g,t,ro]  >=  m.ROmin[g,ro] * m.u_RO[g,t,ro]                                
        model.prohibid_operative_zones_min = Constraint(model.indexGRO_T_RO,rule=prohibid_operative_zones_min)

        def prohibid_operative_zones_max(m,g,t,ro):  
            return  m.ec_RO[g,t,ro]  <=  m.ROmax[g,ro] * m.u_RO[g,t,ro]                                  
        model.prohibid_operative_zones_max = Constraint(model.indexGRO_T_RO,rule=prohibid_operative_zones_max)

        def prohibid_operative_zones1(m,g,t):
            return  sum( m.u_RO[g,t,ro] for ro in m.RO[g] ) == m.u[g,t]                             
        model.prohibid_operative_zones1    = Constraint(model.indexGRO_T,   rule=prohibid_operative_zones1)
            
        def prohibid_operative_zones2(m,g,t):  
            return  sum( m.ec_RO[g,t,ro] for ro in m.RO[g] ) == m.ec[g,t]                             
        model.prohibid_operative_zones2    = Constraint(model.indexGRO_T,   rule=prohibid_operative_zones2)
                             
        def merge11(): 
            a=1

    if False:     
        ## ----------------------- RESERVE OFFERS ----------------------------
        def total_reg_rule(m,t):     ## to account the regulation reserve met
            return sum( m.rre[g,t] 
                       for g in m.G) >= sum( m.rco[b,t] for b in {1,2,3})
        model.total_reg_rule = Constraint(model.T,rule = total_reg_rule)   
            
        def total_spin_rule(m,t):    ## to account the sppining reserve met
            return sum( m.rre[g,t] + m.rs10[g,t] 
                       for g in m.G) >= sum( m.rco[b,t] for b in {1,2,3,4,5,6})
        model.total_spin_rule = Constraint(model.T,rule = total_spin_rule)   
               
        def total_oper_rule(m,t):    ## to account the operative reserve met
            return sum( m.rre[g,t] + m.rs10[g,t] + m.rn10[g,t]
                           for g in m.G) >= sum( m.rco[b,t] for b in {1,2,3,4,5,6,7,8,9})
        model.total_oper_rule = Constraint(model.T,rule = total_oper_rule) 
            
        def total_sup_rule(m,t):    ## to account the supplementary reserve met
            return sum((m.rre[g,t]+m.rs10[g,t]+m.rn10[g,t]+m.rs30[g,t]+m.rn30[g,t]) 
                           for g in m.G) >= sum( m.rco[b,t] for b in m.ORDC)
        model.total_supp_rule = Constraint(model.T,rule = total_sup_rule)   
                     
        def limit_rco_rule(m,b,t):  ## limits of reserve requirements
            return m.rco[b,t] <= m.RCO[b] 
        model.limit_rco_rule = Constraint(model.ORDC, model.T, rule = limit_rco_rule)
            
        def limit_rre_rule(m,g,t):  ## limits of regulation reserve
            return m.rre[g,t] <= m.RRe[g] 
        model.limit_rre_rule = Constraint(model.G, model.T, rule = limit_rre_rule)
            
        def limit_rs10_rule(m,g,t):  ## limits of spinning reserve 10
            return m.rs10[g,t] <= m.RR10[g] * m.u[g,t]
        model.limit_rs10_rule = Constraint(model.G, model.T, rule = limit_rs10_rule)
            
        def limit_rs30_rule(m,g,t):  ## limits of spinning reserve 30
            return m.rs30[g,t] <= m.RR30[g] * m.u[g,t]
        model.limit_rs30_rule = Constraint(model.G, model.T, rule = limit_rs30_rule)
            
        def limit_rn10_rule(m,g,t):  ## limits of non-spinning reserve 10
            return m.rn10[g,t] <= m.RN10[g] * (1-m.u[g,t])
            model.limit_rn10_rule = Constraint(model.G, model.T, rule = limit_rn10_rule)                        
            
        def limit_rn30_rule(m,g,t):  ## limits of non-spinning reserve 30
            return m.rn30[g,t] <= m.RN30[g] * (1- m.u[g,t])
        model.limit_rn30_rule = Constraint(model.G, model.T, rule = limit_rn30_rule)


        def merge12(): 
            aux=1
        
    ## ---------------------------- LOCAL BRANCHING CONSTRAINT LBC 1 (SOFT-FIXING)------------------------------------------    
    ## Define a neighbourhood with LBC1.    
    if(option == 'lbc1'):
                  
        for f in No_SB_Uu:   
            model.u[f[0]+1,f[1]+1].domain = UnitInterval    ## We remove the integrality constraint of the Binary Support 
            if improve == True:          
                model.u[f[0]+1,f[1]+1] = 0                  ## Hints
        for f in SB_Uu:  
            model.u[f[0]+1,f[1]+1].domain = UnitInterval    ## We remove the integrality constraint of the Binary Support 
            if improve == True:          
                model.u[f[0]+1,f[1]+1] = 1                  ## Hints
            
        ## Hints para iniciar desde la última solución válida
        #if improve ==True:
        for g in range(len(G)):
            for t in range(len(T)):
                model.v[g+1,t+1] = V[g][t]                  ## Hints
                model.w[g+1,t+1] = W[g][t]                  ## Hints
                if delta[g][t]  != 0:
                    model.delta[g+1,t+1,delta[g][t]] = 1    ## Hints
                    
        model.cuts = ConstraintList()
        
        # Soft-fixing: adding a new restriction 
        if True:
            ## https://pyomo.readthedocs.io/en/stable/working_models.html
            inside90   = ceil((percent_soft/100) * (len(SB_Uu))) #-len(lower_Pmin_Uu)
            expr       = 0        
            ## Se hace inside90 = 90% solo a el - Soporte Binario -  
            for f in SB_Uu:
                expr += model.u[f[0]+1,f[1]+1]
            model.cuts.add(expr >= inside90)
            print(option,'variables Uu that SB_Uu=1 <= inside90  =', inside90)
            # outside90 = len(SB_Uu)-inside90
            # print(option,'variables Uu that SB_Uu=0 <= outside90 =', outside90)
            
        
        ## Local Branching Constraint (LBC)     
        if True:            
            ## Adding a new restrictions LEFT-BRANCH  <°|((><
            if improve == True or (timeover==True and improve == False) : 
                print('Adding  1  left-branch: ∑lower_Pmin_Uu + ∑SB_Uu ≤',k)                
                expr = 0      
                for f in SB_Uu:                             ## Cuenta los cambios de 1 --> 0  
                    expr += 1 - model.u[f[0]+1,f[1]+1] 
                for f in lower_Pmin_Uu :  # No_SB_Uu        ## Cuenta los cambios de 0 --> 1 
                    expr +=     model.u[f[0]+1,f[1]+1]              
                model.cuts.add(expr <= k)      
        
            ## Adding a new restrictions RIGHT-BRANCH  >>++++++++|°> . o O
            print('Adding ',len(rightbranches),' right-branches:  ∑lower_Pmin_Uu + ∑SB_Uu ≥',k,'+ 1')
            for cut in rightbranches:
                expr = 0      
                ## cut[1]=No_SB_Uu   cut[2]=lower_Pmin_Uu  cut[0]=SB_Uu   
                for f in cut[0]:  ## NUNCA SE MUEVE         ## Cuenta los cambios de 1 --> 0  
                    expr += 1 - model.u[f[0]+1,f[1]+1] 
                for f in cut[2]:  # cut[1]                  ## Cuenta los cambios de 0 --> 1 
                    expr +=     model.u[f[0]+1,f[1]+1] 
                model.cuts.add(expr >= k + 1)
                
               
    ## ---------------------------- LOCAL BRANCHING CONSTRAINT LBC2 (INTEGER VERSION)------------------------------------------    
    ## Define a neighbourhood with LBC2.       
    if(option == 'lbc2'):
                  
        for f in No_SB_Uu:   
            model.u[f[0]+1,f[1]+1].domain = Binary    ## We remove the integrality constraint of the Binary Support 
            if improve == True:          
                model.u[f[0]+1,f[1]+1] = 0            ## Hints
        for f in SB_Uu:  
            model.u[f[0]+1,f[1]+1].domain = Binary    ## We remove the integrality constraint of the Binary Support 
            if improve == True:          
                model.u[f[0]+1,f[1]+1] = 1            ## Hints
            
        ## Hints para iniciar desde la última solución válida
        #if improve == True:
        for g in range(len(G)):
            for t in range(len(T)):
                model.v[g+1,t+1] = V[g][t]                  ## Hints
                model.w[g+1,t+1] = W[g][t]                  ## Hints
                if delta[g][t]  != 0:
                    model.delta[g+1,t+1,delta[g][t]] = 1    ## Hints
        
        model.cuts = ConstraintList()
        
        ## Local Branching Constraint (LBC) 
        if True:            
            ## Adding a new restrictions LEFT-BRANCH  <°|((><
            if improve == True or (timeover==True and improve == False) : 
                print('Adding  1  left-branch: ∑lower_Pmin_Uu  + ∑SB_Uu ≤',k)                
                expr = 0      
                for f in SB_Uu:                             ## Cuenta los cambios de 1 --> 0  
                    expr += 1 - model.u[f[0]+1,f[1]+1] 
                for f in lower_Pmin_Uu :  # No_SB_Uu        ## Cuenta los cambios de 0 --> 1 
                    expr +=     model.u[f[0]+1,f[1]+1]              
                model.cuts.add(expr <= k)      
        
            ## Adding a new restrictions RIGHT-BRANCH  >>++++++++|°> . o O
            print('Adding ',len(rightbranches),' right-branches:  ∑lower_Pmin_Uu  + ∑SB_Uu ≥',k,'+ 1')
            for cut in rightbranches:
                expr = 0      
                ## cut[1]=No_SB_Uu   cut[2]=lower_Pmin_Uu  cut[0]=SB_Uu   
                for f in cut[0]:  ## NO MOVER NUNCA         ## Cuenta los cambios de 1 --> 0  
                    expr += 1 - model.u[f[0]+1,f[1]+1] 
                for f in cut[2]:  # cut[1]                  ## Cuenta los cambios de 0 --> 1 
                    expr +=     model.u[f[0]+1,f[1]+1] 
                model.cuts.add(expr >= k + 1)
                

    ## ---------------------------- HARD VARIABLE FIXING I  ------------------------------------------
    ##     
    if option == 'Hard':
        for f in SB_Uu:
            model.u[f[0]+1,f[1]+1].fix(1)                   ## Hard fixing
        for f in No_SB_Uu: 
            model.u[f[0]+1,f[1]+1] = 0                      ## Hints
        for f in lower_Pmin_Uu:
            model.u[f[0]+1,f[1]+1] = 0                      ## Hints
            
    ## ---------------------------- HARD VARIABLE FIXING III------------------------------------------
    ##     
    if option == 'Hard3':
        model.u.fix(0)                                      ## Hard fixing
        for f in SB_Uu:       
            model.u[f[0]+1,f[1]+1].unfix()                  ## Hard fixing
            model.u[f[0]+1,f[1]+1] = 1                      ## Hints   
        # for f in No_SB_Uu: 
        #     model.u[f[0]+1,f[1]+1].fix(0)                 ## Hard fixing
        for f in lower_Pmin_Uu:
            model.u[f[0]+1,f[1]+1].unfix()    
            model.u[f[0]+1,f[1]+1] = 0                      ## Hints
     
    ## ---------------------------- CHECK FEASIABILITY ------------------------------------------
    ## 
    if option == 'Check':  
        
        for f in SB_Uu: 
            model.u[f[0]+1,f[1]+1].domain = Binary 
            model.u[f[0]+1,f[1]+1].fix(1)                   ## Hard fixing
        for f in No_SB_Uu: 
            model.u[f[0]+1,f[1]+1].domain = Binary 
            model.u[f[0]+1,f[1]+1].fix(0)                   ## Hard fixing
        for g in range(0,len(model.G)):
            for t in range(0,len(model.T)):
                model.v[g+1,t+1].domain   = Binary 
                model.v[g+1,t+1].fix( V[g][t] )             ## Hard fixing
                model.w[g+1,t+1].domain   = Binary 
                model.w[g+1,t+1].fix( W[g][t] )             ## Hard fixing
                if delta[g][t] != 0:
                    model.delta[g+1,t+1,delta[g][t]].domain = Binary 
                    model.delta[g+1,t+1,delta[g][t]].fix(1) ## Hard fixing

    ## ---------------------------- FIX SOLUTION LINEAR ------------------------------------------
    ## 
    if option == 'FixSol':  
        
        for f in SB_Uu: 
            model.u[f[0]+1,f[1]+1].fix(1)                   ## Hard fixing
        for f in No_SB_Uu: 
            model.u[f[0]+1,f[1]+1].fix(0)                   ## Hard fixing
        for g in range(0,len(model.G)):
            for t in range(0,len(model.T)):
                model.v[g+1,t+1].fix( V[g][t] )             ## Hard fixing
                model.w[g+1,t+1].fix( W[g][t] )             ## Hard fixing
                if delta[g][t] != 0:
                    model.delta[g+1,t+1,delta[g][t]].fix(1) ## Hard fixing
                                
    ## ---------------------------- REDUCED COST ------------------------------------------
    ## 
    if option == 'RC':                             
        for f in SB_Uu: 
            model.u[f[0]+1,f[1]+1].setlb(1.0)                 ## Fix upper bound
                    
    ## ---------------------------- KERNEL SEARCH ------------------------------------------
    ##
    if option == 'KS' :    
        model.u.fix(0)                                      ## Hard fixing
        for f in kernel: 
            model.u[f[0]+1,f[1]+1].unfix()  
            model.u[f[0]+1,f[1]+1] = 1                      ## Hints
        for f in bucket: 
            model.u[f[2]+1,f[3]+1].unfix()                  
            model.u[f[2]+1,f[3]+1] = 0                      ## Hints
            
        model.cuts = ConstraintList()
        expr       = 0      
        for f in bucket:                                    ## Cuenta los elementos del bucket
            expr += model.u[f[2]+1,f[3]+1] 
        model.cuts.add(expr >= 1)            
        
  
        
    ## Creating thread
    # t1  = threading.Thread(target=merge1)
    # t2  = threading.Thread(target=merge2)    
    # t3  = threading.Thread(target=merge3)    
    # t4  = threading.Thread(target=merge4)    
    # t5  = threading.Thread(target=merge5)  
    # t6  = threading.Thread(target=merge6)   
    # t7  = threading.Thread(target=merge7)   
    # t8  = threading.Thread(target=merge8)   
    # t8b = threading.Thread(target=merge8b)   
    # t9  = threading.Thread(target=merge9)  
      
    # t10 = threading.Thread(target=merge10)
    # t11 = threading.Thread(target=merge11)
    # t12 = threading.Thread(target=merge12)   

    # t1.start(); t2.start(); t3.start(); t4.start(); t5.start(); t6.start(); t7.start(); t8.start(); t8b.start(); t9.start(); t10.start(); t11.start(); t12.start()   ## starting threads 
    # t1.join();  t2.join();  t3.join();  t4.join();  t5.join();  t6.join();  t7.join();  t8.join();  t8b.join();  t9.join();  t10.join();  t11.join();  t12.join()   ## wait until thread 1 is completely executed     
          
 
 
    #print(option,"All threads completely executed!") # https://www.geeksforgeeks.org/multithreading-python-set-1/
    


    return model, inside90


