#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('sync_american_stock_info',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))
          
sync_american_stock_info = BashOperator(task_id="sync_american_stock_info", bash_command="sh /usr/lib/carter/dbsync/scripts/choise_american_stock.sh ", dag=dag)
