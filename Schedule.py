from flet import flet, Page, Column, Row, Container, padding, alignment, LinearGradient, popup_menu_button, animation, control, Text
from datetime import date
import calendar
obj = calendar.Calendar()

#Login page


#Calendar

def main(page: Page):

  #Dictionary to store the dates
  _content_dic ={}


  #datetime to get the current date so we can find it by default
  _year_now = int(date.today().strftime('%Y'))
  _month_now = int(date.today().strftime('%m'))
  _day_now = int(date.today().strftime('%d'))

#Highlight dates 
  def _highlight_date(e):
      if e.control.bgcolor == 'blue900':
       pass
      else:
          if e.data =='true':
              e.control.bgcolor = 'white10'
              e.control.update()
          else:
              e.control.bgcolor = '#0c0f16'
              e.control.update()

#Task Entry
  def _create_entry(e):
      _content_column.controls.append(
          Row(
              controls=[
                  Container(
                      border_radius=8,
                      padding=12,
                      expand=True,
                      gradient=LinearGradient(
                          begin=alignment.center_left,
                          end=alignment.center_right,
                          colors=['blue900', 'shadow'],
                      ),
                      content=Text(
                          f'You have a task on\n{e.control.data}',
                          size=10, color='white70'
                      ),
                  ),
              ]

          )
      )

      _content_column.update()
      

  def _popup(e):
      _title.visible = False
      _title.update()
      if e.control.height != _main.height * 0.55:
          e.control.height = _main.height * 0.55
          e.control.update()
          #when expanded, cal is shown
          for key in _content_dic:
              for month in _content_dic[key]:
                if month == _month_now and key == _year_now:
                  _content_dic[key][month].visible = True
                  _content_dic[key][month].update()


      else:
          e.control.height = _main.height * 0.13
          e.control.update()
          #when expanded, cal is shown
          for key in _content_dic:
              for month in _content_dic[key]:
                if month == _month_now and key == _year_now:
                  _content_dic[key][month].visible = False
                  _content_dic[key][month].update()

          _title.visible = True
          _title.update()
        
      pass


  #Main Container
  _main = Container(
     width=290,
     height=590,
     bgcolor='black',
     padding=8,
     border_radius=35, 
     alignment=alignment.center,
    )

  #Main Column

  _main_column = Column(
    spacing=2, 
    scroll='auto', 
    alignment='start'
  )

  #Calendar Container
  _calendar_container = Container(
      width=_main.width, 
      height=_main.height * 0.13,
      gradient=LinearGradient(
          begin=alignment.bottom_left,
          end=alignment.bottom_left,
          colors=['#1e293b', '#0f172a'],
      ),
      border_radius=30,
      alignment=alignment.center,
      on_click=lambda e: _popup(e),
      animate=animation.Animation(duration=320, curve='develerate')
  )



  _calendar_container.content = _main_column

#
  _title = Container(
    content=Text(
      'SCHEDULE', color='White70', weight='bold'

    )
)

#
  _main_column.controls.append(_title)

#
  _content_column = Column(
    scroll='auto',
    expand=True,
    alignment='start',
    controls=[
        Container(
            padding=15,
            content=Text(
                'Scheduled Tasks',
                color='white70',
                weight='bold',
                size=13,
            ),
        )
    ],
)

#
  _main.content = Column(
      alignment='end',
      controls=[
          Container(
              expand=True,
              content=_content_column,

          ),
            _calendar_container,

      ],
  )

#Months Addition
  months = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December'     
  ]

#Weeks Addition
  weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
#Weekday Row
  _row_weekday = Row(spacing=2, alignment='center')
#Weekday Function

  for day in weekday:
      _row_weekday.controls.append(
          Container(
              width=32,
              height=32,
              border_radius=5,
              alignment=alignment.center,
              content=Text(day, size=9, color='White70')
          )
      )
      
#1st Loop thru date range
  for year in range (2022, 2025):
    #Nested loop
    _content_dic[year] = {}
    for month in range(1, 13):
      #
      _inner_column = Column(
          horizontal_alignment='center',
          spacing=2,
      )
      #Setting visible to False Hides the calendar element.
      _inner = Container(
        visible=False,
        content=_inner_column,
      )

      _main_column.controls.append(_inner)

      _row_year = Row(
          spacing=2, alignment='center',
          controls=[
              Text(
                  f'{months[month -1]} {year}',
                  size=12, color='white70',
              )


          ]
      )

      _inner_column.controls.append(_row_year)
      _inner_column.controls.append(_row_weekday)

      #
      #Now we iterate through the days
      for days in obj.monthdayscalendar(year, month):
          _row = Row(
              spacing=2,
              alignment='center'
          )

          _inner_column.controls.append(_row)
          #inner loop because days => nested list
          for day in days:
              if day != 0:
                  __ = Container(
                      width=32,
                      height=32,
                      bgcolor='#0c0f16',
                      border_radius=5,
                      alignment=alignment.center,
                      content=Text(
                          f'{day}',
                          size=10,
                          color='White70',
                      ),
                      #This is used to show the date
                      data=f'{months[month -1]} {day}, {year}',

                      #on-click
                      on_click=lambda e: _create_entry(e),
                      #on_hover
                      on_hover=lambda e: _highlight_date(e)
                  )
                  _row.controls.append(__)
                  #Checks if the date is today and changes the box to a new bg color
                  if month == _month_now and day == _day_now:
                      __.bgcolor = 'blue900'
              else:
                  _row.controls.append(
                      Container(
                          width=32,
                          height=32,
                          border_radius=5,
                      )
                  )
            #Add the content to the dictionary
              _content_dic[year][month] = _inner



  page.add(_main)

    
  page.horizontal_alignment='center'
  page.vertical_alignment='center'
  page.update()

if __name__ == '__main__':
  flet.app(target=main)