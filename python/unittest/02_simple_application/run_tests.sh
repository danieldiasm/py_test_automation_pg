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

prepare() {
    create_venv
    activate_venv
    cd ./blog
}

run_test_type() {
    `python -m unittest discover -s ./tests/$1/ -p "*_test.py"`
    deactivate
}

if [[ $TESTS == "unit" ]]; then
    echo "Running unit tests..."
    prepare
    run_test_type "unit"

elif [[ $TESTS == "integration" ]]; then
    echo "Running integration tests..."
    prepare
    run_test_type "integration"

elif [[ $TESTS == "system" ]]; then
    echo "Running system tests..."
    prepare
    run_test_type "system"

elif [[ $TESTS == "all" ]]; then
    echo "everything"
    echo "Running unit tests..."
    prepare
    run_test_type

else
    echo -e "Use one of the arguments:
     unit        - run all the unit tests.
     integration - run all the integration tests
     system      - run all the system tests
     all         - run all the tests"
fi
