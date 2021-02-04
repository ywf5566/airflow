# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}
dag = DAG(
    'kd01_announce_page_parser',
    default_args=default_args,
    description='announce_page_parser',
    schedule_interval='0 20 * * *',
    start_date=datetime(2020, 12, 21, 20, 0)
)
# ==========================================================tasks======================================================
parse_announce_page = BashOperator(task_id="parse_announce_page",
                                   bash_command="cd /usr/lib/carter/event-news-scheduler;sh "
                                                "project/extractor/script/parse_announce_page.sh dev ",
                                   dag=dag)
