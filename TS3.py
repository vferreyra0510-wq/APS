# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:45:16 2026

@author: ferre
"""

import numpy as np
import matplotlib.pyplot as plt

#sen (k(detla)fn) ----> 1 Hz = fs/2

N = 1000
fs = 1000
k = N/4 
vmax = np.sqrt(2) 
dc = 0
ph = 0
ff = k*(fs/N)

#%% FUNCION

#Lenguaje en tiempo de discreto
def mi_funcion_sen(k):

    n = np.arange(N) / fs # tt: vector del tiempo.Todos los instantes en los que tomás una muestra de la señal.

    xx = dc + vmax * np.sin(2*np.pi*k*(fs/N)*n + ph)
    
    return (n,xx)

#%% INCISO A

n,xx = mi_funcion_sen(k)

eje_frec = np.arange(0, N//2) * fs/N #Nos prepara la FFT

yf = 1/N * np.fft.fft(xx)

XX_mod = np.abs(yf)

espectro = (XX_mod)**2
dens_espc = 10*np.log10(2*(espectro[:N//2])) # Densidad de potencia espectral

plt.plot(eje_frec, dens_espc,':x')
plt.title("Espectro de la señal")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("db")
plt.show()

#%% Potencia 

pot_tiempo = np.suma(xx**2) / N

pot_frec = np.suma(np.abs(yf)**2)

print(pot_tiempo)
print(pot_frec)

#%% METODO ZERO PADDING A 

n, xx = mi_funcion_sen(k)

N_padding = 10*N

xx_padding = np.concatenate((xx, np.zeros(9*N)))

eje_frec1 = np.arange(0, N_padding//2, ) * fs/N_padding

yf = 1/N * np.fft.fft(xx_padding)

XX_mod = np.abs(yf)

espectro = XX_mod**2

dens_espc = 10*np.log10(2*espectro[:N_padding//2])

plt.figure()
plt.plot(eje_frec1, dens_espc,':x')
plt.title("Espectro con Zero Padding")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("dB")
plt.ylim(-80, 0)
plt.grid()
plt.show()

#%% INCISO B

n,xx2 = mi_funcion_sen(k+0.25)

eje_frec = np.arange(0, N//2, fs/N) * fs/N #Nos prepara la FFT

yf = 1/N * np.fft.fft(xx2)

XX_mod = np.abs(yf)

espectro = (XX_mod)**2
dens_espc =  10*np.log10(2*(espectro[:N//2])) # Densidad de potencia espectral

plt.figure()
plt.plot(eje_frec, dens_espc,':x')
plt.title("Espectro de la señal")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("dB")
plt.ylim(-80, 0)
plt.grid()
plt.show()

#%% METODO ZERO PADDING B

n, xx2 = mi_funcion_sen(k + 0.25)

N_padding = 10*N

xx_padding = np.concatenate((xx2, np.zeros(9*N)))

eje_frec1 = np.arange(0, N_padding//2, ) * fs/N_padding

yf = 1/N * np.fft.fft(xx_padding)

XX_mod = np.abs(yf)

espectro = XX_mod**2

dens_espc = 10*np.log10(2*espectro[:N_padding//2])

plt.figure()
plt.plot(eje_frec1, dens_espc,':x')
plt.title("Espectro con Zero Padding")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("dB")
plt.ylim(-80, 0)
plt.grid()
plt.show()

#%% INCISO C

n,xx3 = mi_funcion_sen(k+0.5)

eje_frec = np.arange(0, N//2, fs/N) * fs/N #Nos prepara la FFT

yf = 1/N * np.fft.fft(xx3)

XX_mod = np.abs(yf)

espectro = (XX_mod)**2
dens_espc =  10*np.log10(2*(espectro[:N//2])) # Densidad de potencia espectral

plt.figure()
plt.plot(eje_frec, dens_espc,':x')
plt.title("Espectro de la señal")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("dB")
plt.ylim(-80, 0)
plt.grid()
plt.show()
#%% METODO ZERO PADDING C

n, xx3 = mi_funcion_sen(k + 0.5)

N_padding = 10*N

xx_padding = np.concatenate((xx3, np.zeros(9*N)))

eje_frec1 = np.arange(0, N_padding//2, ) * fs/N_padding

yf = 1/N * np.fft.fft(xx_padding)

XX_mod = np.abs(yf)

espectro = XX_mod**2

dens_espc = 10*np.log10(2*espectro[:N_padding//2])

plt.figure()
plt.plot(eje_frec1, dens_espc,':x')
plt.title("Espectro con Zero Padding")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("dB")
plt.ylim(-80, 0)
plt.grid()
plt.show()




