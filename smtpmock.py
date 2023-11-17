from datetime import datetime

from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP, Session, Envelope


class CustomHandler:
    async def handle_DATA(self,server:SMTP,session:Session,envelope:Envelope)->str:
        print('Connected')
        with open(datetime.now().strftime('%Y%m%d%H%M%S'),'w') as fo:
            fo.write(envelope.content)
        #return '500 Could not process your message'
        return '250 OK'

if __name__=='__main__':
    handler = CustomHandler()
    controller = Controller(handler,hostname='127.0.0.1', port=25)
    controller.start()
    input('SMTP running')
    controller.stop()
