#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'afroot03'
}
dag = DAG(
    'parse_announce_page',
    default_args=default_args,
    description='beta_info_update',
    schedule_interval='0 */8 * * *',
    catchup=False,
    start_date=datetime(2021, 1, 18, 0, 0)
)

parse_announce_page = BashOperator(task_id="parse_announce_page", bash_command="cd /usr/lib/carter/event-news-scheduler;sh project/extractor/script/parse_announce_page.sh prod ", dag=dag)
