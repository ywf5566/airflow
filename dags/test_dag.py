# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator  # 执行bash命令需要的类
from airflow.contrib.operators.ssh_operator import SSHOperator  # 通过ssh_conn_id执行任务需要的类
from airflow.operators.dagrun_operator import TriggerDagRunOperator  # 设置dag任务之间的下游依赖需要的类
from datetime import timedelta
from datetime import datetime

# 设置Dag的默认参数
''' 'owner' 之后的参数为可选参数，并不是必须的'''
# retries ：任务失败之后重新执行的次数
# retry_delay：间隔多久重新执行
# end_date ：任务的结束时间，一般不设置
# on_success_callback:任务成功后的回调函数
# on_failure_callback：任务失败后的回调函数
default_args = {
    'owner': '该任务所属账户',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'end_date': datetime(2016, 1, 1),
    # 'on_success_callback': some_other_function,
    # 'on_failure_callback': some_function,
}

# 创建Dag任务，注意start_date的设置要设置为实际需要执行的日期提前一个schedule_interval时间之前
dag = DAG(
    '设置dag任务的唯一id',
    default_args=default_args,
    description='添加任务的描述信息',
    schedule_interval='0 8 * * *',
    start_date=datetime(2020, 12, 21, 8, 0)
)
# ==========================================================tasks======================================================
task1 = BashOperator(
    task_id="设置唯一task-id",
    bash_command="执行任务的bash命令,比如sh执行脚本等",
    dag=dag)

task2 = SSHOperator(
    task_id='设置task-id',
    ssh_conn_id='conn_id从web端进行添加',
    command="执行命令，和bash一样，注意参数是command 不是 bash_command",
    dag=dag
)

task3 = TriggerDagRunOperator(
    task_id='设置taskid',
    trigger_dag_id="下一个要执行的dag-id",
    dag=dag
)
# ==========================================================dependence=================================================
# 该依赖表示task1执行完后执行task2，task2执行完后执行task3，task3的作用是触发下一个dag任务的执行
task1 >> task2 >> task3
