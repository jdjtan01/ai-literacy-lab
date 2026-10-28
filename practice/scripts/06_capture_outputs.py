"""Capture REAL outputs for your own examples. Writes a dated markdown file you can paste into your notes.
Run: python 06_capture_outputs.py        (set RUNS below for repeats)"""
import json, os, datetime
from common import ask, MODEL
RUNS = 2
prompts = json.load(open("../data/sample_prompts.json", encoding="utf-8"))
os.makedirs("../outputs", exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
path = f"../outputs/captured_{stamp}.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(f"# Captured outputs\nModel: {MODEL}\nTime: {stamp}\nThese are real responses from your own runs. They will differ if you run again.\n\n")
    for p in prompts:
        f.write(f"## {p['id']}\n```\n{p['prompt']}\n```\n")
        for r in range(RUNS):
            text, usage = ask(p["prompt"], max_tokens=400)
            f.write(f"\n**Run {r+1}** (in {usage.input_tokens} tokens, out {usage.output_tokens})\n\n{text.strip()}\n")
        f.write("\n")
print("Saved", path)
