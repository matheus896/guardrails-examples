# Import Guard and Validator
from guardrails.hub import CsvMatch
from guardrails import Guard

# Setup Guard
guard = Guard().use(
    CsvMatch
)

guard.validate("name,email\njohn,john@example.com\njane,jane@example.com")  # Validator passes
guard.validate("name,email\njohn\njane,jane@example.com")  # Validator fails