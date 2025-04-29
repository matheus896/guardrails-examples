# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import CompetitorCheck


# Setup Guard
guard = Guard().use(
    CompetitorCheck, ["Flamengo", "Botafogo", "Fluminense"], "exception"
)

response = guard.validate(
    "Grande Vasco é o maior time do Rio de Janeiro"
)  # Validator passes

try:
    response = guard.validate("Flamengo é um clube de futebol")  # Updating for better validation context
    print("Validation Passed:", response)
except Exception as e:
    print(f"Validation Error: {e}")