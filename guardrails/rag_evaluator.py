# Import Guard and Validator
from guardrails.hub import LlmRagEvaluator, HallucinationPrompt
from guardrails import Guard

# Setup Guard
guard = Guard().use(
    LlmRagEvaluator(
        eval_llm_prompt_generator=HallucinationPrompt(prompt_name="hallucination_judge_llm"),
        llm_evaluator_fail_response="hallucinated",
        llm_evaluator_pass_response="factual",
        llm_callable="gpt-4o-mini",
        on_fail="exception",
        on="prompt"
    ),
)

metadata = {
    "user_message": "User message",
    "context": "Context retrieved from RAG application",
    "llm_response": "Proposed response from LLM before Guard is applied"
}

guard.validate(llm_output="Proposed response from LLM before Guard is applied", metadata=metadata)