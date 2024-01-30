from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from helpers import load_dataframe

app = Dash(__name__)

df = load_dataframe(input_type="csv", csv_path="apiGradesv3.csv")
df = df[df["campus"] == "UBCV"]  # just ubcv

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(df["subject"].unique(), "CPSC", id="xaxis-column"),
                        dcc.RadioItems(
                            ["Linear", "Log"], "Linear", id="xaxis-type", inline=True
                        ),
                    ],
                    style={"width": "48%", "display": "inline-block"},
                ),
                html.Div(
                    [
                        dcc.Dropdown(df["course"].unique(), "210", id="yaxis-column"),
                        dcc.RadioItems(
                            ["Linear", "Log"], "Linear", id="yaxis-type", inline=True
                        ),
                    ],
                    style={"width": "48%", "float": "right", "display": "inline-block"},
                ),
            ]
        ),
        dcc.Graph(id="indicator-graphic"),
        dcc.Slider(
            df["year"].min(),
            df["year"].max(),
            step=None,
            id="year--slider",
            value=df["year"].max(),
            marks={str(year): str(year) for year in df["year"].unique()},
        ),
    ]
)


@callback(
    Output("indicator-graphic", "figure"),
    Input("xaxis-column", "value"),
    Input("yaxis-column", "value"),
    Input("xaxis-type", "value"),
    Input("yaxis-type", "value"),
    Input("year--slider", "value"),
)
def update_graph(
    xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value
):
    dff = df[df["year"] == year_value]

    fig = px.scatter(
        x=dff[dff["subject"] == xaxis_column_name]["Value"],
        y=dff[dff["course"] == yaxis_column_name]["Value"],
        hover_name=dff[dff["course"] == yaxis_column_name]["section"],
    )

    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode="closest")

    fig.update_xaxes(
        title=xaxis_column_name, type="linear" if xaxis_type == "Linear" else "log"
    )

    fig.update_yaxes(
        title=yaxis_column_name, type="linear" if yaxis_type == "Linear" else "log"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
