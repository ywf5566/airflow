#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('theme_heat',
          default_args=default_args,
          schedule_interval='15 0 */1 * * ',
          catchup=False,
          start_date=datetime(2020, 11, 24, 16, 0))

blockEventStatistic = BashOperator(task_id="blockEventStatistic",
                                   bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockEventStatistic.sh ",
                                   dag=dag)
blockPriceHeat = BashOperator(task_id="blockPriceHeat",
                              bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockPriceHeat.sh ", dag=dag)
stockResearchCount = BashOperator(task_id="stockResearchCount",
                                  bash_command="sh /usr/lib/carter/theme_heat/scripts/stock/stockResearchCount.sh ",
                                  dag=dag)
blockNewHeat = BashOperator(task_id="blockNewHeat",
                            bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockNewHeat.sh ", dag=dag)
stockFund = BashOperator(task_id="stockFund", bash_command="sh /usr/lib/carter/theme_heat/scripts/stock/stockFund.sh ",
                         dag=dag)
stockResearchHeat = BashOperator(task_id="stockResearchHeat",
                                 bash_command="sh /usr/lib/carter/theme_heat/scripts/stock/stockResearchHeat.sh ",
                                 dag=dag)
blockFundHeat = BashOperator(task_id="blockFundHeat",
                             bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockFundHeat.sh ", dag=dag)
blockResearchHeat = BashOperator(task_id="blockResearchHeat",
                                 bash_command="sh /usr/lib/carter/theme_heat/scripts/block/blockResearchHeat.sh ",
                                 dag=dag)

stockResearchCount >> [stockResearchHeat]
stockFund >> [blockFundHeat]
stockResearchHeat >> [blockResearchHeat]
