import dash

from app.dashboard.layout import layout

def dashApp(routes_pathname_prefix):
    
    app = dash.Dash(
        __name__,
        server=False,
        routes_pathname_prefix = routes_pathname_prefix,
    )

    app.layout = layout()
    
    return app
