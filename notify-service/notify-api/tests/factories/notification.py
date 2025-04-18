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

"""notification factory."""

from datetime import UTC, datetime, timedelta
from enum import Enum
from typing import ClassVar

from faker import Faker

from notify_api.models import Notification, NotificationSendResponse
from tests.factories.attachment import AttachmentFactory
from tests.factories.content import ContentFactory

faker = Faker()


class NotificationFactory:  # pylint: disable=too-few-public-methods
    """notification factory."""

    class Models(dict, Enum):
        """Notification model data."""

        PENDING_1: ClassVar[dict] = {
            "id": 1,
            "recipients": faker.safe_email(),
            "requestDate": faker.date_time(),
            "requestBy": faker.user_name(),
            "statusCode": Notification.NotificationStatus.PENDING,
        }

        PENDING_2: ClassVar[dict] = {
            "id": 2,
            "recipients": faker.safe_email(),
            "requestDate": faker.date_time(),
            "requestBy": faker.user_name(),
            "statusCode": Notification.NotificationStatus.PENDING,
        }

        LESS_1_HOUR: ClassVar[dict] = {
            "id": 1,
            "recipients": faker.safe_email(),
            "requestDate": datetime.now(UTC) - timedelta(hours=1),
            "requestBy": faker.user_name(),
            "statusCode": Notification.NotificationStatus.FAILURE,
        }

        OVER_1_HOUR: ClassVar[dict] = {
            "id": 1,
            "recipients": faker.safe_email(),
            "requestDate": datetime.now(UTC) - timedelta(hours=10),
            "requestBy": faker.user_name(),
            "statusCode": Notification.NotificationStatus.FAILURE,
        }

    class RequestData(dict, Enum):
        """Notification post request payload data."""

        REQUEST_1: ClassVar[dict] = {
            "recipients": "abc@gmail.com",
            "requestBy": faker.user_name(),
            "requestDate": faker.date_time(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }

        REQUEST_2: ClassVar[dict] = {
            "recipients": "abc1@gmail.com",
            "requestBy": faker.user_name(),
            "requestDate": faker.date_time(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }

        REQUEST_3: ClassVar[dict] = {
            "recipients": "abc@gmail.com",
            "requestDate": faker.date_time(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }

    class RequestProviderData(dict, Enum):
        """Content post request payload data for test provider."""

        REQUEST_PROVIDER_1: ClassVar[dict] = {
            "provider": Notification.NotificationProvider.GC_NOTIFY,
            "data": {
                "recipients": "abc@gmail.com",
                "requestBy": faker.user_name(),
                "requestDate": faker.date_time(),
                "notifyType": "EMAIL",
                "content": ContentFactory.RequestProviderData.CONTENT_REQUEST_PROVIDER_1,
            },
        }

        REQUEST_PROVIDER_2: ClassVar[dict] = {
            "provider": Notification.NotificationProvider.SMTP,
            "data": {
                "recipients": "abc@gmail.com",
                "requestBy": faker.user_name(),
                "requestDate": faker.date_time(),
                "notifyType": "EMAIL",
                "content": ContentFactory.RequestProviderData.CONTENT_REQUEST_PROVIDER_2,
            },
        }

        REQUEST_PROVIDER_3: ClassVar[dict] = {
            "provider": Notification.NotificationProvider.HOUSING,
            "data": {
                "recipients": "abc@gmail.com",
                "requestBy": "STRR",
                "requestDate": faker.date_time(),
                "notifyType": "EMAIL",
                "content": ContentFactory.RequestProviderData.CONTENT_REQUEST_PROVIDER_1,
            },
        }

    class RequestBadData(dict, Enum):
        """Notification post payload with inconsistent data."""

        # email empty
        REQUEST_BAD_1: ClassVar[dict] = {
            "recipients": "",
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }

        # without email
        REQUEST_BAD_2: ClassVar[dict] = {
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }
        # bad email
        REQUEST_BAD_3: ClassVar[dict] = {
            "recipients": "aaa",
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }
        # bad email
        REQUEST_BAD_4: ClassVar[dict] = {
            "recipients": "aaa@aaa.com, bbbb",
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }
        # bad email
        REQUEST_BAD_5: ClassVar[dict] = {
            "recipients": "aaa@aaa.com, bbbb@bbb",
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }
        # bad email
        REQUEST_BAD_6: ClassVar[dict] = {
            "recipients": "aaa.com, bbbb@bbb.com",
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }

        # bad phone
        REQUEST_BAD_61: ClassVar[dict] = {
            "recipients": "+345678901230",
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestData.CONTENT_REQUEST_1,
        }

        # subject empty
        REQUEST_BAD_7: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestBadData.CONTENT_REQUEST_BAD_1,
        }
        # without subject
        REQUEST_BAD_8: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestBadData.CONTENT_REQUEST_BAD_2,
        }
        # without body
        REQUEST_BAD_9: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": ContentFactory.RequestBadData.CONTENT_REQUEST_BAD_3,
        }
        # name empty
        REQUEST_BAD_10: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": {
                "subject": faker.text(),
                "body": faker.text(),
                "attachments": [AttachmentFactory.RequestBadData.FILE_REQUEST_BAD_1],
            },
        }
        # without name
        REQUEST_BAD_11: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": {
                "subject": faker.text(),
                "body": faker.text(),
                "attachments": [AttachmentFactory.RequestBadData.FILE_REQUEST_BAD_2],
            },
        }
        # file content empty
        REQUEST_BAD_12: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": {
                "subject": faker.text(),
                "body": faker.text(),
                "attachments": [AttachmentFactory.RequestBadData.FILE_REQUEST_BAD_3],
            },
        }
        # without file content
        REQUEST_BAD_13: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": {
                "subject": faker.text(),
                "body": faker.text(),
                "attachments": [AttachmentFactory.RequestBadData.FILE_REQUEST_BAD_4],
            },
        }
        # without file content
        REQUEST_BAD_14: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": {
                "subject": faker.text(),
                "body": faker.text(),
                "attachments": [AttachmentFactory.RequestBadData.FILE_REQUEST_BAD_5],
            },
        }
        # without file content
        REQUEST_BAD_15: ClassVar[dict] = {
            "recipients": faker.safe_email(),
            "requestBy": faker.user_name(),
            "content": {
                "subject": faker.text(),
                "body": faker.text(),
                "attachments": [AttachmentFactory.RequestBadData.FILE_REQUEST_BAD_6],
            },
        }

    class SendResponseData(dict, Enum):
        """Notification post request payload data."""

        SEND_RESPONSE = NotificationSendResponse(responseId=faker.text(), recipient="abc@gmail.com")
        SEND_RESPONSE_2 = NotificationSendResponse(responseId=faker.text(), recipient="recipient2")
        SMS_SEND_RESPONSE = NotificationSendResponse(responseId=faker.text(), recipient="+12508888888")

    @staticmethod
    def create_model(session, notification_info: dict = Models.PENDING_1):
        """Produce a notification model."""
        notification = Notification(
            recipients=notification_info["recipients"],
            request_date=notification_info["requestDate"],
            request_by=notification_info.get("requestBy", ""),
            status_code=notification_info.get("statusCode"),
        )
        session.add(notification)
        session.commit()

        return notification
