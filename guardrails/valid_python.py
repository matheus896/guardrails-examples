# guardrails hub install hub://reflex/valid_python
from guardrails.hub import ValidPython
from guardrails import Guard

# Setup Guard
guard = Guard().use(ValidPython, on_fail="exception")

# Correct python
correct_python = """

x = 1
y = 2

print(x+y)

"""

incorrect_python = """

x = 1
y = 2

print x+y

"""

guard.validate(correct_python)  # Validator passes
try:
    guard.validate(incorrect_python)  # Validator fails
except Exception as e:
    print(e)