#!/usr/bin/python

from codigo import MB_pattern_code

archivo_mpeg = 'CH63_PID0110.mpg'

name_mb = ['2_P4', '20_P4', '21_P4', '49_P4', '2_B5', '102_B5']
pos_mb = [792516, 793313, 793325, 795832, 1012799, 1014775]

indice = 5
#Cargamos el primer macrobloque
m1 = MB_pattern_code(name_mb[indice]) #Generamos un elemento de la clase de MB_pattern_code
m1.load(archivo_mpeg) #Cargamos el primer archivo
m1.set_MB_pos(pos_mb[indice]) #Asignamos la posición del primer macrobloque
m1.proc_MB_params_pattern_code()
m1.show_MB_params_pattern_code()




