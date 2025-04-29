# Importar Guardião e Validador
from guardrails.hub import DetectPII
from guardrails import Guard

# Configurar o Guardião
guardiao = Guard().use(
    DetectPII, ["EMAIL_ADDRESS", "PHONE_NUMBER"], "exception"
)

# Testando um texto seguro (validação aprovada)
guardiao.validate("Bom dia!")  # Validação aprovada

try:
    # Testando um texto contendo dados sensíveis (validação falha)
    guardiao.validate(
        "Se estiver interessado, inscreva-se em nao_e_um_email_real@guardrailsai.com"
    )  # Validação falha
except Exception as e:
    print(e)  # Exibe a exceção gerada pela falha na validação
