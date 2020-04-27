#hoyhyohyohyoyhoyhoyhyoy
import numpy as np
import cv2
import cv2.cv as cv
import argparse



#cargamos el clasificador
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#cargamos la imagen dada 

p = argparse.ArgumentParser("Muestra una imagen")
p.add_argument("archivo",default=None,action="store", 
    help="Nombre de archivo")
opts = p.parse_args()
#lectura de imagen para reconocimiento
img = cv2.imread(opts.archivo)

#redimension para mejorar la performance

dimension_x = 160
dimension_y = 120


x = dimension_x 
y = dimension_y 

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', x, y)          

#creamos la mascara
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.resizeWindow('gray', dimension_x, dimension_y)          

gray = cv2.resize(gray, (x,y))    
img = cv2.resize(img,(x,y))

#buscamos las coordenadas de los rostros (si existen)
#guardamos su posicion
t = cv.GetTickCount()
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
t = cv.GetTickCount() - t
print "tiempo de la deteccion = %gms" % (t/(cv.GetTickFrequency()*1000.))

#dibujamos rectangulo en el rostro si existe
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#mostramos la imagen y su mascara
cv2.imshow('img',img)
cv2.imshow('gray',gray)
#para salir del programa
while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()








