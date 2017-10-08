## Ejercicios Tema 2

## Desarrollo basado en pruebas

### Ejercicio 1: Descargar y ejecutar las pruebas de alguno de los proyectos anteriores, y si sale todo bien, hacer un pull request a este proyecto con tests adicionales, si es que faltan (en el momento que se lea este tema).

### Ejercicio 2: Para la aplicación que se está haciendo, escribir una serie de aserciones y probar que efectivamente no fallan. Añadir tests para una nueva funcionalidad, probar que falla y escribir el código para que no lo haga (vamos, lo que viene siendo TDD).

Ejercicio realizado en el proyecto de la asignatura como parte de los test.

### Ejercicio 3: Convertir los tests unitarios anteriores con assert a programas de test y ejecutarlos desde mocha, usando descripciones del test y del grupo de test de forma correcta. Si hasta ahora no has subido el código que has venido realizando a GitHub, es el momento de hacerlo, porque lo vas a necesitar un poco más adelante.



### Ejercicio 4: Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).

Para poder hacer uso de distintas versiones de Python he optado por el entorno virtual *virtualenv*.

La instalación se lleva a cabo cn la siguiente orden:

>>sudo apt-get install python-virtualenv

Una vez instalado creamos el directorio en el cual queremos ejecutar el entorno virtual y hacemos lo siguiente:

>>virtualenv EntornoVirtualIV


![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/crear_entorno_virtual.png)

Ya tenemos el directorio virtualizado, para iniciar el servicio usamos:

>>source bin/activate

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/iniciar_virtualenv.png)

Y por último para desactivar el entorno virtual:

>>deactivate

### Ejercicio 5: Como ejercicio, algo ligeramente diferente: una web para calificar las empresas en las que hacen prácticas los alumnos. Las acciones serían:  Crear empresa, Listar calificaciones para cada empresa, crear calificación y añadirla (comprobando que la persona no la haya añadido ya), borrar calificación (si se arrepiente o te denuncia la empresa o algo), Hacer un ránking de empresas por    calificación, por ejemplo, Crear un repositorio en GitHub para la librería y crear un pequeño programa que use algunas de sus funcionalidades. Si se quiere hacer con cualquier otra aplicación, también es válido. Se trata de hacer una aplicación simple que se pueda hacer rápidamente con un generador de aplicaciones como los que incluyen diferentes marcos MVC. Si cuesta mucho trabajo, simplemente prepara una aplicación que puedas usar más adelante en el resto de los ejercicios.
