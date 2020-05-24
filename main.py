# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import statistics
import datos as data
from PyQt5 import QtCore, QtGui, QtWidgets

# import csv

# # DATOS DEL CSV ORGANIZADOS EN LISTAS DEPENDIENDO DE SUS CATEGORIAS

# # Se abre el archivo csv
# f = open("200518COVID19MEXICO.csv", "r")
# reader = csv.reader(f)

# # Lista con TODOS los datos (177 134 DATOS)
# datos = []

# for row in reader:
#     datos.append(row)

# # print("TODOS los datos:")
# # print(datos)

# # FECHA ACTUALIZACION
# lista_fechaActualizacion = []
# for item in datos:
#     lista_fechaActualizacion.append(item[0])
# # print(lista_fechaActualizacion)

# # ID REGISTRO
# lista_idRegistro = []
# for item in datos:
#     lista_idRegistro.append(item[1])
# # print(lista_idRegistro)

# # ORIGEN
# lista_origen = []
# for item in datos:
#     lista_origen.append(item[2])
# # print(lista_origen)

# # SECTOR
# lista_sector = []
# for item in datos:
#     lista_sector.append(item[3])
# # print(lista_sector)

# # ENTIDAD UM (Entidad donde se ubica la unidad médica que brindó la atención)
# lista_entidadUM = []
# for item in datos:
#     lista_entidadUM.append(item[4])
# # print(lista_entidadUM)

# # SEXO
# lista_sexo = []
# for item in datos:
#     lista_sexo.append(item[5])
# # print(lista_sexo)

# # ENTIDAD NAC (Entidad de nacimiento del paciente)
# lista_entidadNAC = []
# for item in datos:
#     lista_entidadNAC.append(item[6])
# # print(lista_entidadNAC)

# # ENTIDAD RES (Entidad de residencia del paciente)
# lista_entidadRES = []
# for item in datos:
#     lista_entidadRES.append(item[7])
# # print(lista_entidadRES)

# # MUNICIPIO RES (Municipio de residencia del paciente)
# lista_municipioRES = []
# for item in datos:
#     lista_municipioRES.append(item[8])
# # print(lista_municipioRES)

# # Tipo Paciente
# lista_tipoPaciente = []
# for item in datos:
#     lista_tipoPaciente.append(item[9])
# # print(lista_tipoPaciente)

# # FECHA INGRESO
# lista_fechaIngreso = []
# for item in datos:
#     lista_fechaIngreso.append(item[10])
# # print(lista_fechaIngreso)

# # FECHA SINTOMAS
# lista_fechaSintomas = []
# for item in datos:
#     lista_fechaSintomas.append(item[11])
# # print(lista_fechaSintomas)

# # FECHA DEFUNCION
# lista_fechaDefuncion = []
# for item in datos:
#     lista_fechaDefuncion.append(item[12])
# # print(lista_fechaDefuncion)

# # INTUBADO
# lista_intubado = []
# for item in datos:
#     lista_intubado.append(item[13])
# # print(lista_intubado)

# # NEUMONIA
# lista_neumonia = []
# for item in datos:
#     lista_neumonia.append(item[14])
# # print(lista_neumonia)

# # EDAD DE PACIENTE
# lista_edad = []
# for item in datos:
#     lista_edad.append(item[15])
# lista_edad.pop(0)
# lista_edad = [int(i) for i in lista_edad]
# # print(lista_edad)

# # NACIONALIDAD (Mexicano o Extranjero)
# lista_nacionalidad = []
# for item in datos:
#     lista_nacionalidad.append(item[16])
# # print(lista_nacionalidad)

# # EMBARAZO
# lista_embarazo = []
# for item in datos:
#     lista_embarazo.append(item[17])
# # print(lista_embarazo)

# # LENGUA INDIGENA
# lista_lenguaIndigena = []
# for item in datos:
#     lista_lenguaIndigena.append(item[18])
# # print(lista_lenguaIndigena)

