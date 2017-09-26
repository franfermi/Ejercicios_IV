## Ejercicios Tema 1

## Introducción a la infraestructura virtual: concepto y soporte físico

### Ejercicio 1: Consultar en el catálogo de alguna tienda de informática el precio de un ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años. Consultar este artículo en Infoautónomos sobre el tema.

El ordenador elegido para este ejercicio es un **Servidor HPE ProLiant ML30 Gen9**, podemos encontrar información sobre el en
[Hewlett Packard Enterprise](https://www.hpe.com/es/es/product-catalog/servers/proliant-servers/pip.hpe-proliant-ml30-gen9-server.1008556812.html),
con un coste en [Amazon](https://www.amazon.es/Hewlett-Packard-Enterprise-ProLiant-E3-1220V5/dp/B01C6Z1T1A/ref=pd_lpo_sbs_147_t_0?_encoding=UTF8&psc=1&refRID=9D5J8FVDPG4M836XS2RN)
de 869,88€ con IVA incluido y 718,91 sin IVA.

Según se comenta en la página proporcionada en el ejercicio, el gasto deducible en concepto de amortización, tiene un máximo del 25% sobre el valor sin IVA.

Los siguientes cálculos están realizados suponiendo que la compra el ordenador se realiza a principios de año, si se realiza
el 1 de abril por ejemplo, sólo tendremos 9 meses del año por lo que hay que multiplicar por 0.75.

Por tanto, con una deducción del 25% en 4 años, la amortización sería de 217.47€/año.

Para una amortización de 7 años al 25%, obtenemos 124.27€/año.

### Ejercicio 2: Usando las tablas de precios de servicios de alojamiento en Internet “clásicos”, es decir, que ofrezcan Virtual Private Servers o servidores físicos, y de proveedores de servicios en la nube, comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo tipo de procesador en los dos vendedores) y con el resto de las características similares (tamaño de disco duro equivalente a transferencia de disco duro) en el caso de que la infraestructura comprada se usa sólo el 1% o el 10% del tiempo.

En este ejercicio voy a utilizar un VPS de [Strato](https://www.strato.es/vps-linux/), con un coste de 4,49€/mes los tres primeros meses, después 8,99€/mes.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema1/Capturas/precios_VPS.png)

Y para realizar su comparación con un servicio en la nube, he seleccionado A2v2 de [Azure](https://azure.microsoft.com/es-es/pricing/details/cloud-services/), con un coste de 0,1097€/h.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema1/Capturas/precios_cloud_azure.png)

Ambos poseen caractersticas similares, utilizan dos procesadores Intel Xeon con 4GB de RAM.

-Uso del 1% del tiempo:

* Servidor VPS: (4,49 x 3) + (8,99 x 9) = 92,2€ el primer año, el resto de los años 107,88€

* Servidor Cloud: 87,6h/año x 0,1097 = 9,61€/año

-Uso del 10% del tiempo:

* Servidor VPS: (4,49 x 3) + (8,99 x 9) = 92,2€ el primer año, el resto de los años 107,88€

* Servidor Cloud: 876h/año x 0,1097 = 96,1€/año

Como conclusión podemos decir que con poco uso con diferencia es ms económico el servicio cloud, pero si aumentamos considerablemente su uso puede ser que nos interese más optar por un servidor VPS.

### Ejercicio 3: En general, cualquier ordenador con menos de 5 o 6 años tendrá estos flags. ¿Qué modelo de procesador es? ¿Qué aparece como salida de esa orden? Si usas una máquina virtual, ¿qué resultado da? ¿Y en una Raspberry Pi o, si tienes acceso, el procesador del móvil?

El modelo del procesador es: AMD Quad-Core E2-3800

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema1/Capturas/flags.png)

La misma salida se repite 4 veces porque se muestra una vez por cada núcleo.

En una máquina virtual no muestra nada.

### Ejercicio 4

### 4.1: Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden kvm-ok.

Si no tenemos instalado kvm_ok como es mi caso, tenemos que instalar el siguiente programa:

>> sudo apt-get install cpu-checker

El resultado es el siguiente:

>> HINT: Enter your BIOS setup and enable Virtualization Technology (VT), and then hard poweroff/poweron your system
>> KVM acceleration can NOT be used

Me dice que KVM no está disponible porque no se encuentra habilitado en la BIOS.

### 4.2: Instalar un hipervisor para gestionar máquinas virtuales, que más adelante se podrá usar en pruebas y ejercicios.

He instalado VMware Player ya que Virtualbox no me funciona. Lo descargamos de la página oficial y para instalarlo:

>> sudo sh VMware-Player-12.5.7-5813279.x86_64.bundle

### Ejercicio 5: Darse de alta en servicios de nube usando ofertas gratuitas o cupones que pueda proporcionar el profesor.

El servicio en el cual me voy a dar de alta sería en Azure, en el podemos acceder mediante nuestra cuenta Microsoft.

En mi caso le he pedido al profesor un código promocional.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema1/Capturas/cuenta_azure.png)

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema1/Capturas/cuenta_azure_confirmada.png)

Una vez activada la cuenta, esperamos unos minutos, tras los cuales nos llegará un correo de confirmación. Ya tenemos nuestra
suscripción activada.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema1/Capturas/cuenta_suscripci%C3%B3n_azure.png)

### Ejercicio 6: Darse de alta en una web que permita hacer pruebas con alguno de los sistemas de gestión de nube anteriores.

A través del correo de confirmación del ejercicio anterior, podemos acceder al portal de Azure, en el nos encontraremos con los servicios, herramientas, etc, que se proporcionan. En el apartado, Herramientas para desarrolladores tenemos DevTest Labs que es un servicio que ayuda a los desarrolladores y evaluadores a crear rápidamente entornos de Azure al tiempo que se optimizan los recursos y se controlan los costos.

![curl](https://github.com/franfermi/Ejercicios_IV/blob/master/Tema1/Capturas/crear_devTest.png)
