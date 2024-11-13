
# Description
A small example for showing building a multi datasource reader by `hatch` and `pluggy`

# Execution
```bash
cd pluggy-demo-reader
pip install -e .

cd pluggy-demo-reader/extension/plugins/pgsql
pip install -e .

python reader/runner.py
```
Result:
```bash
Registered hooks: {'limit': <HookCaller 'limit'>, 'read': <HookCaller 'read'>}
mysql limit 5 tb_plugin_data
pgsql limit 5 tb_plugin_data
mysql read tb_plugin_data
pgsql read tb_plugin_data
```
