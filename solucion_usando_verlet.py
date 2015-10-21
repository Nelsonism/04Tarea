from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt
#Condiciones iniciales
condicion_inicial=[10, 0, 0, 0.27] #Escogi Vy=0.27
p=Planeta(condicion_inicial)

Pasos=8000                          #Aca la cantidad de pasos no influye mucho, pero
h=800/Pasos                         #se observo que con tiempo de 800 da las 5 vueltas
T=np.linspace(0,800, Pasos)
x=[10]
y=[0]
Ene=[p.EneActual]

N=1            #Variable auxiliar para interar
while N<Pasos:         #Aplica el metodo de verlet definido en la clase planeta.
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
plt.title('$Trayectoria$ $y$ $Energia$ $vs$ $Tiempo$ \n $Verlet$ $Con$ $v_{y}(0)=0.27$')
plt.xlabel('$x$')
plt.ylabel('$y$')
fig.add_subplot(212)
plt.plot(T, Ene)
plt.xlabel('$Tiempo$')
plt.ylabel('$Energia$')
plt.show()
fig.savefig('verlet.png')

