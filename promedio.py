Nota1=int(input("Ingrese la primera nota"))
Nota2=int(input("Ingrese la segunda nota"))
Nota3=int(input("Ingrese la tercera nota"))
prom= (Nota1+Nota2+Nota3)/3
if prom>=6:
 print("APROBADA")
else:print("NO APROBADA") 
print(f"EL promedio de las notas es",prom)

#si queremos verlo en la manera de que cada nota individual sea aprobada o no
Nota1=int(input("Ingrese la primera nota"))
Nota2=int(input("Ingrese la segunda nota"))
Nota3=int(input("Ingrese la tercera nota"))
if Nota1>=6:
   print(" NOTA 1 APROBADA")
else:print(" NOTA 1 NO APROBADA") 
if Nota2>=6:
   print(" NOTA 2 APROBADA")
else:print(" NOTA 2 NO APROBADA") 
if Nota3>=6:
   print(" NOTA 3 APROBADA")
else:print("NOTA 3 NO APROBADA") 
