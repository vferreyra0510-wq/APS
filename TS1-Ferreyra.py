# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:21:23 2026

@author: ferre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# %% 1) Señal sinusoidal de 2 KHz que tenga al menos 10 puntos por período.
# N = 1000
# fs = 20000
# k = 100
# vmax = 1
# dc = 0
# ph = 0
# f0 = k*(fs/N)

# #Lenguaje en tiempo de discreto
# def mi_funcion_sen():

#     n = np.arange(N) / fs # tt: vector del tiempo.Todos los instantes en los que tomás una muestra de la señal.

#     xx = dc + vmax * np.sin(2*np.pi*f0*n + ph)
    
#     return (n,xx)

# n,xx = mi_funcion_sen()

# # Calculamos la FFT :

# XX = np.fft.fft(xx)   # Representación de xx en el dominio de la frecuencia. La función fft toma esas 1000 muestras y calcula los coeficientes de la DFT
# print(XX[900])
# print(XX[100]) # Es el coeficiente de la DFT asociado a 2000 Hz, la frecuencia del senoide.

# mod_XX = np.abs(XX) # El módulo es útil para visualizar un espectro: nos permite ver claramente dónde están las componentes importantes.

# freq = np.fft.fftfreq(N, d=1/fs) # Construimos un vector de frecuencias

# plt.figure()
# plt.plot(freq, mod_XX,'.')
# plt.title("Módulo de la Transformada de Fourier")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("|X[k]|")
# plt.grid()
# plt.show()

# plt.figure()
# plt.plot(n, xx)
# plt.grid()
# plt.xlabel("Tiempo [s]")
# plt.ylabel("Amplitud [V]")
# plt.title("Señal senoidal de 2 kHz")
# plt.show()
# %% 2) Misma señal con 2 W de potencia media y desfasada en π/2.
# N = 1000
# fs = 20000
# k = 100
# vmax = 2
# dc = 0
# ph = np.pi/2
# f0 = k*(fs/N)

# #Lenguaje en tiempo de discreto
# def mi_funcion_sen():

#     n = np.arange(N) / fs # tt: vector del tiempo.Todos los instantes en los que tomás una muestra de la señal.

#     xx = dc + vmax * np.sin(2*np.pi*f0*n + ph)
    
#     return (n,xx)

# n,xx = mi_funcion_sen()

# # Calculamos la FFT :

# XX = np.fft.fft(xx)   # Representación de xx en el dominio de la frecuencia. La función fft toma esas 1000 muestras y calcula los coeficientes de la DFT
# print(XX[900])
# print(XX[100]) # Es el coeficiente de la DFT asociado a 2000 Hz, la frecuencia del senoide.

# mod_XX = np.abs(XX) # El módulo es útil para visualizar un espectro: nos permite ver claramente dónde están las componentes importantes.
# print(mod_XX[900])

# freq = np.fft.fftfreq(N, d=1/fs) # Construimos un vector de frecuencias

# plt.figure()
# plt.plot(freq, mod_XX,'.')
# plt.title("Módulo de la Transformada de Fourier")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("|X[k]|")
# plt.grid()
# plt.show()

# plt.figure()
# plt.plot(n, xx)
# plt.grid()
# plt.xlabel("Tiempo [s]")
# plt.ylabel("Amplitud [V]")
# plt.title("Señal senoidal de 2 kHz")
# plt.show()
# %% 3) Una secuencia aleatoria de ruido normalmente distribuido con DC (valor medio) 0V y varianza 0.1 W.

# N = 1000
# fs = 20000

# var = 0.1
# ruido = np.random.normal (0,np.sqrt(var),N)

# n = np.arange(N) / fs # Esto representa los instantes en los que tomaste cada muestra.

# plt.figure()
# plt.plot(n, ruido)
# plt.grid()
# plt.xlabel("Tiempo [s]")
# plt.ylabel("Amplitud [V]")
# plt.title("Ruido normalmente distribuido")
# plt.show()

# # Calculamos la FFT :
     
# RR = np.fft.fft(ruido) # Son los 1000 coeficientes de la DFT de ese ruido.. Vector de nros complejos

# mod_RR = np.abs(RR) # Tamano de esa componente frecuencial

