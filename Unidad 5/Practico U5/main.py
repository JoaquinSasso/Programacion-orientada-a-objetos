from flask import Flask, request, render_template, redirect, session, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

import datetime
app = Flask(__name__)
app.config.from_pyfile("config.py")
from models import Paquete, Repartidor, Transporte, Sucursal, db
db.init_app(app)
@app.route("/")
def elegir_sucursal():
   return render_template("elegir-sucursal.html", sucursales = Sucursal.query.order_by(Sucursal.numero).all())

@app.route("/set_sucursal", methods=["POST"])
def set_sucursal():
   if request.method == "POST":
      session["sucursal_id"] = request.form["sucursal"]
   return redirect("/home")
 
@app.route("/home", methods=["GET", "POST"])
def home():
   if "sucursal_id" not in session:
        return redirect("/")
   return render_template("inicio.html")

@app.route("/registrar_paquete", methods=["GET", "POST"])
def registrar_paquete():
   if "sucursal_id" not in session:
      return redirect("/")
   sucursales = Sucursal.query.order_by(Sucursal.numero).all()
   if request.method == "POST":
      try:
         nuevo_paquete = Paquete(
            numeroenvio= 1000 + ((Paquete.query.count() + 2) * 10),
            peso=request.form["peso"],
            nomdestinatario = request.form["nomdestinatario"],
            dirdestinatario = request.form["dirdestinatario"],
            idsucursal=session["sucursal_id"],
            entregado = False
         )
         db.session.add(nuevo_paquete)
         db.session.commit()
         flash("Paquete registrado exitosamente")
      except Exception as e:
         db.session.rollback()
         flash(f"Error al registrar el paquete: {str(e)}")
      return redirect("/home")
   return render_template("registrar-paquete.html", sucursales=sucursales)

@app.route("/seleccionar_sucursal_destino", methods=["GET", "POST"])
def seleccionar_sucursal_destino():
    if request.method == "POST":
        sucursal_id = request.form.get("sucursal")
        return redirect(f"/registrar_transporte/{sucursal_id}")
    sucursales = Sucursal.query.filter(Sucursal.id != session["sucursal_id"]).order_by(Sucursal.numero).all()
    return render_template("seleccionar_sucursal_destino.html", sucursales=sucursales)

@app.route("/registrar_transporte/<int:sucursal_destino_id>", methods=["GET", "POST"])
def registrar_transporte(sucursal_destino_id):
   if request.method == "POST":
      try:
         paquete_ids = request.form.getlist("paquete")
         if paquete_ids == []:
            raise IndexError
         numerotransporte = Transporte.query.count() + 1
         fechahorasalida = datetime.datetime.now()

         nuevo_transporte = Transporte(
               numerotransporte=numerotransporte,
               fechahorasalida=fechahorasalida,
               fechahorallegada=None,
               idsucursal=sucursal_destino_id
         )
         db.session.add(nuevo_transporte)
         db.session.commit()

         for paquete_id in paquete_ids:
               nuevo_paquete : Paquete
               nuevo_paquete = Paquete.query.get(paquete_id)
               nuevo_paquete.idtransporte = nuevo_transporte.id
         db.session.commit()
         flash("Transporte registrado con exito.")
      except IndexError:
         flash("No hay paquetes que asignados al transporte")
      except Exception as e:
         flash(f"Hubo un error al registrar el transporte")
      finally:
         return redirect("/home")
   paquetes = Paquete.query.filter_by(idsucursal=session["sucursal_id"], entregado=False, idtransporte=None).all()
   return render_template("registrar_transporte.html", sucursal_id=sucursal_destino_id, paquetes=paquetes)

@app.route("/registrar_llegada", methods=["GET", "POST"])
def registrar_llegada():
   sucursal_id = session.get("sucursal_id")
   if not sucursal_id:
        flash("No se ha seleccionado una sucursal")
        return redirect("/seleccionar_sucursal")

   if request.method == "POST":
      try:
         transporte_ids = request.form.getlist("transporte")
         if transporte_ids == []:
            raise IndexError
         fechahorallegada = datetime.datetime.now()

         for transporte_id in transporte_ids:
            transporte: Transporte
            transporte = Transporte.query.get(transporte_id)
            if transporte and transporte.fechahorallegada is None:
               transporte.fechahorallegada = fechahorallegada
               paquetes : list[Paquete]
               paquetes = Paquete.query.filter_by(idtransporte = transporte.id)
               for paquete in paquetes:
                  paquete.idsucursal = transporte.idsucursal
                  paquete.idtransporte = None

         db.session.commit()
         
         flash("Llegada registrada con exito")
      except IndexError:
         flash("No se selecciono ningun transporte")
      except Exception as e:
         db.session.rollback()
         flash(f"Hubo un error al registrar la llegada{str(e)}")
      finally:
         return redirect("/home")
    
   transportes = Transporte.query.filter_by(idsucursal=sucursal_id, fechahorallegada=None).all()
   return render_template("registrar_llegada.html", transportes=transportes)


if __name__ == "__main__":
   with app.app_context():
      db.create_all()
   app.run(debug=True)