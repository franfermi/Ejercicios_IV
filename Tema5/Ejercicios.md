## Ejercicios Tema 5

## Virtualización completa: uso de máquinas virtuales

### Ejercicio 1: Instalar los paquetes necesarios para usar KVM. Se pueden seguir estas instrucciones. Ya lo hicimos en el primer tema, pero volver a comprobar si nuestro sistema está preparado para ejecutarlo o hay que conformarse con la paravirtualización.

Realizamos la comprobación con:

<code>sudo kvm-ok</code>

El resultado al igual que en el tema 1 es el siguiente:

![curl]()

Me dice que KVM no está disponible porque no se encuentra habilitado en la BIOS. No consigo habilitar la opción de virtualización debido al poco acceso que me da la BIOS.

Instalamos los paquetes necesarios para usar KVM.

<code>apt install qemu-kvm libvirt-clients libvirt-daemon-system</code>

Para poder administrar máquinas como usuario, hay que añadir este último a algunos grupos.

![curl]()


### Ejercicio 2: Crear varias máquinas virtuales con algún sistema operativo libre tal como Linux o BSD. Si se quieren distribuciones que ocupen poco espacio con el objetivo principalmente de hacer pruebas se puede usar CoreOS (que sirve como soporte para Docker) GALPon Minino, hecha en Galicia para el mundo, Damn Small Linux, SliTaz (que cabe en 35 megas) y ttylinux (basado en línea de órdenes solo).

Para la realización de este ejercicio he utilizado la distribución SliTaz por su poco espacio en disco.

Creamos un disco duro en el cual se alojará nuestra distribución.

<code>qemu-img create -f qcow2 slitaz.img 8G</code>

![curl]()

Y pos último instalamos en la imagen de disco creada anteriormente, la ISO descargada.

<code>qemu-system-x86_64 -hda slitaz.img -cdrom slitaz-4.0.iso</code>

![curl]()

SliTaz corriendo bajo qemu.

![curl]()

### Ejercicio 4: Crear una máquina virtual Linux con 512 megas de RAM y entorno gráfico LXDE a la que se pueda acceder mediante VNC y ssh.

Voy a utilizar Trisquel que posee una versión de escritorio LXDE.

Creamos el disco en el que se almacenará nuestra máquina virtual.

<code>qemu-img create -f qcow2 trisquel.img 4G</code>

![curl]()

Ahora instalamos en la imagen creada la ISO de Trisquel descargada con 512 megas de RAM.

<code>qemu-system-x86_64 -hda trisquel.img -cdrom trisquel-mini_7.0_i686.iso -m 512M</code>

![curl]()

Trisquel corriendo bajo qemu con 512 megas de RAM.

![curl]()

Acceso a Trisquel mediante VNC.

<code>qemu-system-x86_64 -hda trisquel.img -cdrom trisquel-mini_7.0_i686.iso -m 512M -vnc :1 &</code>

![curl]()


### Ejercicio 5: Crear una máquina virtual ubuntu e instalar en ella alguno de los servicios que estamos usando en el proyecto de la asignatura.

Para el despliegue final del proyecto de la asignatura, lo he realizado en azure utilizando una máquina virtual ubuntu que servirá el contenido de mi aplicación.

![Proyecto_IV](https://github.com/franfermi/Infraestructura-Virtual_IV)
