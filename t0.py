# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:37:26 2026

@author: ferre
"""
import numpy as np
import matplotlib.pyplot as plt

# %% Definiciones

N = 1000
fs = 1000

def mi_funcion_sen(vmax, dc, ff, ph, nn, fs):

    tt = np.arange(nn) / fs # tt: vector del tiempo.Todos los instantes en los que tomás una muestra de la señal.

    xx = dc + vmax * np.sin(2 * np.pi * ff * tt + ph)
    
    return (tt,xx)
# %% ff=2

vmax = 1.5 #Amplitud
dc = 0 #Por donde oscila. desplaza verticalmente toda la senoide
ph = 0 #fase inicial
ff = 2 #Entiendo que es la frecuencia

tt, xx = mi_funcion_sen(vmax, dc, ff, ph, N, fs)

plt.figure()
plt.plot(tt, xx)
plt.grid()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.title("Señal senoidal de 2 Hz")
plt.show()
# %% ff=100

vmax = 1.5 #Amplitud
dc = 0 #Por donde oscila. desplaza verticalmente toda la senoide
ph = 0 #fase inicial
ff = 100 #Entiendo que es la frecuencia

tt, xx = mi_funcion_sen(vmax, dc, ff, ph, N, fs)

plt.figure()
plt.plot(tt, xx)
plt.grid()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.title("Señal senoidal de 100 Hz")
plt.show()
# %% ff=500

vmax = 1.5 #Amplitud
dc = 0 #Por donde oscila. desplaza verticalmente toda la senoide
ph = 0 #fase inicial
ff = 500 #Entiendo que es la frecuencia

tt, xx = mi_funcion_sen(vmax, dc, ff, ph, N, fs)

plt.figure()
plt.plot(tt, xx)
plt.grid()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.title("Señal senoidal de 500 Hz")
plt.show()
# %% ff=999

vmax = 1.5 
dc = 0 
ph = 0 
ff = 999 

tt, xx = mi_funcion_sen(vmax, dc, ff, ph, N, fs)

plt.figure()
plt.plot(tt, xx)
plt.grid()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.title("Señal senoidal de 999 Hz")
plt.show()
# %% ff=1001

vmax = 1.5 
dc = 0 
ph = 0 
ff = 1001

tt, xx = mi_funcion_sen(vmax, dc, ff, ph, N, fs)

plt.figure()
plt.plot(tt, xx)
plt.grid()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.title("Señal senoidal de 1001 Hz")
plt.show()
# %% ff=2001

vmax = 1.5 
dc = 0 
ph = 0 
ff = 2001 

tt, xx = mi_funcion_sen(vmax, dc, ff, ph, N, fs)

plt.figure()
plt.plot(tt, xx)
plt.grid()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.title("Señal senoidal de 2001 Hz")
plt.show()
# %% Señal cuadrada

def mi_funcion_cuadrada(vmax, dc, ff, ph, nn, fs):

    tt = np.arange(nn) / fs

    seno = np.sin(2 * np.pi * ff * tt + ph)

    xx = dc + vmax * np.where(seno >= 0, 1, -1)

    return tt, xx
# %% 

vmax = 1.5 
dc = 0 
ph = 0
ff = 2 #Entiendo que es la frecuencia

tt, xx = mi_funcion_cuadrada(vmax, dc, ff, ph, N, fs)

plt.figure()
plt.plot(tt, xx)
plt.grid()
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.title("Señal senoidal de 2 Hz")
plt.show()

