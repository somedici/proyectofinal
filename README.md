Meeting Psico -> App Booking Psico

Mi proyecto final se denomina: "Meeting Psico -> App Booking Psico". Su objetivo principal es proporcionar una primera aproximación a una aplicación para reservar sesiones con terapeutas en línea. La idea surgió con la intención de ofrecer un espacio gratuito para el cuidado de la salud mental, accesible para todos, y al mismo tiempo dar a conocer las diversas opciones terapéuticas disponibles.

Aún quedan aspectos por revisar y mejorar, especialmente relacionados con la gestión de terapeutas, sus horarios y el proceso de reservas. Estoy comprometida con la continua evolución y mejora de esta aplicación.

La página principal muestra el 'home' de la aplicación con las distintas opciones de terapias disponibles online. En la barra de navegación hacia la derecha están los enlaces 'Log in' y 'Log out'. Luego, en la barra de navegación hacia la izquierda, se puede acceder a 'Crear Reserva', visualizar todas las reservas en 'Todas las Reservas', explorar las terapias en 'Terapias' y conocer algunos de los terapeutas en 'Terapeutas'.

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
