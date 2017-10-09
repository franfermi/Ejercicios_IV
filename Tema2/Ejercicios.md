## Ejercicios Tema 2

## Desarrollo basado en pruebas

### Ejercicio 1: Descargar y ejecutar las pruebas de alguno de los proyectos anteriores, y si sale todo bien, hacer un pull request a este proyecto con tests adicionales, si es que faltan (en el momento que se lea este tema).

### Ejercicio 2: Para la aplicación que se está haciendo, escribir una serie de aserciones y probar que efectivamente no fallan. Añadir tests para una nueva funcionalidad, probar que falla y escribir el código para que no lo haga (vamos, lo que viene siendo TDD).

Ejercicio realizado en el proyecto de la asignatura como parte de los test.

### Ejercicio 3: Convertir los tests unitarios anteriores con assert a programas de test y ejecutarlos desde mocha, usando descripciones del test y del grupo de test de forma correcta. Si hasta ahora no has subido el código que has venido realizando a GitHub, es el momento de hacerlo, porque lo vas a necesitar un poco más adelante.



### Ejercicio 4: Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).

Para poder hacer uso de distintas versiones de Python he optado por el entorno virtual *virtualenv*.

La instalación se lleva a cabo con la siguiente orden:

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

En mi caso he creado un sitio web que hace uso de MVC con ASP.NET y MVC alojado en Azure ya que tenemos una cuenta creada del ejercicio del tema anterior.

Es una aplicación muy sencilla que únicamente muestra información sobre las empresas introducidas. Lo que quería mostrar en este ejercicio es el uso del patrón de diseño MVC.

Lo primero que he hecho es crear un pequeño proyecto web con Visual Studio seleccionando una plantilla tipo web llamada: *ASP.NET Web Application*.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/AppWeb_ASPNET.PNG)

Y que haga uso del patrón de diseño MVC.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/MVC.PNG)

En el árbol de directorios creado para el proyecto podemos observar que tenemos una carpeta para Controladores, otra para Modelos y otra para Vistas.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/raiz_proyecto.PNG)

El contenido del proyecto lo dejaré en el subdirectorio Tema2 de los ejercicios.

Lo primero que he creado ha sido el Modelo, en mi caso es una clase Empresa con varios atributos los cuales se mostrarán en la web.

Tras esto, creamos el Controlador basado en MVC, en el he añadido una función que devuelve la información de una empresa especificada.

Y por último, la Vista, como voy a mostrar información detallada sobre una empresa, elijo una plantilla de tipo *Details* y la asocio a mi clase Empresa.

La vista en local de la web sería la siguiente:

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/web_localhost.PNG)

Como último paso, y opcional al ejercicio, aprovechando la cuenta de Azure, he publicado la web.

Para ellos creamos una aplicación web en Azure.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/app_web_azure.PNG)

Y publicamos nuestro proyecto.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/publicar_azure.PNG)

La web funcionando bajo Azure sería la siguiente:

![curl](![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema2/Capturas/publicar_azure.PNG)
