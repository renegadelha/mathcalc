from dash import Dash, html, dcc, State, exceptions
from dash.dependencies import Input,Output
import processar

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Fórmula de Bhaskara',className='banner'),
    html.Br(),
    html.Div(children=[
        html.Div([html.A('Valor de A:', className='textInput'),
                  dcc.Input(id='inputA', value='0', type='text'),
                  html.A('Valor de B:', className='textInput'),
                  dcc.Input(id='inputB', value='0', type='text'),
                  html.A('Valor de C:', className='textInput'),
                  dcc.Input(id='inputC', value='0', type='text'),

                  html.Button(id='botaoInput', n_clicks=0, children='Calcular', className='botao')
                  ]),
        html.Br(),
        html.Div(id='data_output', children=['Resposta'],className='resposta')

    ], className='banner'),


    ], className='back')

@app.callback(
    Output('data_output', 'children'),
    Input('botaoInput', 'n_clicks'),
    State('inputA', 'value'),
    State('inputB', 'value'),
    State('inputC', 'value'),
    prevent_initial_call=True

)
def update_table(n_clicks, valueA, valueB, valueC):


    print(f'{valueA} {valueB} {valueC}')
    if int(valueA) > 0:
        total = processar.bhaskara(int(valueA), int(valueB), int(valueC))
        child = html.Div([
            f'RESPOSTA= {total}'
        ])
        return child

    elif len(valueA) == 0:
        raise exceptions.PreventUpdate

if __name__ == '__main__':

    app.run_server(debug=True, port=8053)

