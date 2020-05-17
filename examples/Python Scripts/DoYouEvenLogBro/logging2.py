import pytest,os
import logging
import allure

logging.basicConfig(filename="test2.log",level=logging.DEBUG)
mylogger = logging.getLogger()

#############################################################################
@allure.description(''' Setup for the entire module ''')
def setup_module(module):
    mylogger.info('Inside Setup')
    # Do the actual setup stuff here
    pass

@allure.description(''' Setup for the entire module ''')
def setup_function(func):
    ''' Setup for test functions '''
    print("chek dis out 1")
    allure.dynamic.description("Actual description")
    print("check dis out 2")
    #allure.dynamic.description_html("<p>Actual HTML description</p>")
    if func == test_one:
        mylogger.info(' Hurray !!')

@allure.description(''' Test One ''')
def test_one():
    mylogger.info('Inside Test 1')
    #assert 0 == 1
    pass

def test_two():
    ''' Test Two '''
    mylogger.info('Inside Test 2')
    pass

@allure.description_html("""<h1>Html test description -- Test three </h1>""")
def test_three():

    mylogger.warning('O, O, an Oopsie')
    assert 6>11




if __name__ == '__main__':
    mylogger.info(' About to start the tests ')

    pytest.main(args=[os.path.abspath(__file__)])

    mylogger.info(' Done executing the tests ')