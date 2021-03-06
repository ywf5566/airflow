#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator


default_args = {'owner': 'afroot04', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('Fix_deap_check_05',
          default_args=default_args,
          catchup=False,
          schedule_interval=None,
          start_date=datetime(2021, 5, 6, 16, 0))

l2_factor_check = SSHOperator(task_id="l2_factor_check", ssh_conn_id="kd05_keydriver",command="date ", dag=dag, pool="factor")
check_qsdata = SSHOperator(task_id="check_qsdata", ssh_conn_id="kd05_keydriver",command="date ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_8 = SSHOperator(task_id="fac_daily_kd_deap_factor_8", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531307 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_2 = SSHOperator(task_id="fac_daily_kd_deap_factor_2", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531301 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_3 = SSHOperator(task_id="fac_daily_kd_deap_factor_3", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531302 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_1 = SSHOperator(task_id="fac_daily_kd_deap_factor_1", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531300 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_6 = SSHOperator(task_id="fac_daily_kd_deap_factor_6", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531305 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_7 = SSHOperator(task_id="fac_daily_kd_deap_factor_7", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531306 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_4 = SSHOperator(task_id="fac_daily_kd_deap_factor_4", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531303 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5 = SSHOperator(task_id="fac_daily_kd_deap_factor_5", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531304 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_18 = SSHOperator(task_id="fac_daily_kd_deap_factor_18", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531317 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_19 = SSHOperator(task_id="fac_daily_kd_deap_factor_19", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531318 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_16 = SSHOperator(task_id="fac_daily_kd_deap_factor_16", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531315 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_11 = SSHOperator(task_id="fac_daily_kd_deap_factor_11", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531310 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_25 = SSHOperator(task_id="fac_daily_kd_deap_factor_25", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531324 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_24 = SSHOperator(task_id="fac_daily_kd_deap_factor_24", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531323 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_12 = SSHOperator(task_id="fac_daily_kd_deap_factor_12", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531311 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_13 = SSHOperator(task_id="fac_daily_kd_deap_factor_13", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531312 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_14 = SSHOperator(task_id="fac_daily_kd_deap_factor_14", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531313 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_20 = SSHOperator(task_id="fac_daily_kd_deap_factor_20", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531319 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_23 = SSHOperator(task_id="fac_daily_kd_deap_factor_23", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531322 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_17 = SSHOperator(task_id="fac_daily_kd_deap_factor_17", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531316 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_35 = SSHOperator(task_id="fac_daily_kd_deap_factor_35", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531334 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_29 = SSHOperator(task_id="fac_daily_kd_deap_factor_29", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531328 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_30 = SSHOperator(task_id="fac_daily_kd_deap_factor_30", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531329 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_27 = SSHOperator(task_id="fac_daily_kd_deap_factor_27", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531326 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_33 = SSHOperator(task_id="fac_daily_kd_deap_factor_33", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531332 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_34 = SSHOperator(task_id="fac_daily_kd_deap_factor_34", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531333 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_31 = SSHOperator(task_id="fac_daily_kd_deap_factor_31", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531330 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_32 = SSHOperator(task_id="fac_daily_kd_deap_factor_32", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531331 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_43 = SSHOperator(task_id="fac_daily_kd_deap_factor_43", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531342 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_44 = SSHOperator(task_id="fac_daily_kd_deap_factor_44", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531343 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_40 = SSHOperator(task_id="fac_daily_kd_deap_factor_40", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531339 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_36 = SSHOperator(task_id="fac_daily_kd_deap_factor_36", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531335 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_51 = SSHOperator(task_id="fac_daily_kd_deap_factor_51", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531350 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_48 = SSHOperator(task_id="fac_daily_kd_deap_factor_48", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531347 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_37 = SSHOperator(task_id="fac_daily_kd_deap_factor_37", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531336 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_38 = SSHOperator(task_id="fac_daily_kd_deap_factor_38", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531337 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_39 = SSHOperator(task_id="fac_daily_kd_deap_factor_39", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531338 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_45 = SSHOperator(task_id="fac_daily_kd_deap_factor_45", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531344 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_47 = SSHOperator(task_id="fac_daily_kd_deap_factor_47", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531346 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_41 = SSHOperator(task_id="fac_daily_kd_deap_factor_41", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531340 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_64 = SSHOperator(task_id="fac_daily_kd_deap_factor_64", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531363 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_55 = SSHOperator(task_id="fac_daily_kd_deap_factor_55", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531354 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_56 = SSHOperator(task_id="fac_daily_kd_deap_factor_56", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531355 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_52 = SSHOperator(task_id="fac_daily_kd_deap_factor_52", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531351 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_60 = SSHOperator(task_id="fac_daily_kd_deap_factor_60", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531359 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_62 = SSHOperator(task_id="fac_daily_kd_deap_factor_62", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531361 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_58 = SSHOperator(task_id="fac_daily_kd_deap_factor_58", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531357 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_59 = SSHOperator(task_id="fac_daily_kd_deap_factor_59", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531358 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_72 = SSHOperator(task_id="fac_daily_kd_deap_factor_72", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531371 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_73 = SSHOperator(task_id="fac_daily_kd_deap_factor_73", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531372 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_70 = SSHOperator(task_id="fac_daily_kd_deap_factor_70", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531369 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_65 = SSHOperator(task_id="fac_daily_kd_deap_factor_65", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531364 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_77 = SSHOperator(task_id="fac_daily_kd_deap_factor_77", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531376 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_76 = SSHOperator(task_id="fac_daily_kd_deap_factor_76", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531375 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_66 = SSHOperator(task_id="fac_daily_kd_deap_factor_66", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531365 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_67 = SSHOperator(task_id="fac_daily_kd_deap_factor_67", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531366 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_69 = SSHOperator(task_id="fac_daily_kd_deap_factor_69", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531368 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_74 = SSHOperator(task_id="fac_daily_kd_deap_factor_74", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531373 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_75 = SSHOperator(task_id="fac_daily_kd_deap_factor_75", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531374 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_71 = SSHOperator(task_id="fac_daily_kd_deap_factor_71", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531370 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_87 = SSHOperator(task_id="fac_daily_kd_deap_factor_87", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531386 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_80 = SSHOperator(task_id="fac_daily_kd_deap_factor_80", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531379 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_81 = SSHOperator(task_id="fac_daily_kd_deap_factor_81", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531380 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_78 = SSHOperator(task_id="fac_daily_kd_deap_factor_78", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531377 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_85 = SSHOperator(task_id="fac_daily_kd_deap_factor_85", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531384 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_86 = SSHOperator(task_id="fac_daily_kd_deap_factor_86", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531385 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_83 = SSHOperator(task_id="fac_daily_kd_deap_factor_83", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531382 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_84 = SSHOperator(task_id="fac_daily_kd_deap_factor_84", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531383 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_93 = SSHOperator(task_id="fac_daily_kd_deap_factor_93", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531392 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_88 = SSHOperator(task_id="fac_daily_kd_deap_factor_88", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531387 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_89 = SSHOperator(task_id="fac_daily_kd_deap_factor_89", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531388 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_91 = SSHOperator(task_id="fac_daily_kd_deap_factor_91", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531390 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_92 = SSHOperator(task_id="fac_daily_kd_deap_factor_92", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531391 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_94 = SSHOperator(task_id="fac_daily_kd_deap_factor_94", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531393 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")
check_all_factor = SSHOperator(task_id="check_all_factor", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factors-check.sh 2021-03-01 2021-05-06 False ", dag=dag, pool="factor")


check_qsdata >> [fac_daily_kd_deap_factor_8, fac_daily_kd_deap_factor_2, fac_daily_kd_deap_factor_3, fac_daily_kd_deap_factor_1, fac_daily_kd_deap_factor_6, fac_daily_kd_deap_factor_7, fac_daily_kd_deap_factor_4, fac_daily_kd_deap_factor_5, fac_daily_kd_deap_factor_18, fac_daily_kd_deap_factor_19, fac_daily_kd_deap_factor_16, fac_daily_kd_deap_factor_11, fac_daily_kd_deap_factor_25, fac_daily_kd_deap_factor_24, fac_daily_kd_deap_factor_12, fac_daily_kd_deap_factor_13, fac_daily_kd_deap_factor_14, fac_daily_kd_deap_factor_20, fac_daily_kd_deap_factor_23, fac_daily_kd_deap_factor_17]
fac_daily_kd_deap_factor_52 >> [fac_daily_kd_deap_factor_78]
l2_factor_check >> [check_qsdata]
fac_daily_kd_deap_factor_18 >> [fac_daily_kd_deap_factor_43]
fac_daily_kd_deap_factor_19 >> [fac_daily_kd_deap_factor_44]
fac_daily_kd_deap_factor_30 >> [fac_daily_kd_deap_factor_56]
fac_daily_kd_deap_factor_31 >> [fac_daily_kd_deap_factor_58]
fac_daily_kd_deap_factor_36 >> [fac_daily_kd_deap_factor_65]
fac_daily_kd_deap_factor_51 >> [fac_daily_kd_deap_factor_77]
fac_daily_kd_deap_factor_34 >> [fac_daily_kd_deap_factor_62]
fac_daily_kd_deap_factor_35 >> [fac_daily_kd_deap_factor_64]
fac_daily_kd_deap_factor_11 >> [fac_daily_kd_deap_factor_36]
fac_daily_kd_deap_factor_12 >> [fac_daily_kd_deap_factor_37]
fac_daily_kd_deap_factor_13 >> [fac_daily_kd_deap_factor_38]
fac_daily_kd_deap_factor_58 >> [fac_daily_kd_deap_factor_83]
fac_daily_kd_deap_factor_38 >> [fac_daily_kd_deap_factor_67]
fac_daily_kd_deap_factor_16 >> [fac_daily_kd_deap_factor_40]
fac_daily_kd_deap_factor_17 >> [fac_daily_kd_deap_factor_41]
fac_daily_kd_deap_factor_69 >> [fac_daily_kd_deap_factor_92]
fac_daily_kd_deap_factor_81 >> [check_all_factor]
fac_daily_kd_deap_factor_39 >> [fac_daily_kd_deap_factor_69]
fac_daily_kd_deap_factor_87 >> [check_all_factor]
fac_daily_kd_deap_factor_86 >> [check_all_factor]
fac_daily_kd_deap_factor_85 >> [check_all_factor]
fac_daily_kd_deap_factor_84 >> [check_all_factor]
fac_daily_kd_deap_factor_14 >> [fac_daily_kd_deap_factor_39]
fac_daily_kd_deap_factor_89 >> [check_all_factor]
fac_daily_kd_deap_factor_62 >> [fac_daily_kd_deap_factor_86]
fac_daily_kd_deap_factor_65 >> [fac_daily_kd_deap_factor_88]
fac_daily_kd_deap_factor_64 >> [fac_daily_kd_deap_factor_87]
fac_daily_kd_deap_factor_67 >> [fac_daily_kd_deap_factor_91]
fac_daily_kd_deap_factor_59 >> [fac_daily_kd_deap_factor_84]
fac_daily_kd_deap_factor_55 >> [fac_daily_kd_deap_factor_80]
fac_daily_kd_deap_factor_83 >> [check_all_factor]
fac_daily_kd_deap_factor_8 >> [fac_daily_kd_deap_factor_35]
fac_daily_kd_deap_factor_88 >> [check_all_factor]
fac_daily_kd_deap_factor_2 >> [fac_daily_kd_deap_factor_29]
fac_daily_kd_deap_factor_3 >> [fac_daily_kd_deap_factor_30]
fac_daily_kd_deap_factor_1 >> [fac_daily_kd_deap_factor_27]
fac_daily_kd_deap_factor_6 >> [fac_daily_kd_deap_factor_33]
fac_daily_kd_deap_factor_7 >> [fac_daily_kd_deap_factor_34]
fac_daily_kd_deap_factor_4 >> [fac_daily_kd_deap_factor_31]
fac_daily_kd_deap_factor_5 >> [fac_daily_kd_deap_factor_32]
fac_daily_kd_deap_factor_47 >> [fac_daily_kd_deap_factor_75]
fac_daily_kd_deap_factor_45 >> [fac_daily_kd_deap_factor_74]
fac_daily_kd_deap_factor_44 >> [fac_daily_kd_deap_factor_73]
fac_daily_kd_deap_factor_29 >> [fac_daily_kd_deap_factor_55]
fac_daily_kd_deap_factor_41 >> [fac_daily_kd_deap_factor_71]
fac_daily_kd_deap_factor_40 >> [fac_daily_kd_deap_factor_70]
fac_daily_kd_deap_factor_25 >> [fac_daily_kd_deap_factor_51]
fac_daily_kd_deap_factor_24 >> [fac_daily_kd_deap_factor_48]
fac_daily_kd_deap_factor_27 >> [fac_daily_kd_deap_factor_52]
fac_daily_kd_deap_factor_20 >> [fac_daily_kd_deap_factor_45]
fac_daily_kd_deap_factor_23 >> [fac_daily_kd_deap_factor_47]
fac_daily_kd_deap_factor_48 >> [fac_daily_kd_deap_factor_76]
fac_daily_kd_deap_factor_91 >> [check_all_factor]
fac_daily_kd_deap_factor_92 >> [check_all_factor]
fac_daily_kd_deap_factor_93 >> [check_all_factor]
fac_daily_kd_deap_factor_94 >> [check_all_factor]
fac_daily_kd_deap_factor_70 >> [fac_daily_kd_deap_factor_93]
fac_daily_kd_deap_factor_78 >> [check_all_factor]
fac_daily_kd_deap_factor_33 >> [fac_daily_kd_deap_factor_60]
fac_daily_kd_deap_factor_76 >> [check_all_factor]
fac_daily_kd_deap_factor_77 >> [check_all_factor]
fac_daily_kd_deap_factor_74 >> [check_all_factor]
fac_daily_kd_deap_factor_75 >> [check_all_factor]
fac_daily_kd_deap_factor_72 >> [check_all_factor]
fac_daily_kd_deap_factor_73 >> [check_all_factor]
fac_daily_kd_deap_factor_32 >> [fac_daily_kd_deap_factor_59]
fac_daily_kd_deap_factor_71 >> [fac_daily_kd_deap_factor_94]
fac_daily_kd_deap_factor_66 >> [fac_daily_kd_deap_factor_89]
fac_daily_kd_deap_factor_56 >> [fac_daily_kd_deap_factor_81]
fac_daily_kd_deap_factor_60 >> [fac_daily_kd_deap_factor_85]
fac_daily_kd_deap_factor_43 >> [fac_daily_kd_deap_factor_72]
fac_daily_kd_deap_factor_80 >> [check_all_factor]
fac_daily_kd_deap_factor_37 >> [fac_daily_kd_deap_factor_66]