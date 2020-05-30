# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import matplotlib.pyplot as plt
import random
import numpy as np
import statistics
from tabulate import tabulate
import datos as data
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(936, 810)
        self.tituloProyecto = QtWidgets.QLabel(Dialog)
        self.tituloProyecto.setGeometry(QtCore.QRect(230, 10, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tituloProyecto.setFont(font)
        self.tituloProyecto.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloProyecto.setObjectName("tituloProyecto")
        self.tituloAnalisisDescriptivo = QtWidgets.QLabel(Dialog)
        self.tituloAnalisisDescriptivo.setGeometry(QtCore.QRect(10, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tituloAnalisisDescriptivo.setFont(font)
        self.tituloAnalisisDescriptivo.setObjectName("tituloAnalisisDescriptivo")
        self.comboBoxAnalisisDescriptivo = QtWidgets.QComboBox(Dialog)
        self.comboBoxAnalisisDescriptivo.setGeometry(QtCore.QRect(150, 120, 171, 22))
        self.comboBoxAnalisisDescriptivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxAnalisisDescriptivo.setEditable(False)
        self.comboBoxAnalisisDescriptivo.setMinimumContentsLength(1)
        self.comboBoxAnalisisDescriptivo.setObjectName("comboBoxAnalisisDescriptivo")
        self.comboBoxAnalisisDescriptivo.addItem("")
        self.comboBoxAnalisisDescriptivo.addItem("")
        self.comboBoxAnalisisDescriptivo.addItem("")
        self.comboBoxAnalisisDescriptivo.addItem("")
        self.comboBoxAnalisisDescriptivo.addItem("")
        self.comboBoxAnalisisDescriptivo.addItem("")
        self.botonAnalisisDescriptivo = QtWidgets.QPushButton(Dialog)
        self.botonAnalisisDescriptivo.setGeometry(QtCore.QRect(330, 120, 151, 23))
        self.botonAnalisisDescriptivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAnalisisDescriptivo.setDefault(False)
        self.botonAnalisisDescriptivo.setObjectName("botonAnalisisDescriptivo")
        self.labelSeleccioneDato = QtWidgets.QLabel(Dialog)
        self.labelSeleccioneDato.setGeometry(QtCore.QRect(10, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSeleccioneDato.setFont(font)
        self.labelSeleccioneDato.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSeleccioneDato.setObjectName("labelSeleccioneDato")
        self.lineaSeparacion = QtWidgets.QFrame(Dialog)
        self.lineaSeparacion.setGeometry(QtCore.QRect(0, 320, 931, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineaSeparacion.setFont(font)
        self.lineaSeparacion.setAutoFillBackground(False)
        self.lineaSeparacion.setLineWidth(1)
        self.lineaSeparacion.setMidLineWidth(1)
        self.lineaSeparacion.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineaSeparacion.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineaSeparacion.setObjectName("lineaSeparacion")
        self.tituloGraficaDispersion = QtWidgets.QLabel(Dialog)
        self.tituloGraficaDispersion.setGeometry(QtCore.QRect(10, 160, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tituloGraficaDispersion.setFont(font)
        self.tituloGraficaDispersion.setObjectName("tituloGraficaDispersion")
        self.labelDatoXDispersion = QtWidgets.QLabel(Dialog)
        self.labelDatoXDispersion.setGeometry(QtCore.QRect(10, 200, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoXDispersion.setFont(font)
        self.labelDatoXDispersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoXDispersion.setObjectName("labelDatoXDispersion")
        self.tituloAnalisisCorrelacion = QtWidgets.QLabel(Dialog)
        self.tituloAnalisisCorrelacion.setGeometry(QtCore.QRect(10, 240, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tituloAnalisisCorrelacion.setFont(font)
        self.tituloAnalisisCorrelacion.setObjectName("tituloAnalisisCorrelacion")
        self.datoXDispersion = QtWidgets.QComboBox(Dialog)
        self.datoXDispersion.setGeometry(QtCore.QRect(70, 200, 69, 22))
        self.datoXDispersion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoXDispersion.setObjectName("datoXDispersion")
        self.datoXDispersion.addItem("")
        self.labelDatoYDispersion = QtWidgets.QLabel(Dialog)
        self.labelDatoYDispersion.setGeometry(QtCore.QRect(150, 200, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoYDispersion.setFont(font)
        self.labelDatoYDispersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoYDispersion.setObjectName("labelDatoYDispersion")
        self.datoYDispersion = QtWidgets.QComboBox(Dialog)
        self.datoYDispersion.setGeometry(QtCore.QRect(210, 200, 121, 22))
        self.datoYDispersion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoYDispersion.setObjectName("datoYDispersion")
        self.datoYDispersion.addItem("")
        self.botonGraficaDispersion = QtWidgets.QPushButton(Dialog)
        self.botonGraficaDispersion.setGeometry(QtCore.QRect(340, 200, 141, 23))
        self.botonGraficaDispersion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonGraficaDispersion.setDefault(False)
        self.botonGraficaDispersion.setFlat(False)
        self.botonGraficaDispersion.setObjectName("botonGraficaDispersion")
        self.labelDatoYCorrelacion = QtWidgets.QLabel(Dialog)
        self.labelDatoYCorrelacion.setGeometry(QtCore.QRect(150, 280, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoYCorrelacion.setFont(font)
        self.labelDatoYCorrelacion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoYCorrelacion.setObjectName("labelDatoYCorrelacion")
        self.datoYCorrelacion = QtWidgets.QComboBox(Dialog)
        self.datoYCorrelacion.setGeometry(QtCore.QRect(210, 280, 121, 22))
        self.datoYCorrelacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoYCorrelacion.setObjectName("datoYCorrelacion")
        self.datoYCorrelacion.addItem("")
        self.datoXCorrelacion = QtWidgets.QComboBox(Dialog)
        self.datoXCorrelacion.setGeometry(QtCore.QRect(70, 280, 69, 22))
        self.datoXCorrelacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoXCorrelacion.setObjectName("datoXCorrelacion")
        self.datoXCorrelacion.addItem("")
        self.labelDatoXCorrelacion = QtWidgets.QLabel(Dialog)
        self.labelDatoXCorrelacion.setGeometry(QtCore.QRect(10, 280, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoXCorrelacion.setFont(font)
        self.labelDatoXCorrelacion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoXCorrelacion.setObjectName("labelDatoXCorrelacion")
        self.botonAnalisisCorrelacion = QtWidgets.QPushButton(Dialog)
        self.botonAnalisisCorrelacion.setGeometry(QtCore.QRect(340, 280, 151, 23))
        self.botonAnalisisCorrelacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAnalisisCorrelacion.setAutoDefault(True)
        self.botonAnalisisCorrelacion.setDefault(False)
        self.botonAnalisisCorrelacion.setObjectName("botonAnalisisCorrelacion")
        self.output = QtWidgets.QLabel(Dialog)
        self.output.setGeometry(QtCore.QRect(20, 340, 541, 461))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.output2 = QtWidgets.QLabel(Dialog)
        self.output2.setGeometry(QtCore.QRect(570, 340, 361, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output2.setFont(font)
        self.output2.setAlignment(QtCore.Qt.AlignCenter)
        self.output2.setObjectName("output2")
        self.labelDatoXRegresion = QtWidgets.QLabel(Dialog)
        self.labelDatoXRegresion.setGeometry(QtCore.QRect(500, 280, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoXRegresion.setFont(font)
        self.labelDatoXRegresion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoXRegresion.setObjectName("labelDatoXRegresion")
        self.datoYRegresion = QtWidgets.QComboBox(Dialog)
        self.datoYRegresion.setGeometry(QtCore.QRect(700, 280, 121, 22))
        self.datoYRegresion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoYRegresion.setObjectName("datoYRegresion")
        self.datoYRegresion.addItem("")
        self.tituloRegresion = QtWidgets.QLabel(Dialog)
        self.tituloRegresion.setGeometry(QtCore.QRect(500, 240, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tituloRegresion.setFont(font)
        self.tituloRegresion.setObjectName("tituloRegresion")
        self.datoXRegresion = QtWidgets.QComboBox(Dialog)
        self.datoXRegresion.setGeometry(QtCore.QRect(560, 280, 69, 22))
        self.datoXRegresion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoXRegresion.setObjectName("datoXRegresion")
        self.datoXRegresion.addItem("")
        self.labelDatoYRegresion = QtWidgets.QLabel(Dialog)
        self.labelDatoYRegresion.setGeometry(QtCore.QRect(640, 280, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoYRegresion.setFont(font)
        self.labelDatoYRegresion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoYRegresion.setObjectName("labelDatoYRegresion")
        self.botonRegresion = QtWidgets.QPushButton(Dialog)
        self.botonRegresion.setGeometry(QtCore.QRect(830, 280, 101, 23))
        self.botonRegresion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonRegresion.setDefault(False)
        self.botonRegresion.setFlat(False)
        self.botonRegresion.setObjectName("botonRegresion")

        # Añadir más elementos al comboBoxAnalisisDescriptivo 
        # self.comboBoxAnalisisDescriptivo.addItem("Hello")

        # Conecta el boton de Obtener Análisis Descriptivo
        self.botonAnalisisDescriptivo.clicked.connect(self.clickAnalisisDescriptivo)

        # Conecta el boton de Obtener Gráfica Dispersión
        self.botonGraficaDispersion.clicked.connect(self.clickGraficaDispersion)

        # Conecta el boton de Obtener Análisis Correlación
        self.botonAnalisisCorrelacion.clicked.connect(self.clickAnalisisCorrelacion)

        # Conecta el boton de Obtener Regresión
        self.botonRegresion.clicked.connect(self.clickRegresion)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tituloProyecto.setText(_translate("Dialog", "Proyecto Análisis de Datos del COVID-19"))
        self.tituloAnalisisDescriptivo.setText(_translate("Dialog", "Análisis Descriptivo"))
        self.comboBoxAnalisisDescriptivo.setItemText(0, _translate("Dialog", "Edad"))
        self.comboBoxAnalisisDescriptivo.setItemText(1, _translate("Dialog", "Sector"))
        self.comboBoxAnalisisDescriptivo.setItemText(2, _translate("Dialog", "Entidad Ubicación Unidad Médica"))
        self.comboBoxAnalisisDescriptivo.setItemText(3, _translate("Dialog", "Entidad Nacimiento Paciente"))
        self.comboBoxAnalisisDescriptivo.setItemText(4, _translate("Dialog", "Entidad Residencia Paciente"))
        self.comboBoxAnalisisDescriptivo.setItemText(5, _translate("Dialog", "Municipio Residencia Paciente"))
        self.botonAnalisisDescriptivo.setText(_translate("Dialog", "Obtener Análisis Descriptivo"))
        self.labelSeleccioneDato.setText(_translate("Dialog", "Seleccione el dato"))
        self.tituloGraficaDispersion.setText(_translate("Dialog", "Gráfica Dispersión"))
        self.labelDatoXDispersion.setText(_translate("Dialog", "Dato X"))
        self.tituloAnalisisCorrelacion.setText(_translate("Dialog", "Análisis Correlación"))
        self.datoXDispersion.setItemText(0, _translate("Dialog", "Edad"))
        self.labelDatoYDispersion.setText(_translate("Dialog", "Dato Y"))
        self.datoYDispersion.setItemText(0, _translate("Dialog", "Entidad Federativa"))
        self.botonGraficaDispersion.setText(_translate("Dialog", "Obtener Gráfica Dispersión"))
        self.labelDatoYCorrelacion.setText(_translate("Dialog", "Dato Y"))
        self.datoYCorrelacion.setItemText(0, _translate("Dialog", "Entidad Federativa"))
        self.datoXCorrelacion.setItemText(0, _translate("Dialog", "Edad"))
        self.labelDatoXCorrelacion.setText(_translate("Dialog", "Dato X"))
        self.botonAnalisisCorrelacion.setText(_translate("Dialog", "Obtener Análisis Correlación"))
        self.output.setText(_translate("Dialog", "OUTPUT"))
        self.output2.setText(_translate("Dialog", "OUTPUT 2"))
        self.labelDatoXRegresion.setText(_translate("Dialog", "Dato X"))
        self.datoYRegresion.setItemText(0, _translate("Dialog", "Entidad Federativa"))
        self.tituloRegresion.setText(_translate("Dialog", "Regresión"))
        self.datoXRegresion.setItemText(0, _translate("Dialog", "Edad"))
        self.labelDatoYRegresion.setText(_translate("Dialog", "Dato Y"))
        self.botonRegresion.setText(_translate("Dialog", "Obtener Regresión"))
        

    # Función del Botón de Obtener Análisis Descriptivo
    def clickAnalisisDescriptivo(self):
        variable = self.comboBoxAnalisisDescriptivo.currentText()
        
        # EDAD
        if variable == "Edad":
            # Media
            media = statistics.mean(data.lista_edad)
            # print(media)
            # Mediana
            mediana = statistics.median(data.lista_edad)
            # print(mediana)
            # Moda
            moda = statistics.mode(data.lista_edad)
            # print(moda)
            # Desv. Estándar
            devEstandar = statistics.stdev(data.lista_edad)
            # print(devEstandar)
            # Varianza
            varianza = statistics.variance(data.lista_edad)
            # print(varianza)            
            # Mínimo
            minimo = min(data.lista_edad)
            # print(minimo)
            # Máximo
            maximo = max(data.lista_edad)
            # print(maximo)
            # Rango
            rango = maximo - minimo
            # print(rango)
            # Suma
            suma = 0
            for i in data.lista_edad:
                suma += i
            # print(suma)
            # No. de datos
            noDatos = len(data.lista_edad)
            # print(noDatos)


            table = [["Media", media], ["Mediana", mediana], ["Moda", moda], ["Desv. Estandar", devEstandar], ["Varianza", varianza], ["Minimo", minimo], ["Maximo", maximo], ["Rango", rango], ["Suma", suma], ["No. de datos", noDatos]]
            headers = ["ANALISIS DESCRIPTIVO"]
            
            final = (tabulate(table, headers, colalign=(" ","center"), tablefmt="simple"))               

            # Imprimir Analisis Descriptivo
            self.output.setText(final)

             # Imprimir Diccionario de Términos
            self.output2.setText(" ")

        # SECTOR
        elif variable == "Sector":
            # Media
            media = statistics.mean(data.lista_sector)
            # print(media)
            # Mediana
            mediana = statistics.median(data.lista_sector)
            # print(mediana)
            # Moda
            moda = statistics.mode(data.lista_sector)
            # print(moda)
            # Desv. Estándar
            devEstandar = statistics.stdev(data.lista_sector)
            # print(devEstandar)
            # Varianza
            varianza = statistics.variance(data.lista_sector)
            # print(varianza)            
            # Mínimo
            minimo = min(data.lista_sector)
            # print(minimo)
            # Máximo
            maximo = max(data.lista_sector)
            # print(maximo)
            # Rango
            rango = maximo - minimo
            # print(rango)
            # Suma
            suma = 0
            for i in data.lista_sector:
                suma += i
            # print(suma)
            # No. de datos
            noDatos = len(data.lista_sector)
            # print(noDatos)


            table = [["Media", media], ["Mediana", mediana], ["Moda", moda], ["Desv. Estandar", devEstandar], ["Varianza", varianza], ["Minimo", minimo], ["Maximo", maximo], ["Rango", rango], ["Suma", suma], ["No. de datos", noDatos]]
            headers = ["ANALISIS DESCRIPTIVO"]
            
            final = (tabulate(table, headers, colalign=(" ","center"), tablefmt="simple"))               

            # Imprimir Analisis Descriptivo
            self.output.setText(final)

            table2 = [["1", "CRUZ ROJA"], ["2", "DIF"], ["3", "ESTATAL"], ["4", "IMSS"], ["5", "IMSS-BIENESTAR"], ["6", "ISSSTE"], ["7", "MUNICIPAL"], ["8", "PEMEX"], ["9", "PRIVADA"], ["10", "SEDENA"], ["11", "SEMAR"], ["12", "SSA"], ["13", "UNIVERSITARIO"], ["99", "NO ESPECIFICADO"]]
            headers2 = ["CLAVE", "DESCRIPCION"]
            
            final2 = (tabulate(table2, headers2, colalign=(" ","center"), tablefmt="simple")) 

            # Imprimir Diccionario de Términos
            self.output2.setText(final2)

        # ENTIDAD UBICACION UNIDAD MEDICA
        elif variable == "Entidad Ubicación Unidad Médica":
            # Media
            media = statistics.mean(data.lista_entidadUM)
            # print(media)
            # Mediana
            mediana = statistics.median(data.lista_entidadUM)
            # print(mediana)
            # Moda
            moda = statistics.mode(data.lista_entidadUM)
            # print(moda)
            # Desv. Estándar
            devEstandar = statistics.stdev(data.lista_entidadUM)
            # print(devEstandar)
            # Varianza
            varianza = statistics.variance(data.lista_entidadUM)
            # print(varianza)            
            # Mínimo
            minimo = min(data.lista_entidadUM)
            # print(minimo)
            # Máximo
            maximo = max(data.lista_entidadUM)
            # print(maximo)
            # Rango
            rango = maximo - minimo
            # print(rango)
            # Suma
            suma = 0
            for i in data.lista_entidadUM:
                suma += i
            # print(suma)
            # No. de datos
            noDatos = len(data.lista_entidadUM)
            # print(noDatos)


            table = [["Media", media], ["Mediana", mediana], ["Moda", moda], ["Desv. Estandar", devEstandar], ["Varianza", varianza], ["Minimo", minimo], ["Maximo", maximo], ["Rango", rango], ["Suma", suma], ["No. de datos", noDatos]]
            headers = ["ANALISIS DESCRIPTIVO"]
            
            final = (tabulate(table, headers, colalign=(" ","center"), tablefmt="simple"))               

            # Imprimir Analisis Descriptivo
            self.output.setText(final)

            table2 = [["1", "AGUASCALIENTES"], ["2", "BAJA CALIFORNIA"], ["3", "BAJA CALIFORNIA SUR"], ["4", "CAMPECHE"], ["5", "COAHUILA"], ["6", "COLIMA"], ["7", "CHIAPAS"], ["8", "CHIHUAHUA"], ["9", "CIUDAD DE MÉXICO"], ["10", "DURANGO"], ["11", "GUANAJUATO"], ["12", "GUERRERO"], ["13", "HIDALGO"], ["14", "JALISCO"], ["15", "MÉXICO"], ["16", "MICHOACÁN"], ["17", "MORELOS"], ["18", "NAYARIT"], ["19", "NUEVO LEÓN"], ["20", "OAXACA"], ["21", "PUEBLA"], ["22", "QUERÉTARO"], ["23", "QUINTANA ROO"], ["24", "SAN LUIS POTOSÍ"], ["25", "SINALOA"], ["26", "SONORA"], ["27", "TABASCO"], ["28", "TAMAULIPAS"], ["29", "TLAXCALA"], ["30", "VERACRUZ"], ["31", "YUCATÁN"], ["32", "ZACATECAS"], ["36", "ESTADOS UNIDOS MEXICANOS"], ["97", "NO APLICA"], ["98", "SE IGNORA"], ["99", "NO ESPECIFICADO"]]
            headers2 = ["CLAVE ENTIDAD", "ENTIDAD FEDERATIVA"]
            
            final2 = (tabulate(table2, headers2, colalign=(" ","center"), tablefmt="simple")) 

            # Imprimir Diccionario de Términos
            self.output2.setText(final2)

        # ENTIDAD NACIMIENTO PACIENTE
        elif variable == "Entidad Nacimiento Paciente":
            # Media
            media = statistics.mean(data.lista_entidadNAC)
            # print(media)
            # Mediana
            mediana = statistics.median(data.lista_entidadNAC)
            # print(mediana)
            # Moda
            moda = statistics.mode(data.lista_entidadNAC)
            # print(moda)
            # Desv. Estándar
            devEstandar = statistics.stdev(data.lista_entidadNAC)
            # print(devEstandar)
            # Varianza
            varianza = statistics.variance(data.lista_entidadNAC)
            # print(varianza)            
            # Mínimo
            minimo = min(data.lista_entidadNAC)
            # print(minimo)
            # Máximo
            maximo = max(data.lista_entidadNAC)
            # print(maximo)
            # Rango
            rango = maximo - minimo
            # print(rango)
            # Suma
            suma = 0
            for i in data.lista_entidadNAC:
                suma += i
            # print(suma)
            # No. de datos
            noDatos = len(data.lista_entidadNAC)
            # print(noDatos)


            table = [["Media", media], ["Mediana", mediana], ["Moda", moda], ["Desv. Estandar", devEstandar], ["Varianza", varianza], ["Minimo", minimo], ["Maximo", maximo], ["Rango", rango], ["Suma", suma], ["No. de datos", noDatos]]
            headers = ["ANALISIS DESCRIPTIVO"]
            
            final = (tabulate(table, headers, colalign=(" ","center"), tablefmt="simple"))               

            # Imprimir Analisis Descriptivo
            self.output.setText(final)

            table2 = [["1", "AGUASCALIENTES"], ["2", "BAJA CALIFORNIA"], ["3", "BAJA CALIFORNIA SUR"], ["4", "CAMPECHE"], ["5", "COAHUILA"], ["6", "COLIMA"], ["7", "CHIAPAS"], ["8", "CHIHUAHUA"], ["9", "CIUDAD DE MÉXICO"], ["10", "DURANGO"], ["11", "GUANAJUATO"], ["12", "GUERRERO"], ["13", "HIDALGO"], ["14", "JALISCO"], ["15", "MÉXICO"], ["16", "MICHOACÁN"], ["17", "MORELOS"], ["18", "NAYARIT"], ["19", "NUEVO LEÓN"], ["20", "OAXACA"], ["21", "PUEBLA"], ["22", "QUERÉTARO"], ["23", "QUINTANA ROO"], ["24", "SAN LUIS POTOSÍ"], ["25", "SINALOA"], ["26", "SONORA"], ["27", "TABASCO"], ["28", "TAMAULIPAS"], ["29", "TLAXCALA"], ["30", "VERACRUZ"], ["31", "YUCATÁN"], ["32", "ZACATECAS"], ["36", "ESTADOS UNIDOS MEXICANOS"], ["97", "NO APLICA"], ["98", "SE IGNORA"], ["99", "NO ESPECIFICADO"]]
            headers2 = ["CLAVE ENTIDAD", "ENTIDAD FEDERATIVA"]
            
            final2 = (tabulate(table2, headers2, colalign=(" ","center"), tablefmt="simple")) 

            # Imprimir Diccionario de Términos
            self.output2.setText(final2)

        # ENTIDAD RESIDENCIA PACIENTE
        elif variable == "Entidad Residencia Paciente":
            # Media
            media = statistics.mean(data.lista_entidadRES)
            # print(media)
            # Mediana
            mediana = statistics.median(data.lista_entidadRES)
            # print(mediana)
            # Moda
            moda = statistics.mode(data.lista_entidadRES)
            # print(moda)
            # Desv. Estándar
            devEstandar = statistics.stdev(data.lista_entidadRES)
            # print(devEstandar)
            # Varianza
            varianza = statistics.variance(data.lista_entidadRES)
            # print(varianza)            
            # Mínimo
            minimo = min(data.lista_entidadRES)
            # print(minimo)
            # Máximo
            maximo = max(data.lista_entidadRES)
            # print(maximo)
            # Rango
            rango = maximo - minimo
            # print(rango)
            # Suma
            suma = 0
            for i in data.lista_entidadRES:
                suma += i
            # print(suma)
            # No. de datos
            noDatos = len(data.lista_entidadRES)
            # print(noDatos)


            table = [["Media", media], ["Mediana", mediana], ["Moda", moda], ["Desv. Estandar", devEstandar], ["Varianza", varianza], ["Minimo", minimo], ["Maximo", maximo], ["Rango", rango], ["Suma", suma], ["No. de datos", noDatos]]
            headers = ["ANALISIS DESCRIPTIVO"]
            
            final = (tabulate(table, headers, colalign=(" ","center"), tablefmt="simple"))               

            # Imprimir Analisis Descriptivo
            self.output.setText(final)

            table2 = [["1", "AGUASCALIENTES"], ["2", "BAJA CALIFORNIA"], ["3", "BAJA CALIFORNIA SUR"], ["4", "CAMPECHE"], ["5", "COAHUILA"], ["6", "COLIMA"], ["7", "CHIAPAS"], ["8", "CHIHUAHUA"], ["9", "CIUDAD DE MÉXICO"], ["10", "DURANGO"], ["11", "GUANAJUATO"], ["12", "GUERRERO"], ["13", "HIDALGO"], ["14", "JALISCO"], ["15", "MÉXICO"], ["16", "MICHOACÁN"], ["17", "MORELOS"], ["18", "NAYARIT"], ["19", "NUEVO LEÓN"], ["20", "OAXACA"], ["21", "PUEBLA"], ["22", "QUERÉTARO"], ["23", "QUINTANA ROO"], ["24", "SAN LUIS POTOSÍ"], ["25", "SINALOA"], ["26", "SONORA"], ["27", "TABASCO"], ["28", "TAMAULIPAS"], ["29", "TLAXCALA"], ["30", "VERACRUZ"], ["31", "YUCATÁN"], ["32", "ZACATECAS"], ["36", "ESTADOS UNIDOS MEXICANOS"], ["97", "NO APLICA"], ["98", "SE IGNORA"], ["99", "NO ESPECIFICADO"]]
            headers2 = ["CLAVE ENTIDAD", "ENTIDAD FEDERATIVA"]
            
            final2 = (tabulate(table2, headers2, colalign=(" ","center"), tablefmt="simple")) 

            # Imprimir Diccionario de Términos
            self.output2.setText(final2)

        # MUNICIPIO RESIDENCIA PACIENTE
        elif variable == "Municipio Residencia Paciente":
            # Media
            media = statistics.mean(data.lista_municipioRES)
            # print(media)
            # Mediana
            mediana = statistics.median(data.lista_municipioRES)
            # print(mediana)
            # Moda
            moda = statistics.mode(data.lista_municipioRES)
            # print(moda)
            # Desv. Estándar
            devEstandar = statistics.stdev(data.lista_municipioRES)
            # print(devEstandar)
            # Varianza
            varianza = statistics.variance(data.lista_municipioRES)
            # print(varianza)            
            # Mínimo
            minimo = min(data.lista_municipioRES)
            # print(minimo)
            # Máximo
            maximo = max(data.lista_municipioRES)
            # print(maximo)
            # Rango
            rango = maximo - minimo
            # print(rango)
            # Suma
            suma = 0
            for i in data.lista_municipioRES:
                suma += i
            # print(suma)
            # No. de datos
            noDatos = len(data.lista_municipioRES)
            # print(noDatos)


            table = [["Media", media], ["Mediana", mediana], ["Moda", moda], ["Desv. Estandar", devEstandar], ["Varianza", varianza], ["Minimo", minimo], ["Maximo", maximo], ["Rango", rango], ["Suma", suma], ["No. de datos", noDatos]]
            headers = ["ANALISIS DESCRIPTIVO"]
            
            final = (tabulate(table, headers, colalign=(" ","center"), tablefmt="simple"))               

            # Imprimir Analisis Descriptivo
            self.output.setText(final)

            # Imprimir Diccionario Términos
            self.output2.setText(" ")

    # Función del Botón de Obtener Gráfica Dispersión
    def clickGraficaDispersion(self):
        print("FUNCIONA BOTON GRAFICA DISPERSION")
        self.GraficaCorrelacion()#GRAFICA DE DISPERSION 
    # Función del Botón de Obtener Análisis Correlación

        #CREO QUE SERIA UNA BUENA IDEA QUITAR EL BOTON DE ANALISIS DE CORRELACION Y HACER QUE CUANDO SE SAQUE LA GRAFICA DE CORRELACION TAMBIEN APAREZCA EL CALCULO DE CORRELACION
    def clickAnalisisCorrelacion(self):
        X = self.datoXCorrelacion.currentText()
        Y = self.datoYCorrelacion.currentText()

        if X == "Edad" and Y == "Entidad Federativa":
            y = data.lista_entidadUM     
            x = data.lista_edad

            y1 = np.array(y)
            x1 = np.array(x)

            mediaX = statistics.mean(data.lista_edad)
            mediaY = statistics.mean(data.lista_entidadUM)
            sumaX = 0
            for i in data.lista_edad:
                sumaX += i
                
                sumaY = 0
            for e in data.lista_edad:
                sumaY += e

            Columna1 = 0
            for i in data.lista_edad:
                n = i-mediaX
                Columna1 += n

            Columna2 = 0
            for i in data.lista_edad:
                n = i-mediaY
                Columna2 += n

            Columna3 = (sumaX - mediaX)*(sumaY - mediaY)
            Columna4 = (sumaX - mediaX)**2
            Columna5 = (sumaY - mediaY)**2
            Columna6 = (Columna1**2)**0.5
            Columna7 = (Columna2**2)**0.5
            correlacion = np.corrcoef(x1, y1)[0, 1]

            tableC = [["X-M(X)", Columna1], ["Y-M(Y)", Columna2], ["(X-M(X))(Y-M(Y))", Columna3], ["X-M(X)^2", Columna4], ["Y-M(Y)^2", Columna5], ["(sum(X-X)^2)^0.5", Columna6], ["(sum(Y-Y)^2)^0.5", Columna7], ["Correlacion", correlacion]]
            headersC = ["ANALISIS DE CORRELACION"]
            
            finalC = (tabulate(tableC, headersC, colalign=(" ","center"), tablefmt="simple"))               

            # Imprimir Analisis Descriptivo
            self.output.setText(finalC)

                   
        print("FUNCIONA BOTON ANALISIS CORRELACION")
        print(Columna1)

    def clickRegresion(self):
        print("FUNCIONA BOTON REGRESION")
        

    #FUNCION QUE PROJECTA LA GRAFICA DE MATPLOT SOBRE LA DISPERSION
    def GraficaCorrelacion(self):
        variableX = self.datoXDispersion.currentText()
        variableY = self.datoYDispersion.currentText()

        if variableX == "Edad" and variableY == "Entidad Federativa":
            y = data.lista_entidadUM     
            x = data.lista_edad
            dx = np.random.choice(np.arange(len(x)), 1000, replace=False)

            y1= np.array(y)
            x1= np.array(x)
        
            y_sample = y1[dx]
            x_sample = x1[dx]

        
            plt.scatter(x_sample,y_sample)
            plt.ylabel("Entidades Federativa")
            plt.xlabel("Edad de los Casos")

        
        
            plt.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
