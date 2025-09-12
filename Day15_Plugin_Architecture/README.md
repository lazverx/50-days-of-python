# Day 15 – Plugin Architecture

**Date:** 2025-09-12  

## What I Learned
- How to design a **plugin architecture** in Python.
- Dynamically discovering and loading modules using `pkgutil` and `importlib`.
- Creating a `PluginBase` class for consistent plugin behavior.

## Tasks Completed
- Built a `core.py` that scans the `plugins/` folder.
- Implemented two example plugins:
  - `HelloPlugin` → prints a greeting.
  - `MathPlugin` → performs a simple calculation.
- Ensured that all plugins extend `PluginBase` and implement a `run()` method.

## Files
- `core.py` → Main program to load and run plugins.
- `plugins/hello.py` → Example greeting plugin.
- `plugins/math_plugin.py` → Example math plugin.

## How to Run
```bash
python core.py
