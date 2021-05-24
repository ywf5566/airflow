#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('sync_zyyx',
          default_args=default_args,
          schedule_interval='30 */1 * * *',
          catchup=False,
          start_date=datetime(2021, 5, 24, 12, 0))

sync_zyyx = BashOperator(task_id="sync_zyyx", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_zyyx.sh ", dag=dag)