# Day 8 – Descriptor Protocol

**Date:** 2025-09-05  

## What I Learned
- Understanding the **descriptor protocol** in Python (`__get__`, `__set__`, `__delete__`).  
- Difference between **data descriptors** (implement both `__get__` and `__set__`) and **non-data descriptors** (only `__get__`).  
- How Python internally uses descriptors (e.g., `property`, `staticmethod`, `classmethod`).  
- How to build custom descriptors for validation and attribute control.  

## Tasks Completed
- Implemented a basic descriptor that logs attribute access.  
- Created a data descriptor to enforce type checking.  
- Compared custom descriptor with built-in `property`.  

## Files
- `descriptorprotocol.py`  
- `README.md`
