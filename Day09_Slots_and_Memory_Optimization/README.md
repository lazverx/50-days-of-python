# Day 9 – __slots__ and Memory Optimization

**Date:** 2025-09-06  

## What I Learned
- By default, Python objects store attributes in a dynamic `__dict__`, which is flexible but memory-heavy.  
- Using `__slots__` restricts allowed attributes and removes `__dict__`, leading to **significant memory savings**.  
- `__slots__` can improve performance for attribute access, but reduces flexibility (no adding new attributes outside `__slots__`).  
- Compared memory usage between a normal class and a slotted class using `sys.getsizeof`.  
- When to use:
  - ✅ Lots of small objects (e.g., millions of nodes, records).  
  - ❌ When flexibility and dynamic attributes are required.  

## Tasks Completed
- Created a normal `Person` class and a slotted `PersonSlots` class.  
- Measured memory difference.  
- Tested performance in attribute access.  

## Files
- `slotsmemory.py`  
- `README.md`
