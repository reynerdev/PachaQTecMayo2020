import logging
import os.path
from os import remove 







class log:
    def __init__(self, nombreLogger):
        # create logger
        self.logger = logging.getLogger(nombreLogger)
        self.logger.filename = 'app.log'
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.FileHandler("app.log", mode='a')
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    def debug(self, mensaje):
        self.logger.debug(mensaje)

    def info(self, mensaje):
        self.logger.info(mensaje)

    def warning(self, mensaje):
        self.logger.warning(mensaje)

    def error(self, mensaje):
        self.logger.error(mensaje)

    def critical(self, mensaje):
        self.logger.critical(mensaje)



class fileManager:
    logD = log("fileManager")

    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo,'r')
            return file.read()
        except Exception as e:
            return e
        

    def borrarArchivo(self):
        directorioActual = os.getcwd()
        path = directorioActual+"\\"+self.nombreArchivo
        self.logD.debug(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                self.logD.debug("removiendo archivo")

            except Exception as error:
                self.logD.error(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            self.logD.debug(path)
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(linea + "\n")
                except Exception as e:
                    self.logD.error(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            self.logD.error(error)





class Menu:
    __log = log("Menu")
    #__log = utils.log("Menu")
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def mostrarMenu(self):
        self.limpiarPantalla()
        opSalir = True
        while(opSalir):
            self.limpiarPantalla()
            print(Color.BLUE+":::::::::::::BIENVENIDOS EMPRESA MARTINPEREZ::::::::::::::"+Color.CEND)
            print(Color.BLUE+":::::::::::::::::::" +self.nombreMenu + "::::::::::::::::::"+Color.CEND)
            
            for (key, value) in self.listaOpciones.items():
                print(key, "\t:: ", value)
            #print("Salir \t\t::  9")
            opcion = 100
            try:
                print(Color.CYAN+"Escoge tu opcion"+Color.CEND)
                opcion = int(input())
            except ValueError as error:
                self.__log.error(error)
                print(Color.RED+"Opcion invalida deben ser numeros del 0 al 2"+Color.CEND)
            contOpciones = 0
            for (key, value) in self.listaOpciones.items():
                if(opcion == int(value)):
                   contOpciones += 1
            if(contOpciones == 0):
                print(Color.RED+"Escoge una opcion valida"+Color.CEND)
                self.__log.debug("No escoje opion")
                sleep(3)
            else:
                opSalir = False

        return opcion

    def limpiarPantalla(self):
        def clear():
            #return os.system('cls')
            return os.system('clear')
        clear()




