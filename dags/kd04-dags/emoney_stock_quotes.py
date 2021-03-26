#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {'owner': 'afroot04', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('emoney_stock_quotes',
          default_args=default_args,
          schedule_interval='39 9 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

sync_dayquota = BashOperator(task_id="sync_dayquota", bash_command="sh /lib/carter/dbsync/scripts/sync_dayquota.sh ",
                             dag=dag)

trigger_daily_am_task = TriggerDagRunOperator(
    task_id='trigger_daily_am_task',
    trigger_dag_id='KD05_kdalpha_daily_am_task',
    trigger_rule='all_done',
    dag=dag
)

sync_dayquota >> trigger_daily_am_task
