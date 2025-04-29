from guardrails import Guard
from guardrails.hub import GibberishText
guard = Guard()
guard.name = 'guardiao_texto_sem_sentido'
print("GUARD PARAMETERS UNFILLED! UPDATE THIS FILE!")  # TODO: Remove this when parameters are filled.
guard.use(GibberishText())  # TODO: Add parameters.