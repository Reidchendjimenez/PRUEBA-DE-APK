import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Control"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    def on_click_registrar(e):
        if not input_nombre.value:
            input_nombre.error_text = "Falta el nombre"
        else:
            lista_registros.controls.insert(0, ft.Text(f"✅ {input_nombre.value} - Registrado", color="green"))
            input_nombre.value = ""
        page.update()

    input_nombre = ft.TextField(label="Nombre del Personal", width=300)
    lista_registros = ft.Column()

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("CONTROL DE ACCESO", size=30, weight="bold"),
                input_nombre,
                ft.ElevatedButton("REGISTRAR ENTRADA", on_click=on_click_registrar, icon=ft.icons.ADD_TASK),
                ft.Divider(),
                ft.Text("Historial Reciente:", size=20),
                lista_registros
            ]),
            padding=20
        )
    )

# ESTO ES LO IMPORTANTE:
# view=ft.AppView.WEB_BROWSER permite que Codespaces te dé el link automáticamente
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)