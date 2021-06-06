# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Project Organization

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

## Install the environment

```
poetry install
```

## Running the tests

```
poetry run pytest
```

## Running the program

```
poetry run main
```

## Serve the docs

```
poetry run mkdocs serve
```