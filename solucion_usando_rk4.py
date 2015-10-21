from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt
#Condiciones iniciales
condicion_inicial=[10, 0, 0, 0.27]  #Escogi Vy=0.27
p=Planeta(condicion_inicial)
Pasos=800                             #En este metodo necesite una cantidad moderada de pasos
h=800/Pasos                          #para que los gráficos den cosas razonables. Con tiempo igual a
T=np.linspace(0,800, Pasos)    #800 se logran las 5 vueltas
x=[10]
y=[0]
Ene=[p.EneActual]

N=1        #Variable auxiliar para interar
while N<Pasos:               #Aplica el metodo de runge-kutta 4 definido en la clase planeta.
    p.avanza_rk4(h)
    N+=1
    x.append(p.y_actual[0])
    y.append(p.y_actual[1])
    p.energia_total()
    Ene.append(p.EneActual)
#Plots
fig=plt.figure()
fig.add_subplot(211)
plt.plot(x,y)
plt.title('$Trayectoria$ $y$ $Energia$ $vs$ $Tiempo$ \n $RK4$ $Con$ $v_{y}(0)=0.27$')
plt.xlabel('$x$')
plt.ylabel('$y$')
fig.add_subplot(212)
plt.plot(T, Ene)
plt.xlabel('$Tiempo$')
plt.ylabel('$Energia$')
plt.show()
fig.savefig('rk4.png')
