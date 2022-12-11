# Unittest - Basic

Note:
Unittest comes with the python interpreter, so nothing else should be needed.

## About the tests
 1 - Test App
 These consist on basic unit tests asserting if the function returns the expected result.

 2 - Test Mock
 These consist on Mock, which shows a bit how to mock a function replacing it with a mock.

## How to run tests of this directory.

A reliable source of information: https://devguide.python.org/testing/run-write-tests/.
Unittest Doc page: https://docs.python.org/3/library/unittest.html

To run this tests you should have your terminal inside the unittest directory:

```
.../unittest$ python -m unittest discover ./sample_basic/
```

Then you should get:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```