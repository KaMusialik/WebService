#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import protokoll as prot


class MyPlotts:
    def __init__(self, f_dict):
        file_protokoll=f_dict.get('protokoll_file_MyPlotts')
        self.oprot = prot.Protokoll(file_protokoll)   
    
    def PlotteAblaufleistung(self, data_dict):
        fig1, ax1 = plt.subplots()
        
        data=[]
        for nummer, wert in data_dict.items():
            data.insert(nummer, wert)
            
        ax1.set_title('Ablaufleistung')
        
        ax1.boxplot(data, vert=False, sym='', labels=['Pangaea Life'], patch_artist=True)
