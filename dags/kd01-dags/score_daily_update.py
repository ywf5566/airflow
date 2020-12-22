# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import pytz
default_args = {
    'owner': 'kd01_update'
}

dag = DAG(
    'score_daily_update',
    default_args=default_args,
    description='score daily update',
    schedule_interval='0 1 * * *',
    start_date=datetime(2020, 12, 21, 1, 0)
)
# ==========================================================tasks======================================================
report_year_update = BashOperator(task_id="report_year_update",
                                  bash_command="source /usr/lib/carter/carter-racker/racker-env/bin/activate;cd "
                                               "/usr/lib/carter/carter-racker/racker/core/update_touyan_task;python "
                                               "company_report_date_update.py  ",
                                  dag=dag)
relative_value_score_daily_update_199 = BashOperator(task_id="relative_value_score_daily_update_199",
                                                     bash_command="whoami;source /usr/lib/carter/carter-racker/racker"
                                                                  "-env/bin/activate;cd "
                                                                  "/usr/lib/carter/carter-racker/racker/core"
                                                                  "/update_touyan_task;python "
                                                                  "relative_score_update_task_199.py ",
                                                     dag=dag)
product_info_update = BashOperator(task_id="product_info_update",
                                   bash_command="source /usr/lib/carter/carter-racker/racker-env/bin/activate;cd "
                                                "/usr/lib/carter/carter-racker/racker/core/update_touyan_task;python "
                                                "major_product_data_clean_auto_update.py ",
                                   dag=dag)
relative_value_score_daily_update = BashOperator(task_id="relative_value_score_daily_update",
                                                 bash_command="source /usr/lib/carter/carter-racker/racker-env/bin"
                                                              "/activate;cd "
                                                              "/usr/lib/carter/carter-racker/racker/core"
                                                              "/update_touyan_task;python "
                                                              "relative_score_update_task.py ",
                                                 dag=dag)
