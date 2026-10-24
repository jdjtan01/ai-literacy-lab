"""Week 10: minimal RAG with no extra dependencies.
Retrieval here is simple word overlap. Exercise: swap retrieve() for embeddings and compare."""
import json, re
STOP = set("a an the of to for in on is are do does can i my me how what many much per or and be it".split())

def words(t): return {w for w in re.findall(r"[a-z0-9:$]+", t.lower()) if w not in STOP}

def retrieve(question, chunks, k=2):
    qw = words(question)
    scored = sorted(chunks, key=lambda c: len(qw & words(c)), reverse=True)
    return [c for c in scored[:k] if qw & words(c)]

if __name__ == "__main__":
    from common import ask
    chunks = [l for l in open("../data/policy.txt", encoding="utf-8").read().splitlines()[1:] if l.strip()]
    qs = json.load(open("../data/policy_questions.json"))
    found = good = 0
    for item in qs:
        ctx = retrieve(item["q"], chunks)
        if item["expect"] and any(item["expect"] in c for c in ctx): found += 1
        source = "\n".join(ctx) or "(nothing retrieved)"
        ans, _ = ask(f'Answer using only <source>. If missing, reply exactly: "Not found in the provided text."\n<source>\n{source}\n</source>\nQuestion: {item["q"]}', max_tokens=150)
        refused = "Not found in the provided text" in ans
        good += refused if item["expect"] is None else (item["expect"] in ans and not refused)
        print(f"{item['q']}\n  retrieved: {len(ctx)} chunk(s) | {ans.strip()[:120]}")
    n = sum(1 for i in qs if i["expect"])
    print(f"\nRetrieval hit rate: {found}/{n} | Answer score: {good}/{len(qs)}")
