# UBC Grades - Dash
Building off of the original incredible [ubcgrades.com](ubcgrades.com) project, I am utilizing [Plotly's Dash](dash.plotly.com) system to analyze and visualize UBC grade data.

## Data sources
From the [ubcgrades.com API](https://ubcgrades.com/api-reference/v3), I can receive grades distributions as json objects, then transform them into dataframes for python and plotly to manage.

For example
`https://ubcgrades.com/api/v3/grades/UBCV/2022S`