# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import statistics
from tabulate import tabulate
import datos as data
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(931, 631)
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
        self.tituloAnalisisDescriptivo.setGeometry(QtCore.QRect(30, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tituloAnalisisDescriptivo.setFont(font)
        self.tituloAnalisisDescriptivo.setObjectName("tituloAnalisisDescriptivo")
        self.comboBoxAnalisisDescriptivo = QtWidgets.QComboBox(Dialog)
        self.comboBoxAnalisisDescriptivo.setGeometry(QtCore.QRect(170, 120, 171, 22))
        self.comboBoxAnalisisDescriptivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxAnalisisDescriptivo.setEditable(False)
        self.comboBoxAnalisisDescriptivo.setMinimumContentsLength(1)
        self.comboBoxAnalisisDescriptivo.setObjectName("comboBoxAnalisisDescriptivo")
        self.comboBoxAnalisisDescriptivo.addItem("Edad")
        self.comboBoxAnalisisDescriptivo.addItem("Sector")
        self.comboBoxAnalisisDescriptivo.addItem("Entidad Ubicacion Unidad Medica")
        self.comboBoxAnalisisDescriptivo.addItem("Entidad Nacimiento Paciente")
        self.comboBoxAnalisisDescriptivo.addItem("Entidad Residencia Paciente")
        self.comboBoxAnalisisDescriptivo.addItem("Municipio Residencia Paciente")
        self.botonAnalisisDescriptivo = QtWidgets.QPushButton(Dialog)
        self.botonAnalisisDescriptivo.setGeometry(QtCore.QRect(350, 120, 161, 23))
        self.botonAnalisisDescriptivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAnalisisDescriptivo.setDefault(False)
        self.botonAnalisisDescriptivo.setObjectName("botonAnalisisDescriptivo")
        self.labelSeleccioneDato = QtWidgets.QLabel(Dialog)
        self.labelSeleccioneDato.setGeometry(QtCore.QRect(30, 120, 131, 16))
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
        self.tituloAnalisisDescriptivo_2 = QtWidgets.QLabel(Dialog)
        self.tituloAnalisisDescriptivo_2.setGeometry(QtCore.QRect(30, 160, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tituloAnalisisDescriptivo_2.setFont(font)
        self.tituloAnalisisDescriptivo_2.setObjectName("tituloAnalisisDescriptivo_2")
        self.labelDatoXDispersion = QtWidgets.QLabel(Dialog)
        self.labelDatoXDispersion.setGeometry(QtCore.QRect(30, 200, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoXDispersion.setFont(font)
        self.labelDatoXDispersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoXDispersion.setObjectName("labelDatoXDispersion")
        self.tituloAnalisisDescriptivo_3 = QtWidgets.QLabel(Dialog)
        self.tituloAnalisisDescriptivo_3.setGeometry(QtCore.QRect(30, 240, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tituloAnalisisDescriptivo_3.setFont(font)
        self.tituloAnalisisDescriptivo_3.setObjectName("tituloAnalisisDescriptivo_3")
        self.datoXDispersion = QtWidgets.QComboBox(Dialog)
        self.datoXDispersion.setGeometry(QtCore.QRect(90, 200, 69, 22))
        self.datoXDispersion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoXDispersion.setObjectName("datoXDispersion")
        self.labelDatoYDispersion = QtWidgets.QLabel(Dialog)
        self.labelDatoYDispersion.setGeometry(QtCore.QRect(180, 200, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoYDispersion.setFont(font)
        self.labelDatoYDispersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoYDispersion.setObjectName("labelDatoYDispersion")
        self.datoYDispersion = QtWidgets.QComboBox(Dialog)
        self.datoYDispersion.setGeometry(QtCore.QRect(240, 200, 69, 22))
        self.datoYDispersion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoYDispersion.setObjectName("datoYDispersion")
        self.botonGraficaDispersion = QtWidgets.QPushButton(Dialog)
        self.botonGraficaDispersion.setGeometry(QtCore.QRect(320, 200, 161, 23))
        self.botonGraficaDispersion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonGraficaDispersion.setDefault(False)
        self.botonGraficaDispersion.setFlat(False)
        self.botonGraficaDispersion.setObjectName("botonGraficaDispersion")
        self.labelDatoYCorrelacion = QtWidgets.QLabel(Dialog)
        self.labelDatoYCorrelacion.setGeometry(QtCore.QRect(180, 280, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoYCorrelacion.setFont(font)
        self.labelDatoYCorrelacion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoYCorrelacion.setObjectName("labelDatoYCorrelacion")
        self.datoYCorrelacion = QtWidgets.QComboBox(Dialog)
        self.datoYCorrelacion.setGeometry(QtCore.QRect(240, 280, 69, 22))
        self.datoYCorrelacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoYCorrelacion.setObjectName("datoYCorrelacion")
        self.datoXCorrelacion = QtWidgets.QComboBox(Dialog)
        self.datoXCorrelacion.setGeometry(QtCore.QRect(90, 280, 69, 22))
        self.datoXCorrelacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.datoXCorrelacion.setObjectName("datoXCorrelacion")
        self.labelDatoXCorrelacion = QtWidgets.QLabel(Dialog)
        self.labelDatoXCorrelacion.setGeometry(QtCore.QRect(30, 280, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDatoXCorrelacion.setFont(font)
        self.labelDatoXCorrelacion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDatoXCorrelacion.setObjectName("labelDatoXCorrelacion")
        self.botonAnalisisCorrelacion = QtWidgets.QPushButton(Dialog)
        self.botonAnalisisCorrelacion.setGeometry(QtCore.QRect(320, 280, 161, 23))
        self.botonAnalisisCorrelacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botonAnalisisCorrelacion.setAutoDefault(True)
        self.botonAnalisisCorrelacion.setDefault(False)
        self.botonAnalisisCorrelacion.setObjectName("botonAnalisisCorrelacion")
        self.output = QtWidgets.QLabel(Dialog)
        self.output.setGeometry(QtCore.QRect(20, 340, 891, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")

        # Añadir más elementos al comboBoxAnalisisDescriptivo 
        # self.comboBoxAnalisisDescriptivo.addItem("Hello")

        # Conecta el boton de Obtener Análisis Descriptivo
        self.botonAnalisisDescriptivo.clicked.connect(self.clickAnalisisDescriptivo)

        # Conecta el boton de Obtener Gráfica Dispersión
        self.botonGraficaDispersion.clicked.connect(self.clickGraficaDispersion)

        # Conecta el boton de Obtener Análisis Correlación
        self.botonAnalisisCorrelacion.clicked.connect(self.clickAnalisisCorrelacion)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tituloProyecto.setText(_translate("Dialog", "Proyecto Análisis de Datos del COVID-19"))
        self.tituloAnalisisDescriptivo.setText(_translate("Dialog", "Análisis Descriptivo"))
        self.comboBoxAnalisisDescriptivo.setItemText(0, _translate("Dialog", "Edad"))
        self.botonAnalisisDescriptivo.setText(_translate("Dialog", "Obtener Análisis Descriptivo"))
        self.labelSeleccioneDato.setText(_translate("Dialog", "Seleccione el dato"))
        self.tituloAnalisisDescriptivo_2.setText(_translate("Dialog", "Gráfica Dispersión"))
        self.labelDatoXDispersion.setText(_translate("Dialog", "Dato X"))
        self.tituloAnalisisDescriptivo_3.setText(_translate("Dialog", "Análisis Correlación"))
        self.labelDatoYDispersion.setText(_translate("Dialog", "Dato Y"))
        self.botonGraficaDispersion.setText(_translate("Dialog", "Obtener Gráfica Dispersión"))
        self.labelDatoYCorrelacion.setText(_translate("Dialog", "Dato Y"))
        self.labelDatoXCorrelacion.setText(_translate("Dialog", "Dato X"))
        self.botonAnalisisCorrelacion.setText(_translate("Dialog", "Obtener Análisis Correlación"))
        self.output.setText(_translate("Dialog", "OUTPUT"))


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

        # ENTIDAD UBICACION UNIDAD MEDICA
        elif variable == "Entidad Ubicacion Unidad Medica":
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


    # Función del Botón de Obtener Gráfica Dispersión
    def clickGraficaDispersion(self):
        print("FUNCIONA BOTON GRAFICA DISPERSION")


    # Función del Botón de Obtener Análisis Correlación
    def clickAnalisisCorrelacion(self):
        print("FUNCIONA BOTON ANALISIS CORRELACION")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
