# -*- coding: utf-8 -*-
from datetime import datetime, date, time, timedelta
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {'owner': 'afroot01', 'retries': 2, 'retry_delay': timedelta(minutes=1),
                'start_date': datetime.strptime('2021-05-09 14:58:00', "%Y-%m-%d %H:%M:%S")}
dag = DAG('kd06_kd_strategy', default_args=default_args, schedule_interval=None)
kd06_job_start_task = SSHOperator(
    task_id='kd06_job_start_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/monitor_start_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_block_indicator_task = SSHOperator(
    task_id='kd06_block_indicator_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v4_block_indicator_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_v3_model_rsync = SSHOperator(
    task_id='kd06_v3_model_rsync', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd06 ''', trigger_rule='all_success', dag=dag)

kd06_indicator_daily_task = SSHOperator(
    task_id='kd06_indicator_daily_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/indicator_daily_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_v3_dk_daily_task = SSHOperator(
    task_id='kd06_v3_dk_daily_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v3_dk_daily_task.sh dev ''', trigger_rule='all_success', dag=dag)

kd06_stockrnn_daily_task = SSHOperator(
    task_id='kd06_stockrnn_daily_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/stockrnn_daily_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_v3_src_strategy_daily_task = SSHOperator(
    task_id='kd06_v3_src_strategy_daily_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v3_src_strategy_daily_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_v3_strategy_daily_task = SSHOperator(
    task_id='kd06_v3_strategy_daily_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v3_strategy_daily_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_job_end_task = SSHOperator(
    task_id='kd06_job_end_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/monitor_end_task.sh dev ''', trigger_rule='all_success', dag=dag)

kd06_stock_indicator_task = SSHOperator(
    task_id='kd06_stock_indicator_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v4_stock_indicator_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

kd06_strategy_report_week = SSHOperator(
    task_id='kd06_strategy_report_week', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/strategy_report_week_task.sh dev ''', trigger_rule='all_success',
    dag=dag)

trigger_pm_task = TriggerDagRunOperator(
    task_id='trigger_pm_task', trigger_dag_id='kd06_alpha_daily_pm_task', trigger_rule='all_success', dag=dag)

kd06_v3_src_alphanet_strategy_daily_task = SSHOperator(
    task_id='kd06_v3_src_alphanet_strategy_daily_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v3_src_alphanet_strategy_daily_task.sh dev ''',
    trigger_rule='all_success', dag=dag)

kd06_v3_src_xgb_gru_alphanet_strategy_daily_task = SSHOperator(
    task_id='kd06_v3_src_xgb_gru_alphanet_strategy_daily_task', ssh_conn_id='kd06@keydriver',
    command=r'''sh /usr/lib/carter/kd_strategy/script/v3_src_xgb_gru_alphanet_strategy_daily_task.sh dev ''',
    trigger_rule='all_success', dag=dag)

kd06_job_start_task >> kd06_block_indicator_task
kd06_job_start_task >> kd06_v3_model_rsync
kd06_job_start_task >> kd06_indicator_daily_task
kd06_job_start_task >> kd06_v3_dk_daily_task
kd06_job_start_task >> kd06_stockrnn_daily_task
kd06_v3_model_rsync >> kd06_v3_src_strategy_daily_task
kd06_v3_src_strategy_daily_task >> kd06_v3_strategy_daily_task
kd06_v3_strategy_daily_task >> kd06_job_end_task
kd06_indicator_daily_task >> kd06_job_end_task
kd06_v3_dk_daily_task >> kd06_job_end_task
kd06_strategy_report_week >> kd06_job_end_task
kd06_stockrnn_daily_task >> kd06_job_end_task
kd06_v3_src_alphanet_strategy_daily_task >> kd06_job_end_task
kd06_v3_src_xgb_gru_alphanet_strategy_daily_task >> kd06_job_end_task
kd06_block_indicator_task >> kd06_stock_indicator_task
kd06_stock_indicator_task >> kd06_strategy_report_week
kd06_job_end_task >> trigger_pm_task
kd06_v3_model_rsync >> kd06_v3_src_alphanet_strategy_daily_task
kd06_v3_src_strategy_daily_task >> kd06_v3_src_xgb_gru_alphanet_strategy_daily_task
kd06_v3_src_alphanet_strategy_daily_task >> kd06_v3_src_xgb_gru_alphanet_strategy_daily_task
kd06_stockrnn_daily_task >> kd06_v3_src_xgb_gru_alphanet_strategy_daily_task