import os
import sys

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

api_module = sys.path.insert(0, os.path.join(BASE_DIR, 'core/api'))

