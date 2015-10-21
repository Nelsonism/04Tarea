class Planeta(object):
    def __init__(self, condicion_inicial, alpha=0):
        self.y_actual=condicion_inicial
        self.t_actual=0.
        self.alpha=alpha
        G=M=m=1                                                #Para que GMm=1
        X, Y, Vx, Vy=self.y_actual
        r=(X**2+Y**2)**(0.5)                                #Transformar las coordenadas x e y en radio
        self.EneActual=0.5*m*(Vx**2+Vy**2)-G*M*m/r+self.alpha*G*M*m/r**2

    def ecuacion_de_movimiento(self):
        X, Y, Vx, Vy=self.y_actual
        G=M=1
        r=(X**2+Y**2)**(0.5)
        Fx=-X*(G*M/r**3-2*self.alpha*G*M/r**4)     #Ecuaciones de movimiento donde fx y fy
        Fy=-Y*(G*M/r**3-2*self.alpha*G*M/r**4)     #son las derivadas parciales del potencial
        return [Vx, Vy, Fx, Fy]                             #divididos por la masa para obtener aceleracion

    def avanza_euler(self, h):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo h usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        vx,vy,fx,fy=self.ecuacion_de_movimiento()
        NewX=vx*h+self.y_actual[0]                          #Nuevos Datos
        NewY=vy*h+self.y_actual[1]                         #
        NewVx=fx*h+self.y_actual[2]                        #
        NewVy=fy*h+self.y_actual[3]                        #
        self.y_actual=[NewX, NewY, NewVx, NewVy] #Actualiza
        self.t_actual+=h                                           #Agrega el paso h en cada iteracion
        pass

    def avanza_rk4(self, h):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        X, Y, Vx, Vy=self.y_actual                         
        K1=self.ecuacion_de_movimiento()              #Para cada K recalcula la ecuación de movimiento

        self.y_actual=[X+K1[0]/2., Y+K1[1]/2., Vx+K1[2]/2., Vy+K1[3]/2.]
        K2=self.ecuacion_de_movimiento()
        
        self.y_actual=[X+K2[0]/2., Y+K2[1]/2., Vx+K2[2]/2., Vy+K2[3]/2.]
        K3=self.ecuacion_de_movimiento()

        self.y_actual=[X+K3[0], Y+K3[1], Vx+K3[2], Vy+K3[3]]
        K4=self.ecuacion_de_movimiento()

        NewX=X+(1/6.)*h*(K1[0]+2*K2[0]+2*K3[0]+K4[0])         #Aplica el metodo de Runge-Kutta4
        NewY=Y+(1/6.)*h*(K1[1]+2*K2[1]+2*K3[1]+K4[1])        #con las K calculadas
        NewVx=Vx+(1/6.)*h*(K1[2]+2*K2[2]+2*K3[2]+K4[2])    #
        NewVy=Vy+(1/6.)*h*(K1[3]+2*K2[3]+2*K3[3]+K4[3])    #
        self.y_actual=[NewX, NewY, NewVx, NewVy]
        self.t_actual+=h
        pass

    def avanza_verlet(self, h):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        X, Y, Vx, Vy=self.y_actual                                        #Usamos la ecuacion de movimiento para
        Vx, Vy, Fx, Fy=self.ecuacion_de_movimiento()          #obtener la velocidad y aceleración
        NewX=X+h*Vx+Fx*(h**2)/2.
        NewY=Y+h*Vy+Fy*(h**2)/2.
        self.y_actual=[NewX, NewY, Vx, Vy]                         #Se obtienen los Vn+1 y an+1,
        Vx1, Vy1, Fx1, Fy1=self.ecuacion_de_movimiento()   #necesarios para el metodo de verlet
        NewVx=Vx+Fx1*h/2.+Fx*h/2.
        NewVy=Vy+Fy1*h/2.+Fy*h/2.
        self.y_actual=[NewX, NewY, NewVx, NewVy]
        self.t_actual+=h
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        G=M=m=1
        X, Y, Vx, Vy=self.y_actual
        Vx, Vy, Fx, Fy=self.ecuacion_de_movimiento()
        r=(X**2+Y**2)**(0.5)
        self.EneActual=0.5*m*(Vx**2+Vy**2)-G*M*m/r + self.alpha*G*M*m/r**2
        pass

