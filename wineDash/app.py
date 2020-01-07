import dash 
import dash_bootstrap_components as dbc 

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

server = app.server
app.config.suppress_callback_exceptions = True