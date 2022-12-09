from flet import flet, Page, Column, Row, Container, padding, alignment, LinearGradient, popup_menu_button, animation, control, Text


def main(page: Page):

 #Main Container
  _home = Container(
     width=290,
     height=590,
     bgcolor='black',
     padding=8,
     border_radius=35, 
     alignment=alignment.center,
    )

  #Main Column

  _home_column = Column(
    spacing=2, 
    scroll='auto', 
    alignment='start'
  )
  page.add(_home)
  page.update()
  
flet.app(target=main)