from core import PluginBase


class MathPlugin(PluginBase):
    name = "MathPlugin"

    def run(self):
        print("2 + 2 =", 2 + 2)
