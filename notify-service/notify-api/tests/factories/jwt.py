# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Data for the JWT tokens."""

PUBLIC_USER = "public_user"
STAFF_ROLE = "staff"


def helper_create_jwt(jwt_manager, roles: list[str] | None = None, username: str = "test-user"):  # pylint: disable=dangerous-default-value
    """Create a jwt bearer token with the correct keys, roles and username."""
    if roles is None:
        roles = []
    token_header = {"alg": "RS256", "typ": "JWT", "kid": "flask-jwt-oidc-test-client"}
    claims = {
        "iss": "https://example.localdomain/auth/realms/example",
        "sub": "43e6a245-0bf7-4ccf-9bd0-e7fb85fd18cc",
        "aud": "example",
        "exp": 2539722391,
        "iat": 1539718791,
        "jti": "flask-jwt-oidc-test-support",
        "typ": "Bearer",
        "username": f"{username}",
        "realm_access": {"roles": [*roles]},
    }
    return jwt_manager.create_jwt(claims, token_header)


def create_header(jwt_manager, roles: list[str] | None = None, username: str = "test-user", **kwargs):  # pylint: disable=dangerous-default-value
    """Return a header containing a JWT bearer token."""
    if roles is None:
        roles = []
    token = helper_create_jwt(jwt_manager, roles=roles, username=username)
    headers = {**kwargs, "Authorization": "Bearer " + token}
    return headers
