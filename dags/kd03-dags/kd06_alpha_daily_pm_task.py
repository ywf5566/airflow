# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {'owner': 'kd06@keydriver', 'retries': 2, 'retry_delay': timedelta(minutes=1),
                'start_date': datetime.strptime('2021-05-09 10:09:00', "%Y-%m-%d %H:%M:%S")}
dag = DAG('kd06_alpha_daily_pm_task', default_args=default_args, schedule_interval=None)
kd06_kdalpha_pm_start_task = SSHOperator(
    task_id='kd06_kdalpha_pm_start_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_start_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_v3_model_rsync = SSHOperator(
    task_id='kd06_v3_model_rsync', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd06 ''', trigger_rule='all_success', dag=dag)

kd06_kdalpha_am_task = SSHOperator(
    task_id='kd06_kdalpha_am_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh dev ''',
    trigger_rule='all_success', dag=dag)

kd06_kdalpha_pm_task = SSHOperator(
    task_id='kd06_kdalpha_pm_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_pm_task.sh dev ''',
    trigger_rule='all_success', dag=dag)

kd06_kdalpha_strategy_rank_task = SSHOperator(
    task_id='kd06_kdalpha_strategy_rank_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_kdalpha_pm_end_task = SSHOperator(
    task_id='kd06_kdalpha_pm_end_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_end_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_kdalpha_pm_start_task >> kd06_v3_model_rsync
kd06_v3_model_rsync >> kd06_kdalpha_am_task
kd06_kdalpha_am_task >> kd06_kdalpha_pm_task
kd06_kdalpha_pm_task >> kd06_kdalpha_strategy_rank_task
kd06_kdalpha_strategy_rank_task >> kd06_kdalpha_pm_end_task
