# Self-Correcting AI Agent for Incident Resolution

## Problem

Most AI agents fail silently.
They take actions, but when things go wrong, they loop or produce useless outputs.

## Solution

This project builds an autonomous agent that:

* Detects failures
* Logs them explicitly
* Avoids repeating the same mistake
* Adapts its behavior

## Key Idea

Failure is treated as a **first-class signal**, not noise.

---

## Architecture

```
Logs → Plan → Act → Verify → Detect Failure → Adapt
```

* Planner (LLM - Groq / GPT-OSS)
* Tool Layer (modular actions)
* Memory (history + failures)
* Control Loop (self-correcting)

---

## Features

* Autonomous decision-making
* Failure tracking
* Loop detection
* Modular tools (plug-and-play)
* Root cause + prevention summary

---

## Demo

### 1. Failure Case

```
python main.py -f
```

Agent detects invalid log path and enters failure loop → recorded.

### 2. Resolution Case

```
python main.py logs.txt
```

Agent:

* Reads logs
* Diagnoses issue
* Executes fix
* Verifies resolution

---

## Example Output

```
FINAL: resolved

TRACE:
...

FAILURES:
...

SUMMARY:
{
  "root_cause_guess": "...",
  "actions_taken": [...],
  "prevention": "..."
}
```

---

## Tech Stack

* Python
* Groq (openai/gpt-oss-120b)
* Modular agent architecture

---

## Why This Matters

Most agents:

```
input → LLM → output
```

This system:

```
input → loop → failure → correction → outcome
```

---

## Future Work

* Persistent failure memory (vector DB)
* Real infrastructure integration
* Multi-agent planning

---
