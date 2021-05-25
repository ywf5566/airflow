#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('newsProcessMonitor',
          default_args=default_args,
          schedule_interval='*/30 * * * *',
          catchup=False,
          start_date=datetime(2021, 5, 25, 14, 0))

monitorNewsProcess = BashOperator(task_id="monitorNewsProcess",
                                  bash_command="sh /usr/lib/carter/separateDagobahTask/scripts/Monitor/monitorNewsProcess.sh ",
                                  dag=dag)
