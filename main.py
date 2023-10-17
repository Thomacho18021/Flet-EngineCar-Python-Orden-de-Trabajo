import flet as ft
from flet import *


def main(page: ft.Page):

    def add_clicked(e):
        page.add(
            ft.Text(
                "Vehiculo Nuevo:\n"
                + patente.value +
                "\n"+marca.value +
                "\n"+modelo.value +
                "\n"+year.value +
                "\n"+combustible.value +
                "\n"+kilometraje.value +
                "\n"+numeroorden.value))
        patente.value = ""
        marca.value = ""
        modelo.value = ""
        year.value = ""
        combustible.value = ""
        kilometraje.value = ""
        page.update()

    patente = ft.TextField(label="Patente", max_length=6,
                           col={"md": 2})
    marca = ft.TextField(label="Marca", col={"md": 2})
    modelo = ft.TextField(label="Modelo", col={"md": 2})
    year = ft.Dropdown(label="Año", options=[
        ft.dropdown.Option("2000"),
        ft.dropdown.Option("2001"),
        ft.dropdown.Option("2002"),
        ft.dropdown.Option("2003"),
        ft.dropdown.Option("2004"),
        ft.dropdown.Option("2005"),
        ft.dropdown.Option("2006"),
        ft.dropdown.Option("2007"),
        ft.dropdown.Option("2008"),
        ft.dropdown.Option("2009"),
        ft.dropdown.Option("2010")
    ],
        col={"md": 2})
    combustible = ft.Dropdown(label="Combustible", options=[
        ft.dropdown.Option("Bencina"),
        ft.dropdown.Option("Diesel"),
        ft.dropdown.Option("Electrico")
    ],
        col={"md": 2})

    kilometraje = ft.TextField(label="Kilometraje", col={
                               "md": 2})

    numeroorden = ft.TextField(
        label="N° Orden", read_only=True, value=str(), col={"md": 3})

    # General
    cbDoc = ft.Checkbox(label="Documentos", value=False)
    cbGPS = ft.Checkbox(label="GPS", value=False)
    cbChaleco = ft.Checkbox(label="Chaleco", value=False)
    cbPlacas = ft.Checkbox(label="Placas", value=False)
    cbTAG = ft.Checkbox(label="TAG", value=False)

    # Seguridad

    cbBotiquin = ft.Checkbox(label="Botiquin", value=False)
    cbExtintor = ft.Checkbox(label="Extintor", value=False)
    cbBarAntivuelco = ft.Checkbox(label="Barra Antivuelco", value=False)
    cbRuedaRepuesto = ft.Checkbox(label="Rueda Repuesto", value=False)
    cbBarraInterna = ft.Checkbox(label="Barra Interna", value=False)
    cbTriangulo = ft.Checkbox(label="Triangulo", value=False)
    cbGata = ft.Checkbox(label="Gata", value=False)
    cbLlaveRepuesto = ft.Checkbox(label="Llave Repuesto", value=False)

    # Niveles y Luces

    cbAceiteMotor = ft.Checkbox(label="Aceite Motor", value=False)
    cbNeumaticos = ft.Checkbox(label="Neumáticos", value=False)
    cbAguaLimpiaparabrisas = ft.Checkbox(
        label="Agua LimpiaParabrisas", value=False)
    cbRefrigerante = ft.Checkbox(label="Refrigerante", value=False)
    cbLuces = ft.Checkbox(label="Luces", value=False)
    cbFrenos = ft.Checkbox(label="Frenos", value=False)
    cbSenalizadoras = ft.Checkbox(label="Señalizadores", value=False)

    # Adicionales
    cbCableAcero = ft.Checkbox(label="Cable Acero", value=False)
    cbParrilla = ft.Checkbox(label="Parrilla", value=False)
    cbLonaPickUp = ft.Checkbox(label="Lona Pick Up", value=False)
    cbSillaBebe = ft.Checkbox(label="Silla Bebé", value=False)
    cbNeumaticoAdicional = ft.Checkbox(
        label="Neumático Adicional", value=False)
    cbOtros = ft.Checkbox(label="Otros", value=False)
    txtOtro = ft.TextField(label="Otros")

    page.appbar = ft.AppBar(
        title=ft.Text("Engine Car"),
        center_title=True,
        elevation=4
    )

    page.add(
        ft.ResponsiveRow([
            patente, year, marca, modelo, combustible, kilometraje
        ]),
        ft.ResponsiveRow([
            ft.Column([
                ft.Text("General"),
                cbDoc,
                cbChaleco,
                cbGPS,
                cbPlacas,
                cbTAG
            ], col={"md": 3}),

            ft.Column([
                ft.Text("Seguridad"),
                cbBotiquin,
                cbExtintor,
                cbBarAntivuelco,
                cbRuedaRepuesto,
                cbBarraInterna,
                cbTriangulo,
                cbGata,
                cbLlaveRepuesto
            ], col={"md": 3}),

            ft.Column([
                ft.Text("Niveles y Luces"),
                cbAceiteMotor,
                cbNeumaticos,
                cbAguaLimpiaparabrisas,
                cbRefrigerante,
                cbLuces,
                cbFrenos,
                cbSenalizadoras
            ], col={"md": 3}),

            ft.Column([
                ft.Text("Adicionales"),
                cbCableAcero,
                cbParrilla,
                cbLonaPickUp,
                cbSillaBebe,
                cbNeumaticoAdicional,
                cbOtros,
                txtOtro
            ], col={"md": 3})


        ]),
        ft.ResponsiveRow([ft.ElevatedButton(
            text="Guardar", on_click=add_clicked)])

    )

    page.add(ft.ResponsiveRow([ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Patente")),
            ft.DataColumn(ft.Text("Marca")),
            ft.DataColumn(ft.Text("Modelo")),
            ft.DataColumn(ft.Text("Año")),
            ft.DataColumn(ft.Text("Combustible")),
            ft.DataColumn(ft.Text("Kilometraje")),
            ft.DataColumn(ft.Text("Fecha y Hora")),
            ft.DataColumn(ft.Text("N° Orden"))
        ],
        rows=[
        ],
        border_radius=10,
        bgcolor="grey"
    )]))


ft.app(target=main)
