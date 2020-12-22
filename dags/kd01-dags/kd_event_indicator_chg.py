# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'keydriver'
}
dag = DAG(
    'kd01_keydriver_event_indicator_chg',
    default_args=default_args,
    description='kd_event_indicator_chg',
    schedule_interval='0 18 * * *',
    start_date=datetime(2020, 12, 21, 18, 0)
)
# ==========================================================tasks======================================================
a_stock_week = SSHOperator(task_id="a_stock_week", ssh_conn_id="kd01_keydriver",command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python a_stock_chg_week.py ", dag=dag)
a_stock_day = SSHOperator(task_id="a_stock_day", ssh_conn_id="kd01_keydriver",command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python a_stock_chg_day.py ", dag=dag)
a_stock_month = SSHOperator(task_id="a_stock_month", ssh_conn_id="kd01_keydriver",command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python a_stock_chg_month.py ", dag=dag)
sw2_chg = SSHOperator(task_id="sw2_chg", ssh_conn_id="kd01_keydriver",command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python sw_index_chg_day.py ", dag=dag)

