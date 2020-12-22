# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'keydriver'
}

dag = DAG(
    'kd01_keydriver_research_report_parser',
    default_args=default_args,
    description='research_report_parser',
    schedule_interval='0 20 * * *',
    start_date=datetime(2020, 12, 21, 20, 0)
)
# ==========================================================tasks======================================================
parse_research_report = SSHOperator(task_id="parse_research_report", ssh_conn_id="kd01_keydriver",
                                    command="cd /usr/lib/carter/event-news-scheduler;sh project/extractor/script/parse_research_report.sh dev ", dag=dag)
research_report_opinion_detection = SSHOperator(task_id="research_report_opinion_detection", ssh_conn_id="kd01_keydriver",command="cd /usr/lib/carter/event-news-scheduler;sh project/extractor/script/opinion_detection.sh dev ", dag=dag)

parse_research_report >> research_report_opinion_detection
