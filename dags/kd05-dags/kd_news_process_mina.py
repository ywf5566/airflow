#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('kd_news_process_mina',
          default_args=default_args,
          schedule_interval='*/2 * * * *',
          catchup=False,
          start_date=datetime(2021, 5, 24, 15, 0))

infoPoolSummary = BashOperator(task_id="infoPoolSummary",
                               bash_command="sh /usr/lib/carter/kd_news_process/scripts/Mina/infoPoolSummary.sh ",
                               dag=dag,
                               pool="factor")
infoPoolWebSummary = BashOperator(task_id="infoPoolWebSummary",
                                  bash_command="sh /usr/lib/carter/kd_news_process/scripts/Mina/infoPoolWebSummary.sh ",
                                  dag=dag,
                                  pool="factor")