# freq = np.fft.fftfreq(N, d=1/fs) # Construimos un vector de frecuencias

# plt.figure()
# plt.plot(freq, mod_RR,'.')
# plt.title("Módulo de la Transformada de Fourier del ruido normal")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("|R[k]|")
# plt.grid()
# plt.show()
# %% 4) Una secuencia aleatoria de ruido uniformemente distribuido con DC (valor medio) 0 V y varianza 0.1 W

# N = 1000
# fs = 20000
# var = 0.1
# V = np.sqrt(3*var) # Amplitud
# ruido = np.random.uniform (-V,V,N)

# n = np.arange(N) / fs # Esto representa los instantes en los que tomaste cada muestra.

# plt.figure()
# plt.plot(n, ruido)
# plt.grid()
# plt.xlabel("Tiempo [s]")
# plt.ylabel("Amplitud [V]")
# plt.title("Ruido uniformemente distribuido")
# plt.show()

# # Calculamos la FFT :
     
# RR = np.fft.fft(ruido) # Son los 1000 coeficientes de la DFT de ese ruido.. Vector de nros complejos

# mod_RR = np.abs(RR) # Tamano de esa componente frecuencial

# freq = np.fft.fftfreq(N, d=1/fs) # Construimos un vector de frecuencias

# plt.figure()
# plt.plot(freq, mod_RR,'.')
# plt.title("Módulo de la Transformada de Fourier del ruido uniforme")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("|R[k]|")
# plt.grid()
# plt.show()
# # %% 5) Un pulso rectangular de la misma frecuencia, 1 W de potencia y ciclo de actividad del 50%

# N = 1000
# fs = 20000
# f0 = 2000

# n = np.arange(N) / fs
# xx = signal.square(2*np.pi*f0*n, duty = 0.5) # duty = 0.5 significa ciclo de actividad del 50%.

# plt.figure()
# plt.plot(n,xx)
# plt.title("Senal rectangular de 2 kHz")
# plt.xlabel("Tiempo [s]")
# plt.ylabel("Amplitud [V]")
# plt.grid()
# plt.show()

# # Calculamos la FFT :
    
# rec = np.fft.fft(xx)

# mod_rec = np.abs(rec)

# freq = np.fft.fftfreq(N, d=1/fs)

# plt.figure()
# plt.plot(freq, mod_rec,'.')
# plt.title("Módulo de la Transformada de Fourier de la senal rectangular")
# plt.xlabel("Frecuencia [Hz]")
# plt.ylabel("|R[k]|")
# plt.grid()
# plt.show()
# %% Bonus 1

# N = 1000

# pulso = signal.unit_impulse(N)
# pulso_desplazado = signal.unit_impulse(N,idx = 4)

# n = np.arange(N)

# plt.figure()
# plt.stem(n, pulso)
# plt.grid()
# plt.xlabel("n [muestras]")
# plt.ylabel("Amplitud")
# plt.title("Impulso unitario")
# plt.show()

# plt.figure()
# plt.stem(n, pulso_desplazado)
# plt.xlim(-1, 10)
# plt.grid()
# plt.xlabel("n [muestras]")
# plt.ylabel("Amplitud")
# plt.title("Impulso unitario desplazado")
# plt.show()

# %% Bonus 2

N = 1000
fs = 20000
k = 100
vmax = 2
dc = 0
ph = np.pi/2
f0 = k*(fs/N)

#Lenguaje en tiempo de discreto
def mi_funcion_sen():

    n = np.arange(N) / fs # tt: vector del tiempo.Todos los instantes en los que tomás una muestra de la señal.

    xx = dc + vmax * np.sin(2*np.pi*f0*n + ph)
    
    return (n,xx)

n,xx = mi_funcion_sen()

# Calculamos la FFT :

XX = np.fft.fft(xx)   # Representación de xx en el dominio de la frecuencia. La función fft toma esas 1000 muestras y calcula los coeficientes de la DFT

mod_XX = np.abs(XX) # El módulo es útil para visualizar un espectro: nos permite ver claramente dónde están las componentes importantes.

freq = np.fft.fftfreq(N, d=1/fs) # Construimos un vector de frecuencias

pot_fft = (1/N**2) * np.sum(mod_XX**2) #Teorema de Parserval

print (pot_fft)












