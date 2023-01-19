from dash import Dash, html, dcc, State, exceptions
import datetime


app = Dash(__name__)
server = app.server #server heroku reconhecer a app

app.layout = html.Div([
    html.H1('DICA PARA TODOS'),
    html.A("vá pesquisar no google", href='http://www.google.com', target='blank'),
    html.H2(children=[datetime.datetime.now()])
])

if __name__ == '__main__':

    app.run_server(debug=True, port=8053)