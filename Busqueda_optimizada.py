#Busqueda optimizada 
import  pandas as pd
from googlesearch import search
google_query= str(input("Ingrese la palabra a buscar"))
link = list()
count=0

for i in search(google_query,start = 0,pause =2):
    if count<30:
        link.append(i)
        print(i)
    else: break
    count+=1
df =pd.DataFrame({'link':link},index=list(range(1,31)))
  
df.to_csv('link.csv',index= False)
