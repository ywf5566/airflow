from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot01',
                'start_date': datetime.strptime('2021-01-05 01:00:00', "%Y-%m-%d %H:%M:%S")}

dag = DAG('update_trade_date',
          default_args=default_args,
          schedule_interval='0 1 * * *')

main = BashOperator(
    task_id='main',
    bash_command=r'''sh /lib/carter/dbsync/scripts/update_trade_date.sh ''',
    trigger_rule='all_success',
    dag=dag)
