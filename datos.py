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
# print(lista_origen)

# SECTOR
lista_sector = []
for item in datos:
	lista_sector.append(item[3])
# print(lista_sector)

# ENTIDAD UM (Entidad donde se ubica la unidad médica que brindó la atención)
lista_entidadUM = []
for item in datos:
	lista_entidadUM.append(item[4])
# print(lista_entidadUM)

# SEXO
lista_sexo = []
for item in datos:
	lista_sexo.append(item[5])
# print(lista_sexo)

# ENTIDAD NAC (Entidad de nacimiento del paciente)
lista_entidadNAC = []
for item in datos:
	lista_entidadNAC.append(item[6])
# print(lista_entidadNAC)

# ENTIDAD RES (Entidad de residencia del paciente)
lista_entidadRES = []
for item in datos:
	lista_entidadRES.append(item[7])
# print(lista_entidadRES)

# MUNICIPIO RES (Municipio de residencia del paciente)
lista_municipioRES = []
for item in datos:
	lista_municipioRES.append(item[8])
# print(lista_municipioRES)

# Tipo Paciente
lista_tipoPaciente = []
for item in datos:
	lista_tipoPaciente.append(item[9])
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
# print(lista_intubado)

# NEUMONIA
lista_neumonia = []
for item in datos:
	lista_neumonia.append(item[14])
# print(lista_neumonia)

# EDAD DE PACIENTE
lista_edad = []
for item in datos:
	lista_edad.append(item[15])
lista_edad.pop(0)
lista_edad = [int(i) for i in lista_edad]
# print(lista_edad)

# NACIONALIDAD (Mexicano o Extranjero)
lista_nacionalidad = []
for item in datos:
	lista_nacionalidad.append(item[16])
# print(lista_nacionalidad)

# EMBARAZO
lista_embarazo = []
for item in datos:
	lista_embarazo.append(item[17])
# print(lista_embarazo)

# LENGUA INDIGENA
lista_lenguaIndigena = []
for item in datos:
	lista_lenguaIndigena.append(item[18])
# print(lista_lenguaIndigena)

# DIABETES
lista_diabetes = []
for item in datos:
	lista_diabetes.append(item[19])
# print(lista_diabetes)

# EPOC
lista_EPOC = []
for item in datos:
	lista_EPOC.append(item[20])
# print(lista_EPOC)

# ASMA
lista_asma = []
for item in datos:
	lista_asma.append(item[21])
# print(lista_asma)

# INMUNOSUPRESION
lista_INMUSUPR = []
for item in datos:
	lista_INMUSUPR.append(item[22])
# print(lista_INMUSUPR)

# HIPERTENSION
lista_hipertension = []
for item in datos:
	lista_hipertension.append(item[23])
# print(lista_hipertension)

# OTRAS ENFERMEDADES
lista_otra = []
for item in datos:
	lista_otra.append(item[24])
# print(lista_otra)

# CARDIOVASCULAR
lista_cardiovascular = []
for item in datos:
	lista_cardiovascular.append(item[25])
# print(lista_cardiovascular)

# OBESIDAD
lista_obesidad = []
for item in datos:
	lista_obesidad.append(item[26])
# print(lista_obesidad)

# Insuficiencia renal crónica
lista_renalCronica = []
for item in datos:
	lista_renalCronica.append(item[27])
# print(lista_renalCronica)

# TABAQUISMO
lista_tabaquismo = []
for item in datos:
	lista_tabaquismo.append(item[28])
# print(lista_tabaquismo)

# Otro caso (Si el paciente tuvo contacto con algún otro caso diagnosticado con COVID)
lista_otroCaso = []
for item in datos:
	lista_otroCaso.append(item[29])
# print(lista_otroCaso)

# RESULTADO
lista_resultado = []
for item in datos:
	lista_resultado.append(item[30])
# print(lista_resultado)

# MIGRANTE
lista_migrante = []
for item in datos:
	lista_migrante.append(item[31])
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
# print(lista_UCI)