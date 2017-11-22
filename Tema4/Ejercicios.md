## Ejercicios Tema 4

## Virtualización ligera usando contenedores

### Ejercicio 1: Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en GitHub como en el sitio web está bastante más avanzada; para evitar problemas sobre todo con las herramientas que vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 1.0.

Para instalar *lxc* usamos el siguiente comando:

<code>sudo apt-get install</code>

Un vez instalado comprobamos que se ha instalado correctamente, que está habilitado y que es soportado por el kernel de linux.

![curl](Imagen)

Por último, la versión de *lxc* instalada en mi máquina es:

![curl](Imagen)

### Ejercicio 2: Crear y ejecutar un contenedor basado en tu distribución y otro basado en otra distribución, tal como Fedora. Nota En general, crear un contenedor basado en tu distribución y otro basado en otra que no sea la tuya.

Creamos un contenedor llamado *una-caja* y en el instalamos Ubuntu.

<code>sudo lxc-create -t ubuntu -n una-caja</code>

Una vez que se muestre esto por pantalla, ya tenemos el contenedor listo para ser usado.

![curl](Imagen)

Voy a instalar como segunda distribución, un contenedor de *Gentoo Linux*.

<code>sudo lxc-create -t gentoo -n gentoo</code>

Para iniciar un contenedor usamos la orden:

<code>sudo lxc-start -n contenedor<code>

Para comprobar que ambos contenedores se han instalado y están iniciados, usamos:

<code>sudo lxc-ls --fancy</code>

![curl](Imagen)

### Ejercicio 3: Instalar docker.

Para instalar Docker tenemos primero que agregar la clave GPG para el repositorio oficial del Docker al sistema.

<code>sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D</code>

Añadimos el repositorio Docker.

<code>sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'</code>

Y por último, trás actualizar la base de datos de paquetes.

<code>sudo apt-get install -y docker-engine</code>

Para comprobar que Docker está instalado, el daemon iniciado y el proceso habilitado para iniciar el arranque:

<code>sudo systemctl status docker</code>

![curl](Imagen)

### Ejercicio 4:

#### 1. Instalar a partir de docker una imagen alternativa de Ubuntu y alguna adicional, por ejemplo de CentOS.

Para instalar una imagen a partir de docker:

<code>sudo docker pull centos</code>

La de imagen de ubuntu ya la tenía instalada de unas pruebas anteriores.

### 2. Buscar e instalar una imagen que incluya MongoDB.

De nuevo usamos la misma orden que en el apartado anterior e instalamos *mongo*.

<code>sudo docker pull mongo</code>

Por último, para comprobar que las imágenes se han instalado en nuestro equipo.

<code>docker images</code>

![curl](Imagen)

### Ejercicio 5: Crear un usuario propio e instalar alguna aplicación tal como nginx en el contenedor creado de esta forma, usando las órdenes propias del sistema operativo con el que se haya inicializado el contenedor.

Lo primero que haremos es iniciar el contenedor, en mi caso *ubuntu*, que hemos creado anteriormente.

<code>sudo docker run -i -t ubuntu /bin/bash</code>

Una vez iniciado el contendor, procedemos a crear un usuario junto con su contraseña y a darle permisos de superusuario.

![curl](Imagen)

Ahora ya podemos instalar *nginx* en nuestro contenedor con nuestro usuario creado.

<code>sudo apt-get install nginx</code>

Si queremos iniciar el nginx y comprobar que se está ejecutando:

![curl](Imagen)

### Ejercicio 6: Crear a partir del contenedor anterior una imagen persistente con commit.

Para crear una imagen persistente con commit, tenemos que averiguar el IC que identifica a la imagen.

<code>sudo docker ps -a</code>

Luego, para obtener el ID largo:

<code>sudo docker inspect ID_corto</code>

![curl](Imagen)

Para finalizar, como ya tenemos el ID largo, podemos hacer el commit persistente.

<code>sudo docker commit ID_largo nombre</code>

![curl](Imagen)

### Ejercicio 7: Crear un Dockerfile para el servicio web que se ha venido desarrollando en el proyecto de la asignatura.

[Dockerfile](https://github.com/franfermi/Infraestructura-Virtual_IV/blob/master/Dockerfile) de mi proyecto.

### Ejercicio 8: Desplegar un contenedor en alguno de estos servicios, de prueba gratuita o gratuitos.

* DockerHub: https://hub.docker.com/r/franfermi/subjectsgii_bot/

* Azure: https://subjectsgiibot.azurewebsites.net/
