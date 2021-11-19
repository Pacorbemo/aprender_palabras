# generate random integer values
from random import seed
from random import randint
def palabras(direccion):
    file1 = open(direccion + 'palabras.txt', 'r')                                                   # abrimos el fichero para lectura (2)
    Lines = file1.readlines()                                                                       # leemos todas las líneas del fichero al array Lines
    error = False
    directo = {}
    inverso = {}

    for line in Lines:                                                                              # cogemos cada una de las líneas (line) del array 
        line = line.split(',')                                                                      # separamos la linea en las dos palabras separando por la coma
        if (len(line) != 2):                                                                        # comprobamos que la linea tiene dos partes separadas por ","
            print('Error leyendo el fichero de palabras: '+line)
            error = True                                                                            # comprobamos si hay error en el fichero
            break
        uno = line[0].strip()                                                                       # nos quedamos con ambas partes (uno, dos) y lo metemos en dos diccionarios (directo e inverso)
        dos = line[1].strip()
        directo[uno] = dos
        inverso[dos] = uno

    if (~error):                                                                                    # si no hay error en el fichero
        while True:                                                                                 # leemos el modo de pregunta (directo o inverso)
            modo = input('¿Directo (0) o inverso (1)? ')
            if modo == '':                                                                          # si la respuesta es intro el programa tomara el valor Directo
                break
            try:
                modo = int(modo)
            except:
                continue
            if (modo >= 0 and modo <= 1):
                modo = int(modo)
                break
        if modo == 0 or modo == '':                                                                 # segun el modo, copiamos el diccionario directo o inverso a dic que es el que vamos a usar
            dic = directo.copy()
        else:
            dic = inverso.copy()
        max = len(dic)                                                                              # nos queamos con el numero de palabras del diccionario (max)
        while True:                                                                                 # preguntamos cuantas palabras queremos que tenga el cuestionario
            palabras = input('¿Cuantas palabras (0 - todas, max:'+str(max)+')? ')
            if palabras == '':                                                                      # si la respuesta es intro el programa tomara el valor maximo
                palabras = max
                break
            try:
                palabras = int(palabras)
            except:
                continue
            if (palabras >= 0 and palabras <= max):
                break
        if (palabras == 0):
            palabras = max
        total = palabras                                                                            # recordamos el total de palabras
        acertadas = 0                                                                               # inicializamos contador de palabras acertadas
        while (palabras > 0):
            pick = randint(0, len(dic)-1)                                                           # elegimos aleatoriamente un numero de entre el número de elementos del diccionario
            keys = list(dic.keys())                                                                 # nos queamos con las "llaves" del diccionario
            a = keys[pick]                                                                          # cogemos la palabra elegida
            b = dic[a]                                                                              # y su traducción
            del dic[a]                                                                              # eliminamos la palabra elegida del diccionario (para que no vuelva a salir luego)
            respuesta = input(a + ": ")                                                             # leemos la respuesta
            if (b.lower() == respuesta.lower()):                                                    # si pasado todo a minúscula, coincide la respuesta con la correcta, lo indicamos y aumentamos "acertadas"
                acertadas = acertadas + 1
                print("correcto " + str(acertadas) + "/" + str(total))
            else:
                print("incorrecto " + str(acertadas) + "/" + str(total))
            palabras = palabras -1                                                                  # reducimos el contador de palabras a preguntar
        if (total > 0):                                                                             # al terminar damos la nota
            print("Total: "+ str(acertadas*10/total) + " ("+str(acertadas) + "/" + str(total)+")")


palabras(r'D:\Proyectos\Python/')                                          # la direccion debe estar precedidad de una r antes de '' y debe acabar en barra / no en \
