def reporte():
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
			except Exception:
				pass
		inicio=inicio+1
	contador=len(precios)

	start=4
	cero=0
	emptyfile=""
	while cero<contador:
		concatenable="<tr> \n<th>"+ str(start)+") "+str(nombres[cero])+"</th>"+"<th>"+str(precios[cero])+"</th>\n"+"</tr>\n"
		emptyfile=emptyfile+concatenable
		cero=cero+1
		start=start+1
	sendMessage=False
	while sendMessage==False:
		try:
			if 0==0:
				static_index=open("templates/general.html","w")
				void=open("static/templates2.void").read()
				static_index.write(void)
				static_index.write(emptyfile)
				static_index.close()
				sendMessage=True
		except Exception:
			pass
