# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'keydriver'
}

dag = DAG(
    'kd01_keydriver_news_process',
    default_args=default_args,
    description='kd_news_process',
    schedule_interval='*/10 * * * *',
    start_date=datetime(2020, 12, 22, 13, 20)
)
# ==========================================================tasks======================================================
update_cluster_id = SSHOperator(task_id="update_cluster_id", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step1/updateClusterId.sh ", dag=dag)
predict_news_sync = SSHOperator(task_id="predict_news_sync", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step1/predictorProcess.sh ", dag=dag)
keydriver_news_process = SSHOperator(task_id="keydriver_news_process", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step2/keydriverProcess.sh ", dag=dag)
update_em_news_by_es_news = SSHOperator(task_id="update_em_news_by_es_news", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step2/updateEmTopNews.sh ", dag=dag)
supplement_industry = SSHOperator(task_id="supplement_industry", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementIndustry.sh ", dag=dag)
supplement_em_news = SSHOperator(task_id="supplement_em_news", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementEmNews.sh ", dag=dag)
supplement_summary = SSHOperator(task_id="supplement_summary", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step3/supplementSummary.sh ", dag=dag)
syncNotTopNewsToEm = SSHOperator(task_id="syncNotTopNewsToEm", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step4/syncNotTopNewsToEm.sh ", dag=dag)

# ==========================================================dependencies======================================================

update_cluster_id >> predict_news_sync >> keydriver_news_process >> [update_em_news_by_es_news, supplement_industry]
update_em_news_by_es_news >> supplement_em_news >> supplement_summary >> syncNotTopNewsToEm
