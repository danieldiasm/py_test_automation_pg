# Unittest - Essentials

On this Directory there will be more essential stuff of testing _for a developer_,
but not so basic as the 01_test_basics.

You'll be able to find:

- Unit Tests
- Integration Tests
- System Tests

This comprises the most important basic skills for a developer, since those tests usually would be the developer's responsibility to make.

It depends on the company or team if the system test is made by the test team or development team.

The system test will be having a better focus on Directory 03.

This is an application a bit more complex than the first one, since it has to offer the opportunity of integration and system testing.

#### What is Integration Testing?

Integration testing verifies how different parts of a system work together. It focuses on testing the interactions between different components of the system, then verifies that the system as a whole is working correctly.

<br>

#### About Unittest:

Unittest is a library that comes build-in on Python, so you'll be able to do
some testing only having Python installed on the system.

<br>

### What you can find in here:

1 - The Application
a - Tests
2 - Jenkinsfile
3 - Requirements File
4 - Script that runs the tests for you (takes arguments)

<br>

## How to run tests of this directory USING SCRIPT.

```
.../02_simple_application$ ./run_tests.sh [unit/integration/system]
```

The argument "prepare" makes a venv to run the tests, it is the ideal way to be done before running tests.

The argument "all" makes the venv and then run all the tests on it, deactivating removing it at the end, this is my favourite.

## How to run tests of this directory MANUALLY.

To run this tests you should have your terminal inside the unittest directory:

```
.../02_simple_application$ python -m unittest discover ./blog/
```

Then you should get:

```
....
----------------------------------------------------------------------
Ran 19 tests in 0.010s

OK
```

## Where to read more about the library unittest

A reliable source of information: https://devguide.python.org/testing/run-write-tests/.
Unittest Doc page: https://docs.python.org/3/library/unittest.html
