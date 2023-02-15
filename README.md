# Práctica de Garaje Odoo

## Resumen general
En esta práctica veremos como hacer un módulo de gestión de un garaje en Odoo Local utilizando los lenguajes XML, Python y CSV. Explicando uno a uno los archivos y sus funcionalidades, y también de manera ordenada en función del orden de edición que hemos seguido.

![Captura app](./screenshots/lista_aplicaciones.png)

## Manifest
El archivo [Manifest](./__manifest__.py) nos sirve para editar la información general del módulo, ya sea el autor, descripciones, web propia, etc. pero también en este archivo tenemos que declarar que archivos van a ser utilizados, en nuestro caso por ejemplo creamos el archivo [garaje_security](./security/garaje_security.xml) y este ha de ser declarado en 'data' para poder ser utilizado, al igual que declarar el módulo como aplicación. El resultado sería algo así:

![Captura manifest datos generales](./screenshots/modulo_gararaje_app.png)

![Captura manifest datos técnicos](./screenshots/datos_tecnicos_modulo_garaje_app.png)

![Captura manifest características generales](./screenshots/caracteristicas_instaladas_modulo_garaje_app.png)

## Models
En el archivo [Models](./models/models.py) declararemos todas las clases que queremos que existan en nuestro módulo y, a su vez, sus atributos. Hemos de distinguir aquí los atributos que empiecen por _ y los que no, ya que si su comienzo es por este carácter Odoo lo leerá como información general de la clase, o modelo, por lo tanto no se asignará como atributo. Otros código que podemos ver son los comenzados por def, los cuales indican que estamos creando un método, en nuestro caso para el módulo coche, por ejemplo. Una vez terminada esta parte de código hemos de comenzar la relación entre tablas (indicada por los comentarios en el código) teniendo que especificar que clase de relación tiene cada clase con los atributos de otras (esto es realmente como relacionar las primary keys entre tablas en Python).

![Captura ver modelos](./screenshots/modelos_garaje.png)

![Captura ver modelo aparcamiento con atributos](./screenshots/modelos_garaje_aparcamiento_campos.png)

![Captura ver modelo coche con atributos](./screenshots/modelos_garaje_coche_campos.png)

![Captura ver modelo mantenimiento con atributos](./screenshots/modelos_garaje_mantenimiento_campos.png)

## Views
Este archivo [Views](./views/views.xml) será como mostrar gráficamente el modelo, esto quiere decir que este archivo es el que muestra la interfaz gráfica tanto los campos, como los formularios de los mismos. También podemos observar que podemos crear varias vistas, ya que si revisamos el código, están creadas vistas como el Search, Calendar, etc. 

![Captura ver vista calendario](./screenshots/mantenimientos_calendario_info.png)

La estructura del código es simple, ya que primero hemos de declarar las vistas con sus respectivos formularios y vistas, y seguidamente definir los menús para poder llamarlos a que sean visibles. Y también llamarlo mediante el <menuitem> para que aparcezca en la parte superior de la pantalla (a modo de menú).

Para los formularios se utilizan etiquetas simples como <field> para indicar que es un campo y <group> para hacer la agrupación estética de los cambios. No tenemos que declarar de que tipo es cada campo, como podría ser un checkbox, ya que ya hemos indicado que tipo son en el archivo [Models](./models/models.py).

![Captura ver vista](./screenshots/mantenimientos_info_coche.png)
  
## Security
Para la seguridad primero hemos de crear de archivo [Garaje_security](./security/garaje_security.xml), en este declararemos los distintos grupos de usuarios que vamos a tener en nuestro módulo, en este caso hemos declarado dos, usuario y director, el cual también hereda de usuario. Para ello, en el código simplemente indicamos su nombre y referenciamos sobre qué módulo se crean y en el caso del director referenciar de dónde hereda.

![Captura ver grupos de seguridad](./screenshots/usuarios_compañias_grupos.png)

Sin embargo tenemos otro archivo denominado [ir.model.access](./security/ir.model.access.csv) el cual es el que otorga los permisos a cada grupo de usuarios, para la edición de este archivo hemos utilizado [LibreOffice](https://es.libreoffice.org/) ya que la lectura del código es difícil, por lo tanto, hemos de declarar los modelos sobre los que actúan los nuevo usuarios y los números del final de cada línea nos indicarán qué permisos tienen (lectura, escritura, creación y desconexión). Dato curioso es que si entramos al archivo desde Github, aparece como una hoja de excel.

![Captura ver grupos de seguridad con permisos](./screenshots/grupos_garaje_usuario_permisos.png)

![Captura ver permisos en mantenimiento](./screenshots/modelos_garaje_mantenimiento_permisos.png)
  
![Captura ver permisos en coche](./screenshots/modelos_garaje_coche_permisos.png)
  
![Captura ver permisos en aparcamiento](./screenshots/modelos_garaje_aparcamiento_permisos.png)

## Demo
En este apartado se va a crear una serie de datos de prueba que se puedan visualizar en el módulo garaje, para esto se accede a la carpeta [Demo](./demo/demo.xml) y se añaden los datos teniendo en cuenta la estructura del archivo [models](./models/models.py) para que lo recozca y se visualicen correctamente.

Los datos que se añaden son de los diferentes modelos: aparcamiento, coches y mantenimiento

![Bloque aparcamiento](./screenshots/app_garaje_bloques_aparcamiento.png)

![Bloque coches](./screenshots/app_garaje_bloques_coches.png)

![Bloque mantenimiento](./screenshots/app_garaje_bloques_mantenimientos.png)

Dentro de cada uno de los módulos se han incluido los datos de forma detallada:

### Aparcamiento
![Aparcamiento_info_general](./screenshots/aparcamiento_plaza_mayor_info_general.png)

En esta captura se puede observar la relación entre aparcamiento y coches
![Aparcamiento_info_general](./screenshots/aparcamiento_plaza_mayor_info_coche.png)
