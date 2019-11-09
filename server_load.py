def load():
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
	return nombres , precios
