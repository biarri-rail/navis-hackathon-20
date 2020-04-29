# Navis Hackathon 2020

# Navis on the Map: Better Together



## First time setup

Global dependencies
- python 3.7, possibly with pyenv https://github.com/pyenv/pyenv
  ```
  pyenv install 3.7.8
  ```
- `poetry` https://github.com/python-poetry/poetry
  ```
  pip install
  ```

In the repo
- Tell pyenv to use 3.7
  ```
  pyenv local 3.7.3
  ```
- Install the python dependencies
  ```
  poetry install
  ````

## Running it/working with

1. Running the application
    ```
    poetry run app
    ```
2. Open up the app at http://127.0.0.1:8050/


Getting into the virtualenv setup by peotry
```
poetry shell
```

## Dash 101

In `app.py`, the `app` is built up by adding components to the layout. `app.run_server()` is called to start the Dash server.

HTML components can be added with `html`. e.g. `html.div`.
Interactive components can be added with `dcc`, e.g. `dcc.Input`, `dcc.Dropdown`.

`app.index_string` can be set with an HTML template. Data such as css and scripts can be added to the template with `{%css%}` and `app.css.append_css`.

A plotly figure is like any other component being added to the app. `fig.add_trace()` allows multiple graphs to be superimposed. `fig.update_layout()` is used to add titles, axes, etc.

Interactivity is controlled by adding a function which accepts an input component property and returns the output component property. Decorate it with `@app.callback(Output(component_id, component_property), [Input(component_id, component_property)])`. For example:

```
@app.callback(Output(component_id="display", component_property="content"), [Input(component_id="input", component_property="input_text")]):
def update_my_comp(input_text):
    return "You have told us {}.".format(input_text)
```
