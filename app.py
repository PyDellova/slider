from dash import Dash, dcc, html, Input, Output
app = Dash(__name__)
  
app.layout = html.Div([
    dcc.Slider(id='slider', min=0, max=10, step=1, value=5),
    html.Div(id='output')
])
  
@app.callback(
    Output('output', 'children'),
    Input('slider', 'value')
)
def update_output(value):
    return f'Slider value is {value}'
  
if __name__ == '__main__':
    app.run(debug=True)
