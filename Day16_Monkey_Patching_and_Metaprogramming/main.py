import types


# === Normal Class ===
class MathOps:
    def add(self, x, y):
        return x + y


# --- Monkey Patching Example ---
def new_add(self, x, y):
    print(f"[MonkeyPatch] Adding {x} and {y}")
    return x + y + 100  # intentionally changed behavior


# === Metaprogramming Example with Dynamic Class Creation ===
def method_factory(msg):
    def dynamic_method(self):
        return f"Dynamic says: {msg}"
    return dynamic_method


# Create class dynamically using `type`
DynamicClass = type(
    "DynamicClass",
    (object,),
    {
        "hello": lambda self: "Hello from dynamic class!",
        "custom": method_factory("I was generated at runtime 🚀"),
    }
)


# === Runtime Patching Example ===
class Service:
    def run(self):
        return "Running service..."


def patch_service():
    def hacked_run(self):
        return "[Patched] Service intercepted!"
    Service.run = hacked_run  # Replace method at runtime


if __name__ == "__main__":
    print("=== Monkey Patching ===")
    m = MathOps()
    print("Before patch:", m.add(2, 3))
    # Apply monkey patch
    MathOps.add = new_add
    print("After patch:", m.add(2, 3))

    print("\n=== Dynamic Class with type() ===")
    obj = DynamicClass()
    print(obj.hello())
    print(obj.custom())

    print("\n=== Runtime Service Patching ===")
    s = Service()
    print("Before patch:", s.run())
    patch_service()
    print("After patch:", s.run())
