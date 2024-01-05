import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()
fig = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=list(df.columns), fill_color="paleturquoise", align="left"
            ),
            cells=dict(
                values=[
                    df.total_bill,
                    df.tip,
                    df.sex,
                    df.smoker,
                    df.day,
                    df.time,
                ],
                fill_color="lavender",
                align="left",
            ),
        )
    ]
)
fig.show()


# Here we use a column with categorical data
fig = px.histogram(df, x="day")
fig.show()
