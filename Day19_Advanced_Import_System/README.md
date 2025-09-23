# Day 19 – Advanced Import System

**Date:** 2025-09-16  

## What I Learned
- How Python handles imports internally (`import`, `sys.path`, `__all__`).
- Using `importlib` for dynamic imports at runtime.
- Inspecting and modifying `sys.path`.
- Creating a **custom loader** and **meta path finder** to simulate module injection.

## Tasks Completed
- Implemented normal imports with restricted exports using `__all__`.
- Dynamically imported the `math` module with `importlib`.
- Printed Python’s import search path (`sys.path`).
- Built a custom loader & finder to create a **fake module** (`dynamic_module`) on the fly.

## Files
- `main.py`
