# -*- coding: utf-8 -*-

import requests
import protokoll as prot

class WebService:
    
    def __init__(self, f_dict):
        file_protokoll=f_dict.get('protokoll_file_AufrufWS')
        self.oprot = prot.Protokoll(file_protokoll)

        # setzt den Benutzername und das Passwort
        self.username = "bayerische"
        self.password = "aljvie"

        # setzt die url, den header und die Post JSON
        self.url = 'https://planetbayerische.ivfp.eu/api/PriipCalculation'
        self.header = {'Content-type': 'application/json'}



    #  function, fuer eine verschoenerte darstellung
    def print_output(self, header, content):
        print(header)
        print(content)
        for x in range(20):
            print("-", end="")
        print()

    def aufrufWebservice(self, data):

        # macht ein post request, mit der url, der authentification, den header und die json die geposted werden soll
        response = requests.post(self.url, auth=(self.username, self.password), headers=self.header, json=data)
        
        print()
        
        # gibt den response in der konsole aus
        self.print_output('Response Code', response)
        self.print_output('Response Header', response.headers)
        self.print_output('Response', response.text)
        
        return response.text
        
