#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('KD-FACTOR-DEAP-AND-CHECK',
          default_args=default_args,
          schedule_interval=None,
          start_date=datetime(2020, 12, 17, 17, 0))

# ============================================== tasks ==================================================
l2_factor_check = BashOperator(task_id="l2_factor_check", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh l2_factor_check ", dag=dag)
check_qsdata = BashOperator(task_id="check_qsdata", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_qsdata ", dag=dag)
fac_daily_kd_deap_factor_8 = BashOperator(task_id="fac_daily_kd_deap_factor_8", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531307 ", dag=dag)
fac_daily_kd_deap_factor_2 = BashOperator(task_id="fac_daily_kd_deap_factor_2", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531301 ", dag=dag)
fac_daily_kd_deap_factor_3 = BashOperator(task_id="fac_daily_kd_deap_factor_3", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531302 ", dag=dag)
fac_daily_kd_deap_factor_1 = BashOperator(task_id="fac_daily_kd_deap_factor_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531300 ", dag=dag)
fac_daily_kd_deap_factor_6 = BashOperator(task_id="fac_daily_kd_deap_factor_6", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531305 ", dag=dag)
fac_daily_kd_deap_factor_7 = BashOperator(task_id="fac_daily_kd_deap_factor_7", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531306 ", dag=dag)
fac_daily_kd_deap_factor_4 = BashOperator(task_id="fac_daily_kd_deap_factor_4", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531303 ", dag=dag)
fac_daily_kd_deap_factor_5 = BashOperator(task_id="fac_daily_kd_deap_factor_5", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531304 ", dag=dag)
fac_daily_kd_deap_factor_18 = BashOperator(task_id="fac_daily_kd_deap_factor_18", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531317 ", dag=dag)
fac_daily_kd_deap_factor_19 = BashOperator(task_id="fac_daily_kd_deap_factor_19", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531318 ", dag=dag)
fac_daily_kd_deap_factor_23 = BashOperator(task_id="fac_daily_kd_deap_factor_23", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531322 ", dag=dag)
fac_daily_kd_deap_factor_24 = BashOperator(task_id="fac_daily_kd_deap_factor_24", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531323 ", dag=dag)
fac_daily_kd_deap_factor_25 = BashOperator(task_id="fac_daily_kd_deap_factor_25", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531324 ", dag=dag)
fac_daily_kd_deap_factor_11 = BashOperator(task_id="fac_daily_kd_deap_factor_11", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531310 ", dag=dag)
fac_daily_kd_deap_factor_12 = BashOperator(task_id="fac_daily_kd_deap_factor_12", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531311 ", dag=dag)
fac_daily_kd_deap_factor_13 = BashOperator(task_id="fac_daily_kd_deap_factor_13", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531312 ", dag=dag)
fac_daily_kd_deap_factor_14 = BashOperator(task_id="fac_daily_kd_deap_factor_14", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531313 ", dag=dag)
fac_daily_kd_deap_factor_20 = BashOperator(task_id="fac_daily_kd_deap_factor_20", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531319 ", dag=dag)
fac_daily_kd_deap_factor_16 = BashOperator(task_id="fac_daily_kd_deap_factor_16", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531315 ", dag=dag)
fac_daily_kd_deap_factor_17 = BashOperator(task_id="fac_daily_kd_deap_factor_17", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531316 ", dag=dag)
fac_daily_kd_deap_factor_35 = BashOperator(task_id="fac_daily_kd_deap_factor_35", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531334 ", dag=dag)
fac_daily_kd_deap_factor_29 = BashOperator(task_id="fac_daily_kd_deap_factor_29", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531328 ", dag=dag)
fac_daily_kd_deap_factor_30 = BashOperator(task_id="fac_daily_kd_deap_factor_30", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531329 ", dag=dag)
fac_daily_kd_deap_factor_27 = BashOperator(task_id="fac_daily_kd_deap_factor_27", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531326 ", dag=dag)
fac_daily_kd_deap_factor_33 = BashOperator(task_id="fac_daily_kd_deap_factor_33", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531332 ", dag=dag)
fac_daily_kd_deap_factor_34 = BashOperator(task_id="fac_daily_kd_deap_factor_34", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531333 ", dag=dag)
fac_daily_kd_deap_factor_31 = BashOperator(task_id="fac_daily_kd_deap_factor_31", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531330 ", dag=dag)
fac_daily_kd_deap_factor_32 = BashOperator(task_id="fac_daily_kd_deap_factor_32", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531331 ", dag=dag)
fac_daily_kd_deap_factor_43 = BashOperator(task_id="fac_daily_kd_deap_factor_43", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531342 ", dag=dag)
fac_daily_kd_deap_factor_44 = BashOperator(task_id="fac_daily_kd_deap_factor_44", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531343 ", dag=dag)
fac_daily_kd_deap_factor_47 = BashOperator(task_id="fac_daily_kd_deap_factor_47", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531346 ", dag=dag)
fac_daily_kd_deap_factor_48 = BashOperator(task_id="fac_daily_kd_deap_factor_48", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531347 ", dag=dag)
fac_daily_kd_deap_factor_51 = BashOperator(task_id="fac_daily_kd_deap_factor_51", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531350 ", dag=dag)
fac_daily_kd_deap_factor_36 = BashOperator(task_id="fac_daily_kd_deap_factor_36", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531335 ", dag=dag)
fac_daily_kd_deap_factor_37 = BashOperator(task_id="fac_daily_kd_deap_factor_37", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531336 ", dag=dag)
fac_daily_kd_deap_factor_38 = BashOperator(task_id="fac_daily_kd_deap_factor_38", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531337 ", dag=dag)
fac_daily_kd_deap_factor_39 = BashOperator(task_id="fac_daily_kd_deap_factor_39", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531338 ", dag=dag)
fac_daily_kd_deap_factor_45 = BashOperator(task_id="fac_daily_kd_deap_factor_45", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531344 ", dag=dag)
fac_daily_kd_deap_factor_40 = BashOperator(task_id="fac_daily_kd_deap_factor_40", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531339 ", dag=dag)
fac_daily_kd_deap_factor_41 = BashOperator(task_id="fac_daily_kd_deap_factor_41", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531340 ", dag=dag)
fac_daily_kd_deap_factor_64 = BashOperator(task_id="fac_daily_kd_deap_factor_64", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531363 ", dag=dag)
fac_daily_kd_deap_factor_55 = BashOperator(task_id="fac_daily_kd_deap_factor_55", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531354 ", dag=dag)
fac_daily_kd_deap_factor_56 = BashOperator(task_id="fac_daily_kd_deap_factor_56", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531355 ", dag=dag)
fac_daily_kd_deap_factor_52 = BashOperator(task_id="fac_daily_kd_deap_factor_52", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531351 ", dag=dag)
fac_daily_kd_deap_factor_60 = BashOperator(task_id="fac_daily_kd_deap_factor_60", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531359 ", dag=dag)
fac_daily_kd_deap_factor_62 = BashOperator(task_id="fac_daily_kd_deap_factor_62", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531361 ", dag=dag)
fac_daily_kd_deap_factor_58 = BashOperator(task_id="fac_daily_kd_deap_factor_58", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531357 ", dag=dag)
fac_daily_kd_deap_factor_59 = BashOperator(task_id="fac_daily_kd_deap_factor_59", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531358 ", dag=dag)
fac_daily_kd_deap_factor_72 = BashOperator(task_id="fac_daily_kd_deap_factor_72", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531371 ", dag=dag)
fac_daily_kd_deap_factor_73 = BashOperator(task_id="fac_daily_kd_deap_factor_73", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531372 ", dag=dag)
fac_daily_kd_deap_factor_75 = BashOperator(task_id="fac_daily_kd_deap_factor_75", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531374 ", dag=dag)
fac_daily_kd_deap_factor_76 = BashOperator(task_id="fac_daily_kd_deap_factor_76", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531375 ", dag=dag)
fac_daily_kd_deap_factor_77 = BashOperator(task_id="fac_daily_kd_deap_factor_77", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531376 ", dag=dag)
fac_daily_kd_deap_factor_65 = BashOperator(task_id="fac_daily_kd_deap_factor_65", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531364 ", dag=dag)
fac_daily_kd_deap_factor_66 = BashOperator(task_id="fac_daily_kd_deap_factor_66", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531365 ", dag=dag)
fac_daily_kd_deap_factor_67 = BashOperator(task_id="fac_daily_kd_deap_factor_67", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531366 ", dag=dag)
fac_daily_kd_deap_factor_69 = BashOperator(task_id="fac_daily_kd_deap_factor_69", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531368 ", dag=dag)
fac_daily_kd_deap_factor_74 = BashOperator(task_id="fac_daily_kd_deap_factor_74", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531373 ", dag=dag)
fac_daily_kd_deap_factor_70 = BashOperator(task_id="fac_daily_kd_deap_factor_70", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531369 ", dag=dag)
fac_daily_kd_deap_factor_71 = BashOperator(task_id="fac_daily_kd_deap_factor_71", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531370 ", dag=dag)
fac_daily_kd_deap_factor_87 = BashOperator(task_id="fac_daily_kd_deap_factor_87", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531386 ", dag=dag)
fac_daily_kd_deap_factor_80 = BashOperator(task_id="fac_daily_kd_deap_factor_80", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531379 ", dag=dag)
fac_daily_kd_deap_factor_81 = BashOperator(task_id="fac_daily_kd_deap_factor_81", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531380 ", dag=dag)
fac_daily_kd_deap_factor_78 = BashOperator(task_id="fac_daily_kd_deap_factor_78", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531377 ", dag=dag)
fac_daily_kd_deap_factor_85 = BashOperator(task_id="fac_daily_kd_deap_factor_85", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531384 ", dag=dag)
fac_daily_kd_deap_factor_86 = BashOperator(task_id="fac_daily_kd_deap_factor_86", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531385 ", dag=dag)
fac_daily_kd_deap_factor_83 = BashOperator(task_id="fac_daily_kd_deap_factor_83", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531382 ", dag=dag)
fac_daily_kd_deap_factor_84 = BashOperator(task_id="fac_daily_kd_deap_factor_84", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531383 ", dag=dag)
fac_daily_kd_deap_factor_88 = BashOperator(task_id="fac_daily_kd_deap_factor_88", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531387 ", dag=dag)
fac_daily_kd_deap_factor_89 = BashOperator(task_id="fac_daily_kd_deap_factor_89", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531388 ", dag=dag)
fac_daily_kd_deap_factor_91 = BashOperator(task_id="fac_daily_kd_deap_factor_91", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531390 ", dag=dag)
fac_daily_kd_deap_factor_92 = BashOperator(task_id="fac_daily_kd_deap_factor_92", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531391 ", dag=dag)
fac_daily_kd_deap_factor_93 = BashOperator(task_id="fac_daily_kd_deap_factor_93", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531392 ", dag=dag)
fac_daily_kd_deap_factor_94 = BashOperator(task_id="fac_daily_kd_deap_factor_94", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3531393 ", dag=dag)
check_all_factor = BashOperator(task_id="check_all_factor", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factors-check.sh ", dag=dag)

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