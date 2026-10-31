# AI Literacy Lab: practice files

## Run it with no key (offline mode, free)
1. Install Python 3.10 or newer. Nothing else is needed.
2. In a terminal, go to the `scripts` folder and run, for example: `python 02_classify.py`
3. With no API key set, the scripts use `offline.py`, a small rule-based stand-in. It is NOT AI. It follows keyword and pattern rules, so it will make mistakes (for example, around 87% on the classifier and 88% on invoice extraction), and it deliberately adds chatter to some replies so you can watch the validation and retry step work.
4. Use offline mode to learn how the scripts, scoring and validation work. Do not use its scores to judge how well a real model performs.
5. `06_capture_outputs.py` refuses to run offline, because it exists to save real model output.

## Using a real model (optional, costs a little)
1. `pip install anthropic`
2. Create an API key in your provider console. Never commit it.
   - macOS/Linux: `export ANTHROPIC_API_KEY="your-key"`
   - Windows PowerShell: `$env:ANTHROPIC_API_KEY="your-key"`
3. Add a `.gitignore` containing `.env` before you push anything to GitHub.
4. Run the same scripts. Set `OFFLINE=1` to force offline mode even when a key is present.
5. The model name is set in `common.py` (override with `MODEL=...`). Check your provider's docs for current names. API calls cost money, so start with the small files here.

## Files
| File | Week | Exercise |
|---|---|---|
| scripts/01_token_usage.py | 2 | Token counts and temperature variance |
| scripts/02_classify.py + data/messages.csv | 4 | Few-shot classifier, 30 labeled messages (10 edge cases) |
| data/hallucination_questions.md | 6 | 15-question hallucination hunt (no code) |
| scripts/04_grounded_qa.py + data/policy.txt, policy_questions.json | 6 | Grounded Q&A: 5 answerable, 5 unanswerable |
| scripts/03_extract.py + data/invoices.txt, invoices_key.json | 8 | Extraction on 10 invoices, validation, retry, accuracy |
| scripts/06_capture_outputs.py + data/sample_prompts.json | 3 | Capture real model outputs for your own case studies (needs a key) |
| scripts/offline.py | all | The stand-in used when there is no key |
| scripts/05_mini_rag.py | 10 | Mini RAG with word-overlap retrieval; swap in embeddings |

## Notes
- Edit the PROMPT in each script, re-run, and log each version in the Prompt Journal.
- Invoice 4 (no date or currency) and invoice 6 (7/9/2025 is ambiguous) should return null. Models that guess are failing on purpose.
- Invoice 9 has no date or currency, and invoice 10 uses CHF, which should map to "other".
- The Northwind policy is fictional. Never treat it as real policy.
- The hallucination questions in section A name invented people and documents on purpose.
