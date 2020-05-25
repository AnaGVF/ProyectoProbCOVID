import csv

# DATOS DEL CSV ORGANIZADOS EN LISTAS DEPENDIENDO DE SUS CATEGORIAS

# Se abre el archivo csv
f = open("200518COVID19MEXICO.csv", "r")
reader = csv.reader(f)

# Lista con TODOS los datos (177 134 DATOS)
datos = []

for row in reader:
	datos.append(row)

# print("TODOS los datos:")
# print(datos)

# FECHA ACTUALIZACION
lista_fechaActualizacion = []
for item in datos:
	lista_fechaActualizacion.append(item[0])
# print(lista_fechaActualizacion)

# ID REGISTRO
lista_idRegistro = []
for item in datos:
	lista_idRegistro.append(item[1])
# print(lista_idRegistro)

# ORIGEN
lista_origen = []
for item in datos:
	lista_origen.append(item[2])
lista_origen.pop(0)
lista_origen = [int(i) for i in lista_origen]
lista_origen.sort()
# print(lista_origen)

# SECTOR
lista_sector = []
for item in datos:
	lista_sector.append(item[3])
lista_sector.pop(0)
lista_sector = [int(i) for i in lista_sector]
lista_sector.sort()
# print(lista_sector)

# ENTIDAD UM (Entidad donde se ubica la unidad médica que brindó la atención)
lista_entidadUM = []
for item in datos:
	lista_entidadUM.append(item[4])
lista_entidadUM.pop(0)
lista_entidadUM = [int(i) for i in lista_entidadUM]
lista_entidadUM.sort()
# print(lista_entidadUM)

# SEXO
lista_sexo = []
for item in datos:
	lista_sexo.append(item[5])
lista_sexo.pop(0)
lista_sexo = [int(i) for i in lista_sexo]
lista_sexo.sort()
# print(lista_sexo)

# ENTIDAD NAC (Entidad de nacimiento del paciente)
lista_entidadNAC = []
for item in datos:
	lista_entidadNAC.append(item[6])
lista_entidadNAC.pop(0)
lista_entidadNAC = [int(i) for i in lista_entidadNAC]
lista_entidadNAC.sort()
# print(lista_entidadNAC)

# ENTIDAD RES (Entidad de residencia del paciente)
lista_entidadRES = []
for item in datos:
	lista_entidadRES.append(item[7])
lista_entidadRES.pop(0)
lista_entidadRES = [int(i) for i in lista_entidadRES]
lista_entidadRES.sort()
# print(lista_entidadRES)

# MUNICIPIO RES (Municipio de residencia del paciente)
lista_municipioRES = []
for item in datos:
	lista_municipioRES.append(item[8])
lista_municipioRES.pop(0)
lista_municipioRES = [int(i) for i in lista_municipioRES]
lista_municipioRES.sort()
# print(lista_municipioRES)

# Tipo Paciente
lista_tipoPaciente = []
for item in datos:
	lista_tipoPaciente.append(item[9])
lista_tipoPaciente.pop(0)
lista_tipoPaciente = [int(i) for i in lista_tipoPaciente]
lista_tipoPaciente.sort()
# print(lista_tipoPaciente)

# FECHA INGRESO
lista_fechaIngreso = []
for item in datos:
	lista_fechaIngreso.append(item[10])
# print(lista_fechaIngreso)

# FECHA SINTOMAS
lista_fechaSintomas = []
for item in datos:
	lista_fechaSintomas.append(item[11])
# print(lista_fechaSintomas)

# FECHA DEFUNCION
lista_fechaDefuncion = []
for item in datos:
	lista_fechaDefuncion.append(item[12])
# print(lista_fechaDefuncion)

# INTUBADO
lista_intubado = []
for item in datos:
	lista_intubado.append(item[13])
lista_intubado.pop(0)
lista_intubado = [int(i) for i in lista_intubado]
lista_intubado.sort()
# print(lista_intubado)

# NEUMONIA
lista_neumonia = []
for item in datos:
	lista_neumonia.append(item[14])
lista_neumonia.pop(0)
lista_neumonia = [int(i) for i in lista_neumonia]
lista_neumonia.sort()
# print(lista_neumonia)

# EDAD DE PACIENTE
lista_edad = []
for item in datos:
	lista_edad.append(item[15])
lista_edad.pop(0)
lista_edad = [int(i) for i in lista_edad]
lista_edad.sort()
# print(lista_edad)

# NACIONALIDAD (Mexicano o Extranjero)
lista_nacionalidad = []
for item in datos:
	lista_nacionalidad.append(item[16])
lista_nacionalidad.pop(0)
lista_nacionalidad = [int(i) for i in lista_nacionalidad]
lista_nacionalidad.sort()
# print(lista_nacionalidad)

# EMBARAZO
lista_embarazo = []
for item in datos:
	lista_embarazo.append(item[17])
