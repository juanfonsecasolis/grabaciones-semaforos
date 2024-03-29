#!/usr/bin/env python
# Juan M. Fonseca-Solis
# USAGE: python remuestrear.py <base directory> <new sampling rate>
#

import fnmatch
import os
import sys
import scipy.signal
import scipy.io.wavfile
import numpy as np
import matplotlib.pylab as plt

def obtenerRutaWavs(dirBase):
	matches = []
	for root, dirnames, filenames in os.walk(dirBase):
	    for filename in fnmatch.filter(filenames, '*wav'):
		if '.' != filename[0]:
			matches.append(os.path.join(root, filename))
	return matches

def decimarRecuantizar16bits(x, fs, fsP):
	q = fs/fsP
	print 'Factor decimación: %f' % q

	# Es necesario pasar un LPF antes de hacer un downsampling para 
	# evitar aliasing: https://en.wikipedia.org/wiki/Decimation_%28signal_processing%29 
	# (esto se llama decimar)
	y = scipy.signal.decimate(x, q)
	y = y/max(y)
	
	# convertir a 16 bits
	convert_16_bit = float(2**15)
	print 'Nueva cuantizacion: %s' % type(y)
	y = np.int16(y * convert_16_bit)	

	return y

'''
MAIN
'''
dirBase = sys.argv[1]
fsP = int(sys.argv[2])

# procesamos cada archivo por aparte
rutas = obtenerRutaWavs(dirBase)
for ruta in rutas:
	print ruta
	fs, x = scipy.io.wavfile.read(ruta)
	y = decimarRecuantizar16bits(x, fs, fsP)
	nuevaRuta = ruta + 'Rem.wav'
	scipy.io.wavfile.write(nuevaRuta, fsP, y)
	print 'Procesado: %s' % nuevaRuta
	





