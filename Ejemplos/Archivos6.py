from os import system

if __name__ == '__main__':
    system('cls')

    archivoSalida = open('datos.txt','w')

    archivoSalida.write('Una linea de texto\n')
    archivoSalida.write('Otra linea de texto\n')
    archivoSalida.write('Linea de texto con numeros 1234\n')
    archivoSalida.write('Aunque hay numeros 5678, es una linea de texto\n')

    archivoSalida.close()

    archivoEntrada = open("datos.txt",'r')
    print('archivoEntrada.readline()')
    print(archivoEntrada.readline())
    archivoEntrada.close()
    
    print('\n')
