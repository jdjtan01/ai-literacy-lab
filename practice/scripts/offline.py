"""A tiny rule-based stand-in for a language model, so the scripts run with NO API key and NO cost.
It is NOT AI. It uses keyword and pattern rules, and it makes mistakes real models would not.
Use it to see how the scripts, scoring and validation work. Use a real model to judge model quality."""
import re, random
STOP = set("a an the of to for in on is are do does can i my me how what many much per or and be it".split())
MONTHS = "jan feb mar apr may jun jul aug sep oct nov dec".split()

class Usage:
    def __init__(self, i, o): self.input_tokens, self.output_tokens = i, o

def _words(t): return {w for w in re.findall(r"[a-z0-9:$]+", t.lower()) if w not in STOP}

def _num(s):
    s = s.strip(".,")
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".") if re.search(r",\d{2}$", s) else s.replace(",", "")
    try: return float(s)
    except ValueError: return None

def _classify(msg):
    m = msg.lower()
    rules = [("Billing", ["charge", "refund", "invoice", "billing", "receipt", "card", "coupon", "payment", "money", "price"]),
             ("Technical", ["crash", "log in", "login", "logging", "error", "bug", "loads", "load ", "export", "blank", "notification", "startup"]),
             ("Feedback", ["love", "great", "would be", "please add", "consider", "confusing", "thank", "dark mode"])]
    for label, keys in rules:
        if any(k in m for k in keys): return label
    return "Other"

def _extract(text):
    vendor = None
    for pat in [r"(?:from|FROM:?)\s+([A-Z][\w&\.\- ]+?)(?:\s+for\b|\.|,|\n|$)", r"^([A-Z][\w&\.\- ]+)"]:
        mt = re.search(pat, text.strip(), re.M)
        if mt: vendor = mt.group(1).strip(); break
    date = None
    mt = re.search(r"\d{4}-\d{2}-\d{2}", text)
    if mt: date = mt.group(0)
    else:
        mt = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", text)
        if mt: date = f"{mt.group(3)}-{mt.group(2)}-{mt.group(1)}"
        else:
            mt = re.search(r"\b(%s)[a-z]*\.? (\d{1,2}),? (\d{4})" % "|".join(m.capitalize() for m in MONTHS), text)
            if mt: date = f"{mt.group(3)}-{MONTHS.index(mt.group(1).lower())+1:02d}-{int(mt.group(2)):02d}"
    total = None
    ms = re.findall(r"(?:total due|total charged|total|gesamt|amount)[^\d\n]*([\d.,]+)", text, re.I)
    if ms: total = _num(ms[-1])
    else:
        ms = re.findall(r"([\d.,]+)\s*(?:USD|EUR|PHP|CHF|pesos)", text)
        if ms: total = _num(ms[-1])
    cur = None
    if re.search(r"\bUSD\b", text): cur = "USD"
    elif re.search(r"\bEUR\b", text): cur = "EUR"
    elif re.search(r"\bPHP\b|pesos", text): cur = "PHP"
    elif re.search(r"\bCHF\b", text): cur = "other"
    return {"vendor": vendor, "invoice_date": date, "total_amount": total, "currency": cur}

def reply(prompt, temperature=None):
    p = prompt
    if "<text>" in p and "invoice_date" in p:
        body = p.rsplit("<text>", 1)[1].split("</text>", 1)[0]
        out = __import__("json").dumps(_extract(body))
        if "was invalid" not in p and len(body) % 3 == 0:   # simulate a model adding chatter, so you can see the retry work
            return "Here is the JSON you asked for: " + out
        return out
    if "<source>" in p and "Question:" in p:
        src = p.rsplit("<source>", 1)[1].split("</source>", 1)[0]
        q = p.rsplit("Question:", 1)[1]
        best, score = None, 0
        for line in src.splitlines():
            s = len(_words(q) & _words(line))
            if s > score: best, score = line.strip(), s
        return best if score >= 2 else "Not found in the provided text."
    if "Message:" in p and "Classify" in p:
        return _classify(p.rsplit("Message:", 1)[1])
    if "tagline" in p.lower():
        opts = ["Baked fresh daily", "Fresh from our oven", "Warm bread, warm welcome", "Rise and shine", "Crumbs of joy"]
        return opts[0] if not temperature else random.choice(opts)
    return "Offline stand-in: no rule for this prompt. Use a real model for open-ended tasks."

def ask(prompt, temperature=None):
    t = reply(prompt, temperature)
    return t, Usage(len(prompt) // 4, len(t) // 4)
