# 201906180_PracticaLFP

##Manual de Usuario
<p align="justify">
SiempleQL es un lenguaje de consulta que funciona a través de comando que se va a indicar a continuación. 

Los comando es case insensitive lo que significa que no importa si lo escribe en mayúsculas, minúsculas o combinados.

>TODOS LOS COMANDOS SERA ESCRITO EN MAYUSCULA PARA PODER INDENTIFICAR QUE SON COMANDOS QUE PUEDE SER CASE INSENTIVE.

***
***

###Comando CARGAR:
Como su nombre indica se usa el comando para cargar los archivo en ese caso de extensión .json lo cual el archivo debe está en el mismo carpeta que el SimpleQL. 

Para cargar los archivos la estructura seria la siguiente:
~~~
CARGAR archivo1.json, archivo2.json, ……. Archivo.json
~~~
Puede cargar una cantidad N de archivo y después de escribir el nombre de cada archivo con su extensión debe de ingresar un coma (,) si se desea cargar mas archivo.

***
***

###Comando SELECCIONAR:
Puede seleccionar uno o mas registro o atributos de los mismos puede tener condición simples.

Para seleccionar todos los registros de los archivos cargados seria asi:
~~~
SELECCIONAR *
~~~
Puede seleccionar todos los registros donde cumple con cierta condición:
~~~
SELECCIONAR * DONDE nombre = ”Francisco”
~~~
Los nombres debe ir entre comillas, en caso de que el nombre ingresado no existe no se mostrada ningún registro.
También se puede seleccionar algunos atributos de registro donde también puede agregarle una condición:
~~~
SELECCIONAR nombre, edad DONDE promedio = 100
~~~
Puede seleccionar los atributos que está en los registros, nunca podrá mostra atributos que no exista en el registro por ejemplo “Fecha”.

***
***

###Comando MAXIMO:
Comando que encuentra el máximo de un atributo de todos los registros que se cargó previamente.
~~~
MAXIMO edad

MAXIMO promedio
~~~
Este comando solo aplica para los atributos edad y promedio, nunca podrás encontrar el máximo de un atributo “nombre” porque su estructura no es de carácter numérico sino de un texto.

***
***

###Comando MINIMO:
Comando que encuentra el mínimo de un atributo de todos los registros que se cargó previamente.

>MINIMO edad

>MINIMO promedio

Este comando solo aplica para los atributos edad y promedio, nunca podrás encontrar el mínimo de un atributo “nombre” porque su estructura no es de carácter numérico sino de un texto.

***
***

###Comando SUMA:
Comando que suma el atributo especificado de todos los registros que se cargó previamente.
~~~
SUMA edad

SUMA promedio
~~~
Este comando solo aplica para los atributos edad y promedio, nunca podrás sumar un atributo “nombre” porque su estructura no es de carácter numérico sino de un texto.

***
***

###Comando CUENTA:
Comando que permite contar el número de registro que se cargó a la memoria.

Su estructura seria la siguiente:
~~~
CUENTA
~~~
***
***

###Comando REPORTAR:
Este comando permite crear un reporte en HTML de una cantidad N de registros.

Su estructura seria la siguiente:
~~~
REPORTAR N
~~~
Donde N puede ser cualquier numero media vez no sea mayor que la cantidad de registro cargado a la memoria, por ejemplo si cargo 5 registro a la memoria no podrá pedir al programa REPORTAR 10 el programa no será capaz de mostrar 10 registros si previamente solo cargo 5 registros, si intenta hacer esto en el programa le tirada un error donde le indica que el número ingresado es mayor a la cantidad de registros cargados.

</p>