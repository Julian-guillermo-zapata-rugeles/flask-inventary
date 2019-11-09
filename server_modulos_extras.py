"""
Funciones del programa

julian Rugeles
2019
public static Version 1
"""

import os
import time
import sys
import generate as gen
""" Incio del programa """

def cls():

	""" limpiar la consola """

	os.system("cls")

def menu():
	""" Inciar el menu """


	print(open("menu").read())
	condicion=False
	eventos=["1","2","admin"]
	while condicion==False:
		opcion=str(input("opcion > "))
		if opcion in eventos:
			condicion=True
	return opcion

def loadInformation():
	"""Leer la informacion Presente en el archivo Inventario.cvs"""


	load=open("inventario.csv").read()
	separate=load.split("\n")
	inicio=int(0)
	nombres=[]
	precios=[]
	for element in separate:
		if inicio>2:
			try:
				element_sep=element.split(",")
				nombres.append(element_sep[0])
				precios.append(element_sep[1])
			except Exception as e:
				pass
		inicio=inicio+1
	#gen.generar(nombres)
	#os.system("firefox index.html")
	return precios , nombres


def reporteciclico(tuplas):
	precios_originales=tuplas[0]
	nombres_originales=tuplas[1]
	load=open("inventario.csv").read()
	separate=load.split("\n")
	inicio=int(0)
	nombres=[]
	precios=[]
	for element in separate:
		if inicio>2:
			try:
				element_sep=element.split(",")
				nombres.append(element_sep[0])
				precios.append(element_sep[1])
			except Exception as e:
				pass
		inicio=inicio+1
	cls()
	if precios_originales != precios:
		if len(precios_originales)!= len(precios):
			return True
		print(precios_originales)
		print(precios)
		contador=len(precios)
		start=4
		cero=0
		notificacion=""
		sendok=0
		while cero<contador:
			if 0==0:

			#if precios_originales[cero] != precios[cero]:
				if int(precios[cero]) <10:
					concatenable=str(start)+") "+str(nombres_originales[cero])+" cambio de "+str(precios_originales[cero])+" --> "+str(precios[cero])+"\n"
					notificacion=notificacion+concatenable
					sendok=sendok+1
			cero=cero+1
			start=start+1
		cls()
		print("--->  Analizando la el contenido del inventario ")
		time.sleep(3)
		print("--->  Generado Reporte Sobre los Cambios En la Bodega")
		time.sleep(1)
		#mensaje="telegram-send '"+notificacion+"'"() ONLY GNU LINUX TELEGRAM-CLIENT
		sendMessage=False
		while sendMessage==False:
			try:
				import requests
				print("--->  validando la conexion a internet ")
				time.sleep(2)
				response=requests.get("https://www.google.com")
				if response.status_code == 200:
					print('--->  El equipo se Encuentra Conectado a la Red!')
					time.sleep(1)
					print("---> OK ")
					time.sleep(2)
					if sendok>0:
						static_index=open("productos_bajos.txt","w")
						static_index.write(notificacion)
						static_index.close()
						sendok=0
					else:
						print("---> Se detectaron Cambios Pero no Productos con existencias BAJAS")
						print("---> Se generará la actualizacion para los reportes Generales")
						print("---> Un momento ...")
						time.sleep(3)
					sendMessage=True
			except Exception as e:
				print("---> No se pudo establecer una conexion A internet (ALERTA)")
				print("---> Se reintentará operacion en 10 segundos")
				print("---> Un momento...")
				time.sleep(10)
		print("OK!!  completado")
		time.sleep(1)
		print("Msg :  Actualizando Inventario Localmente.")
		time.sleep(5)
		return True
	else:
	#	try:
	#		import requests
	#		response=requests.get("https://www.google.com")
	#		if response.status_code == 200:
	#			print("Status : EN LINEA  (Conectado a Internet)")
	#	except Exception as e:
	#		print("Status : DESCONECTADO (sin conexion a Internet)")
		print("#################################################")
		print("    Esperando por Cambios en el Inventario")
		print("")
		print("Intervalos de 10 segundos")
		print("Hora :")
		print("OMITIDO")
		print("#################################################")
		time.sleep(10)
		return False
def reporte():
	cls()
	load=open("inventario.csv").read()
	separate=load.split("\n")
	inicio=int(0)
	nombres=[]
	precios=[]
	for element in separate:
		if inicio>2:
			try:
				element_sep=element.split(",")
				nombres.append(element_sep[0])
				precios.append(element_sep[1])
			except Exception as e:
				pass
		inicio=inicio+1
	contador=len(precios)
	start=4
	cero=0
	emptyfile=""
	while cero<contador:
		concatenable="<tr> \n<th>"+ str(start)+") "+str(nombres[cero])+"</th>\n"+"</tr>\n"
		emptyfile=emptyfile+concatenable
		cero=cero+1
		start=start+1

	#while cero<contador:
	#	concatenable=str(start)+") "+str(nombres[cero])+" --> "+str(precios[cero])+"\n"
	#	notificacion=notificacion+"-------------- \n"
	#	notificacion=notificacion+concatenable
	#	cero=cero+1
	#	start=start+1
	cls()
	print("--->  Generando Reporte")
	time.sleep(1)
	print("--->  Generado !")
	time.sleep(1)
	sendMessage=False
	while sendMessage==False:
		try:
			import requests
			"""
			print("--->  validando Conexion a Internet ...")
			time.sleep(1)
			response=requests.get("https://www.google.com")"""
			if 0==0:
				static_index=open("reporte_general.html","w")
				void=open("templates2.void").read()
				static_index.write(void)
				static_index.write(emptyfile)
				static_index.close()
				sendMessage=True
		except Exception as e:
			print("Conexion Inestable... Esperando 5 segundos para reintentar")
			time.sleep(5)
	print("notificacion Enviada exitosamente")
	exit()
