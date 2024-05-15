#Ejercicio28
medx= float(input('Ingrese medida de frente: '))
medy= float(input('Ingrese medida de fondo: '))
per= (medx+medy+medy)
sup=(medx*medy)
if medx==medy:
    print('terreno cuadrado')
elif medx!=medy:
    print('terreno rectangular')
    print('El perimetro es: ',per)
    print('La superficie es de: ',sup)
    
#Entradas
frente= float(input('Ingrese la medida del frente: '))
fondo= float(input('Ingrese la medida del fondo: '))
#proceso y salida
perCuadrado= 4* frente
perRectangulo= 2* frente +2*fondo
supRectangulo= frente*fondo

if frente== fondo:
    print('Terreno cuadrado')
    print('El perimetro es: ,perCuadrado')
    print('La superficie es de: ',perRectangulo')
    
    
    