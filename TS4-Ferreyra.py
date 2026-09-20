# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:45:20 2026

@author: ferre
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import windows
#%%

a0 = np.sqrt(2) 
N = 1000
fs = 1000

# 200 realizaciones de fr
f_r = np.random.uniform(-2,2,200)

omega0 = np.pi/2

#Definir el ruido
SNR = 10 #dB 
Ps = 1

Pr = Ps / (10**(SNR/10))

sigma = np.sqrt(Pr) 

# Ruido para las 1000 muestras de las 200 realizaciones

n_a = np.random.normal(0,sigma,(N,200))

#%% 

def mi_funcion_sen():
    
    omega1 = omega0 + f_r*(2*np.pi/N)
    
    omega1 = omega1.reshape(1,200)

    # 1000 muestras
    n = np.arange(N).reshape(N,1)
    
    # Matriz de 1000 x 200
    xx = a0 * np.sin(omega1*n) + n_a
    
    return (n,xx)

n,xx = mi_funcion_sen()


#%% FFT

frecuencia = np.arange(N//2) * fs/N

xx_fft = 1/N * np.fft.fft(xx,axis=0) # Hace una FFT para cada una de las 200 realizaciones

XX_mod = np.abs(xx_fft)

## XX_mod = XX_mod[:N//2, :] # Te deja solo la primera parte positiva para que coincida con omega

espectro = (XX_mod)**2
dens_espc = 10*np.log10(2*(espectro[:N//2]))

#%%

plt.figure()
plt.plot(frecuencia, XX_mod[:N//2, 0])
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.grid()
plt.show()

#%%

# Graficar por ejemplo, la primera de las 200 realizaciones:   [:,0]

plt.figure()
plt.plot(frecuencia, dens_espc)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Potencia [dB]")
plt.grid()
plt.show()

#%%

# Estimador de amplitud
a1 = 2*XX_mod [N//4,:]

# Estimador de frecuencia
maxi = np.argmax(XX_mod[:N//2, :], axis = 0) 

frec_est = maxi * fs/N

plt.figure()

plt.hist(frec_est)

plt.xlabel('Frecuencia')
plt.ylabel('Cantidad de realizaciones')

plt.figure()

plt.hist(a1)

plt.xlabel('Amplitud')
plt.ylabel('Cantidad de realizaciones')

#%% Sesgo y varianza de la amplitud

a1_esperanza = np.mean(a1)

sesgo = a1_esperanza - a0

varianza = np.mean((a1 - a1_esperanza)**2)

print("Esperanza amplitud:", a1_esperanza)
print("Sesgo amplitud:", sesgo)
print("Varianza amplitud:", varianza)

f1 = 250 + f_r

frec_esperanza = np.mean(frec_est)

sesgo_frecuencia = np.mean (frec_est - f1)

varianza_frecuencia = np.mean((frec_est - frec_esperanza)**2)

print("Esperanza frecuencia:", frec_esperanza)
print("Sesgo frecuencia:", sesgo_frecuencia)
print("Varianza frecuencia:", varianza_frecuencia)

#%% Ventana Flattop

ventana = windows.flattop(N)

ventana = ventana.reshape(N,1)

xx_flat = xx * ventana

# FFT

xx_fft_flat = 1/N * np.fft.fft(xx_flat, axis=0)

XX_mod_flat = np.abs(xx_fft_flat)

# Estimador de amplitud

a1_flat = 2*XX_mod_flat [N//4,:]

# Estimador de frecuencia
maxi_flat = np.argmax(XX_mod_flat[:N//2, :], axis = 0) 

frec_est_flat = maxi_flat * fs/N

plt.figure()

plt.hist(a1_flat)

plt.xlabel('Amplitud')
plt.ylabel('Cantidad de realizaciones')


plt.figure()

plt.plot(ventana)

plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

a1_flat_esperanza = np.mean(a1_flat)

sesgo_flat = a1_flat_esperanza - a0

varianza_flat = np.mean((a1_flat - a1_flat_esperanza)**2)

print("Esperanza amplitud:", a1_flat_esperanza)
print("Sesgo amplitud:", sesgo_flat)
print("Varianza amplitud:", varianza_flat)
#%% Ventana blackmanharris

ventana_blackmanharris = windows.blackmanharris(N)

ventana_blackmanharris = ventana_blackmanharris.reshape(N,1)

xx_blackmanharris = xx * ventana_blackmanharris

# FFT

xx_fft_blackmanharris = 1/N * np.fft.fft(xx_blackmanharris, axis=0)

XX_mod_blackmanharris = np.abs(xx_fft_blackmanharris)

# Estimador de amplitud

a1_blackmanharris = 2*XX_mod_blackmanharris [N//4,:]

# Estimador de frecuencia
maxi_blackmanharris = np.argmax(XX_mod_blackmanharris[:N//2, :], axis = 0) 

frec_est_blackmanharris = maxi_blackmanharris * fs/N

plt.figure()

plt.hist(a1_blackmanharris)

plt.xlabel('Amplitud')
plt.ylabel('Cantidad de realizaciones')

plt.figure()

plt.plot(ventana_blackmanharris)

plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()
plt.show()
#%% Ventana hann

ventana_hann = windows.hann(N)

ventana_hann = ventana_hann.reshape(N,1)

xx_hann = xx * ventana_hann

# FFT

xx_fft_hann = 1/N * np.fft.fft(xx_hann, axis=0)

XX_mod_hann = np.abs(xx_fft_hann)

# Estimador de amplitud

a1_hann = 2*XX_mod_hann [N//4,:]

# Estimador de frecuencia
maxi_hann = np.argmax(XX_mod_hann[:N//2, :], axis = 0) 

frec_est_hann = maxi_hann * fs/N

plt.figure()

plt.hist(a1_hann)

plt.xlabel('Amplitud')
plt.ylabel('Cantidad de realizaciones')

plt.figure()

plt.plot(ventana_hann)

plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

#%% Histograma de amplitud juntos

plt.figure()

plt.hist(a1, alpha=0.5, label='Rectangular')
plt.hist(a1_flat, alpha=0.5, label='Flattop')
plt.hist(a1_blackmanharris, alpha=0.5, label='Blackman-Harris')
plt.hist(a1_hann, alpha=0.5, label='Hann')

plt.xlabel('Amplitud')
plt.ylabel('Cantidad de realizaciones')

plt.legend()
plt.grid()
plt.show()

#%% Histograma de frecuencias juntos
plt.figure()

plt.hist(frec_est, histtype='step', label='Rectangular')
plt.hist(frec_est_flat, histtype='step', label='Flattop')
plt.hist(frec_est_blackmanharris, histtype='step', label='Blackman-Harris')
plt.hist(frec_est_hann, histtype='step', label='Hann')

plt.xlabel('Frecuencia')
plt.ylabel('Cantidad de realizaciones')

plt.legend()
plt.grid()
plt.show()





