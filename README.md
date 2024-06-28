## create new project

poetry new microservice-a

## install and activate venv

to create a venv into project folder, see 
```
poetry shell
```


## build the project
```
poetry build
```
The build command builds the source and wheels archives.


## add dependencies
```
poetry add requests pendulum
```

## install dependencies from pyproject.toml
```
poetry install
```
