# Import Guard and Validator
from guardrails.hub import GuardrailsPII
from guardrails import Guard

# Setup Guard
guard = Guard().use(
    GuardrailsPII(entities=["DATE_TIME"], on_fail="fix")
)

guard.validate("I'll meet you at 5pm")  # Validator passes  

try:
    guard.validate("I'll meet you at 5pm on 2022-01-01")
    print("Passou")         
except Exception as e:
    print(f"Validation failed: {e}")