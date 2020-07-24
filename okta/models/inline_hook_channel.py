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


class InlineHookChannel(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.config = config["config"]\
                if "config" in config else None
            self.type = config["type"]\
                if "type" in config else None
            self.version = config["version"]\
                if "version" in config else None
        else:
            self.config = None
            self.type = None
            self.version = None