# Day 18 – Python Internals

**Date:** 2025-09-15  

## What I Learned
- Python object model: identity (`id`), equality (`==`), and reference comparison (`is`).
- How Python manages memory with reference counting and garbage collection.
- Using the `gc` module to inspect and force collection.
- Inspecting Python bytecode using the `dis` module.

## Tasks Completed
- Wrote a demo for object identity and reference counting.
- Created circular references to test garbage collection.
- Disassembled a function into Python bytecode.

## Files
- `main.py` → Python internals demo.

## How to Run
```bash
python main.py
