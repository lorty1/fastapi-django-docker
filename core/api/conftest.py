import os, sys
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
api_module = sys.path.append(BASE_DIR)
print('hello conftest 2', BASE_DIR)
#def pytest_configure():
#    print("Hello World")