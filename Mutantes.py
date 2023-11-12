import Metodos as m

secuenciaADN = m.MatrizGenetica()


secuenciaADN.llenarListaSecuenciaADN()
secuenciaADN.matrizSecuenciaADN()

print("LA MATRIZ DE SECUENCIA DE ADN CREADA DE BASES NITROGENADAS, ES: \n")
secuenciaADN.mostrarMatriz()
print()
print("ESTA SECUENCIA DE ADN PERTENECE A UN HUMANO: ")
secuenciaADN.esMutante()

