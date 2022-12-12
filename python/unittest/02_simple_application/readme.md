# Unittest - Basic

This is an example of a simple application with simple unit tests for it.

Unittest is a library that comes build-in on Python, so you'll be able to do
some testing only having Python installed on the system. 

## What you can find in here
 1 - The Application
 This is a dummy application with few simple functions for you to read or practice 
 writing unit tests for it.

 2 - Tests
 Inside this there are only simple unit tests, no integration or system tests.
 Unit test, ideally is a task that the software developer should be doing. 

 4 - Test Resources Examples
    a - Set-Up
    b - Teardown
    c - Fixtures

 5 - Jenkinsfile
 There is a Jenkinsfile for you to use it on a pipeline, its job is to execute the
 shell script called "run_tests.sh" and execute the tests.


## How to run tests of this directory.

To run this tests you should have your terminal inside the unittest directory:

```
.../unittest$ python -m unittest discover ./application/
```

Then you should get:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

# Where to read more about the library unittest

A reliable source of information: https://devguide.python.org/testing/run-write-tests/.
Unittest Doc page: https://docs.python.org/3/library/unittest.html