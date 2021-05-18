#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {'owner': 'afroot05', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('Sync_dayquota_am_task',
          default_args=default_args,
          schedule_interval='40 9 * * *',
          catchup=False,
          start_date=datetime(2021, 5, 17, 9, 40))

sync_dayquota = BashOperator(task_id="sync_dayquota", bash_bash_command="sh /lib/carter/dbsync/scripts/sync_dayquota.sh ",
                             dag=dag)
kdalpha_am_start_task = BashOperator(task_id="kdalpha_am_start_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_start_task.sh prod ", dag=dag)
kdalpha_daily_am_task = BashOperator(task_id="kdalpha_daily_am_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh prod ", dag=dag)
kdalpha_strategy_rank_task = BashOperator(task_id="kdalpha_strategy_rank_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh prod ", dag=dag)
kdalpha_am_end_task = BashOperator(task_id="kdalpha_am_end_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_end_task.sh prod ", dag=dag)


sync_dayquota >> kdalpha_am_start_task
kdalpha_strategy_rank_task >> [kdalpha_am_end_task]
kdalpha_am_start_task >> [kdalpha_daily_am_task]
kdalpha_daily_am_task >> [kdalpha_strategy_rank_task]