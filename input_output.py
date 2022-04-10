#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import protokoll as prot


class InputOutput(object):

    def __init__(self, f_dict):
        file_protokoll=f_dict.get('protokoll_file_InputOutput')
        self.oprot = prot.Protokoll(file_protokoll)
        
    def LeseOutput(self, respose_str):
        
        dict1 = {}
        dict1 = json.loads(respose_str)
    
        print('------------- Anfang:')
        print('Response Output:')
        print(dict1)
        print('------------- Ende')


        return dict1
    
