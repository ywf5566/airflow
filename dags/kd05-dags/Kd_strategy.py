#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import TaskInstance
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

TI = TaskInstance
default_args = {'owner': 'afroot05', 'retries': 2, 'retry_delay': timedelta(minutes=1),
                'start_date': datetime.strptime('2021-05-17 14:07:00', "%Y-%m-%d %H:%M:%S")}
dag = DAG('Kd_strategy', default_args=default_args, schedule_interval=None)
v3_model_rsync = BashOperator(
    task_id='v3_model_rsync', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd06 ''', trigger_rule='all_success', dag=dag)

indicator_daily_task = BashOperator(
    task_id='indicator_daily_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/indicator_daily_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

v3_dk_daily_task = BashOperator(
    task_id='v3_dk_daily_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v3_dk_daily_task.sh prod ''', trigger_rule='all_success', dag=dag)

stockrnn_daily_task = BashOperator(
    task_id='stockrnn_daily_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/stockrnn_daily_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

block_indicator_task = BashOperator(
    task_id='block_indicator_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v4_block_indicator_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

v3_src_strategy_daily_task = BashOperator(
    task_id='v3_src_strategy_daily_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v3_src_strategy_daily_task.sh prod ''',
    trigger_rule='all_success', dag=dag)

v3_strategy_daily_task = BashOperator(
    task_id='v3_strategy_daily_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v3_strategy_daily_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

stock_indicator_task = BashOperator(
    task_id='stock_indicator_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v4_stock_indicator_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

strategy_report_week_task = BashOperator(
    task_id='strategy_report_week_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/strategy_report_week_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

job_end_task = BashOperator(
    task_id='job_end_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/monitor_end_task.sh prod ''', trigger_rule='all_success', dag=dag)


rsync_kd_policy_position = BashOperator(
    task_id='rsync_kd_policy_position', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/rsync_kd_policy_position.sh ''', trigger_rule='all_success',
    dag=dag)

job_start_task = BashOperator(
    task_id='job_start_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/monitor_start_task.sh prod ''', trigger_rule='all_success',
    dag=dag)

kd05_v3_src_alphanet_strategy_daily_task = BashOperator(
    task_id='kd05_v3_src_alphanet_strategy_daily_task', 
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v3_src_alphanet_strategy_daily_task.sh prod ''',
    trigger_rule='all_success', dag=dag)

kd05_v3_src_xgb_gru_alphanet_strategy_daily_task = BashOperator(
    task_id='kd05_v3_src_xgb_gru_alphanet_strategy_daily_task',
    bash_command=r'''sh /usr/lib/carter/kd_strategy/script/v3_src_xgb_gru_alphanet_strategy_daily_task.sh prod ''',
    trigger_rule='all_success', dag=dag)

trigger_daily_pm_task = TriggerDagRunOperator(
    task_id='trigger_daily_pm_task', trigger_dag_id='Kdalpha_daily_pm_task', trigger_rule='all_success', dag=dag)

job_start_task >> v3_model_rsync
job_start_task >> indicator_daily_task
job_start_task >> v3_dk_daily_task
job_start_task >> stockrnn_daily_task
job_start_task >> block_indicator_task
v3_model_rsync >> v3_src_strategy_daily_task
v3_src_strategy_daily_task >> v3_strategy_daily_task
block_indicator_task >> stock_indicator_task
stock_indicator_task >> strategy_report_week_task
strategy_report_week_task >> job_end_task
v3_strategy_daily_task >> job_end_task
rsync_kd_policy_position >> job_end_task
indicator_daily_task >> job_end_task
v3_dk_daily_task >> job_end_task
kd05_v3_src_xgb_gru_alphanet_strategy_daily_task >> job_end_task
job_end_task >> trigger_daily_pm_task
stockrnn_daily_task >> rsync_kd_policy_position
v3_src_strategy_daily_task >> rsync_kd_policy_position
v3_model_rsync >> kd05_v3_src_alphanet_strategy_daily_task
kd05_v3_src_alphanet_strategy_daily_task >> kd05_v3_src_xgb_gru_alphanet_strategy_daily_task
v3_src_strategy_daily_task >> kd05_v3_src_xgb_gru_alphanet_strategy_daily_task
stockrnn_daily_task >> kd05_v3_src_xgb_gru_alphanet_strategy_daily_task