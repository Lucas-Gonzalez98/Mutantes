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

### 1. Crear instancia de la Clase MatrizGenetica
```
secuenciaADN = m.MatrizGenetica()

```


#### 2. Llenar Lista de Secuencias de ADN y Crear Matriz

```

secuenciaADN.llenarListaSecuenciaADN()
secuenciaADN.matrizSecuenciaADN()

```
### 3. Mostrar la Matriz de Secuencia de ADN
```

print("LA MATRIZ DE SECUENCIA DE ADN CREADA DE BASES NITROGENADAS, ES: \n")
secuenciaADN.mostrarMatriz()
print()
```
### 4. Evaluar si la Secuencia de ADN es Mutante
```
print("ESTA SECUENCIA DE ADN PERTENECE A UN HUMANO: ")
secuenciaADN.esMutante()

```

Estas operaciones son esenciales para la manipulación y representación posterior de las secuencias de ADN en forma matricial, facilitando así el análisis y búsqueda de patrones específicos en la información genética proporcionada por el usuario.








