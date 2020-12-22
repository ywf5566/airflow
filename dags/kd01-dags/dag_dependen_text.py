# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from datetime import datetime

default_args = {
    'owner': 'test'
}

dag = DAG(
    'dag-dependency-text',
    default_args=default_args,
    schedule_interval='*/30 * * * *',
    start_date=datetime(2020, 12, 22, 10, 10),
    catchup=False
)


# 创建文件
task1 = BashOperator(
    task_id='text1',
    bash_command='cd ~/wenFeng/;touch a.txt ',
    dag=dag,
)
# 添加内容
task2 = BashOperator(
    task_id='text2',
    bash_command='cd ~/wenFeng/;echo "This is text echo content" >> a.txt ',
    dag=dag
)