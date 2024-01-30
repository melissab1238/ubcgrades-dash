# UBC Grades - Dash
Building off of the original incredible [ubcgrades.com](ubcgrades.com) project, I am utilizing [Plotly's Dash](dash.plotly.com) system to analyze and visualize UBC grade data with less code.

## Data sources
From the [ubcgrades.com API](https://ubcgrades.com/api-reference/v3), I can receive grades distributions as json objects, then transform them into dataframes for python and plotly to manage.

For example
`https://ubcgrades.com/api/v3/grades/UBCV/2022S`

## Docker-dash
Instructions from [docker-dash](https://github.com/yaojiach/docker-dash/blob/main/README.md)...
### Build and run

`prod` version is served by `gunicorn` instead of the `flask` dev server.

```sh
# dev
docker build -f Dockerfile.dev -t ubcdash-dev .
docker run -p 8050:8050 -v "$(pwd)"/app:/app --rm ubcdash-dev

# prod
docker build -f Dockerfile -t ubcdash-prod .
docker run -p 8050:8050 -v "$(pwd)"/app:/app --rm ubcdash-prod
```
### Access the page

Go to `http://localhost:8050` in browser.

### Switch debug mode in Dockerfile

```dockerfile
ENV DASH_DEBUG_MODE True # False
```

### Development

Install the app requirements for development to get better editor support.

```sh
poetry install
```

Optional: clean initialization of `poetry`:

```sh
poetry init
cat app/requirements.txt | xargs poetry add
```

## Playground jupyter notebook
see [my playground jupyter notebook](playground2.ipynb) for current progress

## Screenshots
![Example output 2](screenshots/cpsc210screenshot.png "Title")

## Future developments
- [x] tidy up imports with requirements.txt
- [x] create a dash app mvp
- [x] showcase sample plotly charts in screenshots
- [x] refine openai outputs
- [x] create dash app with charts that match what is currently on ubcgrades.com
- [ ] find/make a chatgpt interface on dash
- [ ] improve markdown on ipynb file
- [x] separate out helper functions
- [x] improve UI of charts
- [ ] host application and database and functions on the cloud. Ex: GCP Cloud Run, Cloud Store, Cloud Functions. Or Render.com. Docker image would be great too.

## Curent priorities
- [ ] filter dropdowns
- [ ] show "OVERALL" section by defaul
- [ ] year x axis only has 3 options 2021, 2022, 2023. Not 2021.5
- [ ] capitalize labels (axis, legend)
- [ ] give larger marker to the "OVERALL" vs the sections - not sure if this is possible (conditional markers)

## Questions I'd like to be able to answer
- SELECT campus, subject, course where average > 90
- questions: what courses in 3rd and 4th year can I take that have the highest average?
- what courses have the lowest fail rate? (<50 or <55%)
- how do grades compare between sections of the same class?
- how do grades compare between profs over the years/classes?
- does class size influence grades?
- what subjects (CPSC, MATH, etc) have the highest averages?
- what MATH 1xx courses have the highest and lowest averages?