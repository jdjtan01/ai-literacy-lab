"""Shared helper. Reads ANTHROPIC_API_KEY from your environment (never hard-code keys)."""
import os, sys
try:
    import anthropic
except ImportError:
    sys.exit("Run: pip install anthropic")

MODEL = os.environ.get("MODEL", "claude-sonnet-5-5")  # change via: MODEL=... python script.py

def ask(prompt, system=None, max_tokens=600, temperature=None):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY first (see README.md).")
    kw = dict(model=MODEL, max_tokens=max_tokens,
              messages=[{"role": "user", "content": prompt}])
    if system: kw["system"] = system
    if temperature is not None: kw["temperature"] = temperature
    r = anthropic.Anthropic().messages.create(**kw)
    return r.content[0].text, r.usage
