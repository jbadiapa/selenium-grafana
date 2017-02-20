# selenium-grafana

This is selenium unit test to check grafana

To set up the selenium environment you can take a look at
https://gist.github.com/jbadiapa/921c7719c59bfd89cf862fd6bef07d6d

To run the unit test selenium and the chrome plugin are needed.

To run the tox, the Xvfb program is needed:
---
yum install xvfb
---

It can be executed as:
---
python grafana_test.py --ip 192.168.33.51 --username admin --password admin --port 443 --protocol https
---

or edit the tools/run_test.sh to change the --ip argument:
---
tox
---
