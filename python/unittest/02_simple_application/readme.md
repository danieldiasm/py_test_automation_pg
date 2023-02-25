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
4 - Script that runs the tests manually (takes arguments)

<br>

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

## Where to read more about the library unittest

A reliable source of information: https://devguide.python.org/testing/run-write-tests/.
Unittest Doc page: https://docs.python.org/3/library/unittest.html
