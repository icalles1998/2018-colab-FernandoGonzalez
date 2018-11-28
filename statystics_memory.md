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

**Nota:** Con respecto a la importación de las horas, decir que Matlab las guarda en formato de días. Es decir, para Matlab 12:00:00 (hh:mm:ss) se corresponde con 0.5 (días). Es por esto que para el caso de la columna "Tiempo" hemos hecho uso de una función a la que hemos llamado **segundos_tiempo** la cual devuelve el tiempo en segundos al que corresponde el valor en días recogido por Matlab. La especificación de la función es la siguiente:
```
function [num] = segundos_tiempo(num);
    for i = 1:30709
        num(i) = num(i) * 86400;
    end
end
```
Algo parecido ocurre con la columna "Ritmo", con la salvedad de que el formato de esta columna en excel es "mm:ss", por lo que el procedimiento para pasarlo a segundos difiere al anterior tanto en cuanto a que ha de ser dividido por 60. Esto se debe a que Matlab siempre lee este tipo de datos con el formato "hh:mm:ss", pero en este caso, lo que Matlab interpreta como horas son minutos. Como he mencionado, la manera de solucionar esto es igual que la anterior pero dividiendo además por 60, tal como se muestra a continuación. Esta función recibe el nombre de **segundos_ritmo**.
```
function [num] = segundos_tiempo(num);
    for i = 1:30709
        num(i) = num(i) * 86400 / 60;
    end
end
```
## Procedimiento Principal
El procedimiento principal consta de un bucle que en cada vuelta muestra un menú con las diferentes opciones a elegir por el usuario y que finaliza con la elección por parte de éste de la opción "Salir del Programa".
Para imprimir el menú se hace uso de la función **mostrar_menu_pcpal**, a la cual se llama de la siguiente manera: ``mostrar_menu_pcpal();`` y cuya implementación es la siguiente:
```
function [] = mostrar_menu_pcpal();
    disp("Teclee la opción deseada:");
    salto_linea()
    disp("1) Histograma");
    disp("2) Datos Numéricos");
    disp("3) Distribución Gaussiana");
    disp("4) Cálculo de Probabilidades");
    disp("5) Cálculo de Cuartiles");
    disp("6) Salir del Programa");
end
```
La función **salto_linea()** es la siguiente:
```
function [] = salto_linea();
    disp(" ");
end
```
Esta función inserta una linea en blanco.

Posteriormente, con la sentencia ``n = leernum();`` se lee desde teclado el número correspondiente a la elección del usuario. La función **leernum()** se especifica a continuación:
```
function [n] = leernum();
    n = input('Introduzca un numero: ');
end
```
Una vez leído el número introducido por el usuario, el programa entra en una casuística encargada de decidir qué hacer en función de dicho número. A continuación separaré esta casuística por "procedimientos" con el fín del buen entendimiento del código que a partir de este momento se explica:
```
    if n == 1
        procedimiento_1;
    elseif n == 2
        procedimiento_2;
    elseif n == 3
        procedimiento_3;
    elseif n == 4
        procedimiento_4;
    elseif n == 5
        procedimiento_5;
    elseif n == 6
        finish = true;
    else
        disp("Teclee un número del 1 al 6");    
    end
```
En cuanto al caso 'n == 6', decir que se corresponde con la salida del programa. La asignación del valor booleano 'true' a la variable 'finish' significaría la salida del bucle y, por tanto, el fin de la ejecución del programa. En lo que al caso por defecto se refiere, decir que se imprime un mensaje de error indicando el correcto uso del programa con la sentencia

``disp("Teclee un número del 1 al 6");``.
Llegados a este punto, procedo a comentar el funcionamiento de cada uno de los "procedimientos" anteriormente idicados.
### procedimiento_1:
* **Especificación del código:**
```
ok = false;
while ~ok
    impr_submenu1();
    [accion, ok] = leeraccion1();
    salto_linea();
    if ~ok
        disp("Numero introducido Incorrecto");
        salto_linea();
    end
end
ok = false;
while ~ok
    impr_submenu11();
    [cat_elegida, ok] = leercategoria(categoria);
    salto_linea();
    if ~ok
        disp("Categoria introducida Incorrecta");
        salto_linea();
    end
end
impr_operacion1(cat_elegida, accion, categoria, tiempo);
```
* **Explicación del Código:**
En primer lugar, observamos que consta de dos bucles "while". En primer lugar me centraré en el primero:
```
ok = false;
while ~ok
    impr_submenu1();
    [accion, ok] = leeraccion1();
    salto_linea();
    if ~ok
        disp("Numero introducido Incorrecto");
        salto_linea();
    end
end
```
Para comenzar, se declara un booleano que comienza inicializado a "false" y que servirá como condición de salida del bucle. Lo siguiente que se ejecuta una vez dentro del bucle es el procedimiento **impr_submenu1()**, el cual se encarga de imprimir un nuevo menú que indica al usuario su siguiente acción a realizar. Consta del siguiente código:
```
function [] = impr_submenu11();
    disp("Elija Una categoría:");
    salto_linea();
end
```
Como vemos, imprime por pantalla la cadena *Elija Una Categoría* y posteriormente inserta un salto de línea.
