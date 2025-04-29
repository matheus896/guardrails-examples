# Importar Guardião e Validador
from guardrails.hub import BanList
from guardrails import Guard

# Configurar o Guardião com palavras proibidas
guardiao = Guard().use(
    BanList(["porra", "merda"]), on_fail = "exception"
)

# Testando um texto permitido (validação aprovada)
guardiao.validate("Este é um texto seguro.")  # Validação aprovada

try:
    # Testando um texto com palavras proibidas (validação falha)
    guardiao.validate("Vai  p o r r @  e  m e r d @")
    print("Passou")
except Exception as e:
    print("Erro de validação:", e)  # Exibe uma mensagem mais clara sobre a exceção gerada pela falha na validação

