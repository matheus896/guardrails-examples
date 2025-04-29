# Criar um guard-rail (restrição) usando um validador de texto sem sentido
# guardrails create --validators hub://guardrails/gibberish_text --guard-name guardiao_texto_sem_sentido

from guardrails import Guard
from guardrails.hub import GibberishText

# Criando um guardião chamado 'guardiao_texto_sem_sentido'
guard = Guard().use(
    GibberishText, on_fail="exception"
)

try:
    guard.validate(
        """I was running in the forest when I dove into a shoe."""
    )
    print("Texto coerente")
    
except Exception as e:
    print(f"Não faz sentido: {e}")
