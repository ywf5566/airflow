# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'kd01_sync'
}

dag = DAG(
    'kd01_keydriver_theme_heat',
    default_args=default_args,
    description='theme_heat',
    schedule_interval='0 8 */1 * * ',
    start_date=datetime(2020, 12, 1, 8, 0)
)
# ==========================================================tasks======================================================
blockEventStatistic = SSHOperator(task_id="blockEventStatistic", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/block/blockEventStatistic.sh ", dag=dag)
blockPriceHeat = SSHOperator(task_id="blockPriceHeat", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/block/blockPriceHeat.sh ", dag=dag)
stockResearchCount = SSHOperator(task_id="stockResearchCount", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/stock/stockResearchCount.sh ", dag=dag)
blockNewHeat = SSHOperator(task_id="blockNewHeat", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/block/blockNewHeat.sh ", dag=dag)
stockFund = SSHOperator(task_id="stockFund", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/stock/stockFund.sh ", dag=dag)
stockResearchHeat = SSHOperator(task_id="stockResearchHeat", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/stock/stockResearchHeat.sh ", dag=dag)
blockFundHeat = SSHOperator(task_id="blockFundHeat", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/block/blockFundHeat.sh ", dag=dag)
blockResearchHeat = SSHOperator(task_id="blockResearchHeat", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/theme_heat/scripts/block/blockResearchHeat.sh ", dag=dag)

stockResearchCount >> stockResearchHeat >> blockResearchHeat
stockFund >> blockFundHeat
