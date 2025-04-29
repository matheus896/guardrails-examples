# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import ValidSQL

# Setup Guard
guard = Guard().use(
    ValidSQL, on_fail="exception"
)
response = guard.validate("SELECT * FROM EMPLOYEES;")  # Validator passes

try:
    response = guard.validate("SELEKT ID FROM USERS;")  # Validator fails
except Exception as e:
    print(e)