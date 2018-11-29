# Funcionamiento Interno del Programa
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
Una vez leído el número introducido por el usuario, el programa entra en una casuística encargada de decidir qué hacer en función de dicho número. A continuación separaré esta casuística por "procedimientos" con el fin del buen entendimiento del código que a partir de este momento se explica:
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
Llegados a este punto, procedo a comentar el funcionamiento de cada uno de los "procedimientos" anteriormente indicados.
### procedimiento_1:
#### Especificación del Código:
**procedimiento_1** consta de un procedimiento llamado ``hacer_histograma(tiempo)``, el cual imprime por pantalla un histograma teniendo en cuenta todos los tiempos leídos en el fichero excel. A continuación se muestra el código de este procedimiento:
```
function [] = hacer_histograma(t);
    disp("Generando Histograma...");
    salto_linea();
    nbins = 20;
    figure
    hist(t, nbins);
    title('Histograma de tiempos');
end
```
#### Explicación del Código:
Con la sentencia ``nbins = 20;`` se define el número de intervalos de tiempo a representar, los cuales se corresponden con cada una de las barras que se verán representadas, y se guarda en la vaiable "nbins". Posteriormente, se representa el histograma haciendo uso del procedimiento **hist** que Matlab nos proporciona.
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
    a = leernum();
    if a == 1 | a == 2 | a == 3
        ok = true;
    else
        ok = false;
    end
end
```
Como vemos, se lee un número de teclado haciendo uso de la función **leernum()** cuyo código es el siguiente:
```
function [n] = leernum();
    n = input('Introduzca un numero: ');
end
```
y se almacena en "a". Posteriormente se evalúa si dicho número es válido y se almacena un booleano ('true' ó 'false) en "ok". La función devuelve los valores de "a" y "ok".

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

Tras estos dos bucles, llegamos a la sentencia ``impr_operacion1(cat_elegida, accion, categoria, tiempo);``, la cual se trata de una llamada al procedimiento **impr_operacion1** que recibe como parámetros la categoria y la accion elegidas, el array de categorías "categoria" y el array de tiempos "tiempo". A continuación se especifica el código de este procedimiento:
```
function [] = impr_operacion1(celegida, accion, c, t);
    if accion == 1
        impr_media(celegida, c, t); %Imprimir la media
    elseif accion == 2
        impr_mediana(celegida, c, t); %Imprimir la mediana
    else
        impr_desvtip(celegida, c, t); %Imprime la desviacion tipica
    end
    salto_linea();
end
```
Lo que hace este procedimiento es ejecutar cada uno de los procedimientos **impr_media**, **impr_mediana** o **impr_desvtip** según la acción previamente elegida por el usuario y que ya sabemos que es correcta gracias a la previa llamada bloqueante.
* **impr_media:** Imprime la media del tiempo correspondiente a los tiempos de la categoría elegida.
```
function [] = impr_media(celegida, c, t);
    if strcmp(celegida, 'Todas')
        media = ['Media: ', tiempoenhoras(mean(t))];
    else
        arr = [];
        [filas, columnas] = size(c); 
        j = 1;
        for i = 1:filas
           if strcmp(c(i), celegida)
               arr(j) = t(i);
               j = j + 1;
           end
        end
        %Calculo la media
        media = ['Media: ', tiempoenhoras(mean(arr))];
    end
    disp(media);
end
```
Si la categoría introducida se corresponde con el string "Todas", directamente se calcula la media del array de tiempos 't', es decir, teniendo en cuenta **TODAS** las categorías.
```
if strcmp(celegida, 'Todas')
    media = ['Media: ', tiempoenhoras(mean(t))];
```
Si la categoría introducida es cualquier otra distinta de "Todas", se guarda en un array auxiliar llamado 'arr' los tiempos correspondientes a dicha categoría y se calcula la media de este array.
```
else
    arr = [];
    [filas, columnas] = size(c);
    j = 1;
    for i = 1:filas
       if strcmp(c(i), celegida)
           arr(j) = t(i);
           j = j + 1;
       end
    end
    media = ['Media: ', tiempoenhoras(mean(arr))];
