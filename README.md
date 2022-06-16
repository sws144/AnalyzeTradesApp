# AnalyzeTradesApp

Streamlit app version of [P1-AnalyzeTrades project](https://github.com/sws144/quant-trading/tree/master/P1-AnalyzeTrades)

## Virtual Environment Setup

1. install python 3.10 to (windows) system
1. `py -3.10 -m pip install pipx`
1. `py -3.10 -m pipx install poetry` # allows use of poetry without py -3.10 -m prefix commands below
1. navigate to this folder
1. update poetry config to setup virtual environment in project
    1. `py -3.10 -m poetry config virtualenvs.in-project true`
    1. `py -3.10 -m poetry config virtualenvs.path env`
1. create env
    1. `py -3.10 -m poetry shell` # creates venv if none exists
    1. edit pyproject.toml to add dependencies
    1. `py -3.10 -m poetry install` # creates exact virtual environment in lock file
    1.  to install based on pyproject.toml file, `py -3.10 -m poetry update`
1. use env
    1. in vscode, switch to venv while workspace is set to this folder
    1. in windows terminal, `.venv\Scripts\activate`
1. to run app
    1. `streamlit run app.py`