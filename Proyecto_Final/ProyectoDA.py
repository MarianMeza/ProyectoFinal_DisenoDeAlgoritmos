import serial
import time
import array
import scipy.io
import matlab.engine

eng = matlab.engine.start_matlab()
eng.proyectoDA(nargout=0)

mat = scipy.io.loadmat('proyecto_variables.mat')

coord_x = mat['coordenadas_x']
coord_y = mat['coordenadas_y']

coord_x = coord_x[0]
coord_y = coord_y[0]

print('coordenadas x:')
print(coord_x)
print('coordenadas y:')
print(coord_y)

len_coords=len(coord_y)
print(len_coords)

ori=1

print("Inicializar")
port="COM4" 
bluetooth=serial.Serial(port, 38400)#Inicializa comunicación con MARTIN
print("Conectado")
bluetooth.flushInput() 

for j in range(len_coords):
    
    x =	coord_x[j]
    y = coord_y[j]

    #Ir enfrente
    if x==coord_x[j-1]+1  and  y==coord_y[j-1]:
    
        if ori==1:
            bluetooth.write(b"E")
            time.sleep(1.5)
            print('E')
            ori=1
            continue

        if ori==2:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=1
            continue

        if ori==8:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=1
            continue
        

    #Ir en diagonal superior derecha
    if x==coord_x[j-1]+1  and  y==coord_y[j-1]+1:
        
        if ori==1:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=2
            continue
        
        if ori==2:
            bluetooth.write(b"B")
            time.sleep(1.5)
            print('ED')
            ori=2
            continue
        
        if ori==3:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=2
            continue

    #Ir en diagonal superior izquierda
    if x==coord_x[j-1]+1  and  y==coord_y[j-1]-1:
        
        if ori==1:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=8
            continue

        if ori==7:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=8
            continue
        
        if ori==8:
            bluetooth.write(b"B")
            time.sleep(1.5)
            print('ED')
            ori=8
            continue
                 
    #Ir derecha
    if x==coord_x[j-1]  and  y==coord_y[j-1]+1:
    
        if ori==1:
            bluetooth.write(b"D")
            time.sleep(1.5)
            print('D')
            ori=3
            continue   

        if ori==2:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=3
            continue
       
        if ori==3:
            bluetooth.write(b"E")
            time.sleep(1.5)
            print('E')
            ori=3
            continue

        if ori==4:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=3
            continue

        if ori==5:
            bluetooth.write(b"I")
            time.sleep(1.5)
            print('I')
            ori=3
            continue

    #Ir izquierda
    if x==coord_x[j-1]  and  y==coord_y[j-1]-1:
        
        if ori==1:
            bluetooth.write(b"I")
            time.sleep(1.5)
            print('I')
            ori=7
            continue

        if ori==5:
            bluetooth.write(b"D")
            time.sleep(1.5)
            print('D')
            ori=7
            continue

        if ori==6:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=7
            continue

        if ori==7:
            bluetooth.write(b"E")
            time.sleep(1.5)
            print('E')
            ori=7
            continue

        if ori==8:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=7
            continue
    
    #Ir diagonal inferior derecha
    if x==coord_x[j-1]-1  and  y==coord_y[j-1]+1:
        
        if ori==3:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=4
            continue

        if ori==4:
            bluetooth.write(b"B")
            time.sleep(1.5)
            print('ED')
            ori=4
            continue

        if ori==5:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=4
            continue
    
    #Ir diagonal inferior izquierda
    if x==coord_x[j-1]-1  and  y==coord_y[j-1]-1:
        
        if ori==5:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=6
            continue

        if ori==6:
            bluetooth.write(b"B")
            time.sleep(1.5)
            print('ED')
            ori=6
            continue

        if ori==7:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=6
            continue

    #Ir atrás
    if x==coord_x[j-1]-1  and  y==coord_y[j-1]:
        
        if ori==4:
            bluetooth.write(b"Z")
            time.sleep(1.5)
            print('DSD')
            ori=5
            continue

        if ori==5:
            bluetooth.write(b"E")
            time.sleep(1.5)
            print('E')
            ori=5
            continue
        
        if ori==6:
            bluetooth.write(b"A")
            time.sleep(1.5)
            print('DSI')
            ori=5
            continue

bluetooth.close() #Para terminar la conexión
print("Done")
