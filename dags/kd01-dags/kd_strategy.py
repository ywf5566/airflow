# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime


default_args = {
    'owner': 'keydriver'
}
dag = DAG(
    dag_id='kd_strategy',
    default_args=default_args,
    description='kd_strategy,策略',
    schedule_interval='30 20 * * *',
    start_date=datetime(2020, 12, 21, 20, 30)
)
# ==========================================================tasks======================================================
job_start_task = SSHOperator(task_id="job_start_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/monitor_start_task.sh dev ", dag=dag)
block_indicator_task = SSHOperator(task_id="block_indicator_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v4_block_indicator_task.sh dev ", dag=dag)
v3_model_rsync = SSHOperator(task_id="v3_model_rsync", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd01 ", dag=dag)
indicator_daily_task = SSHOperator(task_id="indicator_daily_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/indicator_daily_task.sh dev ", dag=dag)
v3_dk_daily_task = SSHOperator(task_id="v3_dk_daily_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_dk_daily_task.sh dev ", dag=dag)
stock_indicator_task = SSHOperator(task_id="stock_indicator_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v4_stock_indicator_task.sh dev ", dag=dag)
v3_src_strategy_daily_task = SSHOperator(task_id="v3_src_strategy_daily_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_src_strategy_daily_task.sh dev ", dag=dag)
strategy_report_week = SSHOperator(task_id="strategy_report_week", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/strategy_report_week_task.sh dev ", dag=dag)
v3_strategy_daily_task = SSHOperator(task_id="v3_strategy_daily_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_strategy_daily_task.sh dev ", dag=dag)
job_end_task = SSHOperator(task_id="job_end_task", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_strategy/script/monitor_end_task.sh dev ", dag=dag)

# ==========================================================dependencies================================================
job_start_task >> block_indicator_task >> stock_indicator_task >> strategy_report_week >> job_end_task
job_start_task >> v3_model_rsync >> job_end_task
job_start_task >> indicator_daily_task >> job_end_task
job_start_task >> v3_model_rsync >> v3_src_strategy_daily_task >> v3_strategy_daily_task >> job_end_task
