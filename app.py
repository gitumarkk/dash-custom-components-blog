from datetime import date
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from custom_components import MyCustomComponent, MyEditor, MyCalendar

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
                    value="",
                )
            ],
            className="p-4 bg-gray-100 w-full",
        ),
        html.Div(MyEditor(id="my-editor"), className="w-3/5 my-5 mx-auto"),
        html.Div(MyCalendar(id="my-calendar"), className="w-72 mx-auto"),
        html.Div(id="input-result", className="my-5"),
        html.Button(
            "Reset",
            id="clear-input-button",
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded",
        ),
    ],
)


@app.callback(
    Output("input-result", "children"),
    [
        Input("my-custom-component", "value"),
        Input("my-calendar", "date"),
        Input("my-editor", "value"),
    ],
)
def display_input_value(input_value, date_value, editor_value):
    return html.Div(
        children=[
            html.Div(f"Input Value: {input_value}", className=""),
            html.Div(f"Date Value: {date_value}", className=""),
            html.Div(f"Date Value: {editor_value}", className=""),
        ]
    )


@app.callback(
    [
        Output("my-custom-component", "value"),
        Output("my-calendar", "date"),
        Output("my-editor", "value"),
    ],
    [Input("clear-input-button", "n_clicks")],
)
def clear_input_value(n_clicks):
    today = date.today().strftime("%d-%b-%Y")
    if n_clicks:
        return "", today, ""
    return "", today, ""


if __name__ == "__main__":
    app.run_server(debug=True)
