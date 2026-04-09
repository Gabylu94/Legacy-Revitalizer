# LOG.md

## Three prompts that worked best

### 1 — Map the mess before touching it

**Prompt:** Explain what `process_data.py` does step by step: data flow, bad practices, security risks, and design issues.

**Why it helped:** It surfaced everything that actually mattered—globals (`l`, `d`), the overloaded `fn`, plaintext auth, unsafe file I/O, dead code, and weak input handling—so later changes targeted real problems instead of random cleanup.

---

### 2 — Plan under SOLID, then code

**Prompt:** How can I refactor `process_data.py` to follow SOLID and remove globals? Give a step-by-step plan **before** writing any code.

**Why it helped:** It forced an ordered sequence (naming → split responsibilities → errors → security → dead code removal) so the refactor stayed coherent and nothing important was skipped.

---

### 3 — Split the monolith into classes

**Prompt:** Extract persistence, authentication, and in-memory data into **separate classes**, each with a single responsibility, without changing behavior.

**Why it helped:** That was the main structural win: `Authenticator`, `DataManager`, and `FileHandler` replaced the god function and globals. Follow-up prompts (hashing/env vars, try/except and validation, JSON/`with`/`__main__`, removing unused code) then refined those classes without another full rewrite.
