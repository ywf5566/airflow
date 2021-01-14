# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {
    'owner': 'kd06_keydriver'
}

dag = DAG(
    'kdalpha_daily_pm_task',
    default_args=default_args,
    description='kdalpha_daily_pm_task',
    schedule_interval=None,
    catchup=False,
    start_date=datetime(2020, 12, 21, 21, 30)
)
# ==========================================================tasks======================================================
kdalpha_pm_start_task = SSHOperator(task_id="kd06_kdalpha_pm_start_task",
                                    ssh_conn_id="kd06_keydriver",
                                    command="sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_start_task.sh dev ",
                                    dag=dag)
v3_model_rsync = SSHOperator(task_id="kd06_v3_model_rsync",
                             ssh_conn_id="kd06_keydriver",
                             command="sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd06 ",
                             dag=dag)
kdalpha_am_task = SSHOperator(task_id="kd06_kdalpha_am_task",
                              ssh_conn_id="kd06_keydriver",
                              command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh dev ",
                              dag=dag)
kdalpha_pm_task = SSHOperator(task_id="kd06_kdalpha_pm_task",
                              ssh_conn_id="kd06_keydriver",
                              command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_pm_task.sh dev ",
                              dag=dag)
kdalpha_strategy_rank_task = SSHOperator(task_id="kd06_kdalpha_strategy_rank_task",
                                         ssh_conn_id="kd06_keydriver",
                                         command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh dev ",
                                         dag=dag)
kdalpha_pm_end_task = SSHOperator(task_id="kd06_kdalpha_pm_end_task",
                                  ssh_conn_id="kd06_keydriver",
                                  command="sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_end_task.sh dev ",
                                  dag=dag)

kdalpha_pm_start_task >> v3_model_rsync >> kdalpha_am_task >> kdalpha_pm_task >> kdalpha_strategy_rank_task >> kdalpha_pm_end_task



