# pytest learning notes 
## 	 from pytest.com documentation ,release 5.3 
### 2020/2/3 Monday

## CHAPTER 2

* P7 **2.1**

  `>>> pytest [...]`

  `>>> python -m pytest [...]`

They are almost equivalen, except when python calling *sys.path*.

* **2.2**
Exit code
Running pytest can result in six different exit codes:
Exit code 0 All tests were collected and passed successfully
Exit code 1 Tests were collected and run but some of the tests failed
Exit code 2 Test execution was interrupted by the user
Exit code 3 Internal error happened while executing tests
Exit code 4 pytest command line usage error
Exit code 5 No tests were collected
 The exit codes being a part of the public API can be imported and accessed directly using:

`from pytest import ExitCode`

* P8 **2.3** getting help

`pytest --version # shows where pytest was imported from`
`pytest --fixtures # show available builtin function arguments`
`pytest -h | --help # show help on command line and config file options`

* **2.4**  Stopping after the first (or N) failures

`pytest -x # stop after first failure`
`pytest --maxfail=2 # stop after two failures`

* **2.5** Specifying tests / selecting tests

`pytest test_mod.py`
`pytest testing/`
`pytest -k "MyClass and not method"`
`pytest test_mod.py::test_func`
`pytest -m slow run all tests with the @pytest.mark.slow decorator.`
`pytest --pyargs pkg.testing # import pkg.testing`

* **2.6** modifying python trackback printing

`pytest --showlocals `
`pytest -l `
`pytest --tb=auto`
`pytest --tb=long `
`pytest --tb=short `
`pytest --tb=line `
`pytest --tb=native `
`pytest --tb=no `

* **2.7**  Detailed summary report

The -r flag can be used to display a “short test summary info” at the end of the test session.The -r options accepts a number of characters after it, with a used above meaning “all except passes”.
Here is the full list of available characters that can be used:
	- f - failed
	- E - error
	- s - skipped
	- x - xfailed
	- X - xpassed
	- p - passed
	- P - passed with output
	- a - all except pP
	- A - all

* P12 **2.8**  Dropping to PDB (Python Debugger) on failures

`pytest --pdb`

* **2.9** Dropping to PDB (Python Debugger) at the start of a test

`pytest --trace`

* p14 **2.14**  Creating JUnitXML format files

`pytest --junitxml=path`

## CHAPTER 3 
### Using pytest with an existing test suite

* **3.1** Running an existing test suite with pytest
```
cd <repository>
pip install -e . # Environment dependent alternatives include
		 # 'python setup.py develop' and 'conda develop'
```
