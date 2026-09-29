# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:53:02 2026

@author: ferre
"""

import numpy as np
from scipy import signal as sig

import matplotlib.pyplot as plt
   
import scipy.io as sio
from scipy.io.wavfile import write

from scipy.signal import windows

#%%

##################
# Lectura de ECG #
##################

fs_ecg = 1000 # Hz

##################
## ECG con ruido
##################

# para listar las variables que hay en el archivo
#io.whosmat('ECG_TP4.mat')
# mat_struct = sio.loadmat('./ECG_TP4.mat')

# ecg_one_lead = mat_struct['ecg_lead']
# N = len(ecg_one_lead)

# hb_1 = mat_struct['heartbeat_pattern1']
# hb_2 = mat_struct['heartbeat_pattern2']

# plt.figure()
# plt.plot(ecg_one_lead[5000:12000])

# plt.figure()
# plt.plot(hb_1)

# plt.figure()
# plt.plot(hb_2)

##################
## ECG sin ruido
##################

ecg_one_lead = np.load('ecg_sin_ruido.npy')


plt.figure()
plt.plot(ecg_one_lead)

N = 30000
k = 20

l = N//k

ventana = windows.flattop (l)

f, welch = sig.welch(ecg_one_lead,fs = fs_ecg,window = ventana,nperseg = l, noverlap = l//2, nfft = N)

plt.figure()

plt.plot(f, 10*np.log10(welch))

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('PSD [dB/Hz]')
plt.title('PSD del ECG - Método de Welch')
plt.grid()
plt.xlim([0, 50])

# Toda la potencia que tenemos en el espectro
pot_total = np.sum(welch)

#Potencia acumulada
pot_acum = np.cumsum(welch)

# Normalizamos

pot_acum_norm = pot_acum / pot_total

plt.figure()

plt.plot(f, pot_acum_norm)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Potencia acumulada normalizada')
plt.title('Potencia acumulada del ECG')

plt.grid()
plt.xlim([0, 50])
plt.ylim([0, 1])

plt.figure()

energia = 0.99

indice_BW = np.argmax(pot_acum_norm >= energia)

f_BW = f[indice_BW]

print('Ancho de banda del ECG:', f_BW, 'Hz')



#%%

####################################
# Lectura de pletismografía (PPG)  #
####################################

fs_ppg = 400 # Hz

##################
## PPG con ruido
##################

# # Cargar el archivo CSV como un array de NumPy
# ppg = np.genfromtxt('PPG.csv', delimiter=',', skip_header=1)  # Omitir la cabecera si existe


##################
## PPG sin ruido
##################

ppg = np.load('ppg_sin_ruido.npy')

plt.figure()
plt.plot(ppg)

N_ppg = len(ppg)

print(N_ppg)

k = 20

l = N_ppg//k

ventana = windows.flattop(l)

f, welch_ppg = sig.welch(ppg, fs=fs_ppg, window=ventana, nperseg=l, noverlap=l//2, nfft=N)

plt.figure()

plt.plot(f, 10*np.log10(welch_ppg))

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('PSD [dB/Hz]')
plt.title('PSD del PPG - Método de Welch')
plt.grid()
plt.xlim([0, 50])

# Toda la potencia que tenemos en el espectro
pot_total = np.sum(welch_ppg)

#Potencia acumulada
pot_acum = np.cumsum(welch_ppg)

# Normalizamos

pot_acum_norm_ppg = pot_acum / pot_total

plt.figure()

plt.plot(f, pot_acum_norm_ppg)

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Potencia acumulada normalizada')
plt.title('Potencia acumulada del PPG')

plt.grid()
plt.xlim([0, 50])
plt.ylim([0, 1])

plt.figure()

energia_ppg = 0.99

indice_BW = np.argmax(pot_acum_norm_ppg >= energia_ppg)

f_BW = f[indice_BW]

print('Ancho de banda del PPG:', f_BW, 'Hz')


#%%

####################
# Lectura de audio #
####################

# Cargar el archivo CSV como un array de NumPy
#fs_audio, wav_data = sio.wavfile.read('la cucaracha.wav')
fs_audio, wav_data = sio.wavfile.read('prueba psd.wav')
# fs_audio, wav_data = sio.wavfile.read('silbido.wav')

plt.figure()
plt.plot(wav_data)

# si quieren oirlo, tienen que tener el siguiente módulo instalado
# pip install sounddevice
# import sounddevice as sd
# sd.play(wav_data, fs_audio)

N = len(wav_data)

print('N =', N)
print('fs =', fs_audio)

k = 20

l = N//k

ventana = windows.flattop(l)

f, welch_audio = sig.welch(wav_data, fs=fs_audio, window=ventana, nperseg=l, noverlap=l//2, nfft=N)


plt.figure()

plt.plot(f, 10*np.log10(welch_audio))

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('PSD [dB/Hz]')
plt.title('PSD del audio - Método de Welch')

plt.grid()
plt.xlim([0, 10000])

pot_total_audio = np.sum(welch_audio)

pot_acum_audio = np.cumsum(welch_audio)

pot_acum_norm_audio = pot_acum_audio / pot_total_audio

# indice_inf = np.argmax(pot_acum_norm_audio >= 0.005)

# f_inf = f[indice_inf]

# indice_sup = np.argmax(pot_acum_norm_audio >= 0.995)

# f_sup = f[indice_sup]

# BW_audio = f_sup - f_inf

# print('Frecuencia inferior:', f_inf, 'Hz')
# print('Frecuencia superior:', f_sup, 'Hz')
# print('Ancho de banda del audio:', BW_audio, 'Hz')

energia = 0.99

indice_BW_audio = np.argmax(pot_acum_norm_audio >= energia)

f_BW_audio = f[indice_BW_audio]

print('Ancho de banda del audio:', f_BW_audio, 'Hz')

#%%

fs_audio, wav_data = sio.wavfile.read('silbido.wav')

N = len(wav_data)

print('N =', N)
print('fs =', fs_audio)

k = 20

l = N//k

ventana = windows.flattop(l)

f, welch_audio = sig.welch(wav_data, fs=fs_audio, window=ventana, nperseg=l, noverlap=l//2, nfft=N)


plt.figure()

plt.plot(f, 10*np.log10(welch_audio))

plt.xlabel('Frecuencia [Hz]')
plt.ylabel('PSD [dB/Hz]')
plt.title('PSD del audio - Método de Welch')

plt.grid()
plt.xlim([0, 10000])

pot_total_audio = np.sum(welch_audio)

pot_acum_audio = np.cumsum(welch_audio)

pot_acum_norm_audio = pot_acum_audio / pot_total_audio

indice_inf = np.argmax(pot_acum_norm_audio >= 0.005)
indice_sup = np.argmax(pot_acum_norm_audio >= 0.995)

f_inf = f[indice_inf]
f_sup = f[indice_sup]

BW_audio = f_sup - f_inf

print('Frecuencia inferior:', f_inf, 'Hz')
print('Frecuencia superior:', f_sup, 'Hz')
print('Ancho de banda del audio:', BW_audio, 'Hz')

