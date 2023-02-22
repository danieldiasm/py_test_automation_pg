# Unittest - Basics

This is an example of a simple application with simple unit tests for it.

Unittest is a library that comes build-in on Python, so you'll be able to do
some testing only having Python installed on the system. 

## What you can find in here
 1 - The Application
 This is a dummy application with three simple functions for practice of
 writing **unit** tests for it.

 2 - Tests
 Inside the tests directory there are some simple tests.

 Unit test, ideally is a task that the software developer should be doing, 
 not the test team. 

 Integration test in another hand depends on the organization/development team.

3 - Tests Description
   - test_app.py
      - This file contains one unit test and one purposefully **accidental** integration test. Read more in the file.
   - test_mock.py
      - This file contains how to fix the accidental integration test on the previous file, using **Mocking** or **Dependency Injection** technique.

4 - Jenkinsfile
 There is a Jenkinsfile for you to use it on a pipeline, its job is to execute the
 shell script called "run_tests.sh" and execute the tests.


## How to run tests of this directory.

To run this tests you should have your terminal inside the unittest directory:

```
.../unittest$ python3 -m unittest discover ./application/
```

Then you should get:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

<br>
<br>

## Where to read more about the library unittest

A reliable source of information: https://devguide.python.org/testing/run-write-tests/.
Unittest Doc page: https://docs.python.org/3/library/unittest.html

<br>
<br>
<br>

###### File: readme.md
###### Author: Daniel Z. Dias de Moraes
###### Last update: 22 Feb 2023