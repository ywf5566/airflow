#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('update_event_block_correlation',
          default_args=default_args,
          schedule_interval='0 */2 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 18, 16, 0))
updateEventBlockCorrelation = BashOperator(task_id="updateEventBlockCorrelation", bash_command="sh /usr/lib/carter/separateDagobahTask/scripts/KeydriverdbProd/updateEventBlockCorrelation.sh ", dag=dag)
