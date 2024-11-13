import pluggy
import hookspecs
from hookspecs import namesapce
from plugins.mysql import reader

NAMESPACE = namesapce
HOOKSPEC = hookspecs


def main():
    pm = _plugin_manager()
    print("Registered hooks:", pm.hook.__dict__)  # 查看注册的 hooks
    runner = Runner(pm.hook)
    runner.run()


def _plugin_manager():
    pm = pluggy.PluginManager(NAMESPACE)
    pm.add_hookspecs(hookspecs)
 
    pm.load_setuptools_entrypoints(NAMESPACE)
    pm.register(reader)
    print("Available plugins:", pm.get_plugins())
    print("Hook implementations:", pm.hook.limit.get_hookimpls())
    return pm


class Runner:
    def __init__(self, hook):
        self.hook = hook

    def run(self):
        """
        run the plugin
        :return:
        """
        self.hook.limit(n=5, name="tb_plugin_data")
        self.hook.read(name="tb_plugin_data")



if __name__ == "__main__":
    main()
