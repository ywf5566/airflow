#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('kd_news_process_em_top_news',
          default_args=default_args,
          schedule_interval='*/2 * * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

emHotStock = BashOperator(task_id="emHotStock",
                          bash_command="sh /usr/lib/carter/kd_news_process/scripts/EmStock/emStock.sh ", dag=dag)
syncEmWarnings = BashOperator(task_id="syncEmWarnings",
                              bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/syncEmWarnings.sh ",
                              dag=dag)
syncEmTopNews = BashOperator(task_id="syncEmTopNews",
                             bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/syncEmTopNews.sh ", dag=dag)
syncTopNewsToEm = BashOperator(task_id="syncTopNewsToEm",
                               bash_command="sh /usr/lib/carter/kd_news_process/scripts/step4/syncTopNewsToEm.sh ",
                               dag=dag)

syncEmTopNews >> [syncTopNewsToEm]
