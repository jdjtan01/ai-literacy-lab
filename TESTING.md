# Test and review checklist

Do this once after you deploy, and again after any big edit. Tick each box. Write down anything that fails with the page, device and browser.

## 1. Load and links
- [ ] The site opens at your GitHub Pages address with no blank page.
- [ ] Open the browser console (F12). There are no red errors. If lessons or chapters are missing, `lessons.js`, `chapters.js` or `quizzes.js` did not upload next to `index.html`.
- [ ] Sidebar: Overview, all 12 weeks, Glossary, Practice files, Prompt journal and Toolkit each open.
- [ ] Practice files page: click every link. None shows 404. The zip download works.

## 2. Each week (do at least weeks 1, 3, 6, 9 and 12, then spot-check the rest)
- [ ] Learn tab shows the objectives, the full chapter, common mistakes, key terms, study plan, self-check questions and the deep dive.
- [ ] Code blocks are readable and not cut off. Long lines scroll or wrap.
- [ ] Practice tab: ticking exercises saves, and the progress bar moves.
- [ ] Progress check: grading a quiz shows a score and a pass or fail, and shows correct answers with explanations for misses.
- [ ] Each week has 8 questions. Answer positions are not obviously in a pattern.

## 2b. Final exam and search
- [ ] Final exam shows 30 questions, including one scenario question per week. Grading shows a score and lists misses with explanations and week links. Reload gives a different set.
- [ ] Best exam score appears in the sidebar and survives a reload.
- [ ] Search finds terms from chapters and the glossary and links to the right week.

## 3. Saving and data
- [ ] Reload the page. Ticks, scores and journal entries are still there.
- [ ] Toolkit: Export progress downloads a file. Clear progress works after confirming. Import restores it.
- [ ] Prompt journal: add an entry, reload, delete an entry.
- [ ] Glossary: search narrows the list. Week links jump to the right week.
- [ ] Open the site in a private window. It starts fresh with no errors.

## 4. Devices and browsers
- [ ] Chrome or Edge on a computer
- [ ] Firefox
- [ ] Safari (Mac or iPhone)
- [ ] An Android phone and an iPhone: the menu button opens and closes the sidebar, text is readable, tables scroll sideways and the page does not.
- [ ] Zoom to 200 percent. Nothing overlaps.

## 5. Accessibility
- [ ] Use only the keyboard (Tab, Shift+Tab, Enter, Space). You can reach and use every control, and the focus outline is visible.
- [ ] Quiz options can be chosen with the keyboard.
- [ ] Text contrast is comfortable on your screen in a bright room.

## 6. Practice scripts (needs an API key you control)
- [ ] Follow practice/README.md to set up. The key is an environment variable, never a file.
- [ ] `01_token_usage.py` runs. If it errors on the model name or temperature, edit `MODEL` in `common.py`, or remove the temperature setting.
- [ ] `02_classify.py`, `03_extract.py` and `04_grounded_qa.py` run and print a score.
- [ ] `05_mini_rag.py` runs. It should find the right policy line for all 5 answerable questions in its retrieval step.
- [ ] You checked your provider's current pricing before running anything in a loop.

## 7. Content review (give this to someone who knows the subject)
- [ ] Week 2: are the simplified explanations of tokens, attention and sampling acceptable?
- [ ] Weeks 8 to 10: are statements about structured output, no-code tools and the Model Context Protocol still current?
- [ ] Week 11: are the notes on privacy, copyright and the EU AI Act, NIST and the Philippines Data Privacy Act accurate for your audience? This is general guidance, not legal advice.
- [ ] All fictional examples (the permit office, Maya, Rina, the clinic, the Northwind policy) are clearly fictional and fine to publish.
- [ ] Study-plan times and the 6 to 8 hours a week estimate match what a real learner needs. Try one week with a volunteer.
- [ ] Course alignment lines (Google AI Essentials, Prompting Essentials, DeepLearning.AI, Elements of AI, Udemy) are still accurate. Only the Google courses were checked, and only against secondary summaries.

## 8. Before you share it
- [ ] No API key, password or personal data is in any file in the repo.
- [ ] The repo is public only if you intend that. Everything in it is readable.
- [ ] You have a way for learners to report problems, such as a GitHub Issues link.
