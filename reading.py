import json
import util
import os
import pandas as pd
from  math import floor , ceil

def reading(file):
    with open(file) as json_file:
        md = json.load(json_file)
        
    G       = []   ## generators number
    T       = []   ## periodos de tiempo
    S       = {}   ## eslabones de costo variable de arranque
    L       = {}   ## eslabones de costo en piecewise
    C       = {}   ## cost of segment of piecewise
    TSg     = {}   ## eslabones trayectorias de subida
    TDg     = {}   ## eslabones trayectorias de bajada 
    Pb      = {}   ## maximum power available for piecewise segment L for generator g (MW).
    Cb      = {}   ## cost of generator g producing Pb MW of power ($/h).
    De      = {}   ## load
    R       = {}   ## reserve_requirement
    Pmin    = {}   ## power min
    Pmax    = {}   ## power max
    RU      = {}   ## ramp_up_limit", "ramp_up_60min"
    RD      = {}   ## ramp_down_limit", "ramp_down_60min"
    SU      = {}   ## ramp_startup_limit", "startup_capacity"
    SD      = {}   ## ramp_shutdown_limit", "shutdown_capacity"
    UT      = {}   ## time_upminimum
    DT      = {}   ## time_down_minimum
    D       = {}   ## number of hours generator g is required to be off at t=1 (h).
    U       = {}   ## number of hours generator g is required to be on at t=1 (h).
    TD_0    = {}   ## Number of hours that the unit has been offline before the scheduling horizon.
    p_0     = {}   ## power_output_t0
    CR      = {}   ## cost of generator g running and operating at minimum production Pmin ($/h).
    C       = {}   ## 
    Cs      = {}   ## Costo de cada escalón del conjunto S de la función de costo variable de arranque.
    Tunder  = {}   ## lag de cada escalón del conjunto S de la función de costo variable de arranque.
    Startup = {}   ## start-up cost
        
    time_periods = int(md['time_periods'])
    demand       =     md['demand']  
    reserves     =     md['reserves']  

    for t in range(1, time_periods+1):
        T.append(t)    
    De   = dict(zip(T, demand))
    R    = dict(zip(T, reserves))
    
    names_gens = []
    i = 1
    ## Se obtiene nombre de los generadores y número
    for gen in md['thermal_generators']:  
        names_gens.append(gen)
        G.append(i)
        i += 1
        
    must_run             = []
    power_output_minimum = []
    power_output_maximum = []
    ramp_up_limit        = []
    ramp_down_limit      = []
    ramp_startup_limit   = []
    ramp_shutdown_limit  = []
    time_up_minimum      = []
    time_down_minimum    = []
    power_output_t0      = []
    unit_on_t0           = []
    time_up_t0           = []
    time_down_t0         = []   
    startup              = []
    piecewise_production = []
    Piecewise            = []
    Startup              = []
    Ulist                = []
    Dlist                = []
    TD0list              = []
    p_0_list             = []
    u_0_list             = []
    fixed_cost           = []
    SUD                  = []
    PSD                  = [] 
    SDD                  = [] 
    PSU                  = []
    PSUindex             = []
    PSDindex             = []
    abajo_min            = 0
    
    ## To get the data from the generators
    i = 1 ## Cuenta los generadores
    for gen in names_gens:  
        must_run.append(md['thermal_generators'][gen]["must_run"]) #0,
        power_output_minimum.append(md['thermal_generators'][gen]["power_output_minimum"])#80
        power_output_maximum.append(md['thermal_generators'][gen]["power_output_maximum"])#300.0
        ramp_up_limit.append(md['thermal_generators'][gen]["ramp_up_limit"])#50
        ramp_down_limit.append(md['thermal_generators'][gen]["ramp_down_limit"])#30
        ramp_startup_limit.append(md['thermal_generators'][gen]["ramp_startup_limit"])#100
        ramp_shutdown_limit.append(md['thermal_generators'][gen]["ramp_shutdown_limit"])#80
        time_up_minimum.append(md['thermal_generators'][gen]["time_up_minimum"])#3
        time_down_minimum.append(md['thermal_generators'][gen]["time_down_minimum"])#2
        power_output_t0.append(md['thermal_generators'][gen]["power_output_t0"])#120
        unit_on_t0.append(md['thermal_generators'][gen]["unit_on_t0"])#1
        time_up_t0.append(md['thermal_generators'][gen]["time_up_t0"])#1
        time_down_t0.append(md['thermal_generators'][gen]["time_down_t0"])#0        
        try: 
            fixed_cost.append(md['thermal_generators'][gen]["fixed_cost"] )        
            #print(md['thermal_generators'][gen]["fixed_cost"] )       
        except:
            fixed_cost.append(0)   
            
           
        startup = (md['thermal_generators'][gen]["startup"]) # variable start-up cost
        piecewise_production = md['thermal_generators'][gen]["piecewise_production"] #piecewise cost
        
        ## Para obtener los piecewise del costo de los generadores
        lista_aux = []
        j = 0
        for piece in piecewise_production:
            lista_aux.append((piece['mw'],piece['cost']))
            j += 1            
        Piecewise.append(lista_aux)
        
        lista = []
        jj = 1
        for ii in range(j-1):
            lista.append(jj)
            jj= jj+1
        L[i] = lista
                
        ## Obtiene segmentos del costo variable de arranque
        lista_aux2 = []
        lista2     = []
        j = 1        
        for segment in startup:
            if segment['lag']>=time_down_minimum[i-1]:
                lista_aux2.append((segment['lag'],segment['cost']))
                lista2.append(j)
                j += 1         
            
        Startup.append(lista_aux2)
        S[i] = lista2
        
        ## Caso apagado
        if unit_on_t0[i-1] == 0: 
            u_0_list.append(0)   
            aux=max(0,time_down_minimum[i-1] - time_down_t0[i-1])
            Ulist.append(0)
            Dlist.append(aux)
            TD0list.append(time_down_t0[i-1])    
        else:  
        ## Caso prendido
            u_0_list.append(1)
            aux=max(0,time_up_minimum[i-1] - time_up_t0[i-1])
            Ulist.append(aux)
            Dlist.append(0)
            TD0list.append(0)

                
        ## Validaciones de prendido y apagado
        if power_output_t0[i-1] !=0 and unit_on_t0[i-1] == 0:
            print('Error: The generator ',str(i),' cannot be off and its output greater than zero')
            quit()
        if time_down_t0[i-1] !=0 and unit_on_t0[i-1] != 0:
            print('Error: The generator  ',str(i),' cannot be off and on at the same time')
            quit()
        
        ########################################################################
        ## Este código considera las potencias de arranque de los generadores
        #           10             -          100             =   -90  prendido
        #           0              -          100             =   -100 apagado       
        if power_output_t0[i-1]<power_output_minimum[i-1] and power_output_t0[i-1]!=0: ## potencia abajo del mínimo
            abajo_min=abajo_min+1
            print('estado=',gen,unit_on_t0[i-1])
        p_0_list.append(power_output_t0[i-1])
        ########################################################################
        ## Calcularemos los periodos de arranque y las trayectorias de arranque   
        j = 1
        lista = [] 
        if ramp_startup_limit[i-1] >= power_output_minimum[i-1]:
            SUD.append(1)
            PSU.append(power_output_minimum[i-1]) #¿ramp_startup_limit?
            PSUindex.append((i,j))
            lista.append(1)
        else:
            sud = ceil(power_output_minimum[i-1] / ramp_startup_limit[i-1])
            SUD.append(sud+1)
            delta = power_output_minimum[i-1] / sud
            for j in range(1,sud+1+1):
                PSU.append(delta*(j-1))
                PSUindex.append((i,j))   
                lista.append(j)
                j = j + 1           
        TSg[i] = lista    
                
        ## Calcularemos los periodos de apagado y las trayectorias de apagado  
        j = 1        
        lista = []
        if ramp_shutdown_limit[i-1] >= power_output_minimum[i-1]:
            SDD.append(1)
            PSD.append(power_output_minimum[i-1])
            PSDindex.append((i,j))
            lista.append(1)
        else:
            sdd = ceil(power_output_minimum[i-1] / ramp_shutdown_limit[i-1])
            SDD.append(sdd+1)
            delta = power_output_minimum[i-1] / sdd
            k = 1
            for j in range(sdd+1+1,1,-1):
                PSD.append(power_output_minimum[i-1] - delta*(k-1))
                PSDindex.append((i,k))
                lista.append(k)
                k = k + 1
        TDg[i] = lista    
                                 
        i += 1;  ## Se incrementa un generador  
        
    print('SUD PSU') #TSg
    print(SUD ,PSU )#TSg
    print('SDD PSD')#TDg
    print(SDD ,PSD)#TDg
        
        
    ## Termina lectura del JSON
    ######################################################################################
   
   
    ## Se extraen los diccionarios Pb y C de la lista de listas Piecewise    
    k=0; n=0
    for i in Piecewise:
        k=k+1
        n=0
        for j in i:
            n=n+1
            C[k,n] = j[1]
            # ## Se calcula el costo mínimo de operación CR
            # if n==1:
            #     CR[k] = j[0]*j[1] 
        del C[(k,n)]      
         
        
    k=0; n=0
    for i in Piecewise:
        k=k+1
        n=0
        for j in i:
            if n!=0:
                #print(k,",",n,",",j[0],",",j[1])
                Pb[k,n] = j[0]
                Cb[k,n] = j[1]   
            n=n+1
                
    ## Se extraen los diccionarios Tunder y Cs de la lista de listas Startup    
    k=0; n=0
    for i in Startup:
        k=k+1
        n=0
        for j in i:
            n=n+1
            # print(k,",",n,",",j[0],",",j[1])
            Tunder[k,n] = j[0]
            Cs[k,n]     = j[1] 
            
    
    ## Leemos cargas elásticas
    
    LOAD                      = []  
    Ld                        = {}   ## eslabones de oferta de compra en piecewise
    names_loads               = []  
    piecewise_production_load = []
    Piecewise_load            = []    
    Pd                        = {}   ## maximum load for piecewise segment LD for a load "load"(MW).
    Cd                        = {}   ## bid of a load "load" consuming Pd MW of power ($/h).
    try:
        i = 1
        ## Se obtiene nombre de las cargas elásticas y el número total
        for load in md['loads']:  
            names_loads.append(load)
            LOAD.append(i)
            i+=1   
        
        i=1 ## Cuenta las cargas
        for load in names_loads:
            piecewise_production_load = md['loads'][load]["piecewise_production"] # bids offer      
            ## Para obtener los piecewise del costo de los generadores
            lista_aux = []
            j = 0
            for piece in piecewise_production_load:
                lista_aux.append((piece['mw'],piece['cost']))
                j += 1            
            Piecewise_load.append(lista_aux)
            lista = []
            jj = 1
            for ii in range(j):
                lista.append(jj)
                jj = jj + 1
            Ld[i] = lista
            i += 1
                    
        k = 0; n = 0
        for i in Piecewise_load:
            # print(i)
            k = k+1
            n = 1
            for j in i:                
                # print(j)
                # print(k,",",n,",",j[0],",",j[1])
                Pd[k,n] = j[0]
                Cd[k,n] = j[1]               
                n = n+1
        # print('Cd',Cd)
        # print('Pd',Pd)

    except:
        print('reading.py sin información de cargas elásticas')
    
    ## Prohibid operating zones
    GRO   = []    
    oz    = []
    noz   = [] 
    toz   = []
    minoz = [] ## operating zones
    maxoz = [] ## operating zones
    romin = [] ## operating zones
    romax = [] ## operating zones
    try: 
        ## Read generators with prohibid operative zones
        for item in md['operative_zones']['GRO']:  
            GRO.append(item)
        
        ## Read operative zones
        i=0
        for item in md['operative_zones']['oz']:
            minoz.append(item['min'])
            maxoz.append(item['max'])
            i=i+1
            noz.append(i)
        for item in GRO:
            oz.append(noz)
        for i in GRO:
            for j in noz:
                toz.append((i,j))        
        for item in toz:
            #print(power_output_maximum[item[0]-1],minoz[item[1]-1],maxoz[item[1]-1])
            romin.append( power_output_maximum[item[0]-1]*minoz[item[1]-1]*0.01 )
            romax.append( power_output_maximum[item[0]-1]*maxoz[item[1]-1]*0.01  )                
        
    except:        
        print('reading.py sin información de zonas prohibidas')
    
    # print('oz',oz)
    # print('noz',noz) 
    # print('toz',toz)  
    # print('minoz',minoz)  
    # print('maxoz',maxoz)  
    # print('romin',romin)  
    # print('romax',romax)  
    
    # GRO    = [1, 3]
    # RO     = {1: [1, 2, 3], 3: [1, 2, 3]}
    # ROmin  = {(1, 1):  0, (1, 2): 100, (1, 3): 230,    (3, 1):  0, (3, 2): 60, (3, 3): 95}   
    # ROmax  = {(1, 1): 50, (1, 2): 150, (1, 3): 305,    (3, 1): 41, (3, 2): 91, (3, 3): 100}   
    # print('GRO',GRO)
    # print('RO',RO)  
    # print('ROmin',ROmin)
    # print('ROmax',ROmax)   
    
    ## Aqui se pasan de arreglos a diccionarios como los usa Pyomo
    Pmax   = dict(zip(G, power_output_maximum))
    Pmin   = dict(zip(G, power_output_minimum))
    UT     = dict(zip(G, time_up_minimum     ))     
    DT     = dict(zip(G, time_down_minimum   ))  
    u_0    = dict(zip(G, u_0_list            ))          
    U      = dict(zip(G, Ulist               ))              
    D      = dict(zip(G, Dlist               ))             
    TD_0   = dict(zip(G, TD0list             ))                
    SU     = dict(zip(G, ramp_startup_limit  ))
    SD     = dict(zip(G, ramp_shutdown_limit ))
    
    SUD    = dict(zip(G,       SUD           ))
    PSU    = dict(zip(PSUindex,PSU           ))   
    SDD    = dict(zip(G,       SDD           ))
    PSD    = dict(zip(PSDindex,PSD           ))
        
    RU     = dict(zip(G, ramp_up_limit       ))
    RD     = dict(zip(G, ramp_down_limit     ))
    p_0    = dict(zip(G, p_0_list            ))  
    names  = dict(zip(G, names_gens          ))  
    CR     = dict(zip(G, fixed_cost          ))
    
    RO     = dict(zip(GRO, oz                ))   
    ROmin  = dict(zip(toz, romin             ))   
    ROmax  = dict(zip(toz, romax             ))   
    
    ## Para obtener los Psu y los Psd 
    # for i in Pmin:
    #     if SU[1]<Pmin[i]:
    #         print('Pmin',Pmin[i],SU[1])
            
    ## Artificialmente creamos ofertas de venta de reservas    
    Crr   = []  
    Cs10  = []   
    Cs30  = []   
    Cns10 = []   
    Cns30 = []  
    Cordc = []      
    RRe   = []  
    RR10  = []   
    RR30  = []   
    RN10  = []   
    RN30  = []  
    ORDC  = [] ## Segments of ORDC
    RCO   = [] ## Limits of MW for each ORDC segment   
        
    RCO.append(24.0)   # 5 MW    
    RCO.append(22.0)   # 5 MW       
    RCO.append(20.0)   # 5 MW       
    RCO.append(18.0)   # 5 MW       
    RCO.append(16.0)   # 5 MW       
    RCO.append(14.0)   # 5 MW       
    RCO.append(12.0)   # 5 MW       
    RCO.append(10.0)   # 5 MW       
    RCO.append(8.0)    # 5 MW       
    RCO.append(6.0)    # 5 MW       
    RCO.append(4.0)    # 5 MW       
    RCO.append(2.0)    # 5 MW       
    
    Cordc.append(15.0)   # 5 MW    
    Cordc.append(14.0)   # 5 MW       
    Cordc.append(13.0)   # 5 MW       
    Cordc.append(12.0)   # 5 MW       
    Cordc.append(11.0)   # 5 MW       
    Cordc.append(10.0)   # 5 MW       
    Cordc.append(9.0)    # 5 MW       
    Cordc.append(8.0)    # 5 MW       
    Cordc.append(7.0)    # 5 MW       
    Cordc.append(6.0)    # 5 MW       
    Cordc.append(5.0)    # 5 MW       
    Cordc.append(4.0)    # 5 MW       
     
    ## Crea segmentos ORDC
    for i in range(1,len(RCO)+1):
        ORDC.append(i) 
        
    for i in G:
        Crr.append(  1.0) # $ 1
        Cs10.append( 1.0) # $ 1
        Cs30.append( 1.0) # $ 1
        Cns10.append(1.0) # $ 1
        Cns30.append(1.0) # $ 1
        RRe.append(2.0)   # $ 1
        RR10.append(2.0)  # $ 1
        RR30.append(2.0)  # $ 1
        RN10.append(2.0)  # $ 1
        RN30.append(2.0)  # $ 1
           
    Crr      = dict(zip(G    , Crr   ))
    Cs10     = dict(zip(G    , Cs10  ))
    Cs30     = dict(zip(G    , Cs30  ))
    Cns10    = dict(zip(G    , Cns10 ))
    Cns30    = dict(zip(G    , Cns30 ))    
    RRe      = dict(zip(G    , RRe   ))
    RR10     = dict(zip(G    , RR10  ))
    RR30     = dict(zip(G    , RR30  ))
    RN10     = dict(zip(G    , RN10  ))
    RN30     = dict(zip(G    , RN30  ))
    Cordc    = dict(zip(ORDC , Cordc ))
    RCO      = dict(zip(ORDC , RCO   ))

    instance = [G,T,L,S,Pmax,Pmin,UT,DT,De,R,u_0,U,D,TD_0,SU,SUD,PSD,SD,SDD,PSU,RU,RD,p_0,Pb,Cb,C,CR,Cs,Tunder,names,
                LOAD,Ld,Pd,Cd, 
                GRO,RO,ROmin,ROmax, 
                Crr,Cs10,Cs30,Cns10,Cns30,RRe,RR10,RR30,RN10,RN30,ORDC,Cordc,RCO,
                TSg,TDg]
        
            
    return instance