#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('sync_em_stock',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

sync_em_stock_list = BashOperator(task_id="sync_em_stock_list",
                                  bash_command="/usr/lib/carter/dbsync/scripts/sync_em_stock_list.sh ", dag=dag)
