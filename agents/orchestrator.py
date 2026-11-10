import os
import urllib.request
import json

def query_local_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            res_body = json.loads(response.read().decode('utf-8'))
            return res_body.get("response", "Error generating response")
    except Exception as e:
        return f"Connection error: {e}"

def run_veera_pipeline():
    print("--- [VEERA AI] 4-Agent Autonomous Pipeline Initializing ---")
    
    # 1. Sam Altman / Strategist Persona
    print("\n[1/4] Strategist Agent (Sam Altman) analyzing high-margin micro-SaaS opportunities...")
    strat_prompt = "Act as Sam Altman. Identify 1 high-margin, zero-cost digital micro-SaaS product that can be built using Python and hosted for free on Vercel."
    strategy = query_local_ollama(strat_prompt)
    print(strategy[:300] + "...\n")

    # 2. Bill Gates / Architect Persona
    print("[2/4] Architect Agent (Bill Gates) designing system architecture...")
    arch_prompt = f"Based on this strategy: {strategy[:200]}, act as Bill Gates. Write a clean, enterprise-grade directory structure and file layout for this project in Python."
    architecture = query_local_ollama(arch_prompt)
    print(architecture[:300] + "...\n")

    # 3. Elon Musk / Builder Persona
    print("[3/4] Builder Agent (Elon Musk) generating functional code...")
    builder_prompt = f"Act as Elon Musk. Write the core python code file (`app.py`) for the micro-SaaS based on the architecture. Make it concise, functional, and ready to deploy."
    code = query_local_ollama(builder_prompt)
    
    os.makedirs("output", exist_ok=True)
    with open("output/app.py", "w") as f:
        f.write(code)
    print("Code successfully generated and saved to output/app.py\n")

    # 4. Raj Shamani / Growth Persona
    print("[4/4] Growth Agent (Raj Shamani) building organic distribution...")
    growth_prompt = "Act as Raj Shamani. Write a punchy launch post for X (Twitter) and LinkedIn to market this new micro-SaaS product with zero ad spend."
    marketing = query_local_ollama(growth_prompt)
    
    with open("output/marketing_copy.txt", "w") as f:
        f.write(marketing)
    print("Marketing copy saved to output/marketing_copy.txt\n")

if __name__ == "__main__":
    run_veera_pipeline()
