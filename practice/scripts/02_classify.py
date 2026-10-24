"""Week 4: few-shot classifier + accuracy. Edit PROMPT, re-run, compare versions."""
import csv
from common import ask
LABELS = ["Billing", "Technical", "Feedback", "Other"]
PROMPT = """Classify the customer message into exactly one label: Billing, Technical, Feedback, or Other.
Reply with the label only.

Message: "I was charged twice this month." -> Billing
Message: "The app crashes on launch." -> Technical
Message: "Please add a calendar view." -> Feedback
Message: "Where can I find your careers page?" -> Other

Message: "{msg}" ->"""  # v1: change me, keep a log in the Prompt Journal

rows = list(csv.DictReader(open("../data/messages.csv", encoding="utf-8")))
ok = edge_ok = edge_n = 0
for r in rows:
    pred, _ = ask(PROMPT.format(msg=r["message"]), max_tokens=10)
    pred = pred.strip().strip('."').split()[0] if pred.strip() else ""
    hit = pred == r["label"]
    ok += hit
    if r["edge"] == "1": edge_n += 1; edge_ok += hit
    if not hit: print(f"MISS: {r['message']!r} expected {r['label']} got {pred}")
print(f"\nAccuracy: {ok}/{len(rows)} = {ok/len(rows):.0%}")
print(f"Edge cases: {edge_ok}/{edge_n}")
