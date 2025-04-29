# Import Guard and Validator
from guardrails.hub import ValidPython
from guardrails import Guard

# Setup Guard
guard = Guard().use(ValidPython, on_fail="exception")

# Correct python
correct_python = """
import os

def foo():
    print(f"Current path is: {os.getcwd()}")

foo()
"""

incorrect_python = """
import os

def foo()
    print f"Current path is: {os.getcwd()}"

foo()
"""

guard.validate(correct_python)  # Validator passes
try:
    guard.validate(incorrect_python)  # Validator fails
except Exception as e:
    print(f"Validation error: {e}")