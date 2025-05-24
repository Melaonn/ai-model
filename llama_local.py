from llama_cpp import Llama

# Load the GGUF model (adjust path if needed)
llm = Llama(model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=4096, n_threads=8)

def ask_llm(question: str) -> str:
    prompt = f"[INST] {question} [/INST]"
    
    output = llm(prompt, max_tokens=512, stop=["</s>"])
    
    return output["choices"][0]["text"].strip()
