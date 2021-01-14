# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime


default_args = {
    'owner': 'kd06_keydriver'
}
dag = DAG(
    dag_id='kd_strategy',
    default_args=default_args,
    description='kd_strategy,策略',
    schedule_interval='30 20 * * *',
    catchup=False,
    start_date=datetime(2020, 12, 21, 20, 30)
)
# ==========================================================tasks======================================================
job_start_task = SSHOperator(task_id="kd06_job_start_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/monitor_start_task.sh dev ", dag=dag)
block_indicator_task = SSHOperator(task_id="kd06_block_indicator_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v4_block_indicator_task.sh dev ", dag=dag)
v3_model_rsync = SSHOperator(task_id="kd06_v3_model_rsync", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd06 ", dag=dag)
indicator_daily_task = SSHOperator(task_id="kd06_indicator_daily_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/indicator_daily_task.sh dev ", dag=dag)
v3_dk_daily_task = SSHOperator(task_id="kd06_v3_dk_daily_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_dk_daily_task.sh dev ", dag=dag)
stock_indicator_task = SSHOperator(task_id="kd06_stock_indicator_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v4_stock_indicator_task.sh dev ", dag=dag)
v3_src_strategy_daily_task = SSHOperator(task_id="kd06_v3_src_strategy_daily_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_src_strategy_daily_task.sh dev ", dag=dag)
strategy_report_week = SSHOperator(task_id="kd06_strategy_report_week", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/strategy_report_week_task.sh dev ", dag=dag)
v3_strategy_daily_task = SSHOperator(task_id="kd06_v3_strategy_daily_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/v3_strategy_daily_task.sh dev ", dag=dag)
job_end_task = SSHOperator(task_id="kd06_job_end_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/monitor_end_task.sh dev ", dag=dag)
kd06_stockrnn_daily_task = SSHOperator(task_id="kd06_stockrnn_daily_task", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/stockrnn_daily_task.sh dev ", dag=dag)
kd06_rsync_kd_policy_position = SSHOperator(task_id="kd06_rsync_kd_policy_position", ssh_conn_id="kd06_keydriver",command="sh /usr/lib/carter/kd_strategy/script/rsync_kd_policy_position.sh dev ", dag=dag)
trigger_daily_pm_task = TriggerDagRunOperator(task_id="trigger_pm_task", trigger_dag_id="kdalpha_daily_pm_task", trigger_rule="all_done", dag=dag)


# ==========================================================dependencies================================================
job_start_task >> [v3_dk_daily_task, block_indicator_task, indicator_daily_task, v3_model_rsync]
v3_model_rsync >> [v3_src_strategy_daily_task]
indicator_daily_task >> [job_end_task]
v3_dk_daily_task >> [job_end_task]
block_indicator_task >> [stock_indicator_task]
v3_strategy_daily_task >> [job_end_task]
v3_src_strategy_daily_task >> [v3_strategy_daily_task]
stock_indicator_task >> strategy_report_week >> job_end_task
job_start_task >> kd06_stockrnn_daily_task >> kd06_rsync_kd_policy_position >> job_end_task
job_end_task >> trigger_daily_pm_task