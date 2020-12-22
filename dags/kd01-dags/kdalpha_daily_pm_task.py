# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'kd01_factor'
}

dag = DAG(
    'kdalpha_daily_pm_task',
    default_args=default_args,
    description='kdalpha_daily_pm_task',
    schedule_interval='30 21 * * *',
    start_date=datetime(2020, 12, 21, 21, 30)
)
# ==========================================================tasks======================================================
kdalpha_pm_start_task = BashOperator(task_id="kdalpha_pm_start_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_start_task.sh dev ", dag=dag)
v3_model_rsync = BashOperator(task_id="v3_model_rsync", bash_command="sh /usr/lib/carter/kd_strategy/script/v3_model_rsync.sh kd01 ", dag=dag)
kdalpha_am_task = BashOperator(task_id="kdalpha_am_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh dev ", dag=dag)
kdalpha_pm_task = BashOperator(task_id="kdalpha_pm_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_pm_task.sh dev ", dag=dag)
kdalpha_strategy_rank_task = BashOperator(task_id="kdalpha_strategy_rank_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh dev ", dag=dag)
kdalpha_pm_end_task = BashOperator(task_id="kdalpha_pm_end_task", bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_pm_end_task.sh dev ", dag=dag)

kdalpha_pm_start_task >> v3_model_rsync >> kdalpha_am_task >> kdalpha_pm_task >> kdalpha_strategy_rank_task >> kdalpha_pm_end_task



