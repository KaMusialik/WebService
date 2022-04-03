# -*- coding: utf-8 -*-

#import sys
#import PyQt5.QtCore as core
#import PyQt5.QtWidgets as widgets
#import PyQt5.QtGui as gui
#import PyQt5.uic as uic


import protokoll as prot
import input_output as inout
import webservice as ws
import myplotts as myplt

inputDaten={}
outputDaten={}
ablaufleistung={}

files_dict={}

#work directory:
files_dict['work_dir']='/home/pi/Raspi120GB/MeineProjekte/Webservice/'
#files_dict['work_dir']='/Users/karol/MeineProjekte/WebService/WEbservice/'

#einzelne Dateien:
files_dict['mainwindow_file']=files_dict.get('work_dir')+'mainWindow.ui'
files_dict['input_output_file']=files_dict.get('work_dir')+'input_output_file.txt'
files_dict['protokoll_file_main']=files_dict.get('work_dir')+'protokoll_main.txt'
files_dict['protokoll_file_InputOutput']=files_dict.get('work_dir')+'protokoll_InputOutput.txt'
files_dict['protokoll_file_AufrufWS']=files_dict.get('work_dir')+'protokoll_AufrufWS.txt'
files_dict['protokoll_file_MyPlotts']=files_dict.get('work_dir')+'protokoll_MyPlotts.txt'

#app = widgets.QApplication(sys.argv)

#wMainwindow=uic.loadUi(files_dict.get('mainwindow_file'))    

oprot = prot.Protokoll(files_dict.get('protokoll_file_main'))
oinout = inout.InputOutput(files_dict)

ows = ws.WebService(files_dict)

inputDaten = oinout.LeseInput()

response_str=str(ows.aufrufWebservice(inputDaten))

outputDaten = oinout.LeseOutput(response_str)

ablaufleistung=oinout.LeseAblaufleistung(outputDaten)

omyplt = myplt.MyPlotts(files_dict)
omyplt.PlotteAblaufleistung(ablaufleistung)    


#wMainwindow.show()
#sys.exit(app.exec_())