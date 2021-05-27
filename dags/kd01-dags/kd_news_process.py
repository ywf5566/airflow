# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'kd01_news_process',
    default_args=default_args,
    catchup=False,
    schedule_interval='*/20 * * * *',
    start_date=datetime(2021, 1, 27, 17, 0)
)
# ==========================================================tasks======================================================
update_cluster_id = BashOperator(task_id="update_cluster_id", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/updateClusterId.sh ", dag=dag)
predict_news_sync = BashOperator(task_id="predict_news_sync", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/predictorProcess.sh ", dag=dag)
keydriver_news_process = BashOperator(task_id="keydriver_news_process", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step2/keydriverProcess.sh ", dag=dag)
update_em_news_by_es_news = BashOperator(task_id="update_em_news_by_es_news", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step2/updateEmTopNews.sh ", dag=dag)
supplement_industry = BashOperator(task_id="supplement_industry", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementIndustry.sh ", dag=dag)
supplement_em_news = BashOperator(task_id="supplement_em_news", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementEmNews.sh ", dag=dag)
supplement_summary = BashOperator(task_id="supplement_summary", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementSummary.sh ", dag=dag)
syncNotTopNewsToEm = BashOperator(task_id="syncNotTopNewsToEm", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step4/syncNotTopNewsToEm.sh ", dag=dag)

# ==========================================================dependencies======================================================

update_cluster_id >> predict_news_sync >> keydriver_news_process >> [update_em_news_by_es_news, supplement_industry]
update_em_news_by_es_news >> supplement_em_news >> supplement_summary >> syncNotTopNewsToEm
