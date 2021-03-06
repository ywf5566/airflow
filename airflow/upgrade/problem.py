# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import
from typing import NamedTuple, List, Iterable

from airflow.upgrade.rules.base_rule import BaseRule


class RuleStatus(NamedTuple(
    'RuleStatus',
    [
        ('rule', BaseRule),
        ('messages', List[str]),
        ('skipped', bool)
    ]
)):
    @property
    def is_success(self):
        return len(self.messages) == 0

    @classmethod
    def from_rule(cls, rule):
        # type: (BaseRule) -> RuleStatus
        msg = rule.should_skip()
        if msg:
            return cls(rule=rule, messages=[msg], skipped=True)

        messages = []  # type: List[str]
        result = rule.check()
        if isinstance(result, str):
            messages = [result]
        elif isinstance(result, Iterable):
            messages = list(result)
        return cls(rule=rule, messages=messages, skipped=False)
