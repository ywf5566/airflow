# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'kd01_research_report_parser',
    default_args=default_args,
    schedule_interval='0 20 * * *',
    start_date=datetime(2021, 1, 28, 20, 0)
)
# ==========================================================tasks======================================================
parse_research_report = BashOperator(task_id="parse_research_report", 
                                    bash_command="cd /usr/lib/carter/event-news-scheduler;sh project/extractor/script/parse_research_report.sh dev ", dag=dag)
research_report_opinion_detection = BashOperator(task_id="research_report_opinion_detection", bash_command="cd /usr/lib/carter/event-news-scheduler;sh project/extractor/script/opinion_detection.sh dev ", dag=dag)

parse_research_report >> research_report_opinion_detection
