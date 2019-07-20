### Here is some tip trick for config file. I mainly use config file instead of Wato.

- Ignore service check and services: if u want to ignore some service. Add some line below into file main.mk or whatever file has extension is .mk
This will affect cmk -vII pernament.
```python
ignored_checks += [
  ('chrony', ALL_HOSTS),
  ('docker', ALL_HOSTS),
  #('NFS mount', ALL_HOSTS),
  ('postfix_mailq_status',ALL_HOSTS),
]
```

- Ignore services:
```python
ignored_services += [
  (ALL_HOSTS, ['MD Softraid','Resolve_mathias-kettner.de']),
  (ALL_HOSTS, ['Interface docker','Interface veth','Interface br-','Interface cali','Interface tunl0']),
]
```

- Check CPU Win level:
```python
# Check CPU_win Warning/crit level
winperf_cpu_default_levels = (90.0, 100.0)
```
- Check memory win:

```python
# Check memory_win Warning/crit
memory_win_default_levels = {
  "memory" : (99.0, 100.0),
  "pagefile" : (99.0, 100.0),
}
```

- Automatic inventory time:
```python
inventory_check_interval = 120
```


