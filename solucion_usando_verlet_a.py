from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt
#Condiciones iniciales
condicion_inicial = [10, 0, 0, 0.27]  #Escogi Vy=0.27
p=Planeta(condicion_inicial, 10**(-2.312)) #Se agrega el nuevo valor de alfa

Pasos=600000                                       #Los fui aumentando y con este valor alto se tiene
h=4500/Pasos                                        #menor margen de error. Además observando con 
T=np.linspace(0,4500, Pasos)                  #distintos tiempos, note que con t=4500 se dan las
x=[10]                                                    #30 vueltas
y=[0]
Ene=[p.EneActual]

N=1       #Variable auxiliar para interar
while N<Pasos:            #Aplica el metodo de verlet definido en la clase planeta.
    p.avanza_verlet(h)
    N+=1
    x.append(p.y_actual[0])
    y.append(p.y_actual[1])
    p.energia_total()
    Ene.append(p.EneActual)
#Plots
fig=plt.figure()
fig.add_subplot(211)
plt.plot(x,y)
plt.title('$Trayectoria$ $y$ $Energia$ $vs$ $Tiempo$ \n $Verlet$ $Con$ $v_{y}(0)=0.27$ $y$ $a$ $distinto$ $de$ $cero$')
plt.xlabel('$x$')
plt.ylabel('$y$')
fig.add_subplot(212)
plt.plot(T, Ene)
plt.xlabel('$Tiempo$')
plt.ylabel('$Energia$')
plt.show()
fig.savefig('verlet_a.png')
#Ajuste de variables para rellenar con datos
r=[]
rMin=[]
Angulos=[]
Tiempos=[]
W=[]
Wtot=0
for a in range(len(x)):                                        #Agregando todos los radios
    r.append(np.sqrt(x[a]**2+y[a]**2))
for a in range(len(x)-2):                                     #Metodo que detecta los radios minimos
    if r[a+1]<r[a] and r[a+1]<r[a+2]:
        rMin.append(r[a+1])
        alfa=np.arctan((abs(y[a+1]))/abs(x[a+1]))   #Calcula el valor absoluto para tener angulo positivo
        Angulos.append(alfa)                               #utilizando trigonometria

        Tiempos.append((a+1)*4500/600000)        #Se divide en 600000 para normalizar los pasos al tiempo
                                                                     #luego se multiplica por 4500 el tiempo real
for a in range(len(Angulos)-1):                           #Metodo para calcular la velocidad rotacional
    omega=(Angulos[a+1]-Angulos[a])/(Tiempos[a+1]-Tiempos[a])
    W.append(omega)                                       #Agrega todas las 'derivadas' de los angulos
for a in W:
    Wtot+=a                                                     #Suma todas las velocidades
print('La velocidad angular promedio es: '+str(round(Wtot/len(W),8))) #Finalmente se divide por la cantidad de velocidades calculadas

