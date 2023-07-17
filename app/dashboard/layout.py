import dash_core_components as dcc
import dash_html_components as html

def layout():

    """ The dashboard layout """
    layout = html.Div([
    
        html.Div([
            html.A(html.Button('Home', className='main_buttom'), href='/dashboard/'),
            html.A(html.Button('Log Out', className='main_buttom'), href='/logout', style = {'display': 'inline-block', 'float': 'right'})
        ]),
                
        html.Div([
            html.Div(id = 'home_text')
        ]),
                
        html.Div([
            html.Div(
                [
                    html.Div(
                        [
                            html.Center(html.P(children='''Select figure #''')),
                            dcc.Dropdown(
                                id = 'question_num_filter',
                                options = [
                                    {'label': i, 'value': i} for i in range(1, 5)
                                ],
                                value = 1
                            )
                        ],
                        className='nav_buttom',
                        style = {'width': '17%', 'display': 'inline-block'}
                    ),
                ],
                
                id = 'nav_panel',
            ),

            html.Div(
                [
                    html.Br(), html.Br(),
                    html.Center(dcc.Graph(id='graph'))
                ],
                id = 'main_graph'
            )
        ])
    ])
                                
    return layout
