# Práctica de Garaje Odoo

## Resumen general
En esta práctica veremos como hacer un módulo de gestión de un garaje en Odoo Local utilizando los lenguajes XML, Python y CSV. Explicando uno a uno los archivos y sus funcionalidades, y también de manera ordenada en función del orden de edición que hemos seguido.

## Manifest
El archivo [Manifest](./__manifest__.py) nos sirve para editar la información general del módulo, ya sea el autor, descripciones, web propia, etc. pero también en este archivo tenemos que declarar que archivos van a ser utilizados, en nuestro caso por ejemplo creamos el archivo [garaje_security](./security/garaje_security.xml) y este ha de ser declarado en 'data' para poder ser utilizado, al igual que declarar el módulo como aplicación. El resultado sería algo así:

![Captura manifest](./screenshots/modulo_gararaje_app.png)

## Models
En el archivo [Models](./models./models.py) declararemos todas las clases que queremos que existan en nuestro módulo y, a su vez, sus atributos. Hemos de distinguir aquí los atributos que empiecen por _ y los que no, ya que si su comienzo es por este carácter Odoo lo leerá como información general de la clase, o modelo, por lo tanto no se asignará como atributo. Otros código que podemos ver son los comenzados por def, los cuales indican que estamos creando un método, en nuestro caso para el módulo coche, por ejemplo. Una vez terminada esta parte de código hemos de comenzar la relación entre tablas (indicada por los comentarios en el código) teniendo que especificar que clase de relación tiene cada clase con los atributos de otras (esto es realmente como relacionar las primary keys entre tablas en Python).

![Captura ver modelos](./screenshots/modelos_garaje.png)
