#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'afroot03'
}
dag = DAG(
    'research_report_parser',
    default_args=default_args,
    description='beta_info_update',
    schedule_interval='0 20 * * *',
    catchup=False,
    start_date=datetime(2021, 1, 16, 20, 0)
)

parse_research_report = BashOperator(task_id="parse_research_report", bash_command="cd /usr/lib/carter/event-news-scheduler;sh project/extractor/script/parse_research_report.sh prod ", dag=dag)
research_report_opinion_detection = BashOperator(task_id="research_report_opinion_detection", bash_command="cd /usr/lib/carter/event-news-scheduler;sh project/extractor/script/opinion_detection.sh prod ", dag=dag)
parse_research_report >> research_report_opinion_detection