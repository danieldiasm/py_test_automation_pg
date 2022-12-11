# Unittest - Basic

This is an example of a simple application with simple unit tests for it.

Note:
The unittest lib comes with the python interpreter, so nothing else should be needed.

## About the tests
 1 - App
 This is a dummy application to build tests on it.

 2 - Unit Tests
 Inside this basics there are only unittests, no integration or system tests.

 3 - Tests
 This contains the practice test files. Here you can find all sort of tests, from simple
 assertions to mock tests.

 4 - Jenkinsfile
 There is a Jenkinsfile for you to use it on a pipeline!

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