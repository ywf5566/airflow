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

from abc import abstractmethod


class BaseRule(object):
    @property
    @abstractmethod
    def title(self):
        # type: () -> str
        """Short one-line summary"""
        pass

    @property
    @abstractmethod
    def description(self):
        # type: () -> str
        """A long description explaining the problem in detail. This can be an entry from UPDATING.md file."""
        pass

    def should_skip(self):
        """
        Executes a pre check of configuration. If returned value is
        True then the checking the rule is omitted.
        """
        pass

    def check(self):
        pass