# # DIABETES
# lista_diabetes = []
# for item in datos:
#     lista_diabetes.append(item[19])
# # print(lista_diabetes)

# # EPOC
# lista_EPOC = []
# for item in datos:
#     lista_EPOC.append(item[20])
# # print(lista_EPOC)

# # ASMA
# lista_asma = []
# for item in datos:
#     lista_asma.append(item[21])
# # print(lista_asma)

# # INMUNOSUPRESION
# lista_INMUSUPR = []
# for item in datos:
#     lista_INMUSUPR.append(item[22])
# # print(lista_INMUSUPR)

# # HIPERTENSION
# lista_hipertension = []
# for item in datos:
#     lista_hipertension.append(item[23])
# # print(lista_hipertension)

# # OTRAS ENFERMEDADES
# lista_otra = []
# for item in datos:
#     lista_otra.append(item[24])
# # print(lista_otra)

# # CARDIOVASCULAR
# lista_cardiovascular = []
# for item in datos:
#     lista_cardiovascular.append(item[25])
# # print(lista_cardiovascular)

# # OBESIDAD
# lista_obesidad = []
# for item in datos:
#     lista_obesidad.append(item[26])
# # print(lista_obesidad)

# # Insuficiencia renal crónica
# lista_renalCronica = []
# for item in datos:
#     lista_renalCronica.append(item[27])
# # print(lista_renalCronica)

# # TABAQUISMO
# lista_tabaquismo = []
# for item in datos:
#     lista_tabaquismo.append(item[28])
# # print(lista_tabaquismo)

# # Otro caso (Si el paciente tuvo contacto con algún otro caso diagnosticado con COVID)
# lista_otroCaso = []
# for item in datos:
#     lista_otroCaso.append(item[29])
# # print(lista_otroCaso)

# # RESULTADO
# lista_resultado = []
# for item in datos:
#     lista_resultado.append(item[30])
# # print(lista_resultado)

# # MIGRANTE
# lista_migrante = []
# for item in datos:
#     lista_migrante.append(item[31])
# # print(lista_migrante)

# # PAIS NACIONALIDAD (Nacionalidad del paciente)
# lista_paisNacionalidad = []
# for item in datos:
#     lista_paisNacionalidad.append(item[32])
# # print(lista_paisNacionalidad)

# # PAIS ORIGEN (País del que partió el paciente rumbo a Mexico)
# lista_paisOrigen = []
# for item in datos:
#     lista_paisOrigen.append(item[33])
# # print(lista_paisOrigen)

# # UCI (Unidad de Cuidados Intensivos)
# lista_UCI = []
# for item in datos:
#     lista_UCI.append(item[34])
# # print(lista_UCI)

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
        self.comboBoxAnalisisDescriptivo.setGeometry(QtCore.QRect(170, 120, 69, 22))
        self.comboBoxAnalisisDescriptivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxAnalisisDescriptivo.setEditable(False)
        self.comboBoxAnalisisDescriptivo.setMinimumContentsLength(1)
        self.comboBoxAnalisisDescriptivo.setObjectName("comboBoxAnalisisDescriptivo")
        self.comboBoxAnalisisDescriptivo.addItem("")
        self.botonAnalisisDescriptivo = QtWidgets.QPushButton(Dialog)
        self.botonAnalisisDescriptivo.setGeometry(QtCore.QRect(250, 120, 161, 23))
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
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")

        # Añadir más elementos al comboBoxAnalisisDescriptivo 
        # self.comboBoxAnalisisDescriptivo.addItem("Hello")

        # Conecta el boton de Obtener Analisis Descriptivo
        self.botonAnalisisDescriptivo.clicked.connect(self.clickAnalisisDescriptivo)

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
        
        if variable == "Edad":
            # Promedio
            average = statistics.mean(data.lista_edad)
            print(average)
            # Imprimir Analisis Descriptivo
            self.output.setText("Promedio " + str(average))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
