# python modules

this repo is a POC of a python project composed by multiple modules, with shared code (the module_common dir).

Poetry was used as a dependency management tool.

# Tests
use
```bash
$ pytests
```
to easily run all tests.

# Run
module_a contains the main entrypoint of the app
## dev mode

```bash
 uvicorn module_a.app.main:app --reload
```


# Poetry chatsheet
## create new python module
this will record the module into pyproject.toml
```bash
poetry new microservice-a
```

## install and activate venv
you can use uv to create a new venv
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
```

you can then enter the venv using poetry

```bash
poetry shell
```


## build the project

```bash
poetry build
```
The build command builds the source and wheels archives.


## add dependencies to pyproject.toml
```bash
poetry add requests pendulum
```

## install dependencies from pyproject.toml
```bash
poetry install
```
