# Importar Guardião e Validador
from guardrails.hub import RestrictToTopic
from guardrails import Guard

# Configurar o Guardião
guardiao = Guard().use(
    RestrictToTopic(
        valid_topics=["esportes"],  # Tópicos permitidos
        invalid_topics=["música"],  # Tópicos proibidos
        disable_classifier=True,    # Desativar o classificador
        disable_llm=False,          # Manter o LLM ativado
        on_fail="exception"         # Lançar exceção se falhar
    )
)


topico1 = """O Vasco vence o Flamengo por 6x0, que time incrível."""

topico2 = """Os Beatles foram uma banda pop-rock inglesa 
             carismática da década de 1960."""



# Testando um texto sobre esportes (validação bem-sucedida)
try:
    guardiao.validate(topico1)
    print("Tópico 1 é válido")
except:
    print("Texto inválido")
# Testando um texto sobre música (validação falha)
try:
    guardiao.validate(topico2)  # Validação falha
except:
    print("Tópico 2 é inválido")
