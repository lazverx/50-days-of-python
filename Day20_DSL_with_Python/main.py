"""
Day 20 – Domain Specific Language (DSL) with Python
Date: 2025-09-17
"""

# ========================
# Simple Task Automation DSL
# ========================

class Task:
    def __init__(self, name):
        self.name = name
        self.commands = []

    def run(self, command):
        self.commands.append(("run", command))
        return self

    def print(self, message):
        self.commands.append(("print", message))
        return self

    def wait(self, seconds):
        self.commands.append(("wait", seconds))
        return self

    def execute(self):
        import time
        print(f"== Executing Task: {self.name} ==")
        for cmd, arg in self.commands:
            if cmd == "run":
                print(f"[RUN] {arg}")
            elif cmd == "print":
                print(f"[PRINT] {arg}")
            elif cmd == "wait":
                print(f"[WAIT] sleeping for {arg} sec...")
                time.sleep(0.1)  # shortened for demo
        print(f"== Task {self.name} Finished ==\n")


# ========================
# Example DSL Usage
# ========================

if __name__ == "__main__":
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

    # Execute both DSL-defined tasks
    build.execute()
    deploy.execute()
