"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject


class Provisioning(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.action = config["action"]\
                if "action" in config else None
            self.conditions = config["conditions"]\
                if "conditions" in config else None
            self.groups = config["groups"]\
                if "groups" in config else None
            self.profile_master = config["profileMaster"]\
                if "profileMaster" in config else None
        else:
            self.action = None
            self.conditions = None
            self.groups = None
            self.profile_master = None