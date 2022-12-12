import flet
from flet import (
  AppBar,
  ElevatedButton,
  Page,
  Text, 
  View,
  Column, 
  colors,
  Container,
  alignment,
  LinearGradient,
  border_radius,
  padding,
  Image, 
  UserControl,
  Row,
  Icon,
  IconButton,
  margin,
  Card,
  TextButton,
  TextField,
  FilledButton,
  SnackBar,
)

#import is used to send GET/POST requests to the server
import requests

def main(page: Page):
    page.title = 'Routes Example'
    snack = SnackBar(
        Text('Registration Successful!'),
    )

    def GradientGenerator(start, end):
        ColorGradient = LinearGradient(
          begin=alignment.bottom_left,
          end=alignment.top_right,
          colors=[
              start,
              end,
          ],
        )

        return ColorGradient
    def req_register(e, email, password):
        data = {
            'email': email,
            'password': password,
        }
        res = requests.post('https://127.0.0.1:5000/register', json=data)

        if res.status_code == 201:
            snack.open = True
            page.update()
        else:
            snack.content.value = 'You were not registered, please try again.'
            snack.open = True
            page.update()

    def req_login(e, email, password):
        data = {
            'email': email,
            'password': password,
        }

        res = requests.post('https://127.0.0.1:5000/login', json=data)

        if res.status_code == 201:

          page.views.append(
              View(
                  f'/{email}',
                  horizontal_alignment='center',
                  vertical_alignment='center',
                  controls=[
                      Column(
                          alignment='center',
                          horizontal_alignment='center',
                          controls=[
                              Text(
                                  'Successfully Logged in',
                                  size=44,
                                  weight='w700',
                                  text_align='center',
                              ),
                              Text(
                                  f'Login Information:\nEmail: {email}\nPassword: {password}',
                                  size=32,
                                  weight='w500',
                                  text_align='center',
                              ),
                          ],
                        
                      ),
                  ],
              )
          )
        else:
          snack.content.value = 'Could not log in! Try again.'
          snack.open = True
          page.update()

    def route_change(route):
        email = TextField(
            label='Email',
            border='underline',
            width=320,
            text_size=14,
            color='white',
        )

        password = TextField(
            label="Password",
            border='underline',
            width=320,
            text_size=14,
            password=True,
            color='white',
            can_reveal_password=True,
        )

        page.views.clear()
        #Working with views, each page will be a seperate view, IE login page, registration ect...

        #Registration Page
        page.views.append(
            View(
                '/register',
                horizontal_alignment='center',
                vertical_alignment='center',
                controls=[
                    Column(
                        alignment='center',
                        controls=[
                            Card(
                                elevation=15,
                                content=Container(
                                    width=290,
                                    height=590,
                                    padding=padding.all(30),
                                    gradient=GradientGenerator('#1f2937', '#111827'),
                                    border_radius=border_radius.all(12),
                                    content=Column(
                                        horizontal_alignment='center',
                                        alignment='start',
                                        controls=[
                                            Text(
                                                'HuniDew Task App!',
                                                size=32,
                                                weight='w700',
                                                text_align='center',
                                                color='White',
                                            ),
                                            Text(
                                                'Please Login Below or Click Register!',
                                                size=14,
                                                weight='w700',
                                                text_align='center',
                                                color='#64748b',
                                            ),
                                            Container(padding=padding.only(bottom=20)),
                                            email,
                                            Container(padding=padding.only(bottom=10)),
                                            password,
                                            Container(padding=padding.only(bottom=20)),
                                            Row(
                                                alignment='center',
                                                spacing=3,
                                                controls=[
                                                    FilledButton(
                                                        content=Text(
                                                            'register',
                                                            weight='w700',
                                                        ),
                                                        width=120,
                                                        height=30,

                                                        on_click=lambda e: req_register(
                                                            e,
                                                            email.value,
                                                            password.value,
                                                        ),
                                                    ),
                                                    FilledButton(
                                                        content=Text(
                                                            'Login',
                                                            weight='w700',
                                                        ),
                                                        width=120,
                                                        height=30,
                                                        on_click=lambda __: page.go(
                                                            '/login'
                                                        ),

                                                    ),
                                                    snack,
                                              

                                                ],
                                            ),
                                            
                                        ],
                                    ),

                                ),

                            ),
                        ],
                    ),
                ],
            )
        )

        if page.route == '/login':
            page.views.append(
                View(
                    '/login',
                    horizontal_alignment='center',
                    vertical_alignment='center',
                    controls=[
                        Column(
                            alignment='center',
                            controls=[
                                Card(
                                    elevation=15,
                                    content=Container(
                                        width=290,
                                        height=590,
                                        padding=padding.all(30),
                                         gradient=GradientGenerator('#1f2937', '#111827'
                                        ),
                                        border_radius=border_radius.all(12),
                                        content=Column(
                                            horizontal_alignment='center',
                                            alignment='start',
                                            controls=[
                                                Text(
                                                    'HuniDew Registration Page',
                                                    size=32,
                                                    weight='w700',
                                                    text_align='center',
                                                    color='white'
                                                ),
                                                Text(
                                                'Please enter your email and password below to register!',
                                                size=14,
                                                weight='w700',
                                                text_align='center',
                                                color='#64748b',
                                                ),
                                                Container(
                                                    padding=padding.only(bottom=20)
                                                ),
                                                email,
                                                Container(
                                                    padding=padding.only(bottom=10)
                                                ),
                                                password,
                                                Container(
                                                    padding=padding.only(bottom=20)
                                                ),
                                                Row(
                                                    alignment='center',
                                                    spacing=3,
                                                    controls=[
                                                        FilledButton(
                                                            content=Text(
                                                                'Login',
                                                                weight='w700',
                                                            ),
                                                            width=120,
                                                            height=30,
                                                            on_click=lambda e: req_login(
                                                                e,
                                                                email.value,
                                                                password.value,
                                                            ),

                                                        ),
                                                        FilledButton(
                                                            content=Text(
                                                                'Complete',
                                                                weight='w700',   
                                                            ),
                                                            width=120,
                                                            height=30,
                                                            on_click=lambda __: page.go(
                                                                '/register'
                                                            ),
                                                        ),
                                                        snack,

                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),

                                ),
                            ],

                        ),
                    ],
                )
            )
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1] 
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main)

#host='localhost', port=5000, view=flet