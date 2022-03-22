# Módulo de Gimnasio

## Funcionalidad y objetivos
Este módulo nos permite gestionar las actividades de un gimnasio. Se trata de un sencillo módulo que nos permite evaluar todos los conceptos aprendidos este trimestre con respecto a la creación de módulos en Odoo.  

## Modelos

Está formado por **3 modelos**:
* Modelo clase. Modelo que simula la clase de un gimasio.
* Modelo monitor. Modelo que hereda de res.partner por delegación añadiéndole nuevos campos que permiten asociar un contacto como monitor.
* Modelo alumno. Modelo que hereda de res.parter por delegación, al igual que monitor.

## Vistas

Está formado por varias vistas para los **3 modelos**:
* Vistas de clase. Una vista 'tree' (_nombre, dificultad, descripción, duración(min), monitor, alumnos_) y una vista 'form'.
* Vistas de monitor. Una vista 'tree' (_nombre \[partner_id], fecha_inicio) y una vista 'form') y una vista 'form'.
* Vista de alumno. Una vista 'tree' (_nombre \[partner_id], fecha_inicio, antiguedad) y una vista 'form'.
  
## Documentación de uso

Gracias a estos modelos, podremos crear nuestras propias actividades, seleccionando un nombre y un nivel de difícultad (fácil, medio o difícil). También le podremos indicar una breve descripción y la hora de inicio y final. Por último, podemos asociarles **1 monitor** y **varios alumnos**.  
Gráficamente, el módulo se compone de tres vistas trees que permiten obtener una visualización rápida de cada uno de los modelos; y tres vistas form, que permiten editar las actividades, monitores y alumnos. Todo esto queda correctamente implementado utilizando 3 menus item que nos llevarán a las vistas correspondientes.
