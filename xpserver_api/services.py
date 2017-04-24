import logging
import sendgrid
import os
from sendgrid.helpers.mail import *
import random
from django.contrib.auth.models import User
from pyfcm import FCMNotification

logger = logging.getLogger(__name__)


class EmailSender:
    @staticmethod
    def send_activation_email_with(profile):

        logger.info('Starting to build activation email')
        try:
            api_url = os.environ.get('API_URL')
            # create email and send it
            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email("cc-labs-zero@codecentric.de")
            subject = "Activate your xp 2017 account"
            to_email = Email(profile.user.email)
            content = Content("text/html", """
            <html>
            <body>
            <h1>Activate your xp 2017 account</h1>
            <p>
                A xp 2017 account activation has been requested with this email address.
                If you requested this activation, please click this link to finish the process:
            </p>
            <p>
                <a href="%sactivate_account?activation_code=%s&user_name=%s" method="get">Activate</a>
            </p>
            <p>
                If you feel that you have received this mail in error, contact
                <a href="mailto:cc-labs-zero@codecentric.de">cc-labs-zero@codecentric.de</a> for resolving the issue.
            </p>
            </body>
            </html>
            """ % (api_url, profile.activation_code, profile.user.username))

            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            logger.info("Email created for %s" % profile.user.email)
            return response
        except Exception as error:
            logging.error('An exception occurred: {}'.format(error))

    @staticmethod
    def send_password_email_for(email, password):
        logger.info('Starting to build password email')
        try:
            web_url = os.environ.get('WEB_URL')
            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email("cc-labs-zero@codecentric.de")
            subject = "A xp 20017 account has been created for you"
            to_email = Email(email)
            content = Content("text/html", """
            <html>
            <body>
            <h1>A xp 2017 account has been created for you</h1>
            <p>
               You can log into it by navigating to the <a href="%s">xp 2017 login page</a>.
               Your initial password has been set to <b>%s</b>. We recommend changing it after the first login.
            </p>
            </body>
            </html>
            """ % (web_url, password))
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            logger.info("Email created for %s" % email)
            return response
        except Exception as error:
            logging.error('An exception occurred: {}'.format(error))


def generate_activation_code():
    return str(random.getrandbits(64))


def username_present(username):
    return User.objects.filter(username=username).exists()


class PushNotificationSender:
    @staticmethod
    def send_push_notification(fcm_registration_id, message):
        logger.info('Starting to build push notification')
        try:
            push_service = FCMNotification(api_key=os.environ.get('FIREBASE_API_KEY'))
            data_message = {
                "message": message
            }
            push_service.notify_single_device(registration_id=fcm_registration_id, data_message=data_message)
            logger.info('Push notification sent')
        except Exception as error:
            logging.error('An exception occurred: {}'.format(error))
