class MatrizGenetica: 
    def __init__(self):
        self.listaBasesNitrogenadas = []
        self.matrizBasesNitrogenadas = []

    def llenarListaSecuenciaADN(self):
        letrasBaseNitrogenada = {"A", "C", "G", "T"}
        for _ in range(6):            
            while True:
                cadenaNitrogenada = input(f"INGRESE LA SECUENCIA DE BASES NITROGENADAS, TIENE QUE CONTENER 6 BASES NITROGENADAS Y COMO BASE NITROGENADA SOLO  'A', 'C', 'G' o 'T'.\n").upper()

                if len(cadenaNitrogenada) == 6 and all(letra in letrasBaseNitrogenada for letra in cadenaNitrogenada):
                    self.listaBasesNitrogenadas.append(list(cadenaNitrogenada))
                    break
                else: 
                    print(f"Valor no válido. Ingrese una cadena de longitud 6 y que el conteniendo solo sea 'A', 'C', 'G' o 'T'.")

    def matrizSecuenciaADN(self):
        for i in range(6):
            fila = self.listaBasesNitrogenadas[i]
            self.matrizBasesNitrogenadas.append(fila.copy())

    def mostrarMatriz(self):
        for fila in self.matrizBasesNitrogenadas:
            for elemento in fila:
                print(elemento, end=" ")
            print()
        print()

    def esMutante(self):
        contadorEsMutante = 0
        contadorEsMutante += self.contarSecuencias(6, 3, 1, 4)
        contadorEsMutante += self.contarSecuencias(3, 6, 1, 4)
        contadorEsMutante += self.contarSecuencias(3, 3, 1, 4)
        contadorEsMutante += self.contarSecuencias(5, 2, -1, 4)
        if contadorEsMutante > 1:
            print("MUTANTE ")
            print("ES DECIR, CONTIENE MAS DE 1 SECUENCIA DE CUATRO BASES NITROGENDADAS IGUALES")
        else:
            print("NO MUTANTE ")
            print("ES DECIR, NO CONTIENE MAS DE 1 SECUENCIA DE CUATRO BASES NITROGENDADAS IGUALES")

    def contarSecuencias(self, filas, columnas, pasoFila, longitudSecuencia):
        contadorEsMutante = 0
        for fila in range(filas):
            for columna in range(columnas):
                contadorLetrasIguales = 0
                for num in range(1, longitudSecuencia, pasoFila):
                    if self.matrizBasesNitrogenadas[fila][columna] == self.matrizBasesNitrogenadas[fila][columna+num]:
                        contadorLetrasIguales += 1
                if contadorLetrasIguales == (longitudSecuencia-1):
                    contadorEsMutante += 1


                



