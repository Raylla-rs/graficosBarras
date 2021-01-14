# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:21:32 2020

@author: rayll
"""


import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('CENIPA-integrado.csv')

plt.style.use('bmh')

def contagem (data,name):					#funcao de preparacao dos dados - executar antes de chamar as funcoes de graficos
    #a variavel name eh o parametro (escolha uma das colunas do dataset) escolhido para a analise das ocorrencias
    ac=data.query('ocorrencia_classificacao=="ACIDENTE"')	#selecionando a classe acidente (ac)
    acData=pd.DataFrame()
    acData=ac[name]						
    acDataCount=acData.value_counts()				#contagem de acidentes registrados associados ao parametro name
    inc=data.query('ocorrencia_classificacao=="INCIDENTE"')	#selecionando a classe incidente (inc)
    incData=pd.DataFrame()
    incData=inc[name]
    incDataCount=incData.value_counts()				#contagem de incidentes registrados associados ao parametro name
    incG=data.query('ocorrencia_classificacao=="INCIDENTE GRAVE"')	#selecionando a classe incidente grave (incG)
    incGData=pd.DataFrame() 
    incGData=incG[name]
    incGDataCount=incGData.value_counts()			#contagem de incidentes graves registrados associados ao parametro name
    return (acDataCount,incDataCount,incGDataCount)


def graficoH(acDataCount,incDataCount,incGDataCount,name):	#funcao para grafico de barras horizontal
    plt.figure(figsize=(7,6))
    plt.axes().set(xlabel='Frequência')
    plt.title(name,fontsize=14)
    plt.barh(acDataCount.index,acDataCount,color=(0.8,0.3,0.3,0.5),label='Acidente',height=0.3,align='edge')
    plt.barh(incDataCount.index,incDataCount,color=(0.3,0.3,0.8,0.5),label='Incidente',height=0.3)
    plt.barh(incGDataCount.index,incGDataCount,color=(0.8,0.8,0.3,0.5),label='Incidente Grave',height=-0.3,align='edge')
    plt.legend()

def graficoV(acDataCount,incDataCount,incGDataCount,name):	#funcao para grafico de barras vertical
    plt.figure(figsize=(7,6))
    ax=plt.axes()
    ax.set(ylabel='Frequência')
    plt.title(name,fontsize=14)
    plt.bar(acDataCount.index,acDataCount,color=(0.8,0.3,0.3,0.5),label='Acidente',align='edge',width=0.3)
    plt.bar(incDataCount.index,incDataCount,color=(0.3,0.3,0.8,0.5),label='Incidente',width=0.3)
    plt.bar(incGDataCount.index,incGDataCount,color=(0.8,0.8,0.3,0.5),label='Incidente Grave',align='edge',width=-0.3)
    plt.legend()

def graficoP(acDataCount,incDataCount,incGDataCount,name):	#funcao para grafico de porcentagem em barras verticais
    total=pd.concat([acDataCount,incDataCount,incGDataCount],axis=1,ignore_index=True)
    for c in total.columns:
        r=0
        while r<len(total.index):
            x=[total[c].iloc[r]]
            x=pd.DataFrame(x)
            y=x.isnull()
            if y[0].iloc[0]==True:
                total[c].iloc[r]=0
            r+=1
    total['soma']=total.sum(axis=1)
    total['acidenteP']=(total[0]/total.soma)*100
    total['incidenteP']=(total[1]/total.soma)*100
    total['incidenteGP']=(total[2]/total.soma)*100
    plt.figure(figsize=(7,6))
    ax=plt.axes()
    ax.set_ylim(0,100)
    ax.set(ylabel='Porcentagem (%)')
    plt.title(name,fontsize=14)
    plt.bar(total.index,total['incidenteP'],color=(0.3,0.3,0.8,0.5),label='Incidente',width=0.3)
    plt.bar(total.index,total['incidenteGP'],color=(0.8,0.8,0.3,0.5),label='Incidente Grave',width=0.3,bottom=total['incidenteP'])
    plt.bar(total.index,total['acidenteP'],color=(0.8,0.3,0.3,0.5),label='Acidente',width=0.3,bottom=total['incidenteGP']+total['incidenteP'])
    plt.legend(loc=4)


acDataCount,incDataCount,incGDataCount=contagem(data,name) #substituir name pelo nome da coluna a ser analisada
graficoH(acDataCount,incDataCount,incGDataCount,name)

    
    