end
```
Finalmente, con la sentencia ``disp(media);`` se imprime el valor de la media calculado.
* **impr_mediana:** Imprime la mediana del tiempo correspondiente a los tiempos de la categoría elegida. Su impementación es idéntica a **impr_media** salvo por el cálculo de la mediana que se hace llamando al procedimiento ``median(a)`` donde 'a' es el array de tiempos.
* **impr_desvtip:** Imprime la desviación típica del tiempo correspondiente a los tiempos de la categoría elegida. Su impementación es idéntica a **impr_media** salvo por el cálculo de la desviación que se hace llamando al procedimiento ``std(a)`` donde 'a' es el array de tiempos.

La función **tiempoenhoras(n)** se encarga de pasar un tiempo en segundos (que es el argumento 'n') a formato hh:mm:ss y lo devuelve como string. La implementación de esta función es la siguiente:
```
function [s] = tiempoenhoras(n);
    finish = false;
    segs = 0;
    mins = 0;
    horas = 0;
    ts = n;
    while ~finish
        t = ts - 60;
        if t >= 0
            mins = mins + 1;
            ts = t;
        else
            finish = true;
            segs = segs + ts;
        end
        if mins >= 60
            horas = horas + 1;
            mins = mins - 60;
        end
    end
    s = [num2str(horas), ':', num2str(mins), ':', num2str(segs)];
end
```
La algoritmia se trata de ir restando 60 segundos a 'n' e ir incrementando progresivamente los minutos, horas y segundos según corresponda.
### procedimiento_3:
#### Especificación del Código:
Este procedimiento se compone de una llamada al procedimiento **impr_gaussiana** el cual se compone del siguiente código:
```
function [] = impr_gaussiana(t);
    disp("Generando Gaussiana...");
    salto_linea();
    nbins = 20;
    figure
    histfit(t, nbins);
    title('Gaussiana sobre Histograma');
end
```
#### Explicación del Código:
Se define el número de intervalos en los que vamos a agrupar los tiempos guardados en el array 't' que recibe como parámetro este procedimiento y se guarda en 'nbins'. Posteriormente se imprime por pantalla el histograma con la gaussiana superpuesta haciendo uso de la función ``histfit(t, nbins);`` que nos proporciona Matlab.
### procedimiento_4:
#### Especificación del Código:
```
ok = false;
while ~ok
    impr_submenu2();
    [accion, ok] = leeraccion2();
    salto_linea();
    if ~ok
        disp("Numero introducido Incorrecto");
        salto_linea();
    end
end
impr_operacion2(accion, tiempo);
```
El comportamiento del bucle while es muy similar al del "procedimiento_2" salvo por tres sentencias que se explican a continuación:
* ``impr_submenu2();`` Imprime un nuevo submenú. Su código es el siguiente:
```
function [] = impr_submenu2();
    disp("1) Probabilidad por debajo de un tiempo");
    disp("2) Probabilidad por encima de un tiempo");
    disp("3) Probabilidad entre dos tiempos");
end
```
* ``[accion, ok] = leeraccion2();`` Se encarga de leer el número introducido por el usuario, que se corresponde con la acción que éste quiere que se realice, y evalar si es correcta. El valor del número se guarda en "accion" y el booleano que indica si es correcto se guarda en "ok". El código es el siguiente:
```
function [a, ok] = leeraccion2();
    a = leernum();
    if a == 1 | a == 2 | a == 3
        ok = true;
    else
        ok = false;
    end
end
```
* ``impr_operacion2(accion, tiempo);`` Con la llamada a este procedimiento se ejecuta el siguiente código:
```
function [] = impr_operacion2(accion, t);
    if accion == 1
        impr_prob_debajo(t); %Imprimir probabilidad de llegar por debajo de un tiempo determinado
        salto_linea();
    elseif accion == 2
        impr_prob_encima(t); %Imprimir la probabilidad de llegar por encima de un tiempo determinado
        salto_linea();
    else
        impr_prob_entre(t); %Imprimir la probabilidad de llegar entre dos tiempos
        salto_linea();
    end
