## Download Gecko Driver

- https://selenium-python.readthedocs.io/installation.html
- https://github.com/mozilla/geckodriver/releases

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

## Running tests
You can run the all the tests by using this command:

python -m unittest discover -s test -p '*_test.py'

or use the IDE play buttons to run the test as well  

### Importing Dependencies
In pycharm they should get pulled in but if not 
- pip install selenium
- pip install requests

###Plans to refactor: 
- Duplicate Code, create functions 
- Use POM to call objects and not redefine them in every test 
- Add additional browser support other than FF

##Troubleshooting
You  may need to give macOS access to you file system to access firefox driver to run tests


