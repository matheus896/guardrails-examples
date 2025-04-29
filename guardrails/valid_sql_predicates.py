# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import ExcludeSqlPredicates

# Setup Guard
guard = Guard().use(
    ExcludeSqlPredicates, predicates=["Drop"], on_fail="exception"
)

response = guard.validate("select * from employees;")  # Validator passes

try:
    response = guard.validate("drop table departments;")  # Validator fails
except Exception as e:
    print(e)