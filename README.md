# AnalyzeTradesApp

**NOT WORKING BC POETRY CANT FIND ALL DEPENDENCIES SUCH AS PYWIN**

Streamlit app version of [P1-AnalyzeTrades project](https://github.com/sws144/quant-trading/tree/master/P1-AnalyzeTrades)

## Virtual Environment Setup

1. install python 3.10 to (windows) system
1. `py -3.10 -m pip install pipx`
1. `py -3.10 -m pipx install poetry==1.0.10` # allows use of poetry without py -3.10 -m prefix commands below
1. navigate to this folder
1. update poetry config to setup virtual environment in project
    1. `py -3.10 -m poetry config virtualenvs.in-project true`
1. create env
    1. `py -3.10 -m poetry shell` # creates venv if none exists
    1. edit pyproject.toml to add dependencies
    1. `py -3.10 -m poetry install` # creates exact virtual environment in lock file
    1. to install based on updated pyproject.toml file, `py -3.10 -m poetry update`
1. use env
    1. in vscode editor, switch to venv while workspace is set to this folder
    1. in windows terminal, `.venv\Scripts\activate`

## Run Application
1. activate env:  `py -3.10 -m poetry shell`
1. `streamlit run app.py`
1. can enable settings `run on save` to iterate quickly
