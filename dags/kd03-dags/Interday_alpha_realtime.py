#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('Interday_alpha_realtime',
          default_args=default_args,
          schedule_interval='40 10 * * 1-5',
          catchup=False,
          start_date=datetime(2020, 12, 17, 10, 40))
realtime_cal_factor = BashOperator(task_id="realtime_cal_factor", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_realtime.sh ", dag=dag)
