#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   Servo Example - Example of usage ASMpi class

.. Licence MIT
.. codeauthor:: Jan Lipovský <janlipovsky@gmail.com>, janlipovsky.cz
"""

from AMSpi import AMSpi
import time

def ADELANTE():
        print("ADELANTE")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
        time.sleep(5)
def ATRAS():
        print("ATRAS")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
        time.sleep(5)
def DERECHA():
        print("DERECHA")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
        amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4], clockwise=False)
        time.sleep(5)
def IZQUIERDA():
        print("IZQUIERDA")
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise=False)
        amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4])
        time.sleep(5)
def STOP():
        print("Stop")
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])
        time.sleep(1)
def EXIT():
        print("Stop and Exit")
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])

if  __name__ == '__main__':
    with AMSpi() as amspi:    
        amspi.set_74HC595_pins(21, 20, 16)
        amspi.set_L293D_pins(5, 6, 13, 19)
