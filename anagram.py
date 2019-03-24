
palabra1 = "roma"
palabra2 = "amor"
#palabra1 = "enfriamiento"
#palabra2 =  "refinamiento"
lista1 = list(palabra1)
lista2 = list(palabra2)
for i in palabra1:
    if (i in palabra2) :
        #lista1.pop(0) 
        #indice = lista2.index(i)
        try :
            indice = lista2.index(i)
            lista1.pop(0) 
            lista2.pop(indice)
        except:
            exit 
            
        #if lista2.index(i) : 
        #   lista2.pop(indice)
      
if lista1 == [] and lista2 == []:
    print("es anagrama pop ")
else:
    print("no es anagrama pop ")
    







palabra1 = "rama"
palabra2 = "amor"
#palabra1 = "enfriamiento"
#palabra2 =  "refinamiento"
lista1 = list(palabra1)
lista2 = list(palabra2)

i = 0
while i < len(palabra1):
    if (palabra1[i] in palabra2) and len(palabra1) == len(palabra2):
        try :
           lista1 = lista1[i+1:len(palabra1)]
           indice = lista2.index(palabra1[i])
           lista2.pop(indice)
        except:
            exit
    i = i + 1
    
if lista1 == [] and lista2 == []:
    print("es anagrama while - slicing")
else:
    print("no es anagrama while - slicing")



           
