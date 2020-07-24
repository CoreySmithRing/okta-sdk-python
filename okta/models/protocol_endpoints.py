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


class ProtocolEndpoints(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.acs = config["acs"]\
                if "acs" in config else None
            self.authorization = config["authorization"]\
                if "authorization" in config else None
            self.jwks = config["jwks"]\
                if "jwks" in config else None
            self.metadata = config["metadata"]\
                if "metadata" in config else None
            self.slo = config["slo"]\
                if "slo" in config else None
            self.sso = config["sso"]\
                if "sso" in config else None
            self.token = config["token"]\
                if "token" in config else None
            self.user_info = config["userInfo"]\
                if "userInfo" in config else None
        else:
            self.acs = None
            self.authorization = None
            self.jwks = None
            self.metadata = None
            self.slo = None
            self.sso = None
            self.token = None
            self.user_info = None