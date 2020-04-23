# Install requirements

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