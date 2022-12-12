#!/bin/bash

TESTS=$1

create_venv() {
    echo " - Creating a venv."
    `python3.9 -m venv ./testenv`
}

activate_venv() {
    echo " - Activating the venv."
    source ./testenv/bin/activate
}

if [[ $TESTS == "unit" ]]; then
    echo "Running unit tests..."
    create_venv
    activate_venv
    cd ./blog
    python -m unittest discover -s ./tests/unit/ -p "*_test.py"

elif [[ $TESTS == "integration" ]]; then
    echo "integration"
    create_venv
elif [[ $TESTS == "system" ]]; then
    echo "system"
    create_venv
elif [[ $TESTS == "all" ]]; then
    echo "everything"
    create_venv
else
    echo -e "Use one of the arguments:
     unit        - run all the unit tests.
     integration - run all the integration tests
     system      - run all the system tests
     all         - run all the tests"
fi
