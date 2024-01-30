import requests
import json
import pandas as pd
import plotly.express as px
from helpers import load_dataframe
from dash import Dash, html, dcc, callback, Output, Input

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


# df = load_dataframe(input_type="api")
df = load_dataframe(input_type="csv", csv_path="data/apiGradesv3.csv")

# sort df for loading in the dash chart
df.sort_values(by=["faculty_title", "course"])

# starting dropdrown options
starting_options = {
    "campus": [{"label": i, "value": i} for i in df["campus"].unique()],
    "faculty": [{"label": i, "value": i} for i in df["faculty_title"].unique()],
    "subject": [{"label": i, "value": i} for i in df["subject"].unique()],
    "course": [{"label": i, "value": i} for i in df["course"].unique()],
}

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H1(children="UBC Grades - Dash", style={"textAlign": "center"}),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="column",
                    children=[
                        html.Label(["Campus:"]),
                        dcc.Dropdown(
                            options=starting_options["campus"],
                            value="UBCV",
                            id="campus",
                        ),
                    ],
                ),
                html.Div(
                    className="column",
                    children=[
                        html.Label(["Faculty Title:"]),
                        dcc.Dropdown(
                            options=starting_options["faculty"],
                            value="Faculty of Science",
                            id="faculty",
                        ),
                    ],
                ),
                html.Div(
                    className="column",
                    children=[
                        html.Label(["Subject:"]),
                        dcc.Dropdown(
                            options=starting_options["subject"],
                            value="CPSC",
                            id="subject",
                        ),
                    ],
                ),
                html.Div(
                    className="column",
                    children=[
                        html.Label(["Course:"]),
                        dcc.Dropdown(
                            options=starting_options["course"], value=210, id="course"
                        ),
                    ],
                ),
            ],
            style=dict(display="flex"),
        ),
        html.Br(),
        dcc.Graph(id="plot"),
    ]
)


@callback(
    Output("subject", "options"), Output("course", "options"), Input("faculty", "value")
)
def faculty_update(selected_faculty):
    filtered_df = df[df["faculty_title"] == selected_faculty]
    subject_options = [
        {"label": i, "value": i} for i in filtered_df["subject"].unique()
    ]
    course_options = [{"label": i, "value": i} for i in filtered_df["course"].unique()]
    return subject_options, course_options


@callback(
    Output(component_id="plot", component_property="figure"),
    Input(component_id="campus", component_property="value"),
    Input(component_id="faculty", component_property="value"),
    Input(component_id="subject", component_property="value"),
    Input(component_id="course", component_property="value"),
)
def update_graph(campus_value, faculty_value, subject_value, course_value):
    dff = df.copy()
    dff = dff[dff.campus == campus_value]
    dff = dff[dff.faculty_title == faculty_value]
    dff = dff[dff.subject == subject_value]
    dff = dff[dff.course == course_value]
    return px.scatter(
        dff,
        x="year",
        y="average",
        color="average",
        hover_data=["course", "section"],
        labels=dict(year="Year", average="Average", section="Section", course="Course"),
    )


if __name__ == "__main__":
    app.run(debug=True)
