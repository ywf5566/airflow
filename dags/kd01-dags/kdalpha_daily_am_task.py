# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'kd01_factor'
}

dag = DAG(
    dag_id='kdalpha_daily_am_task',
    default_args=default_args,
    description='kdalpha_daily_am_task',
    schedule_interval='45 9 * * *',
    start_date=datetime(2020, 12, 21, 9, 45)
)
# ==========================================================tasks======================================================
kdalpha_am_start_task = BashOperator(task_id="kdalpha_am_start_task",
                                     bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_start_task.sh dev ",
                                     dag=dag)
kdalpha_daily_am_task = BashOperator(task_id="kdalpha_daily_am_task",
                                     bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_daily_am_task.sh dev ",
                                     dag=dag)
kdalpha_strategy_rank_task = BashOperator(task_id="kdalpha_strategy_rank_task",
                                          bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_strategy_rank_task.sh dev ",
                                          dag=dag)
kdalpha_am_end_task = BashOperator(task_id="kdalpha_am_end_task",
                                   bash_command="sh /usr/lib/carter/kd_strategy/script/kdalpha_am_end_task.sh dev ",
                                   dag=dag)

# ==========================================================dependence=================================================
kdalpha_am_start_task >> kdalpha_daily_am_task >> kdalpha_strategy_rank_task >> kdalpha_am_end_task