lista_embarazo.pop(0)
lista_embarazo = [int(i) for i in lista_embarazo]
lista_embarazo.sort()
# print(lista_embarazo)

# LENGUA INDIGENA
lista_lenguaIndigena = []
for item in datos:
	lista_lenguaIndigena.append(item[18])
lista_lenguaIndigena.pop(0)
lista_lenguaIndigena = [int(i) for i in lista_lenguaIndigena]
lista_lenguaIndigena.sort()
# print(lista_lenguaIndigena)

# DIABETES
lista_diabetes = []
for item in datos:
	lista_diabetes.append(item[19])
lista_diabetes.pop(0)
lista_diabetes = [int(i) for i in lista_diabetes]
lista_diabetes.sort()
# print(lista_diabetes)

# EPOC
lista_EPOC = []
for item in datos:
	lista_EPOC.append(item[20])
lista_EPOC.pop(0)
lista_EPOC = [int(i) for i in lista_EPOC]
lista_EPOC.sort()
# print(lista_EPOC)

# ASMA
lista_asma = []
for item in datos:
	lista_asma.append(item[21])
lista_asma.pop(0)
lista_asma = [int(i) for i in lista_asma]
lista_asma.sort()
# print(lista_asma)

# INMUNOSUPRESION
lista_INMUSUPR = []
for item in datos:
	lista_INMUSUPR.append(item[22])
lista_INMUSUPR.pop(0)
lista_INMUSUPR = [int(i) for i in lista_INMUSUPR]
lista_INMUSUPR.sort()
# print(lista_INMUSUPR)

# HIPERTENSION
lista_hipertension = []
for item in datos:
	lista_hipertension.append(item[23])
lista_hipertension.pop(0)
lista_hipertension = [int(i) for i in lista_hipertension]
lista_hipertension.sort()
# print(lista_hipertension)

# OTRAS ENFERMEDADES
lista_otra = []
for item in datos:
	lista_otra.append(item[24])
lista_otra.pop(0)
lista_otra = [int(i) for i in lista_otra]
lista_otra.sort()
# print(lista_otra)

# CARDIOVASCULAR
lista_cardiovascular = []
for item in datos:
	lista_cardiovascular.append(item[25])
lista_cardiovascular.pop(0)
lista_cardiovascular = [int(i) for i in lista_cardiovascular]
lista_cardiovascular.sort()
# print(lista_cardiovascular)

# OBESIDAD
lista_obesidad = []
for item in datos:
	lista_obesidad.append(item[26])
lista_obesidad.pop(0)
lista_obesidad = [int(i) for i in lista_obesidad]
lista_obesidad.sort()
# print(lista_obesidad)

# Insuficiencia renal crónica
lista_renalCronica = []
for item in datos:
	lista_renalCronica.append(item[27])
lista_renalCronica.pop(0)
lista_renalCronica = [int(i) for i in lista_renalCronica]
lista_renalCronica.sort()
# print(lista_renalCronica)

# TABAQUISMO
lista_tabaquismo = []
for item in datos:
	lista_tabaquismo.append(item[28])
lista_tabaquismo.pop(0)
lista_tabaquismo = [int(i) for i in lista_tabaquismo]
lista_tabaquismo.sort()
# print(lista_tabaquismo)

# Otro caso (Si el paciente tuvo contacto con algún otro caso diagnosticado con COVID)
lista_otroCaso = []
for item in datos:
	lista_otroCaso.append(item[29])
lista_otroCaso.pop(0)
lista_otroCaso = [int(i) for i in lista_otroCaso]
lista_otroCaso.sort()
# print(lista_otroCaso)

# RESULTADO
lista_resultado = []
for item in datos:
	lista_resultado.append(item[30])
lista_resultado.pop(0)
lista_resultado = [int(i) for i in lista_resultado]
lista_resultado.sort()
# print(lista_resultado)

# MIGRANTE
lista_migrante = []
for item in datos:
	lista_migrante.append(item[31])
lista_migrante.pop(0)
lista_migrante = [int(i) for i in lista_migrante]
lista_migrante.sort()
# print(lista_migrante)

# PAIS NACIONALIDAD (Nacionalidad del paciente)
lista_paisNacionalidad = []
for item in datos:
	lista_paisNacionalidad.append(item[32])
# print(lista_paisNacionalidad)

# PAIS ORIGEN (País del que partió el paciente rumbo a Mexico)
lista_paisOrigen = []
for item in datos:
	lista_paisOrigen.append(item[33])
# print(lista_paisOrigen)

# UCI (Unidad de Cuidados Intensivos)
lista_UCI = []
for item in datos:
	lista_UCI.append(item[34])
lista_UCI.pop(0)
lista_UCI = [int(i) for i in lista_UCI]
lista_UCI.sort()
# print(lista_UCI)