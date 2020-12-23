#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('deep_factor',
          default_args=default_args,
          schedule_interval='0 4 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 17, 4, 0))

task_3531316_3531332 = BashOperator(task_id="task_3531316_3531332", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3531316 3531332 deep_factor ", dag=dag)
task_3531350_3531368 = BashOperator(task_id="task_3531350_3531368", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3531350 3531368 deep_factor ", dag=dag)
task_3531369_3531383 = BashOperator(task_id="task_3531369_3531383", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3531369 3531383 deep_factor ", dag=dag)
task_3531384_3757482 = BashOperator(task_id="task_3531384_3757482", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3531384 3757482 deep_factor ", dag=dag)
task_3531333_3531347 = BashOperator(task_id="task_3531333_3531347", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3531333 3531347 deep_factor ", dag=dag)
task_3531300_3531315 = BashOperator(task_id="task_3531300_3531315", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3531300 3531315 deep_factor ", dag=dag)
