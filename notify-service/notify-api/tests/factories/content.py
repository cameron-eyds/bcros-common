# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Conent factory."""

from enum import Enum
from typing import ClassVar

from faker import Faker

from notify_api.models import Content
from tests.factories.attachment import AttachmentFactory

faker = Faker()


class ContentFactory:  # pylint: disable=too-few-public-methods
    """Content factory."""

    class Models(dict, Enum):
        """Content model data."""

        CONTENT_1: ClassVar[dict] = {"subject": faker.text(), "body": faker.text()}

    class RequestData(dict, Enum):
        """Content post request payload data."""

        CONTENT_REQUEST_1: ClassVar[dict] = {"subject": faker.text(), "body": faker.text()}

        CONTENT_REQUEST_2: ClassVar[dict] = {
            "subject": faker.text(),
            "body": faker.text(),
            "attachments": [AttachmentFactory.RequestData.FILE_REQUEST_1],
        }

        CONTENT_REQUEST_3: ClassVar[dict] = {
            "subject": faker.text(),
            "body": faker.text(),
            "attachments": [AttachmentFactory.RequestData.FILE_REQUEST_1, AttachmentFactory.RequestData.FILE_REQUEST_2],
        }

    class RequestProviderData(dict, Enum):
        """Content post request payload data for test provider."""

        CONTENT_REQUEST_PROVIDER_1: ClassVar[dict] = {"subject": faker.text(), "body": faker.text()}

        CONTENT_REQUEST_PROVIDER_2: ClassVar[dict] = {
            "subject": faker.text(),
            "body": f"<html><body>{faker.text()}</body></html>",
        }

    class RequestBadData(dict, Enum):
        """Content post payload with inconsistent data."""

        # subject empty
        CONTENT_REQUEST_BAD_1: ClassVar[dict] = {"subject": "", "body": faker.text()}

        # without subject
        CONTENT_REQUEST_BAD_2: ClassVar[dict] = {"body": faker.text()}

        # without body
        CONTENT_REQUEST_BAD_3: ClassVar[dict] = {"subject": faker.text()}

    @staticmethod
    def create_model(session, notification_id: int = 1, content_info: dict = Models.CONTENT_1):
        """Produce a content model."""
        content = Content(subject=content_info["subject"], body=content_info["body"], notification_id=notification_id)
        session.add(content)
        session.commit()
        content = session.merge(content)

        return content
