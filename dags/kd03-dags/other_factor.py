#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('other_factor',
          default_args=default_args,
          schedule_interval='0 4 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 17, 4, 0))


task_2896_418423 = BashOperator(task_id="task_2896_418423", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 2896 418423 other_factor ", dag=dag)
task_3773778_3949907 = BashOperator(task_id="task_3773778_3949907", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3773778 3949907 other_factor ", dag=dag)
task_418424_3773774 = BashOperator(task_id="task_418424_3773774", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 418424 3773774 other_factor ", dag=dag)
task_2603_2895 = BashOperator(task_id="task_2603_2895", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 2603 2895 other_factor ", dag=dag)
