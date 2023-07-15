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
                            html.Center(html.P(children='''Select the Type of Report''')),
                            dcc.Dropdown(
                                id = 'filter_1',
                                options = [{'label': 'Sample', 'value': 'Sample'}],
                                value = ''
                            )
                        ],
                        className='nav_buttom',
                        style = {'width': '17%', 'display': 'inline-block'}
                    ),
                    
                    html.Div(
                        [
                            html.Center(html.P(id = 'filter_2_title')),
                            dcc.Dropdown(id = 'filter_2')
                        ],
                        className='nav_buttom',
                        style = {'width': '23%', 'display': 'inline-block'}
                    ),
                        
                    html.Div(
                        [
                            html.Center(html.P(id = 'filter_3_title')),
                            dcc.Dropdown(id = 'filter_3')                        
                        ],
                        id = 'filter_3_div',
                        className='nav_buttom'
                    ),
                            
                    html.Div(
                        [
                            html.Center(html.P(id = 'filter_4_title')),
                            dcc.Dropdown(id = 'filter_4')                        
                        ],
                        id = 'filter_4_div',
                        className='nav_buttom',
                        style = {'width': '15%', 'display': 'inline-block'}
                    ),
                        
                    html.Div(
                        [
                            html.Center(html.P(children=''' ''')),
                            html.Button(id = 'submit-button-state', n_clicks = 0, children = 'View report', className = 'main_buttom')
                        ],
                        id = 'view_report',
                        className='nav_buttom',
                        style = {'width': '15%', 'display': 'inline-block', 'white-space': 'pre'})
                ],
                
                id = 'nav_panel',
            ),

            html.Div(
                [
                    html.Br(), html.Br(),
                    html.Div(id = 'sce_text'),
                    html.Center(dcc.Graph(id='sce_graph'))
                ],
                id = 'main_graph'
            )
        ])
    ])
                                
    return layout
