# -*- coding: utf-8 -*-
from airflow import DAG
from datetime import datetime
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {
    'owner': 'kd06@keydriver'
}

dag = DAG(
    dag_id='kd06_alpha_daily_am_task',
    default_args=default_args,
    schedule_interval='45 9 * * *',
    catchup=False,
    start_date=datetime(2021, 5, 19, 9, 45)
)
# ==========================================================tasks======================================================

kdalpha_am_start_task = SSHOperator(task_id="kd06_kdalpha_am_start_task",
                                    ssh_conn_id="kd06_keydriver",
                                    command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_start_task.sh dev ",
                                    dag=dag)
kdalpha_daily_am_task = SSHOperator(task_id="kd06_kdalpha_daily_am_task",
                                    ssh_conn_id="kd06_keydriver",
                                    command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh dev ",
                                    dag=dag)
kdalpha_strategy_rank_task = SSHOperator(task_id="kd06_kdalpha_strategy_rank_task",
                                         ssh_conn_id="kd06_keydriver",
                                         command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh dev ",
                                         dag=dag)
kdalpha_am_end_task = SSHOperator(task_id="kd06_kdalpha_am_end_task",
                                  ssh_conn_id="kd06_keydriver",
                                  command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_end_task.sh dev ",
                                  dag=dag)

# ==========================================================dependence=================================================
kdalpha_am_start_task >> kdalpha_daily_am_task >> kdalpha_strategy_rank_task >> kdalpha_am_end_task
