"""Week 2: see token usage and how temperature changes output."""
from common import ask
prompt = "Write a one-sentence tagline for a budgeting app for freelancers."
for temp in (0.0, 1.0):
    print(f"\n--- temperature {temp} ---")
    for run in range(3):
        try:
            text, u = ask(prompt, max_tokens=60, temperature=temp)
        except Exception as e:  # some models restrict sampling settings
            print("Could not set temperature:", e); break
        print(f"run {run+1}: in={u.input_tokens} out={u.output_tokens} | {text.strip()}")
