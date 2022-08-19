  # tarea de computacion avanzada 
import random
import numpy as np  

def listaaleatorio(x):
      """
     funcion para generar una lista de numeros aleatorrios cuya longiutd es igual a m
     return 
     -------------
     x longitud de la lista
     """
      lista =[0] * x
      for i in range(x):
          a= random.randint(-3,3)
          if a !=0 :
              lista[i]=a
          else:
              pass     
      return lista 
  
def sorting(number_array):
    """"
    funcion usada para organizar los array en valor absoluto
    """
    
    util=[]
    for i in number_array: 
        for j in number_array:
            c=sorted(j,key=abs,reverse=True)
            util.append(c)
            
        return util
##pedirle un numero al usuario

n=6
# comprobando que n sea un numero para o impar 
if n%2==0:
    print("even")
    m = ((n/2)-1)
    m = int(m)    
    total=[]   
    for i in range(10000):
    ###### llenado de listas l y k 
        l= listaaleatorio(m)   
        #rint(l)
        k = listaaleatorio(m) 
        #rint(k)
        # construcionde los vector likes vplus and vminus

        a=[l[0]]
        b=k
        c=[-l[0]]
        d=[numero*-1 for numero in k]
        vplus= a + b + c + d 
        #print( "vplus :",vplus)
        # construcion de vector Vminus 
        a1=[0,0]
        b1=l
        c1=[numero*-1 for numero in l]
        vminus= a1 + b1 + c1  
        #print( "vplus :",vminus)
        # creacion de la funcion merger 
        k=np.array(k)
        l=np.array(l)
        vplus= np.array(vplus)
        vminus= np.array(vminus)
        z = np.array((vplus*(vminus**2)).sum()*vplus -((vplus**2)*vminus).sum()*vminus)
        #print(z,i)
        # COMPARACION DE V
        
        zplus= z[z>=0]
        #print(zplus)

        zminus= z[z<0]
        #print(zminus)
        zminus = zminus*(-1)

        c= np.isin(zplus,zminus).any()
        nceros=len(z[z==0])
        
        if c== True or nceros > 0:
            pass   
        else:
            total.append(z)  
            
            
    #convierto un total en un array
    total =np.array(total) 
    # uso la funcion unique para encontrar los valores que no se repiten
    total = np.unique(total,axis=0)
    final =[]
    for i in total:
        for j in total:
            d=np.array(j/np.gcd.reduce(j))
            final.append(d)
            
     
    #uso de la funcion sorting para ordenacion en valor absoluto 
    final=sorting(final)
    # organiza los arrays al reves
    #final1=[]
    #for i in final:
            #c=i[::-1]
            #final1.append(c)
           
            
    final1=np.array(final) 
    final1 =np.unique(final1,axis=0)
    
    final1=final1[final1[:,0]<30]
    final1=final1[final1[:,0]>-30]
    final=final1.astype(int)
    print(final)   

#construccion de parte en en caso de que sea impar 
else:
   print("odd")
   m=(n-3)/2
   m=int(m)
   total=[]
   for i in  range(2500):
       l= listaaleatorio(m)   
       #rint(l)
       k = listaaleatorio(m+1)
       #rint(k)
       # construcionde los vector likes vplus and vminus
       a=[0]
       b=k
       c=[numero*-1 for numero in k]
       uplus= a + b + c  
      #print( "Uplus",uplus)
       # construcion de vector uminus 
       a1=l
       b1=[k[0]]
       c1=[0]
       d1=[numero*-1 for numero in l]
       e1=[-k[1]]
       uminus= a1 + b1 + c1  + d1 + e1
      #print( "uminu",uminus)
       # creacion de la funcion merger 
       k=np.array(k)
       l=np.array(l)
       uplus= np.array(uplus)
       uminus= np.array(uminus)
       z = np.array((uplus*(uminus**2)).sum()*uplus -((uplus**2)*uminus).sum()*uminus)
       #print(z,i)
       # COMPARACION DE z
       
       zplus= z[z>=0]
       #print(zplus)

       zminus= z[z<0]
       #print(zminus)
       zminus = zminus*(-1)

       c= np.isin(zplus,zminus).any()
       nceros=len(z[z==0])
       
       if c== True or nceros > 0:
           pass   
       else:
           total.append(z)  

     #convierto un total en un array
   total =np.array(total) 
     # uso la funcion unique para encontrar los valores que no se repiten
     #le pido que me organise los valores dentro del array de arrays
   total= np.sort(total)
   total = np.unique(total,axis=0)
   final =[]
     #elimino los arrays que tiene z mayor a 12
   for i in total:
         for j in total:
             d=np.sort(np.array(j/np.gcd.reduce(j)))
             final.append(d)
   final =np.unique(final,axis=0)  
   print(final.astype(int))
    
   for i in final:
         print(i)
   print(len(final))
   
     
