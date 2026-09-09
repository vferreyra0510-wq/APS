# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:49:35 2026

@author: ferre
"""
import numpy as np
import matplotlib.pyplot as plt
#%%

N = 1000
fs = 1000
vmax = np.sqrt(2) 
dc = 0
ph = 0
ff = (fs/N)

# Paso de cuantizacion
B = 4
Vfs = 2
qq = (2*Vfs) / (2**B)
kn = 1 #cuánto ruido queremos tener comparado con el ruido de cuantización.
Pq = (qq)**2/12 #potencia teórica del ruido de cuantización.
Pn = kn*Pq #potencia del ruido gaussiano que agregamos a la senoide.

#%% 
#Lenguaje en tiempo de discreto
def mi_funcion_sen():

    n = np.arange(N) / fs # tt: vector del tiempo.Todos los instantes en los que tomás una muestra de la señal.

    xx = dc + vmax * np.sin(2*np.pi*ff*n + ph)
    
    return (n,xx)

n,xx = mi_funcion_sen()

# Declaro el ruido
ruido = np.random.normal (0,np.sqrt(Pn),N)

# Senoide + Ruido
xx_ruido = xx + ruido

#%% Cuantizacion, salida del ADC

xx_q = np.round(xx_ruido / qq) * qq # Lleva cada muestra al nivel de cuantización más cercano.

# Ruido de cuantizacion
nq = xx_q - xx_ruido #cuánto cambió cada muestra debido exclusivamente a la cuantización.

#%% FFT Senoide

frec = np.arange(N//2) * fs/N

xx_fft = 1/N * np.fft.fft(xx)

XX_mod = np.abs(xx_fft)

espectro = (XX_mod)**2
dens_espc = 10*np.log10(2*(espectro[:N//2]))

#%% FFT Senoide + ruido

xx_ruido_fft = 1/N * np.fft.fft(xx_ruido)

XX_ruido_mod = np.abs(xx_ruido_fft)

espectro_ruido = (XX_ruido_mod)**2
dens_espc_ruido = 10*np.log10(2*(espectro_ruido[:N//2]))

#%% FFT de cuantizacion

xx_q_fft = 1/N * np.fft.fft(xx_q)

XX_q_mod = np.abs(xx_q_fft)

espectro_q = (XX_q_mod)**2
dens_espc_q = 10*np.log10(2*(espectro_q[:N//2]))

#%% GRAFICO 

plt.figure()

plt.plot(frec, dens_espc, label='Senoide')
plt.plot(frec, dens_espc_ruido, label='Senoide + ruido')
plt.plot(frec, dens_espc_q, label='Señal cuantizada')

plt.xlabel('Frecuencia [Hz]')
plt.xlim(0, 10)
plt.ylabel('Densidad de potencia [dB]')
plt.ylim(-80, 0)
plt.title('Espectro de las señales')

plt.grid()
plt.legend()

plt.show()

#%% Grafico en el tiempo

plt.figure()

plt.plot(n, xx_q, label='ADC out')
plt.plot(n, xx_ruido, ':', label='ADC in')
plt.plot(n, xx, ':', label='s (analog)')

plt.xlabel('Tiempo [segundos]')
plt.ylabel('Amplitud [V]')
plt.title('Señal muestreada por un ADC')

plt.grid()
plt.legend()
plt.show()

#%% Histograma del ruido de cuantizacion

plt.figure()

plt.hist(nq, bins=10)

plt.xlabel('Error de cuantizacion [V]')
plt.ylabel('Cantidad de muestras')
plt.title('Ruido de cuantizacion')

plt.grid()
plt.show()

#%% Cuantizacion, salida del ADC

# La conclusión conceptual va a ser que al aumentar la cantidad de bits disminuye q, disminuye la potencia del ruido de cuantización y mejora la resolución del ADC.

B = 16
qq1 = (2*Vfs) / (2**B)
xx_q1 = np.round(xx_ruido / qq1) * qq1 # Lleva cada muestra al nivel de cuantización más cercano.

# Ruido de cuantizacion
nq = xx_q - xx_ruido #cuánto cambió cada muestra debido exclusivamente a la cuantización.

xx_q1_fft = 1/N * np.fft.fft(xx_q1)

XX_q1_mod = np.abs(xx_q1_fft)

espectro_q1 = (XX_q1_mod)**2
dens_espc_q1 = 10*np.log10(2*(espectro_q1[:N//2]))

plt.figure()

plt.plot(frec, dens_espc, label='Senoide')
plt.plot(frec, dens_espc_ruido, label='Senoide + ruido')
plt.plot(frec, dens_espc_q1, label='Señal cuantizada')

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Densidad de potencia [dB]')
#plt.ylim(-80, 0)
plt.title('Espectro de las señales')

plt.grid()
plt.legend()

plt.show()

plt.figure()

plt.plot(n, xx_q1, label='ADC out')
plt.plot(n, xx_ruido, ':', label='ADC in')
plt.plot(n, xx, ':', label='s (analog)')

plt.xlabel('Tiempo [segundos]')
plt.ylabel('Amplitud [V]')
plt.title('Señal muestreada por un ADC')

plt.grid()
plt.legend()
plt.show()













