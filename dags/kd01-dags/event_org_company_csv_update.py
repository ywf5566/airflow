# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'aftoot01',
}
dag = DAG(
    'vent_org_company_csv_update',
    default_args=default_args,
    description='event_org_company_csv_update',
    schedule_interval='15 */3 * * *',
    start_date=datetime(2020, 12, 25, 9, 15)
)
# ==========================================================tasks======================================================
event_org_company_csv_update = BashOperator(task_id="event_org_company_csv_update", bash_command="sh /usr/lib/carter/separateDagobahTask/scripts/KeydriverdbProd/updateEventOrgCompany.sh ", dag=dag)
