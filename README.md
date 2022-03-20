# Módulo de Gimnasio
Este sencillo módulo permite evaluar los conceptos aprendidos a lo largo de este trimestre. Se trata de una aplicación que nos permite gestionar las actividades de un gimnasio.  
Está formado por **3 modelos**:
* Modelo clase. Modelo que simula la clase de un gimasio.
* Modelo monitor. Modelo que hereda de res.partner por delegación añadiéndole nuevos campos que permiten asociar un contacto como monitor.
* Modelo alumno. Modelo que hereda de res.parter por delegación, al igual que monitor.
  
Gracias a estos modelos, podremos crear nuestras propias actividades, seleccionando un nombre y un nivel de difícultad (fácil, medio o difícil). También le podremos indicar una breve descripción y la hora de inicio y final. Por último, podemos asociarles **1 monitor** y **varios alumnos**.  
Gráficamente, el módulo se compone de tres vistas trees que permiten obtener una visualización rápida de cada uno de los modelos; y tres vistas form, que permiten editar las actividades, monitores y alumnos. Todo esto queda correctamente implementado utilizando 3 menus item que nos llevarán a las vistas correspondientes.
