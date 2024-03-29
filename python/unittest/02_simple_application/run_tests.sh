#!/bin/bash
# Author: Daniel Z. Dias de Moraes
# Script for preparing the test env and running

TESTS=$1

create_venv() {
    echo " - Creating a venv."
    `python3.9 -m venv ./testenv`
}

install_reqs() {
    echo " - Installing Requirements."
    pip3 install -r requirements.txt
}

activate_venv() {
    echo " - Activating the venv."
    source ./testenv/bin/activate
}

run_test_type() {
    activate_venv
    cd ./blog
    `python -m unittest discover -s ./tests/$1/ -p "*_test.py"`
    deactivate
}

prepare() {
    create_venv
    install_reqs
}

if [[ $TESTS == "prepare" ]]; then
    echo "Preparing test environment..."
    prepare

elif [[ $TESTS == "unit" ]]; then
    echo "Running unit tests..."
    run_test_type "unit"

elif [[ $TESTS == "integration" ]]; then
    echo "Running integration tests..."
    run_test_type "integration"

elif [[ $TESTS == "system" ]]; then
    echo "Running system tests..."
    run_test_type "system"

elif [[ $TESTS == "all" ]]; then
    echo "everything"
    echo "Running all types of tests..."
    prepare
    run_test_type
    echo "Removing venv..."
    rm -R ../testenv
    RES=$?
    if [[ $RES == 1 ]]; then
        echo "An error has ocurred removing venv folder!"
        exit 1;
    else
        echo "Done!"
    fi
else
    echo -e "Use one of the arguments:
     prepare     - create virtual env and install reqs
     unit        - run all the unit tests.
     integration - run all the integration tests
     system      - run all the system tests
     all         - run all the tests"
fi
