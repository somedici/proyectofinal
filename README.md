PsicoAPP

Mi proyecto final se denomina: "PsicoAPP". Su objetivo principal es proporcionar una primera aproximación a una aplicación para reservar sesiones con terapeutas en línea. La idea surgió con la intención de ofrecer un espacio accesible para el cuidado de la salud mental, accesible para todos, y al mismo tiempo dar a conocer las diversas opciones terapéuticas disponibles.

En un contexto marcado por avances tecnológicos, inestabilidad económica y cambios globales, reconocemos la importancia crítica de priorizar la salud mental. Psico App es una plataforma que se enfoca en brindar herramientas para identificar y abordar cualquier síntoma o situación de riesgo que pueda afectar tanto al usuario como a sus seres queridos.

Además, como parte de la misión es proporcionar un apoyo integral, con la idea de integrar una función de emergencia. Este botón de emergencia permite acceder a un centro telefónico especializado, donde se brinda atención gratuita en situaciones de crisis, como ataques de pánico, ideación suicida u otras emergencias similares. (aún está en proceso de desarrollo)

La página principal muestra el 'home' de la aplicación con las distintas opciones de terapias disponibles online. En la barra de navegación hacia la derecha están los botones de 'Registrarse', 'Opciones' y 'Login'. En el campo a desplegar 'Opciones' estan las funcionalidades de crear una reserva, observar esa reserva en la agenda de la plataforma, observar los terapeutas y los tipos de terapia. El flujo del usuario consiste primero en registrarse como usuario, iniciar sesión, crear una reserva con un especialista, observar esa reserva en la agenda, y si es necesario editar la misma. 

Aún falta integrar los terapeutas con cada especilidad, poder editar bien las reservas, filtrar por terapeuta y especialidad y por último, crear el botón de emergencia que te direcciona hacia un servicio de urgencia.

A continuación detallo el paso a paso que realicé para poder inciar el proyecto:
1 - Inicié mi proyecto ejecutando el siguiente comando: <django-admin startproject Meetingpsico>
2 - Levanté el servidor para testear el funcionamiento con: <python manage.py runserver>
3 - Creé una nueva aplicación, ejecutando: <python manage.py startapp bookingpsico>
4 - Creé un archivo 'Urls.py' en mi nueva aplicación 'bookingpsico'
4 - Definí las URLs generales y las de mi aplicación
5 - Definí las vista en el archivo 'views.py'
6 - Definí los templates que son el diseño de mis views.py
6b - Conecte las views en las URLs.
7 - Definí dos modelos de mi aplicación en el archivo 'models.py'
8 - Migré los datos a mi base de datos, ejecutando los siguiente comandos: <python manage.py makemigrations>, <python manage.py migrate>
9 - Configuré el admin con un 'superadmin' para administrar los datos.
10 - Configuré en 'forms.py', los formularios para poder tener manejo de la base de datos y especifiqué el modelo de mi base de datos.