end
```
Dependiendo de la acción introducida por el usuario, se ejecuta el procedimiento **impr_prob_debajo(t)**, **impr_prob_encima(t)** o **impr_prob_entre(t)**. Se procede a explicar cada una de ellas:
##### impr_prob_debajo:
Este procedimiento imprime la probabilidad de conseguir un tiempo menor al introducido por el usuario. Su código se muestra a continuación:
```
function [] = impr_prob_debajo(t);
    tmin = tiempomenor(t);
    ti = leertiempo();
    
    [Y, M, D, H, MN, S] = datevec(ti);
    ti = H*3600+MN*60+S;
    
    media = mean(t);
    desv = std(t);
    
    prob = normcdf(ti, media, desv) - normcdf(tmin, media, desv);
    if prob <= 0
        prob = 0;
    end
    
    salto_linea();
    impr = ['Probabilidad: ', num2str(prob)];
    disp(impr);
end
```
**1.** Se guarda el tiempo menor del array de tiempos 't' haciendo uso de la función **tiempomenor** suyo código es el siguiente:
```
function [n] = tiempomenor(t);
    n = t(1);
    [filas, columnas] = size(t);
    for i = 2:filas
       if t(i) < n
           n = t(i);
       end
    end
end
```
**2.** Se lee el tiempo introducido por el usuario en formato hh:mm:ss haciendo uno de la función **leertiempo** cuyo código es el siguiente:
```
function [c] = leertiempo();
    c = input('Introduzca tiempo en formato hh:mm:ss: ', 's');
end
```
**3.** El tiempo leído se pasa a segundos y se guarda en 'ti' mediante las siguientes sentencias:
```
[Y, M, D, H, MN, S] = datevec(ti);
ti = H*3600+MN*60+S;
```
**4.** Guardamos la media y la desviación típica en las variables 'media' y 'desv' tal como se muestra:
```
media = mean(t);
desv = std(t);
```
**5.** Calculamos la probabilidad deseada con la sentencia ``prob = normcdf(ti, media, desv) - normcdf(tmin, media, desv);`` haciendo uso de la función *normcdf* que Matlab proporciona.
**6.** Imponemos que la probabilidad no pueda ser menor que 0 con el siguiente código:
```
if prob <= 0
    prob = 0;
end
```
**7.** Por último, se imprime la probabilidad de la siguiente manera:
```
impr = ['Probabilidad: ', num2str(prob)];
disp(impr);
```
##### impr_prob_encima:
Imprime la probabilidad de conseguir un tiempo mayor al introducido por el usuario.

Únicamente se diferencia con la anterior en la sentencia ``tmax = tiempomayor(t);``, mediante la que se guarda el tiempo mayor; y en la sentencia ``prob = normcdf(tmax, media, desv) - normcdf(ti, media, desv);``.
El código de la función **tiempomayor** es el mostrado a continuación:
 ```
 function [n] = tiempomayor(t);
    n = t(1);
    [filas, columnas] = size(t);
    for i = 2:filas
       if t(i) > n
           n = t(i);
       end
    end
end
 ```
 ##### impr_prob_entre:
 Imprime la probabilidad de conseguir un tiempo contenido entre dos tiempos introducidos por el usuario.
 
 La especificación del código de este procedimiento es el siguiente:
```
function [] = impr_prob_entre(t);
    
    ti1 = leertiempo();
    ti2 = leertiempo();
   
    [Y, M, D, H, MN, S] = datevec(ti1);
    ti1 = H*3600+MN*60+S;
    
    [Y, M, D, H, MN, S] = datevec(ti2);
    ti2 = H*3600+MN*60+S;
    
    media = mean(t);
    desv = std(t);
    
     tmenor = tiempomenor(t);
     tmayor = tiempomayor(t);
    
    if ti1 >= ti2
        prob = normcdf(ti1, media, desv) - normcdf(ti2, media, desv);
    else
        prob = normcdf(ti2, media, desv) - normcdf(ti1, media, desv);
    end
    if ti1 > tmayor & ti2 > tmayor | ti1 < tmenor & ti2 < tmenor
        prob = 0;
    end
    if prob <= 0
        prob = 0;
    end
    
    salto_linea();
    impr = ['Probabilidad: ', num2str(prob)];
    disp(impr);
