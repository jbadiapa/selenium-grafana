#!/bin/bash
TESTPATH=`dirname $(readlink -f $0)`
PATH=$PATH:.
xvfb-run python selenium-grafana/grafana_test.py --ip 192.168.33.51 --username admin --password admin --protocol https
