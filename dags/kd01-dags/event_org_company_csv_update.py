# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'keydriver',
}
dag = DAG(
    'ke01_keydriver_event_org_company_csv_update',
    default_args=default_args,
    description='event_org_company_csv_update',
    schedule_interval='15 */3 * * *',
    start_date=datetime(2020, 12, 25, 9, 15)
)
# ==========================================================tasks======================================================
event_org_company_csv_update = SSHOperator(task_id="event_org_company_csv_update", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/separateDagobahTask/scripts/KeydriverdbProd/updateEventOrgCompany.sh ", dag=dag)
