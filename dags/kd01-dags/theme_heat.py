# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'kd01_keydriver_theme_heat',
    default_args=default_args,
    schedule_interval='0 8 */1 * * ',
    start_date=datetime(2020, 12, 1, 8, 0)
)
# ==========================================================tasks======================================================
blockEventStatistic = BashOperator(task_id="blockEventStatistic", bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockEventStatistic.sh ", dag=dag)
blockPriceHeat = BashOperator(task_id="blockPriceHeat", bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockPriceHeat.sh ", dag=dag)
stockResearchCount = BashOperator(task_id="stockResearchCount", bash_command="sh /usr/lib/carter/theme_heat/scripts/stock/stockResearchCount.sh ", dag=dag)
blockNewHeat = BashOperator(task_id="blockNewHeat", bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockNewHeat.sh ", dag=dag)
stockFund = BashOperator(task_id="stockFund", bash_command="sh /usr/lib/carter/theme_heat/scripts/stock/stockFund.sh ", dag=dag)
stockResearchHeat = BashOperator(task_id="stockResearchHeat", bash_command="sh /usr/lib/carter/theme_heat/scripts/stock/stockResearchHeat.sh ", dag=dag)
blockFundHeat = BashOperator(task_id="blockFundHeat", bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockFundHeat.sh ", dag=dag)
blockResearchHeat = BashOperator(task_id="blockResearchHeat", bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockResearchHeat.sh ", dag=dag)

stockResearchCount >> stockResearchHeat >> blockResearchHeat
stockFund >> blockFundHeat
