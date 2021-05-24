#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
default_args = {'owner': 'afroot04', 'start_date': datetime.strptime('2021-05-23 08:40:00', "%Y-%m-%d %H:%M:%S")}
dag = DAG('daily_universe_kdcode', default_args=default_args, schedule_interval='40 8 * * *')

main = BashOperator(
    task_id='main',
    bash_command=r'''sh /usr/lib/carter/dbsync/scripts/daily_universe_code.sh  ''',
    trigger_rule='all_success',
    dag=dag)
