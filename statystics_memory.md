# Memoria de la Práctica
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
#### Especificación del Código:
**procedimiento_1** consta de un procedimiento llamado ``hacer_histograma(tiempo)``, el cual imprime por pantalla un histograma teniendo en cuenta todos los tiempos leídos en el fichero excel. A continuación se muestra el código de este procedimiento:
```
function [] = hacer_histograma(t);
    disp("Generando Histograma...");
    salto_linea();
    nbins = 20; %Primero defino el numero de bins
    figure
    hist(t, nbins); %Representar el histograma
    title('Histograma de tiempos');
end
```
#### Explicación del Código:
con la sentencia ``nbins = 20;`` se define el número de intervalos de tiempo a representar, los cuales se corresponden con cada una de las barras que se verán representadas, y se guarda en la vaiable "nbins". Posteriormente, se representa el histograma haciendo uso del procedimiento **hist** que Matlab nos proporciona.
#### Ejemplo Salida:

### procedimiento_2:
#### Especificación del Código:
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
#### Explicación del Código:
En primer lugar, observamos que consta de dos bucles "while". En este caso me centraré en el primero:
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
* ``ok = false;``: Para comenzar, se declara un booleano que comienza inicializado a "false" y que servirá como condición de salida del bucle. 
* ``impr_submenu1();``: Lo siguiente que se ejecuta una vez dentro del bucle es el procedimiento **impr_submenu1()**, el cual se encarga de imprimir un nuevo menú que indica al usuario su siguiente acción a realizar. Consta del siguiente código:
```
function [] = impr_submenu11();
    disp("Elija Una categoría:");
    salto_linea();
end
```
Como vemos, imprime por pantalla la cadena *Elija Una Categoría* y posteriormente inserta un salto de línea.
* ``[accion, ok] = leeraccion1();``: Esta sentencia llama a la función **leeraccion1()**, la cual devuelve dos valores que se guardan en "accion" y "ok" respectivamente. A continuación vemos el código de esta función y la explicación del mismo:
```
function [a, ok] = leeraccion1();
    a = input('Introduzca un Numero: ');
    if a == 1 | a == 2 | a == 3
        ok = true;
    else
        ok = false;
    end
end
```
Como vemos, se lee un número de teclado y se almacena en "a". Posteriormente se evalúa si dicho número es válido y se almacena un booleano ('true' ó 'false) en "ok". La función devuelve los valores de "a" y "ok".

Continuando con el código de **procedimiento_1**, si el número introducido por el usuario es incorrecto (en cuyo caso, "ok" almacenará el valor 'false'), se imprime un mensaje de error de la siguiente manera:
```
if ~ok
    disp("Numero introducido Incorrecto");
    salto_linea();
end
```
Decir que este primer bucle de **procedimiento_1** es una llamada **BLOQUEANTE**, lo cual quiere decir que estará ejecutándose iterativamente hasta que el número leído de teclado sea correcto.

En cuanto al segundo bucle del que consta **procedimiento_1**, decir que es idéntico al ya mencionado salvo por la sentencia ``[cat_elegida, ok] = leercategoria(categoria);``.
Con esta sentencia se llama a la función **leercategoria(categoria)** la cual recibe como parámetro el array "categoria" y devuelve dos valores que se almacenan en "cat_elegida" y "ok" respectivamente. Su implementación es la siguiente:
```
function [c, ok] = leercategoria(cat);
    c = input('Introduzca una categoria de las siguientes: ', 's');
    [filas, columnas] = size(cat); %Me quedo con las filas que contiene el array
    i = 1;
    ok = false;
    %Compruebo si existe la categoria introducida
    while i <= filas & ~ok
        if strcmp(cat(i), c) %comparo ambos strings
            ok = true;
        end
        i = i + 1;
    end
    if strcmp(c, "Todas")
        ok = true;
    end
end
```
Esta función se encarga de leer una categoría introducida por el usuario y comprobar si es correcta, es decir, si se corresponde con alguna de las categorías leídas del fichero excel.
Con la sentencia ``c = input('Introduzca una categoria de las siguientes: ', 's');`` se almacena en "c" la categoría introducida por el usuario (como string). Posteiormente guardo en la variable "filas" el número de elementos que contiene el array "categoria" de la siguiente manera: ``[filas, columnas] = size(cat);``. En las dos líneas sucesivas se declara la variable "i" y se inicializa a 1 y se inicializa la variable "ok" a 'false'. Estas dos variables nos servirán como condicones de salida del bucle, ya que el buccle iterará mientras el valor contenido en "i" sea menor que el numero de elementos del array "categoria" (guardado en "filas") o bien mientras "ok" sea 'fasle'. ¿Cuándo cambia el valor de "ok"? El valor de "ok" responde al siguiente código:
```
if strcmp(cat(i), c)
    ok = true;
end
```
La sentencia ``strcmp(s1, s2)`` compara dos strings ('s1' y 's2') devolviendo '1' si son iguales (o 'true') y '0' sin no lo son (0 'false'). Por lo tanto, en el momento que el string introducido por el usuario sea igual a cualquiera de las categorías guardads en el array "categoria", "ok" pasará a almacenar el valor booleano 'true'. Mientras tanto, este valor será 'false'. Lo que la función **leercategoria()** devuelve son los valores de "c" y "ok", en donde se almacenan la categoría introducida por el usuario y el valor booleano que indica si ésta es correcta, respectivamente.

Por último, el usuario también podrá introducir la cadena "Todas" para que las operaciones siguientes se apliquen a todas las categorías. Es por esto que tenemos que hacer que es string "Todas" sea válido. De eso se encarga el siguiente código también perteneciente a la función **leercategoria()**, como puede observarse:
```
if strcmp(c, "Todas")
    ok = true;
end
```
Igual que en el caso anterior, el segundo bucle de **procedimiento_1** es una llamada **BLOQUEANTE**, lo cual quiere decir que estará ejecutándose iterativamente hasta que la categoría leída de teclado sea correcta.

