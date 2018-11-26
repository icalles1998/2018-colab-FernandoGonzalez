# Memomia de la Práctica
## Importación de datos:
En primer lugar, declaramos el nombre del fichero que vamos a leer (fichero excel) de la siguiente manera: 

```
file = 'resultados_popular.xlsx';
```
Posteriormente, procedemos a leer cada una de las columnas de dicho fichero. Esto lo hacemos definiendo el rango de celdas que queremos leer, tal como se muestra a continuación:
* ``xlRange = 'A1:A30710';`` Para la primera columna.
* ``xlRange = 'B2:B30710';`` Para la segunda columna. Empieza en la segunda celda para que no guardar el titulo, ya que se trata de un string
* ``xlRange = 'C1:C30710';`` Para la tercera columna.
* ``xlRange = 'D1:D30710';`` Para la cuarta columna.
* ``xlRange = 'E1:E30710';`` Para la quinta columna.

La sentencia utilizada para leer el rango de celdas es ``xlsread(file, xlRange);``.

**Nota:** Con respecto a la importación de las horas, decir que matlab las guarda en formato de días. Es decir, para Matlab 12:00:00 (hh:mm:ss) se corresponde con 0.5 (días). Es por esto que para el caso de la columna "Tiempo" hemos hecho uso de una función a la que hemos llamado **segundos_tiempo** la cual devuelve el tiempo en segundos al que corresponde el valor en días recogido por Matlab. La especificación de la función es la siguiente:
```
function [num] = segundos_tiempo(num);
    for i = 1:30709
        num(i) = num(i) * 86400;
    end
end
```
