#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('fix_adjfactor',
          default_args=default_args,
          schedule_interval='0 */1 * * * ',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

fix_adjfaxtor = BashOperator(task_id="fix_adjfaxtor",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/fix_kdadjfactor.sh ", dag=dag)
