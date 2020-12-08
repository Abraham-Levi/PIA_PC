INFORMACION PIA_PC
===========

Este proyecto ejecuta diversas tareas relacionadas con ciberseguridad:

* Obtención de socket en base a un link
* Escaneo de link con Virustotal
* Web Scraping
* Obtención de Metadata
* Obtención de Hashes
* Envío de correo

Cada una de dichas actividades son realizadas en base a parámetros establecidos, los cuales
deberán ser especificados al momento de ejecutar el script.

REQUISITOS:
--------------
* Tener los modulos utilizados en cada uno de los scripts previamente instalados *(requirements.txt)*


EJEMPLOS DE EJECUCION:
--------------
1- PIA.py -link uanl.mx -a 1234567890asdfghjkl

2- PIA.py -b ejemplo.pickle -p C:\Users\abrah\Desktop -t ejemplo.txt -u sucorreo@gmail.com
-w abc123 -y correodestino@gmail.com


.. automodule:: PIA.py
   :members: