"""Shared helper. With no API key, scripts run in OFFLINE mode using a simple stand-in (see offline.py).
With ANTHROPIC_API_KEY set, they call a real model. Force offline with OFFLINE=1. Never hard-code keys."""
import os, sys
MODEL = os.environ.get("MODEL", "claude-sonnet-5-5")  # change via: MODEL=... python script.py
OFFLINE = os.environ.get("OFFLINE") == "1" or not os.environ.get("ANTHROPIC_API_KEY")
if OFFLINE:
    print("OFFLINE MODE: using a simple rule-based stand-in, not a real AI model. "
          "Results show how the scripts work, not how real models perform.\n")

def ask(prompt, system=None, max_tokens=600, temperature=None):
    if OFFLINE:
        from offline import ask as off
        return off(prompt, temperature)
    try:
        import anthropic
    except ImportError:
        sys.exit("Run: pip install anthropic")
    kw = dict(model=MODEL, max_tokens=max_tokens, messages=[{"role": "user", "content": prompt}])
    if system: kw["system"] = system
    if temperature is not None: kw["temperature"] = temperature
    r = anthropic.Anthropic().messages.create(**kw)
    return r.content[0].text, r.usage
