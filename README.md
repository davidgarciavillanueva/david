1. Clase Note
La clase debe ser implementada como una data class.
La clase debe tener las siguientes constantes como variables de clase:
HIGH de tipo str con valor 'HIGH'.
MEDIUM de tipo str con valor 'MEDIUM'.
LOW de tipo str con valor 'LOW'.
La clase debe tener los siguientes atributos:
README.es.md 2024-09-20
2 / 3
code de tipo int inicializado en el constructor.
title de tipo str inicializado en el constructor.
text de tipo str inicializado en el constructor.
importance de tipo str inicializado en el constructor pero con valor por defecto la constante
MEDIUM.
creation_date de tipo datetime. Este atributo no se inicializa en el constructor y tiene como
valor por defecto la fecha y hora actual.
Consejo: Puedes usar la función field del módulo dataclass y la función
datetime.now() del módulo datetime.
tags de tipo list[str]. Este atributo no se inicializa en el constructor y tiene como valor por
defecto una lista vacía.
Consejo: Puedes usar la función field del módulo dataclass, especialmente el
parámetro default_factory.
La clase debe tener un método de instancia add_tag que recibe un parámetro tag de tipo str y
agrega la etiqueta al atributo tags. El método no debe agregar la etiqueta si ya está en el atributo
tags.
La clase debe tener un método de instancia _str_ que devuelve un str con el siguiente formato:
Date: {creation_date}
{title}: {text}
Donde {creation_date} debe ser reemplazado con la fecha de creación de la nota y {title} y
{text} deben ser reemplazados con el título y texto de la nota.
2. Clase Notebook
La clase debe ser implementada como una data class.
La clase debe tener un atributo de instancia notes de tipo dict[int, Note]. No debe ser inicializado
en el constructor y debe tener como valor por defecto un diccionario vacío.
Consejo: Puedes usar la función field del módulo dataclass, especialmente el parámetro
default_factory.
La clase debe tener un método de instancia add_note que recibe los parámetros title de tipo str,
text de tipo str e importance de tipo str y devuelve un int con el código de la nota. El método
debe hacer lo siguiente:
Generar un nuevo código para la nota. El código debe ser un entero único mayor que 0. Puedes
usar la función len para obtener el número de notas y agregar 1 para obtener el nuevo código.
Crear un nuevo objeto Note con los parámetros recibidos y el código generado.
Agregar la nueva nota al atributo notes usando el atributo code de la nota como clave.
Devolver el código de la nota.
README.es.md 2024-09-20
3 / 3
La clase debe tener un método de instancia delete_note que recibe el parámetro code de tipo int. El
método debe eliminar la nota con el código recibido como parámetro del atributo notes.
La clase debe tener un método de instancia important_notes que devuelve una list[Note] con las
notas que tienen la importancia HIGH o MEDIUM.
La clase debe tener un método de instancia notes_by_tag que recibe el parámetro tag de tipo str y
devuelve una list[Note] con las notas que tienen la etiqueta recibida como parámetro.
La clase debe tener un método de instancia tag_with_most_notes que devuelve un str con la
etiqueta que aparece más en las notas. Si hay múltiples etiquetas con el mismo número de notas,
devuelve la primera etiqueta en orden lexicográfico
