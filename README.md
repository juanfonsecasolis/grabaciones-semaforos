# grabaciones-semaforos

Los nombres de los archivos .wav de las muestras se codificaron de la siguiente manera:

CAMPO 1; 1 caracter, describe si se trata de ruido o del sonido del semaforo: 
						s: "sonido" un archivo con el sonido del semaforo 
						r: "ruido" un archivo con ruido ambiental

CAMPO 2; 1 caracter, describe cual dispositivo tomo la muestra: 
						a: "ACE" muestra tomada con el celular galaxy ace
						d: "DUOS" muestra tomada con el celular duos
						l: "LG" muestra tomada con un celular LG-D618

CAMPO 3; 5 caracteres, describe el identificador del semaforo: 
						sem(##): "semaforo" ## sonido tomado cercano a un semaforo. Numero corresponde a un valor numerico que identifica unicamente al semaforo. Ej: sem01, sem02, sem03

CAMPO 4; 1 caracter, describe de qué lado de la calle es la grabación, ya que puede ser al a par del semaforo o del otro lado de la calle: 
						o: "otherside(al otro lado)" La grabacion se tomo al lado opuesto al que estaba el semaforo. Al otro lado de la calle.
						s:	"side(al lado)" La grabacion se tomo al a par del semaforo. 

CAMPO 5; 19 caracteres, fecha y hora de la grabacion, es un valor insertado por la aplicacion con la que se hizo la grabacion, normalmente no concuerdan entre grabaciones, sin embargo el orden en que fueron tomadas define la correspondencia entre las grabaciones simultaneas de los sonidos.
						ano: ano que se realizo la grabacion
						mes: mes que se realizo la grabacion
						dia: dia que se realizo la grabacion
						hora: hora en formato de 24 horas  del del inicio de la grabacion
						minutos: valor del minutero del dispositivo celular del inicio de la grabacion
						segundos: valor del secundero del dispositivo celular en segundos del inicio de la grabacion.
	
Historial de cambios:
---------------------------------------------------
1) Mario Monge Ordonez A93965 y Sharon Corrales Montero A91971, Julio 2013 (creacion inicial)
2) Juan Fonseca, Octubre 2016, modificado para soportar teléfono LG e identificadores de 2 digitos para cada semaforo


						
