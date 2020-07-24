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


class VerifyUserFactorResponse(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]\
                if "_embedded" in config else None
            self.links = config["_links"]\
                if "_links" in config else None
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.factor_result = config["factorResult"]\
                if "factorResult" in config else None
            self.factor_result_message = config["factorResultMessage"]\
                if "factorResultMessage" in config else None
        else:
            self.embedded = None
            self.links = None
            self.expires_at = None
            self.factor_result = None
            self.factor_result_message = None