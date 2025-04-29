from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Carregando variáveis de ambiente, se necessário
load_dotenv()

# Definição do modelo para um prato culinário
class Dish(BaseModel):
    cozinha: str = Field(description="Tipo de culinária (ex: italiana, japonesa, etc.)")
    prato: str = Field(description="Nome do prato recomendado")

from guardrails import Guard

# Prompt modificado para pedir uma recomendação de prato culinário
prompt = """
    Eu gosto de: Pizza, Churrasco, Sushi, 
    Com base nas minhas preferências, qual tipo de culinária você recomenda e qual prato específico eu deveria experimentar?

    ${gr.complete_json_suffix_v2}
"""
guard = Guard.for_pydantic(output_class=Dish)

# Simulação de interação com o modelo de IA
res = guard(
    model="gpt-4o-mini-2024-07-18",
    messages=[{
        "role": "user",
        "content": prompt
    }]
)

# Exibindo a saída validada
print(f"Recomendação de prato: {res.validated_output}")
