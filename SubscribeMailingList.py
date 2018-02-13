import requests

class MailingList:
    
    def __init__(self,email):
        print ("Subscribe or Unsubscribe to mailing list")
        self.email = email
    
    def Subscribe(self, mlist):
        url = 'https://lists.debian.org/cgi-bin/subscribe.pl'
        data = {'user_email':self.email,
                'list':mlist,
                'action':'Subscribe' }

        r = requests.post(url, data=data)
        print(r.content)
        if(int(r.status_code) == 200):
            print('Check your Email to confirm')
    
    def Unsubscribe(self,mlist):
        url = 'https://lists.debian.org/cgi-bin/subscribe.pl'
        data = {'user_email':self.email,
                'list':mlist,
                'action':'Unsubscribe' }

        r = requests.post(url, data=data)
        print(r.content)
        if(int(r.status_code) == 200):
            print('Check your Email to confirm')
    
obj = MailingList('xola@youzend.net')
obj.Subscribe('debian-user-digest') ##'debian-outreach'

obj.Unsubscribe('debian-outreach')
