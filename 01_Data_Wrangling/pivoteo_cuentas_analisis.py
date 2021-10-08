# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:09:19 2019

@author: arman
"""


import pandas as pd
import os
os.getcwd()

os.chdir('C:\\Users\\arman\\Desktop\\Proyectos Manuel Sarmiento\\02 Algoritmos\\Python\\19_05_19')


##   Automatizar pivteo y generación de columna de pivoteo

#  Levantamiento ACOSTCB - 2284 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

acosta = pd.read_csv('ACOSTCB - 2284.csv')
acosta
acosta.info()
acosta_pivot_190519 = acosta.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
acosta_pivot_190519
acosta_pivot_190519.to_csv('ACOSTCB - 2284_adj_190519.csv ')


#  Levantamiento AERMXCB - 1748 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

aermx = pd.read_csv('AERMXCB - 1748.csv')
aermx
aermx.info()
aermx_pivot_190519 = aermx.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
aermx_pivot_190519
aermx_pivot_190519.to_csv('AERMXCB - 1748_adj_190519.csv ')


#  Levantamiento AMICK - 3211 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

amick = pd.read_csv('AMICK - 3211.csv')
amick
amick.info()
amick_pivot_190519 = amick.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
amick_pivot_190519
amick_pivot_190519.to_csv('AMICK - 1748_adj_190519.csv ')


#  Levantamiento BANTECB - 2936 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

bantecb = pd.read_csv('BANTECB - 2936.csv')
bantecb
bantecb.info()
bantecb_pivot_190519 = bantecb.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
bantecb_pivot_190519
bantecb_pivot_190519.to_csv('BANTECB - 2936_adj_190519.csv ')

#  Levantamiento BNMXCB - 80683 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

bnmxcb = pd.read_csv('BNMXCB - 80683.csv')
bnmxcb
bnmxcb.info()
bnmxcb_pivot_190519 = bnmxcb.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
bnmxcb_pivot_190519
bnmxcb_pivot_190519.to_csv('BNMXCB - 80683_adj_190519.csv ')

#  Levantamiento BXMXPI - 3046 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

bxmxpi = pd.read_csv('BXMXPI - 3046.csv')
bxmxpi
bxmxpi.info()
bxmxpi_pivot_190519 = bxmxpi.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
bxmxpi_pivot_190519
bxmxpi_pivot_190519.to_csv('BXMXPI - 3046_adj_190519.csv ')


#  Levantamiento CASCB - 2031 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

cascb = pd.read_csv('CASCB - 2031.csv')
cascb
cascb.info()
cascb_pivot_190519 = cascb.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
cascb_pivot_190519
cascb_pivot_190519.to_csv('CASCB - 2031_adj_190519.csv ')

#  Levantamiento CETETRC - 164265 de información BG y ER ( cuentas relevantes, cortes trimestrales 19_05_19)

cetetrc = pd.read_csv('CETETRC - 164265.csv')
cetetrc
cetetrc.info()
cetetrc_pivot_190519 = cetetrc.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
cetetrc_pivot_190519
cetetrc_pivot_190519.to_csv('CETETRC - 164265_adj_190519.csv ')

#  Levantamiento AEROMEX de información BG y ER ( cuentas relevantes, cortes trimestrales 20_05_19)

aermex = pd.read_csv('AEROMEX.csv')
aermex
aermex.info()
aermex_pivot_190519 = aermex.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
aermex_pivot_190519
aermex_pivot_190519.to_csv('AEROMEX_adj_190519.csv ')

##  Levantamiento 22 de Mayo 2019

os.chdir('C:\\Users\\arman\\Desktop\\Proyectos Manuel Sarmiento\\02 Algoritmos\\Python\\22_05_19')

##  Levantamiento ACOSTCB - 2284 de información BG y ER ( cuentas relevantes, cortes trimestrales 22_05_19)



acostcb = pd.read_csv('ACOSTCB - 2284.csv')
acostcb
acostcb.info()
acostcb_pivot_220519 = acostcb.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
acostcb_pivot_220519
acostcb_pivot_220519.to_csv('ACOSTCB - 2284_adj_220519.csv ')


##  Levantamiento AEROMEX de información BG y ER ( cuentas relevantes, cortes trimestrales 22_05_19)

aeromex = pd.read_csv('AEROMEX.csv')
aeromex
aeromex.info()
aeromex_pivot_220519 = aeromex.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
aeromex_pivot_220519
aeromex_pivot_220519.to_csv('AEROMEX_adj_220519.csv ')

##  Levantamiento PE&OLES de información BG y ER ( cuentas relevantes, cortes trimestrales 22_05_19)

penoles = pd.read_csv('PE&OLES.csv')
penoles
penoles.info()
penoles_pivot_220519 = penoles.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
penoles_pivot_220519
penoles_pivot_220519.to_csv('PE&OLES_adj_220519.csv ')


##  Levantamiento PE&OLES de información BG y ER ( cuentas relevantes, cortes trimestrales 22_05_19)

rcentro = pd.read_csv('RCENTRO.csv')
rcentro
rcentro.info()
rcentro_pivot_220519 = rcentro.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
rcentro_pivot_220519
rcentro_pivot_220519.to_csv('RCENTRO_adj_220519.csv ')

