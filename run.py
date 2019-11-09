"""
from flask import Flask
app=Flask(__name__)



@app.route('/')
def hello():
	return "<center ><h3> Colossus Static	"


if __name__ == '__main__':
	app.run(debug=True)
"""
import os

import server_reporte as Static
import server_bajos as Static_bajos
import server_generate as Static_gen
import server_load as Static_loader
from flask import Flask
from flask import render_template
from flask import request
app = Flask(import_name=__name__)
@app.route("/")
def inicio():
	return render_template("index.html")
@app.route("/reporte")
def reporte():
	productos=Static.reporte()
	print(productos)
	thetime=os.popen("time /T").read() #"time /Twindows"
	thetime=thetime+"(hora local). "
	return render_template("general.html", horalocal=thetime)
@app.route("/bajos")
def bajo_stock():
	Static_bajos.reporte_bajos()
	thetime=os.popen("time /T").read()
	thetime=thetime+"(hora local). "
	return render_template("bajos.html", horalocal=thetime)
@app.route("/modificar")
def modificar_valores():
	Static_gen.generate()
	thetime=os.popen("time /T").read()
	thetime=thetime+"(hora local). "
	return render_template("modificar.html", horalocal=thetime)

@app.route("/public", methods=["GET","POST"])
def change_status():
    try:
        id_producto=request.form["producto"]
        id_cantidad=request.form["cantidad"]
        if request.form["action"]=="RESTAR":
            id_cantidad=int(id_cantidad)*(-1)
        #bb="producto "+str(id_producto)+" cantidad "+str(id_cantidad)
        response_tuple=Static_loader.load()
        nombres=response_tuple[0]
        producto=response_tuple[1]
        utf8names=[]
        for xd in nombres:
            g=xd.replace("Ã±","ñ")
            utf8names.append(g)
            counter=0
        #sucess=False
        for element in utf8names:
            if element==id_producto:
                print("SE ENCONTRARON COINCIDENCIAS EN EL INVENTARIO")
                #sucess=True
                position=counter
            counter=counter+1
                #return render_template("error_solicitud.html")
        print("#####################")
        print(id_producto)
        print(id_cantidad)
        print(utf8names[position])
        if id_producto==utf8names[position]:
            print("Son Iguales")
        else:
            return "<h1><center> PRODUCTO NO TUVO COINCIDENCIAS EN EL INVENTARIO"
        print("#####################")
        if int(id_cantidad)<0:
            operacion="( RESTA )"
        else:
            operacion="( SUMA )"
        print(operacion)
        if int(producto[position])<0 and operacion=="( RESTA )":
            return "<h1><center> ESTE PRODUCTO ESTÁ AGOTADO NO SE PUEDE RESTAR DEL INVENTARIO <br><a href=/><b> REGRESAR </b></a>"
        anterior=int(producto[position])
        print(anterior)
        print("control_1.1")
        nuevo=int(id_cantidad)
        suma=anterior+nuevo
        if suma<0:
            return "<h1><center> AL INTENTAR RESTAR LAS UNIDADES, NOTAMOS QUE EL PRODUCTO DECIENDE POR DEBAJO DE CERO , INGRESE UNA CANTIDAD VALIDAD <br><a href=modificar ><b> REGRESAR </b></a>"
        print("control_1.2")
        print("control_1.3")
        producto[position]=str(suma)
        longitud=len(nombres)
        ceros=0
        print("control_2")
        data=open("inventario.csv","w")
        data.write("\n")
        data.write("\n")
        data.write("\n")
        while ceros<longitud:
            if nombres[ceros]!="":
                writeable=str(nombres[ceros])+","+str(producto[ceros])
                data.write(writeable)
                print(writeable)
                data.write("\n")
            ceros=ceros+1
        def nuevo_registro(operacion,anterior,nuevo,id_producto):
            file=open("registros.txt","a")
            status="ID = "+str(id_producto)
            status1="Transaccion = "+operacion
            status2="Cambió de "+str(anterior)+" --- A ---> "+str(nuevo)
            hora=os.popen("time /T").read()
            fecha=os.popen("date /T").read()
            file.write("####################################################")
            file.write("\n")
            file.write(hora)
            file.write("\n")
            file.write(fecha)
            file.write("\n")
            file.write(status)
            file.write("\n")
            file.write(status1)
            file.write("\n")
            file.write(status2)
            file.write("\n")
            file.write("####################################################")
            file.write("\n")
            file.close()
            nuevo_registro(operacion,anterior,nuevo,id_producto)
        return render_template("producto.html",id_p=id_producto, id_cant=anterior,nuevas=suma)
    except Exception:
        return "<center> LA SOLICITUD FUE RECHAZADA POR EL SERVIDOR "

#if __name__=="__main__":
app.run(debug = True , port=5000) 
