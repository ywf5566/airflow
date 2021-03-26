#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {'owner': 'afroot04', 'retries': 2, 'retry_delay': timedelta(minutes=1)}

dag = DAG('KD05_kdalpha_daily_am_task',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2021, 3, 25, 9, 0))

kdalpha_am_start_task = SSHOperator(task_id="kdalpha_am_start_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_start_task.sh prod ", dag=dag)
kdalpha_daily_am_task = SSHOperator(task_id="kdalpha_daily_am_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh prod ", dag=dag)
kdalpha_strategy_rank_task = SSHOperator(task_id="kdalpha_strategy_rank_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh prod ", dag=dag)
kdalpha_am_end_task = SSHOperator(task_id="kdalpha_am_end_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_end_task.sh prod ", dag=dag)
kdalpha_strategy_rank_task >> [kdalpha_am_end_task]
kdalpha_am_start_task >> [kdalpha_daily_am_task]
kdalpha_daily_am_task >> [kdalpha_strategy_rank_task]
