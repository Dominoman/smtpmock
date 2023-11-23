#!/usr/bin/env python3

import logging
from datetime import datetime

from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP, Session, Envelope


class CustomHandler:
    async def handle_DATA(self, server: SMTP, session: Session, envelope: Envelope) -> str:
        logging.info('Connected')
        logging.info(f"SMTP Mail From:{envelope.mail_from} to: {'.'.join(envelope.rcpt_tos)} Client:{session.peer[0]} {len(envelope.content)} bytes")
        filename = datetime.now().strftime('%Y%m%d%H%M%S')+".eml"
        with open(filename, 'wb') as fo:
            fo.write(envelope.content)
        logging.info(f"Saved:{filename}")
        # return '500 Could not process your message'
        return '250 OK'


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
    handler = CustomHandler()
    controller = Controller(handler, hostname='127.0.0.1', port=25)
    controller.start()
    input('SMTP running')
    controller.stop()
