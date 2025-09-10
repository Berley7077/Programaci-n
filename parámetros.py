#Parámetros por valor y referencia 
#definimos una función que recibe un num
def por_valor (x):
    #Dentro de la f, sumar un 6 al valor recibido
    x+= 6
    print("Dentro por_valor:", x)
    #Definimos una función por medio de lista 
def por_referencia (lista):
    #Se agrega el número 99 a la lista.
    lista.append (99)
    print("Dentro por_referencia", lista)
#Ejemplo con número entero
n->5
por_valor (n)
print("fuera n=",)
#Ejemplo con lista 
num =[1,2]
por_referencia (num)
print("fuera num=", num)
