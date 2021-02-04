# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'aftoot01'
}
dag = DAG(
    'deep_factor',
    default_args=default_args,
    description='deep 因子训练',
    schedule_interval='0 4 * * *',
    start_date=datetime(2020, 12, 21, 4, 0)
)
# ==========================================================tasks=======================================================
task_1960987_1961062 = BashOperator(task_id="task_1960987_1961062", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1960987 1961062 ", dag=dag)
task_1814405_1814481 = BashOperator(task_id="task_1814405_1814481", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1814405 1814481 ", dag=dag)
task_1814558_1960986 = BashOperator(task_id="task_1814558_1960986", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1814558 1960986 ", dag=dag)
task_1961063_1961138 = BashOperator(task_id="task_1961063_1961138", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1961063 1961138 ", dag=dag)
task_1961139_1961214 = BashOperator(task_id="task_1961139_1961214", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1961139 1961214 ", dag=dag)
task_1814482_1814557 = BashOperator(task_id="task_1814482_1814557", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1814482 1814557 ", dag=dag)
