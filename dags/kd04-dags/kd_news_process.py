#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('kd_news_process',
          default_args=default_args,
          schedule_interval='*/10 * * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

update_cluster_id = BashOperator(task_id="update_cluster_id",
                                 bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/updateClusterId.sh ",
                                 dag=dag)
predict_news_sync = BashOperator(task_id="predict_news_sync",
                                 bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/predictorProcess.sh ",
                                 dag=dag)
keydriver_news_process = BashOperator(task_id="keydriver_news_process",
                                      bash_command="sh /usr/lib/carter/kd_news_process/scripts/step2/keydriverProcess.sh ",
                                      dag=dag)
update_em_news_by_es_news = BashOperator(task_id="update_em_news_by_es_news",
                                         bash_command="sh /usr/lib/carter/kd_news_process/scripts/step2/updateEmTopNews.sh ",
                                         dag=dag)
supplement_Industry = BashOperator(task_id="supplement_Industry",
                                   bash_command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementIndustry.sh ",
                                   dag=dag)
supplement_em_news = BashOperator(task_id="supplement_em_news",
                                  bash_command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementEmNews.sh ",
                                  dag=dag)
supplement_summary = BashOperator(task_id="supplement_summary",
                                  bash_command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementSummary.sh ",
                                  dag=dag)
syncNotTopNewsToEm = BashOperator(task_id="syncNotTopNewsToEm",
                                  bash_command="sh /usr/lib/carter/kd_news_process/scripts/step4/syncNotTopNewsToEm.sh ",
                                  dag=dag)


predict_news_sync >> [keydriver_news_process]
supplement_em_news >> [supplement_summary]
keydriver_news_process >> [update_em_news_by_es_news]
update_cluster_id >> [predict_news_sync]
update_em_news_by_es_news >> [supplement_Industry, supplement_em_news]
supplement_summary >> [syncNotTopNewsToEm]
