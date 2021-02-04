#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

""" 由kd03的interday_alpha_daily任务触发 """
default_args = {'owner': 'afroot04', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('KD05_kd_strategy',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2021, 1, 25, 16, 0))

job_start_task = SSHOperator(task_id="job_start_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/monitor_start_task.sh prod ", dag=dag)
v3_dk_daily_task = SSHOperator(task_id="v3_dk_daily_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_dk_daily_task.sh prod ", dag=dag)
block_indicator_task = SSHOperator(task_id="block_indicator_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v4_block_indicator_task.sh prod ", dag=dag)
stockrnn_daily_task = SSHOperator(task_id="stockrnn_daily_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/stockrnn_daily_task.sh prod ", dag=dag)
indicator_daily_task = SSHOperator(task_id="indicator_daily_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/indicator_daily_task.sh prod ", dag=dag)
v3_model_rsync = SSHOperator(task_id="v3_model_rsync", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd06 ", dag=dag)
stock_indicator_task = SSHOperator(task_id="stock_indicator_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v4_stock_indicator_task.sh prod ", dag=dag)
v3_src_strategy_daily_task = SSHOperator(task_id="v3_src_strategy_daily_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_src_strategy_daily_task.sh prod ", dag=dag)
strategy_report_week_task = SSHOperator(task_id="strategy_report_week_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/strategy_report_week_task.sh prod ", dag=dag)
v3_strategy_daily_task = SSHOperator(task_id="v3_strategy_daily_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_strategy_daily_task.sh prod ", dag=dag)
job_end_task = SSHOperator(task_id="job_end_task", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/carter/kd_strategy/script/monitor_end_task.sh prod ", dag=dag)
rsync_kd_policy_position = SSHOperator(task_id="rsync_kd_policy_position", ssh_conn_id="kd05_keydriver",command=" sh /usr/lib/carter/kd_strategy/script/rsync_kd_policy_position.sh", dag=dag)


trigger_daily_pm_task = TriggerDagRunOperator(task_id="trigger_pm_task",
                                              trigger_dag_id="KD05_kdalpha_daily_pm_task",
                                              trigger_rule="all_success", dag=dag)

stock_indicator_task >> [strategy_report_week_task]
block_indicator_task >> [stock_indicator_task]
job_start_task >> [v3_dk_daily_task, block_indicator_task, stockrnn_daily_task, indicator_daily_task, v3_model_rsync]
strategy_report_week_task >> job_end_task
stockrnn_daily_task >> [job_end_task]
indicator_daily_task >> [job_end_task]
v3_dk_daily_task >> [job_end_task]
v3_strategy_daily_task >> [job_end_task]
v3_src_strategy_daily_task >> [v3_strategy_daily_task]
v3_model_rsync >> [v3_src_strategy_daily_task]
job_end_task >> trigger_daily_pm_task