end
```
La principal diferencia con respecto a las dos anteriores es que en este caso se leen de teclado dos tiempos, lo cual se lleva a cabo con las sentencias:
```
ti1 = leertiempo();
ti2 = leertiempo();
```
### procedimiento_5:
#### Especificación del Código:
```
ok = false;
while ~ok
    impr_submenu3();
    [accion, ok] = leeraccion3();
    salto_linea();
    if ~ok
        disp("Numero introducido Incorrecto");
        salto_linea();
    end
end
impr_operacion3(accion, tiempo);
```
#### Explicación del Código
El comportamiento de este bloque de código es idéntico a lo mencionado en casos anteriores salvando las llamadas a  **impr_submenu3** **leeraccion3** y **impr_operacion3**. Procedo a mostrar el código de estos tres procedimientos:
##### impr_submenu3:
```
function [] = impr_submenu3();
    disp("Elija una de las siguientes opciones:");
    salto_linea();
    disp("1) Cálculo de Cuartiles");
    disp("2) Cálculo de Percentiles");
    salto_linea();
end
```
##### leeraccion3:
```
function [a, ok] = leeraccion3();
    a = leernum();
    if a == 1 | a == 2
        ok = true;
    else
        ok = false;
    end
end
```
##### impr_operacion3:
```
function [] = impr_operacion3(a, t);
    if a == 1
        impr_cuartiles(t);
    else
        impr_percentil(t);
    end
end
```
Este procedimiento ejecuta a su vez los procedimientos **impr_cuartiles** o **impr_percentil** en función de la acción elegida por el usuario.
* **impr_cuartiles:** Imprimes los tres cuartiles. Se compone del siguiente código que a su vez hace las llamadas a **impr_primer_cuartil**, **impr_seg_cuartil** e **impr_tercer_cuartil**.
```
function [] = impr_cuartiles(t);
    impr_primer_cuartil(t);
    impr_seg_cuartil(t);
    impr_tercer_cuartil(t);
    salto_linea();
end
```
A continuación se detallan cada uno de los procedimientos:
##### impr_primer_cuartil:
```
function [] = impr_primer_cuartil(t);
    K = 0.25;
    [nelems, cols] = size(t);
    pos = nelems * K;
    arr = sort(t);
    cuart = tiempoenhoras(percentil(pos, arr));
    impr = ['Primer Cuartil: ', cuart];
    disp(impr);
end
```
**1.** En "K" se almacena la medida de posicion del primer cuartil.

**2.** Se guarda en "nelems" el número de elementos del array 't'.

**3.** Se define la posición en la que se encuentra el cuartil.

**4.** Se ordena el array 't' de manera ascendente y se guarda en 'arr'.

**5.** Se calcula el cuartil en formato hh:mm:ss con la función *tiempoenhoras* haciendo uso de la función **percentil**, la cual se compone del siguiente código:
```
function [n] = percentil(pos, arr);
    pos_ent = floor(pos);
    if pos > pos_ent
        n = (arr(pos_ent) + arr(pos_ent + 1)) / 2;
    else
        n = arr(pos_ent);
    end
end
```
Me quedo con la parte entera de la posición y evalúo si la posicion es mayor que su parte entera; en cuyo caso se ejecuta la sentencia ``n = (arr(pos_ent) + arr(pos_ent + 1)) / 2;`` para guardar en 'n' el valor del percentil. De ser iguales la parte entera de 'pos' y 'pos', se ejecuta ``n = arr(pos_ent)``.
**6.** Se imprime el cuartil.
##### impr_seg_cuartil:
El segundo cuartil se corresponde con la mediana, por lo que su código es como se aprecia a continuación:
```
function [] = impr_seg_cuartil(t);
    cuart = tiempoenhoras( median(t));
    impr = ['Segundo Cuartil: ', cuart];
    disp(impr);
end
```
##### impr_tercer_cuartil:
Se comporta exactamente igual que **impr_primer_cuartil** con la salvedad de que el valor de "K" es 0.75, por lo que su código queda de la siguiente manera:
```
function [] = impr_tercer_cuartil(t);
    K = 0.75;
    [nelems, cols] = size(t);
    pos = nelems * K;
    arr = sort(t);
    cuart = tiempoenhoras(percentil(pos, arr));
    impr = ['Tercer Cuartil: ', cuart];
    disp(impr);
