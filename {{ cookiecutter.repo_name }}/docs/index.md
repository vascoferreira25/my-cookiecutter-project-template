# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

### Environment

Make sure you have Poetry environment manager installed and then run:

```shell
poetry install
```

### Run

To run the program run:

```shell
poetry run main
```

### Serve the docs

```
poetry run mkdocs serve
```

### Test

To test the program run:

```shell
poetry run pytest
```

### Coverage report

To get a coverage report run:

```shell
coverage run -m pytest
coverage report
```

This will ensure that you have the environment ready to start parsing.

### Settings

Create a `.env` file to store the project credentials:

```
DATABASE_NAME=database
DATABASE_HOST=localhost
DATABASE_USERNAME=username
DATABASE_PASSWORD=password
USERNAME=some_username
PASSWORD=password
```

Create a `settings.toml` file to store the program settings:

```toml
[scraper]
scrape_website_n_times = 1000
```

## Project layout

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- Where the Mkdocs documentation will stay
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── tests              <- Tests
│   └── out            <- For tests that save files
│
├── {{ cookiecutter.project_slug }} <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   ├── __main__.py    <- The main script to run the program
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── db.py      <- Connect to a database
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── ui            <- Scripts to create a user interface
│   │   └── gui.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── .env               <- Credentials
│
├── settings.toml      <- Program settings
│
├── start_{{ cookiecutter.project_slug }}.ps1 <- utility to start the program from powershell
│
├── mkdocs.yml         <- Settings for Mkdocs
│
└── pyproject.toml     <- Settings for poetry environment manager
```
