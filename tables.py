#!/usr/bin/python


#Código que presenta los diccionarios con los que vamos a trabajar


coded_block_pattern_dict = {'111': 60, '00011100': 35,
                            '1101': 4, '00011011': 13,
                            '1100': 8, '00011010' : 49,
                            '1011': 16, '00011001' : 21,
                            '1010': 32, '00011000' : 41,
                            '10011': 12, '00010111' : 14,
                            '10010': 48, '00010110' : 50,
                            '10001': 20, '00010101' : 22,
                            '10000': 40, '00010100' : 42,
                            '01111': 28, '00010011' : 15,
                            '01110': 44, '00010010' : 51,
                            '01101': 52, '00010001' : 23,
                            '01100': 56, '00010000' : 43,
                            '01011': 1, '00001111' : 25,
                            '01010': 61, '00001110' : 37,
                            '01001': 2, '00001101' : 26,
                            '01000': 62, '00001100' : 38,
                            '001111': 24, '00001011' : 29,
                            '001110': 36, '00001010' : 45,
                            '001101': 3, '00001001' : 53,
                            '001100': 63, '00001000' : 57,
                            '0010111': 5, '00000111' : 30,
                            '0010110': 9, '00000110' : 46,
                            '0010101': 17, '00000101' : 54,
                            '0010100': 33, '00000100' : 58,
                            '0010011': 6, '000000111' : 31,
                            '0010010': 10, '000000110' : 47,
                            '0010001': 18, '000000101' : 55,
                            '0010000': 34, '000000100' : 59,
                            '00011111': 7, '000000011' : 27,
                            '00011110': 11, '000000010' : 39,
                            '00011101': 19, '000000001' : 0}


macroblock_address_increment_dict = {'1' : 1,             '011' : 2,           '010' : 3 ,          '0011': 4 ,          '0010' : 5,
                             '00011' : 6,         '00010' : 7,         '0000111' : 8,       '0000110 ' : 9,      '00001011' : 10,
                             '00001010' : 11,     '00001001' : 12,     '00001000' : 13,     '00000111 ' : 14,    '00000110 ' : 15,
                             '0000010111' : 16,   '0000010110 ' : 17,  '0000010101' : 18,   '0000010100' : 19,   '0000010011 ' : 20,
                             '0000010010' : 21,   '00000100011 ' : 22, '00000100010 ' : 23, '00000100001' : 24,  '00000100000' : 25,
                             '00000011111' : 26,  '00000011110' : 27,  '00000011101' : 28,  '00000011100 ' : 29, '00000011011' : 30,
                             '00000011010' : 31,  '00000011001 ' : 32, '00000011000' : 33}


#### Diccionario macroblock_type pagina 248 norma ITU. Cuadro B.2 y Cuadro B.4
macroblock_type_p = {'1':'0101000',
            '01':'0001000',
            '001':'0100000',
            '00011':'0000100',
            '00010':'1101000',
            '00001':'1001000',
            '000001':'1000100'}
macroblock_type_b = {'10':'0110000',
             '11':'0111000',
             '010':'0010000',
             '011':'0011000',
             '0010':'0100000',
             '0011':'0101000',
             '00011':'0000100',
             '00010':'1111000',
             '000011':'1101000',
             '000010':'1011000',
             '000001':'1000100'}





