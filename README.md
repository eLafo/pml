# Using Jupyter

Just run

```bash
docker-compose up -d
```

and then look for the URL with the token in the logs:

```bash
docker-compose logs
```

# Using an IDE

1. Install [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

2. Create your pyenv
```bash
pyenv install $(cat .python-version)
```

3. Create and activate virtualenv (optional)
```bash
pyenv virtualenv $(cat .python-version) pml
pyenv activate pml
```

4. Install libraries
```bash
pip install -r requirements.txt
```