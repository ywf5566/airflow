#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}

dag = DAG('sync_announcement',
          default_args=default_args,
          schedule_interval=' */30 * * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))
          
sync_announce = BashOperator(task_id="sync_announce", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_announce.sh ", dag=dag)
