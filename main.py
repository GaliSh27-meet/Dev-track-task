import flet as ft

def main(page: ft.Page):
    page.title = "Gali's Dev project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TEAL
    page.appbar = ft.AppBar(
    leading=ft.Icon(ft.Icons.MENU),
    title=ft.Text("Gali", color=ft.Colors.PURPLE),
    bgcolor=ft.Colors.BLUE,
    center_title=True,
    actions=[
        ft.IconButton(ft.Icons.NOTIFICATIONS),
        ft.IconButton(ft.Icons.SETTINGS),
    ],
    elevation=4,
)

    title = ft.Text(
        "Gali's First Codealong",
        size= 80,
        weight= ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    main_container =ft.Container(
        content=ft.Column(
            [
                title,
                ft.Divider(),
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing = 10

        ) ,
        padding= 20,
        border_radius=10
        

    )
    


    page.add(main_container)


    


ft.run(main)