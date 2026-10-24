"""Week 8: structured extraction with validation, one retry, and field-level accuracy."""
import json, re
from common import ask
FIELDS = {"vendor": str, "invoice_date": str, "total_amount": (int, float), "currency": str}
PROMPT = """Extract fields from the text between <text> tags. Return only JSON, no commentary:
{{"vendor": string, "invoice_date": "YYYY-MM-DD" or null, "total_amount": number or null,
  "currency": "USD"|"EUR"|"PHP"|"other" or null}}
If a field is missing or ambiguous (for example 7/9/2025), use null. Do not guess.
<text>
{text}
</text>"""

def parse(raw):
    d = json.loads(re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.M).strip())
    for k, t in FIELDS.items():
        if k not in d: raise ValueError(f"missing field {k}")
        if d[k] is not None and not isinstance(d[k], t): raise ValueError(f"bad type for {k}")
    return d

docs = [t.strip() for t in open("../data/invoices.txt", encoding="utf-8").read().split("=====")]
key = json.load(open("../data/invoices_key.json"))
good = total = fails = 0
for text, truth in zip(docs, key):
    prompt = PROMPT.format(text=text)
    for attempt in (1, 2):
        raw, _ = ask(prompt, max_tokens=200)
        try: out = parse(raw); break
        except Exception as e:
            prompt += f"\n\nYour last reply was invalid ({e}). Return valid JSON only."
            out = None
    if out is None: fails += 1; out = {}
    for k in FIELDS:
        total += 1; hit = out.get(k) == truth[k]; good += hit
        if not hit: print(f"{truth['vendor']}: {k} expected {truth[k]!r} got {out.get(k)!r}")
print(f"\nField accuracy: {good}/{total} = {good/total:.0%} | invalid outputs after retry: {fails}")
