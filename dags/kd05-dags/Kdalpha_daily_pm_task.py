#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import TaskInstance
from airflow.operators.bash_operator import BashOperator

TI = TaskInstance
default_args = {'owner': 'afroot05', 'retries': 2, 'retry_delay': timedelta(minutes=1),
                'start_date': datetime.strptime('2021-05-17 16:36:00', "%Y-%m-%d %H:%M:%S")}
dag = DAG('Kdalpha_daily_pm_task', default_args=default_args, schedule_interval=None)
kdalpha_pm_start_task = BashOperator(
    task_id='kdalpha_pm_start_task',
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_start_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

v3_model_rsync = BashOperator(
    task_id='v3_model_rsync', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd05 ''', trigger_rule='all_success', dag=dag)

kdalpha_am_task = BashOperator(
    task_id='kdalpha_am_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh prod ''',
    trigger_rule='all_success', dag=dag)

kdalpha_pm_task = BashOperator(
    task_id='kdalpha_pm_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_pm_task.sh prod ''',
    trigger_rule='all_success', dag=dag)

kdalpha_strategy_rank_task = BashOperator(
    task_id='kdalpha_strategy_rank_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh prod ''',
    trigger_rule='all_success', dag=dag)

kdalpha_pm_end_task = BashOperator(
    task_id='kdalpha_pm_end_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_end_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

generate_kdalpha_aibs_singal = BashOperator(
    task_id='generate_kdalpha_aibs_singal', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/generate_kdalpha_aibs_signal.sh prod ''',
    trigger_rule='all_success', dag=dag)

kdalpha_pm_start_task >> v3_model_rsync
v3_model_rsync >> kdalpha_am_task
kdalpha_am_task >> kdalpha_pm_task
kdalpha_pm_task >> kdalpha_strategy_rank_task
kdalpha_strategy_rank_task >> kdalpha_pm_end_task
generate_kdalpha_aibs_singal >> kdalpha_pm_end_task
kdalpha_pm_task >> generate_kdalpha_aibs_singal