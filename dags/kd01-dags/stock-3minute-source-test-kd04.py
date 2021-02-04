# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'stock_3minute_source_kd04',
    default_args=default_args,
    schedule_interval='0 */4 * * *',
    start_date=datetime(2020, 12, 22, 12, 0)
)
# ==========================================================tasks======================================================
stock_3minute_source_test_kd04 = BashOperator(task_id="stock_3minute_source_test",
                                              bash_command="sh /usr/lib/carter/stock-3minute-source"
                                                           "/stock_3minute_source/scripts/sync_all.sh ",
                                              dag=dag)
