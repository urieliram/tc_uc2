#!/bin/bash
mivariable="Inicia script para UC"
echo $mivariable

for i in 56 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  21 22 23 24 

#45 46 47 48 49 50 51 52 53 54 55 56
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#21 22 23 24
#37 38 39 40 41 42 43 44
#25 26 27 28 29 30 31 32 33 34 35 36

#GROUP	        INST(n)  GEN(G)	PERIOD(T)	FILES (uc_XX)
#rts_gmlc	    12	 73     48	        (45-56)
#cal            20	 610	48	        (1-20)
#ferc           12	 934	48	        (21-24),(37-44)
#ferc(2)	    12	 978	48	        (25-36)

do

sleep 1s

#Aqui se ejecucuta el programa en python
python3 main.py uc_$i.json yalma #| tee >> Log.log

echo termine ... $i

sleep 20s

done

#mv: mueve o renombra archivos y directorios
#mkdir: crea un directorio.
#cp: copia archivos.
#   s  :  segundos (por defecto)  sleep 10s
#   m  :  minutos
#   h  :  horas
#   d  :  dias

