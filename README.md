#Behave POC

##Installation

1. Install **Python**
  * This example should run with either Python 2 or 3, but I used 3
  * [Here](http://docs.python-guide.org/en/latest/starting/install3/osx/) is a good example of installing Pythong 3 on OSX
2. Install **Behave**
  * Open Terminal, run `pip install behave`
3. Install **selenium** for Python
  * From Terminal, run `pip install selenium`
  * NOTE: I saw a permission error here when pip tried to install to _/usr/local/selenium_, so you many need to run with sudo.
4. If you don't have it already, install [Homebrew](https://brew.sh/)
5. Install **geckodriver** to run on FireFox
  * From Terminal, run `brew install geckodriver`
  * Make sure the directory path to geckdriver is in your $PATH
    * Run `which geckodriver`, and the path up to _geckodriver_ should be in the results of `echo $PATH`
6. Install **Chromedriver** to run Chrome
  * `brew install chromedriver`
  * Make sure the directory path to chromedriver is in your $PATH
    * compare `which chromedriver` and  `echo $PATH`

##Run
* From Terminal, type:
  * `behave` to run all tests
  * `behave --tags=Test_FBG_Logo` to run a single test
