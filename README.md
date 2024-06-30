# python modules

this repo is a POC of a python project composed by multiple modules, with shared code
poetry was used as a dependency management tool

Test module
use
```
$ pytests
```
to easily run all tests.

# Poetry chatsheet
## create new python module
this will record the module into pyproject.toml
```
poetry new microservice-a
```

## install and activate venv
you can use uv to create a new venv
```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
```

you can then enter the venv using poetry

```
poetry shell
```


## build the project

```
poetry build
```
The build command builds the source and wheels archives.


## add dependencies to pyproject.toml
```
poetry add requests pendulum
```

## install dependencies from pyproject.toml
```
poetry install
```
