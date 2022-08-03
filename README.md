# Env Setup
```shell
cd tests/
export PYTHONPATH=./lib
pytest .

# to capture stdout run
# pytest -s
``` 

# Requirements
- python3
- pip install pytest

# setup / teardown
make sure, your tests run a clean setup an cleanup after run, even if the test fails. so use fixture to accomplish this task
