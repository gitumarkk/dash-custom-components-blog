import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from custom_components import MyCustomComponent

external_stylesheets = ["https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    className="text-center",
    children=[
        html.H1(
            children="Hello Dash",
            className="p-4 text-indigo-700 text-xl w-full",
        ),
        html.Div(
            children=[
                MyCustomComponent(
                    id="my-custom-component",
                    label="label is required",
                    value="",  # you can initializes
                )
            ],
            className="p-4 bg-gray-100 w-full",
        ),
        html.Div(id="input-result"),
        html.Button(
            "Clear input",
            id="clear-input-button",
            className="mt-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded",
        ),
    ],
)


@app.callback(
    Output("input-result", "children"), [Input("my-custom-component", "value")]
)
def display_input_value(value):
    return f"You have entered {value}"


@app.callback(
    Output("my-custom-component", "value"), [Input("clear-input-button", "n_clicks")]
)
def clear_input_value(n_clicks):
    if n_clicks:
        return ""


if __name__ == "__main__":
    app.run_server(debug=True)
