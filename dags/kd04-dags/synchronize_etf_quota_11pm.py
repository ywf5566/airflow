#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('synchronize_etf_quota_11pm',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))
          
sync_etf_dayquota_at_8pm = BashOperator(task_id="sync_etf_dayquota_at_8pm", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_kdb_etf_dayquota_at_11pm.sh ", dag=dag)
