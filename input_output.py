#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import protokoll as prot


class InputOutput(object):

    def __init__(self, f_dict):
        file_protokoll=f_dict.get('protokoll_file_InputOutput')
        self.oprot = prot.Protokoll(file_protokoll)
        
    def LeseInput(self):
        
        dict1 = {
        "aufrufnummer": 2,
        "test": True,
        "gesellschaftskennzeichen": "Pangaea Life",
        "tarif": "HR_SonderN",
        "zahlbeitrag": 100,
        "zahlweise": 12,
        "beitragszahlungsdauer": 47,
        "versicherungsdauer": 47,
        "versicherungsbeginn": "2022-05-01",
        "geburtsdatum": "2002-04-01",
        "fonds1": "IVFP80GARANT",
        "fonds2": "LU1675428244",
        "anteil_Fonds1": 1,
        "garantieniveau": 0.8,
        "mindesttodesfallleistung": 4,
        "prozentBtgSumme": 0,
        }
        
        print('------------- Anfang:')
        print('Response Input:')
        print(dict1)
        print('------------- Ende')
        
        return dict1
        
    def LeseOutput(self, respose_str):
        
        dict1 = {}
        dict1 = json.loads(respose_str)
    
        print('------------- Anfang:')
        print('Response Output:')
        print(dict1)
        print('------------- Ende')


        return dict1
    
    def LeseNameUndWert(self, name):
        ausgang={}
        str_name = str(name)
        laenge = len(str_name)
        position = str_name.find('_')
        if position == -1:
            position = laenge
            
        text_vor_position = str_name[0:position]
        text_nach_position = str_name[position+1:]
        ausgang['name_text1'] = text_vor_position
        ausgang['name_text2'] = text_nach_position
        return ausgang
        
    def LeseAblaufleistung(self, outputDaten):
        dict_alles = {}
        dict_ablaufleistung = {}
        dict_name_wert = {}
        
        dict_alles = outputDaten
        
        if dict_alles.get('ablaufleistungen') == None:
            
            # Das Feld aböaufleistungen ist nicht gefüllt
            for name, wert in dict_alles.items():
                if name == 'minimum':
                    dict_ablaufleistung[0] = wert
                    pass
                elif name == 'maximum':
                    dict_ablaufleistung[1000] = wert
                    pass
                else:
                    dict_name_wert=self.LeseNameUndWert(name)
                    if dict_name_wert['name_text1']=='ablauf':
                        nummer = int(dict_name_wert.get('name_text2'))
                        dict_ablaufleistung[nummer] = wert
                    
        else:
            ablaufleistungen = []
            ablaufleistungen = dict_alles.get('ablaufleistungen')
            
            nummer = 0
            for wert in ablaufleistungen:
                dict_ablaufleistung[nummer] = wert
                nummer += 1
        
        print('------------- Anfang:')
        print('Ablaufleistung:')
        print(dict_ablaufleistung)
        print('------------- Ende')
        
        return dict_ablaufleistung