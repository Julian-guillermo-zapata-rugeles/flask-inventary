def generate():
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
	elementos=nombres
	x=open("static/base").read()
	x=x.split("<!--@-->")
	newfile=open("templates/modificar.html","w")
	newfile.write(x[0])
	newfile.write("\n")
	for xd in elementos:
		if xd !="":
			writeable="<option>"+xd+"</option>"
			newfile.write(writeable)
			newfile.write("\n")
	newfile.write(x[2])
	newfile.write("\n")
	newfile.close()
