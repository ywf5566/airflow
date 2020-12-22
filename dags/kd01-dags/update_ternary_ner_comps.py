# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'kd01_event_news'
}

dag = DAG(
    'update_ternary_ner_comps',
    default_args=default_args,
    description='update_ternary_ner_comps',
    schedule_interval='0 12 * * SAT',
    start_date=datetime(2020, 12, 20, 12, 0)
)
# ==========================================================tasks======================================================
update_ternary_enr_comps = BashOperator(task_id="update_ternary_enr_comps",
                                        bash_command="source /usr/lib/carter/event-news-scheduler/event-news-scheduler-venv/bin/activate;cd /usr/lib/carter/event-news-scheduler/project/predictor/predictor/scripts/;python BATCH_UPDATE_TERNARY_NER_COMPS.py ",
                                        dag=dag)
