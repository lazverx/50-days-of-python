import importlib
import pkgutil
import plugins


class PluginBase:
    """Base class for all plugins."""
    name: str = "BasePlugin"

    def run(self, *args, **kwargs):
        raise NotImplementedError("Plugin must implement run() method.")


def load_plugins():
    """Dynamically discover and load all plugins in the plugins package."""
    loaded_plugins = []

    for _, module_name, _ in pkgutil.iter_modules(plugins.__path__):
        module = importlib.import_module(f"plugins.{module_name}")

        # Search for subclasses of PluginBase
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, PluginBase) and attr is not PluginBase:
                loaded_plugins.append(attr())

    return loaded_plugins


if __name__ == "__main__":
    plugins_list = load_plugins()
    print("=== Loaded Plugins ===")
    for plugin in plugins_list:
        print(f"- {plugin.name}")

    print("\n=== Running Plugins ===")
    for plugin in plugins_list:
        plugin.run()
