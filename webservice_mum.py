# -*- coding: utf-8 -*-

import requests
import protokoll as prot
import json

class WebService:
    
    def __init__(self, f_dict):
        file_protokoll=f_dict.get('protokoll_file_AufrufWS_MUM')
        self.oprot = prot.Protokoll(file_protokoll)

        # setzt den Benutzername und das Passwort
        self.username = "string"
        self.password = "string"

        # setzt die url, den header und die Post JSON
        self.url = 'https://stage-t.api.mumsolution.de/volatium'
        self.header = {'Content-type': 'application/json'}

        #hier werden die Daten für den Vertrag abgelegt, der aufgerufen werden soll        
        self.vertrag_dict = {}
        
        self.SetzteVertrag(f_dict.get('vertrag_dict'))

    def SetzteVertrag(self,vtg_dict):
        
        # spezifische für IVFP Angaben:
        self.vertrag_dict = {
            "nichtraucherstatus": "Nichtraucher",
            "hoehstmoeglichebeitragsgarantie": True,
            "beitragsgarantie": 0.8,
            "todesfallleistungAufschubzeit": "Guthaben",
            "prozentBtgSumme": 0,
            "fonds": "string",
            "wertsicherungsfonds": "string",
            "tarifId": 0,
            "strategieId": 0,
            "ueberschusssystem": "KeineAngabe",
            "hoechstmoeglicheBeitragsgarantie": True,
            "mindesttodesfallschutzWert": 0,
            "rentengarantiezeit": 0,
            "kapitalrueckgewaehr": True,
            "rentenbezugsform": "Dynamisch",
            "mitAblaufleistung": True,
            "beitragsdynamik": 0,
            "bAVTarife": "BZML"
        
        }
        
        # variable Angeben, die beim Aufruf vorgegebene werden:
        self.vertrag_dict['beitrag'] = vtg_dict.get('zahlbeitrag')
        if vtg_dict.get('zahlweise') == 12:
            self.vertrag_dict['zahlweise'] = 'Monatlich'
        else:
            self.vertrag_dict['zahlweise'] = 'Einmalbeitrag'
            
        self.vertrag_dict['beitragszahlungsdauer'] = vtg_dict.get('beitragszahlungsdauer')
        self.vertrag_dict['aufschubzeit'] = vtg_dict.get('versicherungsdauer')
        self.vertrag_dict['versicherungsbeginn'] = vtg_dict.get('versicherungsbeginn')
        self.vertrag_dict['geburtsdatum'] = vtg_dict.get('geburtsdatum')
        
        print('------------- Anfang:')
        print('Input Vertrag MuM:')
        print(self.vertrag_dict)
        print('------------- Ende')
        
    
    #  function, fuer eine verschoenerte darstellung
    def print_output(self, header, content):
        print(header)
        print(content)
        for x in range(20):
            print("-", end="")
        print()

    def aufrufWebservice(self):

        # macht ein post request, mit der url, der authentification, den header und die json die geposted werden soll
        response = requests.post(self.url, auth=(self.username, self.password), headers=self.header, json=self.vertrag_dict)
        
        print()
        
        # gibt den response in der konsole aus
        self.print_output('Response Code', response)
        self.print_output('Response Header', response.headers)
        self.print_output('Response', response.text)
        
        return response.text
        
    def LeseOutput(self, respose_str):
        
        dict1={}
        
        print('------------- Anfang:')
        print('Response Output:')
        print(respose_str)
        print('------------- Ende')


        return dict1
    
    def LeseAblaufleistung(self, outputDaten):
        dict_alles = {}
        dict_ablaufleistung = {}
        dict_name_wert = {}
        
        
        print('------------- Anfang:')
        print('Ablaufleistung:')
        print(dict_ablaufleistung)
        print('------------- Ende')
        
        return dict_ablaufleistung    
