# Mutantes
* Nombre y Apellido: Lucas Gonzalez
* Legajo: 51562
* DNI: 41271105
* Email: topolucasnicolas@gmail.com

## Proyecto

Este proyecto consiste en la creación de un programa interactivo en el cual el usuario proporciona una lista de seis secuencias de ADN, cada una compuesta por seis bases nitrogenadas. Las letras permitidas en estas cadenas son exclusivamente A, T, C y G, representando así las bases nitrogenadas del ADN. El programa genera a partir de estas secuencias una matriz de dimensiones 6x6 y determina si la muestra es de un organismo mutante o no.

En la matriz resultante, el programa realiza búsquedas de secuencias de cuatro bases nitrogenadas idénticas tanto en forma oblicua, horizontal como vertical. Si el programa identifica más de una de estas secuencias, concluye que la muestra pertenece a un organismo mutante. Por el contrario, si encuentra cero o una sola secuencia de cuatro bases nitrogenadas iguales, determina que la muestra no pertenece a un organismo mutante. El resultado es presentado al usuario, indicando claramente si la muestra es mutante o no.

## Como lo resolvimos
Inicialmente, diseñamos una clase denominada "MatrizGenetica" para gestionar los objetos relacionados con el proyecto. En la fase de entrada, se implementa un mecanismo para validar que cada una de las seis secuencias de bases nitrogenadas ingresadas por el usuario conste de exactamente seis bases y que estas sean válidas (A, T, C, G). En caso de incumplimiento, se solicita nuevamente la entrada hasta obtener una cadena válida.

Una vez se completa la lista de secuencias, procedemos a crear una matriz de dimensiones 6x6, la cual se presenta al usuario. En esta matriz, se lleva a cabo una búsqueda secuencial de secuencias de cuatro bases nitrogenadas, tanto en sentido oblicuo como horizontal y vertical. Cada vez que se identifica una de estas secuencias, se incrementa un contador.

Posteriormente, al obtener la suma total del contador, se verifica si este valor es superior a uno. De ser así, se concluye que la muestra es mutante y se presenta la correspondiente respuesta. En caso contrario, si el contador no supera el valor de uno, se determina que la muestra no es mutante. 



## Como se utiliza el codigo

Explicaremos lo mas detalladamente como funciona el codigo Mutantes.py

En esta línea, estamos creando una instancia de la clase MatrizGenetica del módulo m y asignándola a la variable secuenciaADN. Esto nos permite trabajar con la matriz genética utilizando la variable secuenciaADN en el resto de nuestro código.

```

secuenciaADN = m.MatrizGenetica()

```

En las dos líneas de código siguientes, el programa realiza las siguientes acciones:

#### 1- Llenar Lista de Secuencias de ADN:

* Se accede a la función `llenarListaSecuenciaADN()`, la cual solicita al usuario que ingrese 6 cadenas de la secuencia de ADN, cada una con 6 bases nitrogenadas.
* Verifica que cada secuencia tenga exactamente 6 bases nitrogenadas y que estas contengan únicamente las letras A, C, T, G.
* Las secuencias válidas se agregan a una lista.

#### 2- Crear Matriz de 6x6 a partir de la Lista de Secuencias de ADN:

* Posteriormente, se utiliza la función `matrizSecuenciaADN()` para ingresar la lista de secuencias de ADN en una matriz de dimensiones 6x6.

```

secuenciaADN.llenarListaSecuenciaADN()
secuenciaADN.matrizSecuenciaADN()

```

Estas operaciones son esenciales para la manipulación y representación posterior de las secuencias de ADN en forma matricial, facilitando así el análisis y búsqueda de patrones específicos en la información genética proporcionada por el usuario.

En estas tres líneas de código, accedemos a una función encargada de imprimir por pantalla la matriz 6x6 que representa la secuencia de ADN construida a partir de las bases nitrogenadas ingresadas por el usuario.

La instrucción `print("MATRIZ DE SECUENCIA DE ADN GENERADA A PARTIR DE BASES NITROGENADAS:\n")`
proporciona una indicación clara al usuario sobre la naturaleza de la información que se mostrará a continuación. Luego, la función `mostrarMatriz()` de la clase `MatrizGenetica` se utiliza para imprimir visualmente la matriz 6x6 en la pantalla. Finalmente, `print()` se emplea para agregar un espacio adicional después de la matriz, mejorando la presentación del resultado.

```

print("LA MATRIZ DE SECUENCIA DE ADN CREADA DE BASES NITROGENADAS, ES: \n")
secuenciaADN.mostrarMatriz()
print()

```

En este bloque de código, se accede a una función que, a su vez, invoca otra función encargada de contabilizar las secuencias de 4 bases nitrogenadas iguales en direcciones oblicuas, verticales y horizontales. Una vez realizada esta cuantificación, se procede a la evaluación de la función `esMutante()`. Si el recuento de secuencias iguales es mayor a 1, el programa devuelve el mensaje "MUTANTE"; de lo contrario, si la cantidad es igual o menor a 1, indica que la secuencia no es mutante.

```

print("ESTA SECUENCIA DE ADN PERTENECE A UN HUMANO: ")
secuenciaADN.esMutante()

```
Esta impresión proporciona una conclusión clara y concisa sobre la evaluación de la secuencia de ADN, mejorando la legibilidad y comprensión del código.



