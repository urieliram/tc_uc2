# from xmlrpc.client import MININT
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

## Online version
## https://colab.research.google.com/drive/15mttuecwMf7bfe6hvb8uK2sAhqsQ2Gkw#scrollTo=kiJzGJszxwGu

class Extract:
  def findPos(self,file,spected, starter = "Node  Left"):
    file = open(file,"r")
    for i,j in enumerate(file):
      if starter in j:
        return [(j.index(k)+len(k)-1) for k in spected]
  
  def getFilelog(self,f):
    with open(f, 'r') as file:
      data = file.read().replace('\n', '')
    tmp = []
    for i in re.findall(r"\w*Logfile\s*\'*[a-zA-z.+]*\'",data):
      tmp.append(i.replace("'","").split(" ")[1])
    return tmp

  def createTables(self,fn):
    table_start = False
    spected = ['Node', 'Left', 'Objective', 'IInf', 'Integer', 'Bound', 'ItCnt', 'Gap']
    expectedPositions = self.findPos(fn,spected)
    tables = {"seconds":[],"ticks":[],"solution":[],"Node":[],"Left":[],"Objective":[],"IInf":[],"Integer":[],"Bound":[],"ItCnt":[],"Gap":[],"cuts":[]}
    time = None
    ticks = None
    cuts = None
    f = open(fn,"r")
    for i in f:
      if re.findall(r"\d{1,}[+]{1}\d{1,}",i):
        i = " ".join(i.split("+"))
      if("Cover cuts applied" in i or "Performing restart 1" in i):
        table_start = False
      if("Elapsed time" in i):
          tmp = [float(k) for k in re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)]
          time = tmp[0]
          ticks = tmp[1]
      if(table_start):        
        if((str(i)[0] == " " or str(i)[0] == "*") and str(i)[expectedPositions[0]].isdigit()):
          i = i.replace("uts: "," uts:")
          tables["seconds"].append(time)
          tables["ticks"].append(ticks)
          tables["solution"].append(1 if i[0]=="*" else 0)
          tables["cuts"].append(None)
          for j,m in zip(expectedPositions,spected):
            if i[j] != " ":
              tmp = ""
              for k in range(j,0,-1):
                if i[k] != " ":
                  tmp += i[k]
                else: 
                  break 
              tmp = tmp[::-1]
              if("ut" in tmp.lower() or "infeasible" in tmp.lower() or "integral" in tmp.lower()):
                if("uts" in tmp.lower()):
                  tables["cuts"][-1] = int(tmp.split(":")[1])
                tables[m].append(tables[m][-1])
              else:
                if m == "Gap":
                  tables[m].append(float(tmp)/100)
                else: 
                  tables[m].append(float(tmp))
            else:
              tables[m].append(None)
      if("Node  Left"):
        table_start = True
    return tables

  def extract(self,fn,t_hard=0):
    variables = {"mipPresolveEliminated":[],"mipPresolveModified":[],"aggregatorDid":[],"reducedMipHasColumns":[],"reducedMipHasNonZero":[],"reducedMipHasBinaries":[],"reducedMipHasGeneral":[],"cliqueTableMembers":[],"rootRelaxSolSeconds":[],"rootRelaxSolTicks":[]}
    variables["logFile"] = self.getFilelog(fn)
    tables = self.createTables(fn)
    f = open(fn, "r")    
    for i in f:
      if("linear optimization" in i):
        variables["linearOpt"] = float(i.replace(" ","").replace("\n","").split(":")[1])
      if("optimality gap tolerance" in i):
        variables["gapTol"] = float(i.replace(" ","").replace("\n","").split(":")[1])
      if("time limit in seconds" in i):
        variables["timeLimit"] = float(i.replace(" ","").replace("\n","").split(":")[1])
      if("emphasis for MIP optimization" in i):
        variables["mipOpt"] = float(i.replace(" ","").replace("\n","").split(":")[1])
      if("Objective sense" in i):
        variables["objSense"] = i.replace(" ","").replace("\n","").split(":")[1]
      if("Variables" in i):
        if("Box:" in i):
          variablesValue = ["variablesValue","Nneg","Box","Binary"]
          for j,k in enumerate(re.findall(r'\d+', i.replace(" ","").replace("\n","").split(":",1)[1])):
            variables[variablesValue[j]] = float(k)
        else:
          variablesValue = ["minLB","maxUb"]
          for j,k in enumerate(re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)):
            variables[variablesValue[j]] = float(k)
      if("Objective nonzeros" in i):
        if("Min" in i or "Max" in i):
          variablesValue = ["objNonZerosMin","objNonZerosMax"]
          for j,k in enumerate(re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)):
            variables[variablesValue[j]] = float(k)
        else:
          variables["objNonZeros"] = float(i.replace(" ","").replace("\n","").split(":")[1])
      if("Linear constraints" in i):
        if("Less" in i):
          variablesValue = ["linearConstraintsValue","less","greater","equal"]
          for j,k in enumerate(re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)):
            variables[variablesValue[j]] = float(k)
        else:
          pass
      if("Nonzeros" in i):
        if("Min" in i):
          variablesValue = ["nonZerosMin","nonZerosMax"]
          for j,k in enumerate(re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)):
            variables[variablesValue[j]] = float(k)
        else:
          variables["nonZeros"] = float(i.replace(" ","").replace("\n","").split(":")[1])
      if("RHS nonzeros" in i):
        if("Min" in i):
          variablesValue = ["rhsNonZerosMin","rhsNonZerosMax"]
          for j,k in enumerate(re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)):
            variables[variablesValue[j]] = float(k)
        else:
          variables["rhsNonZeros"] = float(i.replace(" ","").replace("\n","").split(":")[1])
      if("CPXPARAM_TimeLimit" in i):
        variables["CPXPARAM_TimeLimit"] = float(i.replace("\n","").split(" ")[-1])
      if("MIP Presolve eliminated" in i):
        variables["mipPresolveEliminated"].append([int(k) for k in re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)])
      if("MIP Presolve modified " in i):
        variables["mipPresolveModified"].append(int(re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)[0]))
      if("Reduced MIP has" in i):
        if("indicators." in i):
          tmp = [int(k) for k in re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)]
          variables["reducedMipHasBinaries"].append(tmp[0])
          variables["reducedMipHasGeneral"].append(tmp[1])
        else:
          tmp = [int(k) for k in re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)]
          variables["reducedMipHasColumns"].append(tmp[1])
          variables["reducedMipHasNonZero"].append(tmp[-1])
          reduceHasGeneral = []
      if("Clique" in i):
        variables["cliqueTableMembers"].append(float(i.replace(" ","").replace("\n","").split(":")[1]))
      if("Aggregator did" in i):
        variables["aggregatorDid"].append(int(re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)[0]))
      if("Root relaxation" in i):
        tmp = [float(k) for k in re.findall('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',i)]
        variables["rootRelaxSolSeconds"].append(tmp[0])
        variables["rootRelaxSolTicks"].append(tmp[1])
      if("Lift and" in i):
        variables["liftAndProjectCuts"] = int(i.replace(" ","").replace("\n","").split(":")[1])
      if("Gomory fractional" in i):
        variables["gomoryFract"] = int(i.replace(" ","").replace("\n","").split(":")[1])
        
    ## ------------------------------- Limpia seconds --------------------------------------------------
    df=pd.DataFrame.from_dict(tables).rename(columns={"seconds":"seconds","ticks":"ticks","solution":"solution","Node":"node","Left":"nodesLeft","Objective":"objective","IInf":"iinf","Integer":"bestInteger","Bound":"BestBound","ItCnt":"itCnt","Gap":"gap","cuts":"cuts"})
    df['seconds'] = df['seconds'].fillna(0)
    eps=np.arange(0, 1, 1/(len(df)), dtype=float)
    df['eps'] = eps
    sum_column = df["seconds"] + df["eps"]
    df["seconds"] = sum_column
    df['ticks'] = df['ticks'].fillna(0)
    eps=np.arange(0, 1, 1/(len(df)), dtype=float)
    df['eps'] = eps
    sum_column = df["ticks"] + df["eps"]
    df["ticks"] = sum_column  
    return df,variables
    
    
    
  def read_LBC(self,file):
    df = pd.read_csv(file)
    df.columns = ['seconds', 'bestInteger']
    df['BestBound'] = df['bestInteger']
    df['gap'] = 0
    return df
    
     

  def plot_four_in_one(self,df1,df2,df3,name1='MILP',name2='Hard-fix',name3='Soft-fix',nameins='',id=''):        
    ## https://pandas.pydata.org/pandas-docs/version/0.20.1/visualization.html
    #try:
    if True:
        ## https://pandas.pydata.org/pandas-docs/version/0.20.1/visualization.html
        ## https://matplotlib.org/3.5.0/tutorials/colors/colors.html
        fig, axa = plt.subplots(2, 2, figsize=(9,7))
        ## Imprime costo
        ax1=df1.plot.line( x='seconds',y='bestInteger',color='magenta',style='o-',label='',ax=axa[0,0])
        #ax2=df.plot.line( x='seconds',y='BestBound'  ,color= ax1.lines[-1].get_color(),style='o-',label=name1,ax=ax1)
        ax2=df1.plot.line( x='seconds',y='BestBound'  ,color='magenta',style='o-',label=name1,ax=ax1)

        ax3=df3.plot.line(x='seconds',y='bestInteger',color='blue',style='o-',label='',ax=ax2)
        df3.plot.line(    x='seconds',y='BestBound'  ,color='blue',style='o-',label=name3 ,ax=ax3)
        ## Legend except 1st lines/labels
        lines, labels = ax2.get_legend_handles_labels()
        ax2.legend(lines[0:], labels[0:])
        ## Imprime gap
        ax4=df1.plot.line( x='seconds',y='gap',color='magenta',style='o-',label=name1,ax=axa[1,0])
        df3.plot.line(    x='seconds',y='gap',color='blue' ,style='o-',label=name3,ax=ax4)  
        ax4.set(ylabel='gap') 
        ax2.set(ylabel='cost')

        ## Imprime costo
        ax5=df2.plot.line(x='seconds',y='bestInteger',color='orangered',style='o-',label='',ax=axa[0,1])
        ax6=df2.plot.line(x='seconds',y='BestBound'  ,color='orangered',style='o-',label=name2,ax=ax5)
        ax7=df3.plot.line(x='seconds',y='bestInteger',color='blue'     ,style='o-',label='',ax=ax6)
        df3.plot.line(    x='seconds',y='BestBound'  ,color='blue'     ,style='o-',label=name3,ax=ax7)
        ## Legend except 1st lines/labels
        lines, labels = ax6.get_legend_handles_labels()
        ax6.legend(lines[0:], labels[0:])
        ## Imprime gap
        ax8=df2.plot.line(x='seconds',y='gap',style='o-',color='orangered',label=name2,ax=axa[1,1])
        df3.plot.line(    x='seconds',y='gap',style='o-',color='blue',label=name3,ax=ax8)
        ax8.set(ylabel='gap') 
        ax5.set(ylabel='cost')
        
        # mini=197871658.6
        # maxi=199871658.6
        # ax1.axis([0,  6000, mini, maxi])
        # ax2.axis([0,  6000, mini, maxi])
        # ax3.axis([0,  6000, mini, maxi])
        # ax4.axis([0,  6000, mini, maxi])
        # ax5.axis([0,  6000, mini, maxi])
        # ax6.axis([0,  6000, mini, maxi])
        # ax7.axis([0,  6000, mini, maxi])
        # ax8.axis([0,  6000, mini, maxi])
        

        plt.suptitle('instance: '+nameins, fontsize=14)
        plt.style.use('seaborn-pastel') ## ggplot seaborn-pastel Solarize_Light2 https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
        plt.savefig('four_in_one_'+nameins+'_'+id+'.png', transparent=True)  
        plt.show()
        
    #except:
        #print('Error en <plot_four_in_one>')
      
    return 0



  def plot_all_in_one(self,df1,df2,df3,name1='MILP',name2='Hard',name3='LBC',nameins='',id=''):     

    ## https://pandas.pydata.org/pandas-docs/version/0.20.1/visualization.html
    #try:
    if True:
        ## https://pandas.pydata.org/pandas-docs/version/0.20.1/visualization.html
        ## https://matplotlib.org/3.5.0/tutorials/colors/colors.html
        fig, axa = plt.subplots(1, 1, figsize=(9,7))
        ## Imprime costo
        ax1=df1.plot.line( x='seconds',y='bestInteger',color='magenta',style='o-',label='',ax=axa)
        #ax2=df.plot.line( x='seconds',y='BestBound'  ,color= ax1.lines[-1].get_color(),style='o-',label=name1,ax=ax1)
        ax2=df1.plot.line( x='seconds',y='BestBound'  ,color='magenta',style='o-',label=name1,ax=ax1)

        ax3=df3.plot.line(x='seconds',y='bestInteger',color='blue',style='o-',label='',ax=ax2)
        df3.plot.line(    x='seconds',y='BestBound'  ,color='blue',style='o-',label=name3 ,ax=ax3)
        ## Legend except 1st lines/labels
        lines, labels = ax2.get_legend_handles_labels()
        ax2.legend(lines[0:], labels[0:])
        ## Imprime gap
        # ax4=df1.plot.line( x='seconds',y='gap',color='magenta',style='o-',label=name1,ax=axa)
        # df3.plot.line(    x='seconds',y='gap',color='blue' ,style='o-',label=name3,ax=ax4)  
        # ax4.set(ylabel='gap') 
        # ax2.set(ylabel='cost')

        ## Imprime costo
        ax5=df2.plot.line(x='seconds',y='bestInteger',color='orangered',style='o-',label='',ax=axa)
        ax6=df2.plot.line(x='seconds',y='BestBound'  ,color='orangered',style='o-',label=name2,ax=ax5)
        #ax7=df3.plot.line(x='seconds',y='bestInteger',color='blue'     ,style='o-',label='',ax=ax6)
        #df3.plot.line(    x='seconds',y='BestBound'  ,color='blue'     ,style='o-',label=name3,ax=ax7)
        ## Legend except 1st lines/labels
        lines, labels = ax6.get_legend_handles_labels()
        ax6.legend(lines[0:], labels[0:])
        ## Imprime gap
        # ax8=df2.plot.line(x='seconds',y='gap',style='o-',color='orangered',label=name2,ax=axa)
        # df3.plot.line(    x='seconds',y='gap',style='o-',color='blue',label=name3,ax=ax8)
        # ax8.set(ylabel='gap') 
        # ax5.set(ylabel='cost')
                    
        # mini=198650000
        # maxi=199000000
        # minitime=0
        # maxitime=3500
        # ax1.axis([minitime, maxitime, mini, maxi])
        # ax2.axis([minitime, maxitime, mini, maxi])
        # ax3.axis([minitime, maxitime, mini, maxi])
        # ax5.axis([minitime, maxitime, mini, maxi])
        # ax6.axis([minitime, maxitime, mini, maxi])
        # plt.axis([minitime, maxitime, mini, maxi])   
        
        plt.suptitle('instance: '+nameins, fontsize=14)
        plt.style.use('seaborn-pastel') ## ggplot seaborn-pastel Solarize_Light2 https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
        plt.savefig('four_in_one_'+nameins+'_'+id+'.png', transparent=True)  
        plt.show()
         
    #except:
        #print('Error en <plot_four_in_one>')