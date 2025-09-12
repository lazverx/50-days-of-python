from core import PluginBase


class HelloPlugin(PluginBase):
    name = "HelloPlugin"

    def run(self):
        print("Hello from HelloPlugin! 👋")
