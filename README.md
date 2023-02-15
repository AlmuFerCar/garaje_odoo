# Práctica de Garaje Odoo

## Resumen general
En esta práctica veremos como hacer un módulo de gestión de un garaje en Odoo Local utilizando los lenguajes XML, Python y CSV. Explicando uno a uno los archivos y sus funcionalidades, y también de manera ordenada en función del orden de edición que hemos seguido.

## Manifest
El archivo [Manifest](./__manifest__.py) nos sirve para editar la información general del módulo, ya sea el autor, descripciones, web propia, etc. pero también en este archivo tenemos que declarar que archivos van a ser utilizados, en nuestro caso por ejemplo creamos el archivo [garaje_security](./security/garaje_security.xml) y este ha de ser declarado en 'data' para poder ser utilizado, al igual que declarar el módulo como aplicación. El resultado sería algo así:

![Captura manifest](./screenshots/modulo_gararaje_app.png)

## Models
En el archivo [Models](./models/models.py) declararemos todas las clases que queremos que existan en nuestro módulo y, a su vez, sus atributos. Hemos de distinguir aquí los atributos que empiecen por _ y los que no, ya que si su comienzo es por este carácter Odoo lo leerá como información general de la clase, o modelo, por lo tanto no se asignará como atributo. Otros código que podemos ver son los comenzados por def, los cuales indican que estamos creando un método, en nuestro caso para el módulo coche, por ejemplo. Una vez terminada esta parte de código hemos de comenzar la relación entre tablas (indicada por los comentarios en el código) teniendo que especificar que clase de relación tiene cada clase con los atributos de otras (esto es realmente como relacionar las primary keys entre tablas en Python).

![Captura ver modelos](./screenshots/modelos_garaje.png)

## Views
Este archivo [Views](./views/views.xml) será como mostrar gráficamente el modelo, esto quiere decir que este archivo es el que muestra la interfaz gráfica tanto los campos, como los formularios de los mismos. También podemos observar que podemos crear varias vistas, ya que si revisamos el código, están creadas vistas como el Search, Calendar, etc. 

La estructura del código es simple, ya que primero hemos de declarar las vistas con sus respectivos formularios y vistas, y seguidamente definir los menús para poder llamarlos a que sean visibles. Y también llamarlo mediante el <menuitem> para que aparcezca en la parte superior de la pantalla (a modo de menú).

Para los formularios se utilizan etiquetas simples como <field> para indicar que es un campo y <group> para hacer la agrupación estética de los cambios. No tenemos que declarar de que tipo es cada campo, como podría ser un checkbox, ya que ya hemos indicado que tipo son en el archivo [Models](./models/models.py).

![Captura ver modelos](./screenshots/mantenimientos_info_coche.png)
  
## Security

Para la seguridad primero hemos de crear de archivo [Garaje_security](./security/garaje_security.xml)