end
```
* **impr_percentil:** Imprime el percentil que el usuario desee. el código es el siguiente:
```
function [] = impr_percentil(t);
    ok = false;
    while ~ok
        [npercent, ok] = numpercentil();
        salto_linea();
        if ~ok
            disp('Numero de percentil introducido incorrecto');
        end
    end
    K = npercent / 100;
    [nelems, cols] = size(t);
    pos = nelems * K;
    arr = sort(t);
    perc = tiempoenhoras(percentil(pos, arr));
    impr = ['Percentil ', num2str(npercent), ': ', perc];
    disp(impr);
    salto_linea();
end
```
Como puede observarse, el código se compone de un bucle while que itera tantas veces como sea necesario hasta que el usuario introduzca un número correcto (esto se evalúa con la función *numpercentil()*) y después, una serie de sentencias que son idénticas a la función **impr_primer_cuartil** o **impr_tercer_cuartil** previamente explicadas. Por tanto, la única novedad es que el parámetro "K" depende del número de percentil "npercent" leída de teclado mediante la sentencia ``[npercent, ok] = numpercentil();``. A continuación se muestra el código de la función *numpercentil*:
```
function [n, ok] = numpercentil();
    n = input('Introduzca el número de percentil que desea: ');
    if n >= 1 & n <= 99
        ok = true;
    else
        ok = false;
    end
end
```

# Guía de Uso
Al ejecutar el programa, lo primero que veremos es un menú como el que se ve a continuación:
```
Teclee la opción deseada:
 
1) Histograma
2) Datos Numéricos
3) Distribución Gaussiana
4) Cálculo de Probabilidades
5) Cálculo de Cuartiles
6) Salir del Programa
Introduzca un numero: 
```
En este estado, tecleamos el número que se corresponda con la opción que queremos llevar a cabo.

En el caso de las opciones 2, 4 y 5 se imprimirá un submenú o en ocasiones hasta dos ofreciendo al usuario. Se procede a mostrarlos:
* **Submenú Opción *2) Datos Numéricos*:**
```
Eliga la acción a realizar:
 
1) Media
2) Mediana
3) Desviación Típica
Introduzca un numero:
```
En este punto, el usuario ha de introducir un número dependiendo del cálculo que quiera hacer. Tras esto, se le preguntará sobre la categoría a la que quiere aplicar dicho cálculo de la siguiente manera:

Supongamos que hemos elegido la opción *3) Desviación Típica*
```
Introduzca una categoria:
```
**NOTA:** También se admite la categoría "Todas". Haciendo esto, el cálculo se aplicará a **TODAS** las categorías.

Suponiendo que hemos introducido la categoría 'PromM' una posible salida del programa sería la siguiente:
```
Desviación Típica: 0:10:4.9792
```
* **Submenú Opción *4) Cálculo de Probabilidades*:**
```
1) Probabilidad por debajo de un tiempo
2) Probabilidad por encima de un tiempo
3) Probabilidad entre dos tiempos
Introduzca un numero:
```
Supongamos que elegimos la opción 1. La salida podría ser la siguiente:
```
Introduzca tiempo en formato hh:mm:ss:
```
Y tras haber introducido el tiempo deseado, se imprimirá algo como:
```
Probabilidad: 0.48469
```
* **Submenú Opción *5) Cálculo de Cuartiles*:**
```
1) Cálculo de Cuartiles
2) Cálculo de Percentiles
```
**1.** Suponiendo que elegimos la opción 1, la salida será algo como:
```
Primer Cuartil: 0:51:46
Segundo Cuartil: 0:59:13
Tercer Cuartil: 1:8:15
```
**2.** Suponiendo que elegimos la opción 2, se imprimirá por pantalla un nuevo submenú como el siguiente:
```
Introduzca el número de percentil que desea:
```
Y tras introducir el número (para el ejemplo se ha introducido 21), la salida será como la descrita a continuación:
```
Percentil 21: 0:50:25
```

**NOTA:** Cualquier número introducido que no conste entre las opciones dadas por cualquiera de los menús y/o submenús probocará un aviso de error pero el programa continuará su ejecución.
