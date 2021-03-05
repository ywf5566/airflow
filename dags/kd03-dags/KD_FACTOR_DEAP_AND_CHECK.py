#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {'owner': 'afroot03', 'retries': 2, 'retry_delay': timedelta(minutes=1)}

dag = DAG('KD-FACTOR-DEAP-AND-CHECK',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2020, 12, 17, 17, 0))

# ============================================== tasks ==================================================
l2_factor_check = BashOperator(task_id="l2_factor_check", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh l2_factor_check ", dag=dag, pool="factor")
check_qsdata = BashOperator(task_id="check_qsdata", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_qsdata ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_8 = BashOperator(task_id="fac_daily_kd_deap_factor_8", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531307 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_2 = BashOperator(task_id="fac_daily_kd_deap_factor_2", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531301 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_3 = BashOperator(task_id="fac_daily_kd_deap_factor_3", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531302 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_1 = BashOperator(task_id="fac_daily_kd_deap_factor_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531300 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_6 = BashOperator(task_id="fac_daily_kd_deap_factor_6", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531305 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_7 = BashOperator(task_id="fac_daily_kd_deap_factor_7", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531306 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_4 = BashOperator(task_id="fac_daily_kd_deap_factor_4", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531303 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5 = BashOperator(task_id="fac_daily_kd_deap_factor_5", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531304 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_18 = BashOperator(task_id="fac_daily_kd_deap_factor_18", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531317 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_19 = BashOperator(task_id="fac_daily_kd_deap_factor_19", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531318 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_23 = BashOperator(task_id="fac_daily_kd_deap_factor_23", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531322 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_24 = BashOperator(task_id="fac_daily_kd_deap_factor_24", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531323 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_25 = BashOperator(task_id="fac_daily_kd_deap_factor_25", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531324 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_11 = BashOperator(task_id="fac_daily_kd_deap_factor_11", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531310 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_12 = BashOperator(task_id="fac_daily_kd_deap_factor_12", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531311 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_13 = BashOperator(task_id="fac_daily_kd_deap_factor_13", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531312 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_14 = BashOperator(task_id="fac_daily_kd_deap_factor_14", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531313 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_20 = BashOperator(task_id="fac_daily_kd_deap_factor_20", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531319 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_16 = BashOperator(task_id="fac_daily_kd_deap_factor_16", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531315 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_17 = BashOperator(task_id="fac_daily_kd_deap_factor_17", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531316 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_35 = BashOperator(task_id="fac_daily_kd_deap_factor_35", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531334 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_29 = BashOperator(task_id="fac_daily_kd_deap_factor_29", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531328 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_30 = BashOperator(task_id="fac_daily_kd_deap_factor_30", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531329 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_27 = BashOperator(task_id="fac_daily_kd_deap_factor_27", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531326 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_33 = BashOperator(task_id="fac_daily_kd_deap_factor_33", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531332 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_34 = BashOperator(task_id="fac_daily_kd_deap_factor_34", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531333 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_31 = BashOperator(task_id="fac_daily_kd_deap_factor_31", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531330 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_32 = BashOperator(task_id="fac_daily_kd_deap_factor_32", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531331 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_43 = BashOperator(task_id="fac_daily_kd_deap_factor_43", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531342 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_44 = BashOperator(task_id="fac_daily_kd_deap_factor_44", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531343 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_47 = BashOperator(task_id="fac_daily_kd_deap_factor_47", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531346 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_48 = BashOperator(task_id="fac_daily_kd_deap_factor_48", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531347 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_51 = BashOperator(task_id="fac_daily_kd_deap_factor_51", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531350 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_36 = BashOperator(task_id="fac_daily_kd_deap_factor_36", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531335 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_37 = BashOperator(task_id="fac_daily_kd_deap_factor_37", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531336 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_38 = BashOperator(task_id="fac_daily_kd_deap_factor_38", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531337 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_39 = BashOperator(task_id="fac_daily_kd_deap_factor_39", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531338 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_45 = BashOperator(task_id="fac_daily_kd_deap_factor_45", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531344 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_40 = BashOperator(task_id="fac_daily_kd_deap_factor_40", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531339 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_41 = BashOperator(task_id="fac_daily_kd_deap_factor_41", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531340 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_64 = BashOperator(task_id="fac_daily_kd_deap_factor_64", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531363 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_55 = BashOperator(task_id="fac_daily_kd_deap_factor_55", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531354 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_56 = BashOperator(task_id="fac_daily_kd_deap_factor_56", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531355 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_52 = BashOperator(task_id="fac_daily_kd_deap_factor_52", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531351 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_60 = BashOperator(task_id="fac_daily_kd_deap_factor_60", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531359 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_62 = BashOperator(task_id="fac_daily_kd_deap_factor_62", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531361 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_58 = BashOperator(task_id="fac_daily_kd_deap_factor_58", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531357 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_59 = BashOperator(task_id="fac_daily_kd_deap_factor_59", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531358 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_72 = BashOperator(task_id="fac_daily_kd_deap_factor_72", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531371 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_73 = BashOperator(task_id="fac_daily_kd_deap_factor_73", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531372 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_75 = BashOperator(task_id="fac_daily_kd_deap_factor_75", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531374 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_76 = BashOperator(task_id="fac_daily_kd_deap_factor_76", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531375 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_77 = BashOperator(task_id="fac_daily_kd_deap_factor_77", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531376 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_65 = BashOperator(task_id="fac_daily_kd_deap_factor_65", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531364 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_66 = BashOperator(task_id="fac_daily_kd_deap_factor_66", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531365 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_67 = BashOperator(task_id="fac_daily_kd_deap_factor_67", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531366 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_69 = BashOperator(task_id="fac_daily_kd_deap_factor_69", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531368 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_74 = BashOperator(task_id="fac_daily_kd_deap_factor_74", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531373 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_70 = BashOperator(task_id="fac_daily_kd_deap_factor_70", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531369 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_71 = BashOperator(task_id="fac_daily_kd_deap_factor_71", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531370 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_87 = BashOperator(task_id="fac_daily_kd_deap_factor_87", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531386 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_80 = BashOperator(task_id="fac_daily_kd_deap_factor_80", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531379 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_81 = BashOperator(task_id="fac_daily_kd_deap_factor_81", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531380 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_78 = BashOperator(task_id="fac_daily_kd_deap_factor_78", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531377 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_85 = BashOperator(task_id="fac_daily_kd_deap_factor_85", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531384 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_86 = BashOperator(task_id="fac_daily_kd_deap_factor_86", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531385 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_83 = BashOperator(task_id="fac_daily_kd_deap_factor_83", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531382 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_84 = BashOperator(task_id="fac_daily_kd_deap_factor_84", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531383 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_88 = BashOperator(task_id="fac_daily_kd_deap_factor_88", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531387 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_89 = BashOperator(task_id="fac_daily_kd_deap_factor_89", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531388 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_91 = BashOperator(task_id="fac_daily_kd_deap_factor_91", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531390 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_92 = BashOperator(task_id="fac_daily_kd_deap_factor_92", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531391 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_93 = BashOperator(task_id="fac_daily_kd_deap_factor_93", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531392 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_94 = BashOperator(task_id="fac_daily_kd_deap_factor_94", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531393 ", dag=dag, pool="factor")

fac_daily_kd_deap_factor_5948155 = BashOperator(task_id="fac_daily_kd_deap_factor_5948155", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948155 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948156 = BashOperator(task_id="fac_daily_kd_deap_factor_5948156", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948156 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948157 = BashOperator(task_id="fac_daily_kd_deap_factor_5948157", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948157 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948158 = BashOperator(task_id="fac_daily_kd_deap_factor_5948158", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948158 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948159 = BashOperator(task_id="fac_daily_kd_deap_factor_5948159", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948159 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948160 = BashOperator(task_id="fac_daily_kd_deap_factor_5948160", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948160 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948161 = BashOperator(task_id="fac_daily_kd_deap_factor_5948161", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948161 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948162 = BashOperator(task_id="fac_daily_kd_deap_factor_5948162", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948162 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948163 = BashOperator(task_id="fac_daily_kd_deap_factor_5948163", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948163 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948164 = BashOperator(task_id="fac_daily_kd_deap_factor_5948164", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948164 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948165 = BashOperator(task_id="fac_daily_kd_deap_factor_5948165", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948165 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948166 = BashOperator(task_id="fac_daily_kd_deap_factor_5948166", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948166 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948167 = BashOperator(task_id="fac_daily_kd_deap_factor_5948167", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948167 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948168 = BashOperator(task_id="fac_daily_kd_deap_factor_5948168", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948168 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948169 = BashOperator(task_id="fac_daily_kd_deap_factor_5948169", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948169 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948170 = BashOperator(task_id="fac_daily_kd_deap_factor_5948170", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948170 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948171 = BashOperator(task_id="fac_daily_kd_deap_factor_5948171", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948171 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948172 = BashOperator(task_id="fac_daily_kd_deap_factor_5948172", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948172 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948173 = BashOperator(task_id="fac_daily_kd_deap_factor_5948173", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948173 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948174 = BashOperator(task_id="fac_daily_kd_deap_factor_5948174", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948174 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948175 = BashOperator(task_id="fac_daily_kd_deap_factor_5948175", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948175 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948176 = BashOperator(task_id="fac_daily_kd_deap_factor_5948176", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948176 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948177 = BashOperator(task_id="fac_daily_kd_deap_factor_5948177", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948177 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948178 = BashOperator(task_id="fac_daily_kd_deap_factor_5948178", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948178 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948179 = BashOperator(task_id="fac_daily_kd_deap_factor_5948179", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948179 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948180 = BashOperator(task_id="fac_daily_kd_deap_factor_5948180", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948180 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948181 = BashOperator(task_id="fac_daily_kd_deap_factor_5948181", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948181 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948182 = BashOperator(task_id="fac_daily_kd_deap_factor_5948182", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948182 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948183 = BashOperator(task_id="fac_daily_kd_deap_factor_5948183", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948183 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948184 = BashOperator(task_id="fac_daily_kd_deap_factor_5948184", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948184 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948185 = BashOperator(task_id="fac_daily_kd_deap_factor_5948185", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948185 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948186 = BashOperator(task_id="fac_daily_kd_deap_factor_5948186", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948186 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948187 = BashOperator(task_id="fac_daily_kd_deap_factor_5948187", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948187 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948188 = BashOperator(task_id="fac_daily_kd_deap_factor_5948188", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948188 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948189 = BashOperator(task_id="fac_daily_kd_deap_factor_5948189", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948189 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948190 = BashOperator(task_id="fac_daily_kd_deap_factor_5948190", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948190 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948191 = BashOperator(task_id="fac_daily_kd_deap_factor_5948191", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948191 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948192 = BashOperator(task_id="fac_daily_kd_deap_factor_5948192", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948192 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948193 = BashOperator(task_id="fac_daily_kd_deap_factor_5948193", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948193 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948194 = BashOperator(task_id="fac_daily_kd_deap_factor_5948194", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948194 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948195 = BashOperator(task_id="fac_daily_kd_deap_factor_5948195", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948195 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948196 = BashOperator(task_id="fac_daily_kd_deap_factor_5948196", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948196 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948197 = BashOperator(task_id="fac_daily_kd_deap_factor_5948197", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948197 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948198 = BashOperator(task_id="fac_daily_kd_deap_factor_5948198", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948198 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948199 = BashOperator(task_id="fac_daily_kd_deap_factor_5948199", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948199 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948200 = BashOperator(task_id="fac_daily_kd_deap_factor_5948200", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948200 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948201 = BashOperator(task_id="fac_daily_kd_deap_factor_5948201", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948201 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948202 = BashOperator(task_id="fac_daily_kd_deap_factor_5948202", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948202 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948203 = BashOperator(task_id="fac_daily_kd_deap_factor_5948203", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948203 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948204 = BashOperator(task_id="fac_daily_kd_deap_factor_5948204", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948204 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948205 = BashOperator(task_id="fac_daily_kd_deap_factor_5948205", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948205 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948206 = BashOperator(task_id="fac_daily_kd_deap_factor_5948206", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948206 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948207 = BashOperator(task_id="fac_daily_kd_deap_factor_5948207", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948207 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948208 = BashOperator(task_id="fac_daily_kd_deap_factor_5948208", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948208 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948209 = BashOperator(task_id="fac_daily_kd_deap_factor_5948209", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948209 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948210 = BashOperator(task_id="fac_daily_kd_deap_factor_5948210", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948210 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948211 = BashOperator(task_id="fac_daily_kd_deap_factor_5948211", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948211 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948212 = BashOperator(task_id="fac_daily_kd_deap_factor_5948212", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948212 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948213 = BashOperator(task_id="fac_daily_kd_deap_factor_5948213", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948213 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948214 = BashOperator(task_id="fac_daily_kd_deap_factor_5948214", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948214 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948215 = BashOperator(task_id="fac_daily_kd_deap_factor_5948215", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948215 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948216 = BashOperator(task_id="fac_daily_kd_deap_factor_5948216", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948216 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948217 = BashOperator(task_id="fac_daily_kd_deap_factor_5948217", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948217 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948218 = BashOperator(task_id="fac_daily_kd_deap_factor_5948218", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948218 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948219 = BashOperator(task_id="fac_daily_kd_deap_factor_5948219", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948219 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948220 = BashOperator(task_id="fac_daily_kd_deap_factor_5948220", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948220 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948221 = BashOperator(task_id="fac_daily_kd_deap_factor_5948221", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948221 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948222 = BashOperator(task_id="fac_daily_kd_deap_factor_5948222", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948222 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948223 = BashOperator(task_id="fac_daily_kd_deap_factor_5948223", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948223 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948224 = BashOperator(task_id="fac_daily_kd_deap_factor_5948224", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948224 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948225 = BashOperator(task_id="fac_daily_kd_deap_factor_5948225", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948225 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948226 = BashOperator(task_id="fac_daily_kd_deap_factor_5948226", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948226 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948227 = BashOperator(task_id="fac_daily_kd_deap_factor_5948227", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948227 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948228 = BashOperator(task_id="fac_daily_kd_deap_factor_5948228", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948228 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948229 = BashOperator(task_id="fac_daily_kd_deap_factor_5948229", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948229 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948230 = BashOperator(task_id="fac_daily_kd_deap_factor_5948230", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948230 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948231 = BashOperator(task_id="fac_daily_kd_deap_factor_5948231", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948231 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948232 = BashOperator(task_id="fac_daily_kd_deap_factor_5948232", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948232 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948233 = BashOperator(task_id="fac_daily_kd_deap_factor_5948233", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948233 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948234 = BashOperator(task_id="fac_daily_kd_deap_factor_5948234", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948234 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948235 = BashOperator(task_id="fac_daily_kd_deap_factor_5948235", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948235 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948236 = BashOperator(task_id="fac_daily_kd_deap_factor_5948236", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948236 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948237 = BashOperator(task_id="fac_daily_kd_deap_factor_5948237", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948237 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948238 = BashOperator(task_id="fac_daily_kd_deap_factor_5948238", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948238 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948239 = BashOperator(task_id="fac_daily_kd_deap_factor_5948239", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948239 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948240 = BashOperator(task_id="fac_daily_kd_deap_factor_5948240", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948240 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948241 = BashOperator(task_id="fac_daily_kd_deap_factor_5948241", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948241 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948242 = BashOperator(task_id="fac_daily_kd_deap_factor_5948242", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948242 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948243 = BashOperator(task_id="fac_daily_kd_deap_factor_5948243", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948243 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948244 = BashOperator(task_id="fac_daily_kd_deap_factor_5948244", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948244 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948245 = BashOperator(task_id="fac_daily_kd_deap_factor_5948245", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948245 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948246 = BashOperator(task_id="fac_daily_kd_deap_factor_5948246", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948246 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948247 = BashOperator(task_id="fac_daily_kd_deap_factor_5948247", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948247 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948248 = BashOperator(task_id="fac_daily_kd_deap_factor_5948248", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948248 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948249 = BashOperator(task_id="fac_daily_kd_deap_factor_5948249", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948249 ", dag=dag, pool="factor")
fac_daily_kd_deap_factor_5948250 = BashOperator(task_id="fac_daily_kd_deap_factor_5948250", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5948250 ", dag=dag, pool="factor")

check_all_factor = BashOperator(task_id="check_all_factor", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factors-check.sh ", dag=dag, pool="factor")
# trigger kd01上执行的kd06的任务
trigger_kd01_kd06_alphanet_0_0_1_task = SSHOperator(task_id="trigger_01_alphanet_0_0_1_task", ssh_conn_id="kd01_keydriver", command="source /home/keydriver/airflow/bin/activate;airflow trigger_dag kd06_alphanet_0_0_1_task ", dag=dag)

check_qsdata >> [fac_daily_kd_deap_factor_8, fac_daily_kd_deap_factor_2, fac_daily_kd_deap_factor_3, fac_daily_kd_deap_factor_1, fac_daily_kd_deap_factor_6, fac_daily_kd_deap_factor_7, fac_daily_kd_deap_factor_4, fac_daily_kd_deap_factor_5, fac_daily_kd_deap_factor_18, fac_daily_kd_deap_factor_19, fac_daily_kd_deap_factor_23, fac_daily_kd_deap_factor_24, fac_daily_kd_deap_factor_25, fac_daily_kd_deap_factor_11, fac_daily_kd_deap_factor_12, fac_daily_kd_deap_factor_13, fac_daily_kd_deap_factor_14, fac_daily_kd_deap_factor_20, fac_daily_kd_deap_factor_16, fac_daily_kd_deap_factor_17]
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
fac_daily_kd_deap_factor_76 >> fac_daily_kd_deap_factor_5948156 >> [check_all_factor]
fac_daily_kd_deap_factor_77 >> fac_daily_kd_deap_factor_5948160 >> [check_all_factor]
fac_daily_kd_deap_factor_74 >> fac_daily_kd_deap_factor_5948158 >> [check_all_factor]
fac_daily_kd_deap_factor_75 >> fac_daily_kd_deap_factor_5948159 >> [check_all_factor]
fac_daily_kd_deap_factor_72 >> fac_daily_kd_deap_factor_5948155 >> [check_all_factor]
fac_daily_kd_deap_factor_73 >> fac_daily_kd_deap_factor_5948157 >> [check_all_factor]
fac_daily_kd_deap_factor_32 >> [fac_daily_kd_deap_factor_59]
fac_daily_kd_deap_factor_71 >> [fac_daily_kd_deap_factor_94]
fac_daily_kd_deap_factor_66 >> [fac_daily_kd_deap_factor_89]
fac_daily_kd_deap_factor_56 >> [fac_daily_kd_deap_factor_81]
fac_daily_kd_deap_factor_60 >> [fac_daily_kd_deap_factor_85]
fac_daily_kd_deap_factor_43 >> [fac_daily_kd_deap_factor_72]
fac_daily_kd_deap_factor_80 >> [check_all_factor]
check_qsdata >> fac_daily_kd_deap_factor_5948161 >> fac_daily_kd_deap_factor_5948162 >> fac_daily_kd_deap_factor_5948163 >> fac_daily_kd_deap_factor_5948164 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948165 >> fac_daily_kd_deap_factor_5948166 >> fac_daily_kd_deap_factor_5948167 >> fac_daily_kd_deap_factor_5948168 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948169 >> fac_daily_kd_deap_factor_5948170 >> fac_daily_kd_deap_factor_5948171 >> fac_daily_kd_deap_factor_5948172 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948173 >> fac_daily_kd_deap_factor_5948174 >> fac_daily_kd_deap_factor_5948175 >> fac_daily_kd_deap_factor_5948176 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948177 >> fac_daily_kd_deap_factor_5948178 >> fac_daily_kd_deap_factor_5948179 >> fac_daily_kd_deap_factor_5948180 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948181 >> fac_daily_kd_deap_factor_5948182 >> fac_daily_kd_deap_factor_5948183 >> fac_daily_kd_deap_factor_5948184 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948185 >> fac_daily_kd_deap_factor_5948186 >> fac_daily_kd_deap_factor_5948187 >> fac_daily_kd_deap_factor_5948188 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948189 >> fac_daily_kd_deap_factor_5948190 >> fac_daily_kd_deap_factor_5948191 >> fac_daily_kd_deap_factor_5948192 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948193 >> fac_daily_kd_deap_factor_5948194 >> fac_daily_kd_deap_factor_5948195 >> fac_daily_kd_deap_factor_5948196 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948197 >> fac_daily_kd_deap_factor_5948198 >> fac_daily_kd_deap_factor_5948199 >> fac_daily_kd_deap_factor_5948200 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948201 >> fac_daily_kd_deap_factor_5948202 >> fac_daily_kd_deap_factor_5948203 >> fac_daily_kd_deap_factor_5948204 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948205 >> fac_daily_kd_deap_factor_5948206 >> fac_daily_kd_deap_factor_5948207 >> fac_daily_kd_deap_factor_5948208 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948209 >> fac_daily_kd_deap_factor_5948210 >> fac_daily_kd_deap_factor_5948211 >> fac_daily_kd_deap_factor_5948212 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948213 >> fac_daily_kd_deap_factor_5948214 >> fac_daily_kd_deap_factor_5948215 >> fac_daily_kd_deap_factor_5948216 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948217 >> fac_daily_kd_deap_factor_5948218 >> fac_daily_kd_deap_factor_5948219 >> fac_daily_kd_deap_factor_5948220 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948221 >> fac_daily_kd_deap_factor_5948222 >> fac_daily_kd_deap_factor_5948223 >> fac_daily_kd_deap_factor_5948224 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948225 >> fac_daily_kd_deap_factor_5948226 >> fac_daily_kd_deap_factor_5948227 >> fac_daily_kd_deap_factor_5948228 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948229 >> fac_daily_kd_deap_factor_5948230 >> fac_daily_kd_deap_factor_5948231 >> fac_daily_kd_deap_factor_5948232 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948233 >> fac_daily_kd_deap_factor_5948234 >> fac_daily_kd_deap_factor_5948235 >> fac_daily_kd_deap_factor_5948236 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948237 >> fac_daily_kd_deap_factor_5948238 >> fac_daily_kd_deap_factor_5948239 >> fac_daily_kd_deap_factor_5948240 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948241 >> fac_daily_kd_deap_factor_5948242 >> fac_daily_kd_deap_factor_5948243 >> fac_daily_kd_deap_factor_5948244 >> fac_daily_kd_deap_factor_5948249 >> check_all_factor
check_qsdata >> fac_daily_kd_deap_factor_5948245 >> fac_daily_kd_deap_factor_5948246 >> fac_daily_kd_deap_factor_5948247 >> fac_daily_kd_deap_factor_5948248  >> fac_daily_kd_deap_factor_5948250 >> check_all_factor

fac_daily_kd_deap_factor_37 >> [fac_daily_kd_deap_factor_66]
check_all_factor >> trigger_kd01_kd06_alphanet_0_0_1_task