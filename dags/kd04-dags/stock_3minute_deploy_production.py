#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('stock_3minute_deploy_production',
          default_args=default_args,
          schedule_interval='0 6 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

stock_3minute_deploy_production = BashOperator(task_id="stock_3minute_deploy_production",
                                               bash_command="sh /usr/lib/carter/stock-3minute-source/stock_3minute_source/scripts/call_stock_3minute.sh ",
                                               dag=dag)
