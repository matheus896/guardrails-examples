# Importar Guard e o Validador
from guardrails.hub import RegexMatch
from guardrails import Guard

# Configurar o Guard com o validador
guard = Guard().use(
    RegexMatch, regex="Open.*", 
    on_fail="exception"
)

# Testar uma entrada válida
guard.validate(
    "OpenAI lançou recentemente o GPT-4.5, ele é o mais recente da série GPT"
)

try:
    # Testar uma entrada inválida
    guard.validate(
        "Llama2 da MetaAI é o mais recente da sua série de LLMs de código aberto."
    )
except Exception as e:
    print(e)
