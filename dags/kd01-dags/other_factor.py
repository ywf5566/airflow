# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'kd01_factor_repo'
}

dag = DAG(
    'kd01_other_factor',
    default_args=default_args,
    description='other-factor 因子训练',
    schedule_interval='0 4 * * *',
    start_date=datetime(2020, 12, 21, 4, 0)
)
# ==========================================================tasks=======================================================
task_2603_516214 = BashOperator(task_id="task_2603_516214", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 2603 516214 ", dag=dag)
task_516215_2058928 = BashOperator(task_id="task_516215_2058928", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 516215 2058928 ", dag=dag)
task_2058929_2129864 = BashOperator(task_id="task_2058929_2129864", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 2058929 2129864 ", dag=dag)
task_2129865_2130000 = BashOperator(task_id="task_2129865_2130000", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 2129865 2130000 ", dag=dag)
