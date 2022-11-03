import sys
import util
from   Extract import Extract

## --------------------------------- GRAFICAS -------------------------------------------

instancia = 'archivox.json' ## ejemplo sencillo

instancia = 'uc_56.json'    ## ejemplo de batalla  
instancia = 'uc_55.json'    ## ejemplo de batalla  
instancia = 'uc_54.json'    ## ejemplo de batalla  
instancia = 'uc_53.json'    ## ejemplo de batalla  
instancia = 'uc_51.json'    ## ejemplo de batalla  
instancia = 'uc_50.json'    ## ejemplo de batalla  
instancia = 'uc_49.json'    ## ejemplo de batalla  
instancia = 'uc_48.json'    ## ejemplo de batalla  
instancia = 'uc_47.json'    ## ejemplo de batalla  
instancia = 'uc_46.json'    ## ejemplo de batalla  
instancia = 'uc_45.json'    ## ejemplo de batalla  

instancia = 'uc_38.json'    ## ejemplo medio 
instancia = 'uc_39.json'    ## ejemplo medio 
instancia = 'uc_40.json'    ## ejemplo medio 
instancia = 'uc_41.json'    ## ejemplo medio 
instancia = 'uc_43.json'    ## ejemplo medio 

#instancia = 'uc_02.json'   ## ejemplo de batalla 
#instancia = 'uc_22.json'   ## ejemplo de batalla 
#instancia = 'uc_21.json'   ## ejemplo de batalla 
#instancia = 'uc_02.json'   ## ejemplo de batalla 
#instancia = 'uc_01.json'   ## ejemplo de batalla 
#instancia = 'uc_24.json'   ## ejemplo de batalla 
instancia  = 'uc_80.json'   

## Cargamos parámetros de configuración desde archivo <config>
ambiente, ruta, executable, timeheu, timemilp, emph, symmetry, gap, k, iterstop = util.config_env()
if ambiente == 'yalma':
    if len(sys.argv) != 2:
        print("!!! Something went wrong, try write something like: $python3 ploting.py uc_02")
        print("archivo :", sys.argv[1])
        sys.exit()
    instancia = sys.argv[1]

##Recordar que el pibote es el tercer dataframe bb3

# print('Ploting '+instancia[0:5]+'.log')
# bb1,vari = Extract().extract('logfile'+'Milp'+instancia[0:5]+'.log')  
# bb2,vari = Extract().extract('logfile'+'Hard'+instancia[0:5]+'.log') 
# bb3,vari = Extract().extract('logfile'+'Soft7'+instancia[0:5]+'.log')   
# Extract().plot_four_in_one(bb1,bb2,bb3,'Milp','Hard','Soft7',instancia[0:5],id='a')

bb1,vari = Extract().extract('logfile'+'Milp' +instancia[0:5]+'.log') 
bb2      = Extract().read_LBC('iterLBC1'+instancia[0:5]+'.csv')
bb3      = Extract().read_LBC('iterLBC2'+instancia[0:5]+'.csv')
 
print(bb2)
print(bb3)

# bb2,vari = Extract().extract('logfile'+'Milplb' +instancia[0:5]+'.log') 
# bb3,vari = Extract().extract('logfile'+'Milplbsym'+instancia[0:5]+'.log')    
#Extract().plot_four_in_one(bb1,bb2,bb3,'Milp','Hard3','Milp',instancia[0:5],id='a')

#Extract().plot_four_in_one(bb1,bb2,bb1,'Milp','LBC1','Milp',instancia[0:5],id='a')

Extract().plot_all_in_one(bb1,bb2,bb3,'CPLEX','LBC1','LBC2',instancia[0:5],id='')



# bb1,vari = Extract().extract('logfile'+'lbc1' +instancia[0:5]+'.log') 
# bb2,vari = Extract().extract('logfile'+'Hard' +instancia[0:5]+'.log') 
# bb3,vari = Extract().extract('logfile'+'Soft7'+instancia[0:5]+'.log')    
# Extract().plot_four_in_one(bb1,bb2,bb3,'lbc0','Hard','Soft7',instancia[0:5],id='b')


