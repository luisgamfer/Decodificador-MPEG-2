#!/usr/bin/python

import os
from bitstring import ConstBitStream
import numpy as np

from tables import *

class MB_pattern_code:

    def __init__(self,identificador): #Constructor de la clase
        self.m = None
        self.id = identificador
        self.picture_coding_type = None
        self.MB_address_increment = None
        self.macroblock_type = None
        self.MB_quant = None
        self.MB_motion_forward = None
        self.MB_motion_backward = None
        self.MB_pattern = None
        self.MB_intra = None
        self.spatial_temp_weight_code_flag = None
        self.spatial_temp_wight_classes = None
        self.quantiser_scale_code = None
        self.coded_block_pattern = None
        self.tipo_imagen = None
        self.pattern_code = None
        self.valores_luminancia = None

    def load(self, archivo): #Función que nos lee el archivo

        print("Abriendo archivo...")

        self.f = open(archivo,'rb')
        self.bs = ConstBitStream(self.f)

    def set_MB_pos(self, pos): #Asigna la posición de comienzo del MB

        self.bs.pos = pos
        #self.bs.read("uint:8")

    def proc_MB_params_pattern_code(self):

        #Primeramente, si existe "macroblock_escape" antes de obtener "macroblock_address_increment"
        MB_escape = self.bs.peek('bin:11') #Leemos los primeros 11 bits

        if MB_escape == '00000001000': #Se debe hacer en un while en vez de un if
            MB_escape = self.bs.read('bin:11') #Estos son los bits correspondientes a macroblock_escape.
                                                #La proxima vez que llamemos a read, leerá a partir de ahí

        #Se procede a obtener "macroblock_address_increment"

        for i in range(1,12):
            self.MB_address_increment = self.bs.peek('bin:' +str(i)) #Peak a los siguiente 11 bits
                                                                  #que previamente pasamos a cadena de caracteres

            if self.MB_address_increment in macroblock_address_increment_dict.keys(): #Comprobamos si el valor que se ha hecho peek
                                                                                #coincide con algún valor del diccionario

                self.MB_address_increment = self.bs.read('bin:' +str(i)) #Como está dentro del if, lo almacenamos en la variable


                break #Salimos del bucle

        #Vamos a sacar el tipo de imagen que tenemos

        if self.id.split('_')[-1][0] == 'I':
            self.picture_coding_type = '001'
        if self.id.split('_')[-1][0] == 'P':
            self.picture_coding_type = '010'
        if self.id.split('_')[-1][0] == 'B':
            self.picture_coding_type = '011'



        for i in range (1,10):
            self.macroblock_type = self.bs.peek('bin:' +str(i))

        #Vemos en qué tipo de imagen estamos
            if self.picture_coding_type == '010': #Estamos en una imagen tipo P
                if self.macroblock_type in macroblock_type_p.keys():
                    self.macroblock_type = self.bs.read('bin:' +str(i))
                    self.macroblock_type = str(macroblock_type_p[self.macroblock_type])
                    self.tipo_imagen = 'Tipo P'
                    break #Salimos del bucle

            elif self.picture_coding_type == '011':  # Estamos en una imagen tipo B
                if self.macroblock_type in macroblock_type_b.keys():
                    self.macroblock_type = self.bs.read('bin:' + str(i))
                    self.macroblock_type = str(macroblock_type_b[self.macroblock_type])
                    self.tipo_imagen = 'Tipo B'
                    break #Salimos del bucle

            else:
                    print("La imagen no es ni tipo P ni tipo B")
                    break


        #Asignamos los flags de macroblock_type a una variable
        self.MB_quant = self.macroblock_type[0]
        self.MB_motion_forward = self.macroblock_type[1]
        self.MB_motion_backward = self.macroblock_type[2]
        self.MB_pattern = self.macroblock_type[3]
        self.MB_intra = self.macroblock_type[4]
        self.spatial_temp_weight_code_flag = self.macroblock_type[5]
        self.spatial_temp_wight_classes = self.macroblock_type[6]


        if self.MB_quant == '1': #Si macroblock_quant vale 1, existe el quantiser scale code y lo leemos

            self.quantiser_scale_code = self.bs.read('bin:5')

        if self.MB_pattern == '1': #Si macroblock_patter vale 1, existirá el coded_block_pattern

            if(self.id == '21_P4'): #el inicio de contenido de coded_block_pattern aqui es

                self.bs.pos = 793337

            elif(self.id == '49_P4'):

                self.bs.pos = 795836

            elif(self.id == '2_B5'):

                self.bs.pos = 1012815

            elif(self.id == '102_B5'):

                self.bs.pos = 1014789

            encontrado = False

            for i in range(3,10):

                self.coded_block_pattern = self.bs.peek('bin:' +str(i))

                if self.coded_block_pattern in coded_block_pattern_dict:

                    encontrado = True
                    self.coded_block_pattern = self.bs.read('bin:' +str(i)) #Puesto que el formato es 4:2:0 no hace falta leer más
                    cbp = coded_block_pattern_dict[self.coded_block_pattern]
                    break

            if encontrado == False:
                print("error")


        block_count = 6 #En nuestro caso puesto que estamos trabajando con el formato 4:2:0, block_count vale 6

        self.pattern_code = []

        for i in range(0,block_count):

            if(self.MB_intra == '1'): #Si macroblock_intra está activo

                    self.pattern_code.append('1') #Introducimos en la última posición del array un 1

            else:
                    self.pattern_code.append('0') #Introducimos un 0


        if (self.MB_pattern == '1'):
                for i in range(0,6):
                        if (cbp & (1 <<(5-i))):
                                self.pattern_code[i] = '1'

            #Puesto que es del formato 4:2:0, el código se queda hasta ahí y no hace falta hacer ninguna iteración más

        #Definimos el vector de luminancias
        self.valores_luminancia = ''

        if self.pattern_code[0] == '1':
            self.valores_luminancia += 'Y0'
        else:
            self.valores_luminancia += '-'

        if self.pattern_code[1] == '1':
            self.valores_luminancia += 'Y1'
        else:
            self.valores_luminancia += '-'

        if self.pattern_code[2] == '1':
            self.valores_luminancia += 'Y2'
        else:
            self.valores_luminancia += '-'

        if self.pattern_code[3] == '1':
            self.valores_luminancia += 'Y3'
        else:
            self.valores_luminancia += '-'

        if self.pattern_code[4] == '1':
            self.valores_luminancia += 'CB'
        else:
            self.valores_luminancia += '-'

        if self.pattern_code[5] == '1':
            self.valores_luminancia += 'CR'
        else:
            self.valores_luminancia += '-'



    def show_MB_params_pattern_code(self):

         print("El valor de macroblock_address_increment es: ", macroblock_address_increment_dict[self.MB_address_increment])
         print("El valor de picture_coding_type es: ", self.picture_coding_type,"y es del", self.tipo_imagen)
         print("El valor de macroblock_type es: ", self.macroblock_type)
         print("El valor de quantiser_scale_code es: ", self.quantiser_scale_code)
         print("El valor de coded_block_patter es: ", self.coded_block_pattern)

         print("-----------------------------------------------------------------------------")

         print("El valor de macroblock quant es: ", self.MB_quant)
         print("El valor de macroblock motion forward es: ", self.MB_motion_forward)
         print("El valor de macroblock motion backward es: ", self.MB_motion_backward)
         print("El valor de macroblock pattern es: ", self.MB_pattern)
         print("El valor de macroblock intra es: ", self.MB_intra)
         print("El valor de spatial temp weight code flag es: ", self.spatial_temp_weight_code_flag)
         print("El valor de spatial temp wight classes es: ", self.spatial_temp_wight_classes)

         print("-----------------------------------------------------------------------------")

         print("El valor de pattern_code es: ", ''.join(self.pattern_code))
         print("El valor del vector de luminancias es: ", ''.join(self.valores_luminancia))
