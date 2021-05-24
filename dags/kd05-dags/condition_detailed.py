#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('condition_detailed',
          default_args=default_args,
          schedule_interval='*/5 * * * *',
          catchup=False,
          start_date=datetime(2021, 5, 24, 12, 0))

condition_detailed = BashOperator(task_id="condition_detailed",
                                  bash_command="sh /usr/lib/carter/dbsync/scripts/condition_detailed.sh ", dag=dag)
