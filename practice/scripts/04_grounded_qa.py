"""Week 6: grounded Q&A. Does the model refuse questions the source cannot answer?"""
import json
from common import ask
PROMPT = """Answer using only the text in <source>. Quote the supporting sentence.
If the answer is not in the source, reply exactly: "Not found in the provided text."
<source>
{doc}
</source>
Question: {q}"""
doc = open("../data/policy.txt", encoding="utf-8").read()
qs = json.load(open("../data/policy_questions.json"))
good = 0
for item in qs:
    ans, _ = ask(PROMPT.format(doc=doc, q=item["q"]), max_tokens=200)
    refused = "Not found in the provided text" in ans
    hit = refused if item["expect"] is None else (item["expect"] in ans and not refused)
    good += hit
    print(("OK   " if hit else "MISS ") + item["q"] + "\n     -> " + ans.strip().replace("\n", " ")[:140])
print(f"\nScore: {good}/{len(qs)}")
