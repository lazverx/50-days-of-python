# Day 20 – DSL (Domain Specific Language) with Python

**Date:** 2025-09-17  

## What I Learned
- The concept of **Domain Specific Languages (DSLs)** and how Python can be used to create them.
- Designing a fluent API with method chaining for readability.
- Simulating a mini task automation system with custom commands (`run`, `print`, `wait`).

## Tasks Completed
- Built a `Task` class that allows chaining commands to create a DSL-like interface.
- Implemented `run`, `print`, and `wait` as domain-specific commands.
- Executed tasks sequentially to mimic a real automation workflow.

## Files
- `main.py`

## Example Usage
```python
build = (
    Task("Build Project")
    .print("Starting build process...")
    .run("python compile.py")
    .wait(2)
    .print("Build completed successfully!")
)

deploy = (
    Task("Deploy Project")
    .print("Deploying to staging server...")
    .run("scp project user@staging:/var/www")
    .wait(3)
    .print("Deployment finished!")
)

build.execute()
deploy.execute()
