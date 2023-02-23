# Unittest - Essentials

### **ATENTION! - This is under construction**

On this Directory there will be more essential stuff of testing _for a developer_,
but not so basic as the 01_test_basics.

You'll be able to find:

- Unit Tests
- Integration Tests

This comprises the most important skills for a developer, since those tests normally
would be the developer's responsibility to make.

The system test will be having its own section on Directory 03. It depends on the
company if the system test is being made by the test team or development team. So I'll leave this sepparate for the sake of organizing each subject.

#### About Unittest:

Unittest is a library that comes build-in on Python, so you'll be able to do
some testing only having Python installed on the system.

### What you can find in here:

1 - The Application

2 - Tests

3 - Jenkinsfile

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
