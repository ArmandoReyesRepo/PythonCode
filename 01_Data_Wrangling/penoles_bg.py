# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:09:19 2019

@author: arman
"""


import pandas as pd
import os
os.getcwd()

os.chdir('C:\\Users\\arman\\Desktop\\Proyectos Manuel Sarmiento\\02 Algoritmos\\Python')


#  Levantamiento de información peñoles hasta el 31 de dic del 18 bg
penoles = pd.read_csv('penoles_sarm_todper_bg.csv')

penoles
penoles.info()

penoles_pivot = penoles.pivot(index='concepto..6', columns ='fechafin', values = 'valor')

penoles_pivot

penoles_pivot.to_csv('penoles_adj_bg.csv')


#  Levantamiento de información peñoles hasta el 29 de abr del 19 bg  ( no funcionó falto ajuste fechas)
penoles19 = pd.read_csv('penoles_sarm_todper_bg_19.csv')

penoles19
penoles19.info()

penoles_pivot19 = penoles19.pivot(index='concepto..6', columns ='fechafin', values = 'valor')

penoles_pivot19

penoles_pivot19.to_csv('penoles_adj_bg19.csv')


#  Levantamiento de información de peñoles todo  para Estado de Resultados


penoles_t_1 = pd.read_csv('penoles_sarm_todper_er_2.csv')
penoles_t_1
penoles_t_1.info()
penoles_pivot_t_19_1 = penoles_t_1.pivot(index='concepto..6', columns ='Para Pivote', values = 'valor')
penoles_pivot_t_19_1
penoles_pivot_t_19_1.to_csv('penoles_adj_er19.csv')



#  Levantamiento de información rcentro hasta el 31 de dic del 18 bg
rcentro = pd.read_csv('rcentro_sarm_todper_bg.csv')

rcentro
rcentro.info()

rcentro_pivot = rcentro.pivot(index='concepto..6', columns ='fechafin', values = 'valor')

rcentro_pivot

rcentro_pivot.to_csv('rcentro_adj_bg.csv')

#  Levantamiento de información de rcentro todo  para Estado de Resultados


rcentro_t_1 = pd.read_csv('rcentro_sarm_todper_er_2.csv')
rcentro_t_1
rcentro_t_1.info()
rcentro_pivot_t_19_1 = rcentro_t_1.pivot(index='concepto..6', columns ='Para Pivote', values = 'valor')
rcentro_pivot_t_19_1
rcentro_pivot_t_19_1.to_csv('rcentro_adj_er19.csv')


#  Levantamiento de información para peñoles BG y ER ( sólo cuentas relevantes, cortes trimestrales 8 05 19)

penoles = pd.read_csv('penoles_todo_ctas_relv_80519.csv')
penoles
penoles.info()
penoles_pivot_80519 = penoles.pivot(index = 'concepto..6', columns ='Para Pivote', values = 'valor')
penoles_pivot_80519
penoles_pivot_80519.to_csv('penoles_adj_todo_ctas_relv_80519.csv ')





