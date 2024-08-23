import flet as ft

def main(page: ft.Page):
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_visibility=False,
            thumb_visibility=True,
            thumb_color={
                ft.MaterialState.HOVERED: ft.colors.BLACK,
                ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
            },
            thickness=5,
            radius=15,
            main_axis_margin=5,
            cross_axis_margin=5,
        )
    )

    def go_to_next_page(e):
        page.go("/next")
    def go_to_home_page(e):
        page.go("/")

    # AppBar with proper spacing and alignment
    appbar = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text("CVmaker", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=20),
                    alignment=ft.alignment.center_left,
                    margin=ft.margin.only(left=10),
                    height=55
                ),
                
                ft.Container(
                    content=ft.TextButton("HOME", icon="HOME", icon_color=ft.colors.WHITE, style=ft.ButtonStyle(color=ft.colors.WHITE),on_click=go_to_home_page),
                    alignment=ft.alignment.center_left,
                    margin=ft.margin.only(left=5),
                    height=55
                ),
                
                ft.Container(
                    content=ft.TextButton("My CV", icon="ASSIGNMENT", icon_color=ft.colors.WHITE, style=ft.ButtonStyle(color=ft.colors.WHITE),on_click=go_to_next_page),
                    alignment=ft.alignment.center_left,
                    margin=ft.margin.only(left=15),
                    height=55,
                )
            ],
            expand=True
        ),
        leading_width=200,
        center_title=False,
        bgcolor="#50c7eb",
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        ],
    )

    def build_main_body():
        return ft.ListView([ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        col={"sm": 12, "md": 6, "xl": 6},
                        padding=ft.padding.all(20),
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Image(src="avatar.jpg", height=100, width=100, border_radius=10),
                                        ft.Column(
                                            controls=[
                                                ft.Text("সিভি বানান", weight=ft.FontWeight.BOLD, size=45, color=ft.colors.BLACK),
                                                ft.Text("এখন মুহূর্তের মধ্যে", weight=ft.FontWeight.BOLD, size=25, color=ft.colors.BLACK),
                                            ]
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    content=ft.TextButton("Get Start", width=120, height=40, on_click=go_to_next_page, style=ft.ButtonStyle(bgcolor="#0067ff", color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10))),
                                    margin=ft.margin.only(top=20),
                                    alignment=ft.alignment.center_left,
                                ),
                                ft.Text("AI ব্যাবহার করে বানান নিজের সিভি", weight=ft.FontWeight.BOLD, size=15, color=ft.colors.BLACK),
                                ft.Row(
                                    controls=[
                                        ft.IconButton(icon=ft.icons.FACEBOOK, icon_color="#0067ff"),
                                        ft.IconButton(icon=ft.icons.MESSAGE, icon_color="#0067ff"),
                                        ft.IconButton(icon=ft.icons.LINK, icon_color="#0067ff"),
                                    ]
                                ),
                                ft.Container(
                                bgcolor="#f4c552",
                                border_radius=10,
                                
                                content=ft.ResponsiveRow(
                                    [
                                        
                                        ft.Lottie(
                                            src='lottie.json',
                                            repeat=True,
                                            reverse=False,
                                            animate=True,
                                            col={"sm": 12, "md": 6, "xl": 6},
                                            
                                    ),
                                        ft.Container(
                                            content=ft.Column([
                                            ft.Text("হেল্প লাগলে আমাদের",weight=ft.FontWeight.BOLD,color=ft.colors.WHITE,size=20),
                                            ft.Text("Expert দের সাথে কথা বলেন ",weight=ft.FontWeight.BOLD,color=ft.colors.WHITE,size=15),
                                            ft.FloatingActionButton(icon=ft.icons.ADD)
                                        ],
                                        
                                        ),
                                        margin=ft.margin.only(top=10,left=15,bottom=10),
                                        col={"sm": 12, "md": 6, "xl": 6},
                                        )
                                    ],
                                    expand=True
                                    
                                )
                            )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        border_radius=10,
                    ),
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        col={"sm": 12, "md": 6, "xl": 6},
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Text("বিশ্বাস এখন আপনার হাতে", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, size=20),
                                    margin=ft.margin.only(top=10),
                                    alignment=ft.alignment.top_center
                                ),
                                ft.Image(src="banner.png", border_radius=10, animate_offset=True)
                            ]
                        ),
                        border_radius=10,
                    )
                ],
                spacing=10,
            ),
            expand=True
        )],
        expand=True,
        on_scroll=True
    )

    def build_next_page():
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Welcome to the Next Page", size=30),
                    ft.Text("This is the new page after clicking Get Start.", size=20),
                    # Add more content here as needed
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True
        )

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [build_main_body()], appbar=appbar)
            )
        elif page.route == "/next":
            page.views.append(
                ft.View("/next", [build_next_page()], appbar=appbar)
            )
        page.update()

    page.appbar = appbar
    page.on_route_change = route_change
    page.go("/")

ft.app(target=main, assets_dir="assets")
