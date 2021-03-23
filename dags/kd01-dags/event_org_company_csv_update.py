# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'aftoot01',
}
dag = DAG(
    'event_org_company_csv_update',
    default_args=default_args,
    description='event_org_company_csv_update',
    schedule_interval='15 */3 * * *',
    start_date=datetime(2021, 3, 20, 9, 15)
)
# ==========================================================tasks======================================================
event_org_company_csv_update = BashOperator(task_id="event_org_company_csv_update", bash_command="sh /usr/lib/carter/separateDagobahTask/scripts/KeydriverdbProd/updateEventOrgCompany.sh ", dag=dag)
sync_kd_security_info = BashOperator(task_id="sync_kd_security_info", bash_command="sh /usr/lib/carter/separateDagobahTask/scripts/KeydriverdbProd/syncKdSecurityInfo.sh ")
