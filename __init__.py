#
#
#
#             S.P.A.S. Team 2019
#             Skill for Picroft control over dedicated S.P.A.S. Droids by Denis Zahariev 
#             Made with <3 and Python
#
#

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from os.path import dirname
import requests
import urllib.request
import ssl
__author__ = 'eward'

LOGGER = getLogger(__name__)


class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

    def initialize(self):
        thank_you_intent = IntentBuilder("ThankYouIntent"). \                   #LAMP 1 ON
            require("ThankYouKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent"). \                #LAMP 1 OFF
            require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_how_are_you_intent)

        hello_world_intent = IntentBuilder("HelloWorldIntent"). \               #LAMP 2 ON
            require("HelloWorldKeyword").build()
        self.register_intent(hello_world_intent,
                             self.handle_hello_world_intent)
        
        hello_world_intent2 = IntentBuilder("HelloWorldIntent2"). \             #LAMP 2 OFF
            require("HelloWorldKeyword2").build()
        self.register_intent(hello_world_intent2,
                             self.handle_hello_world_intent2)
        
        

    def handle_thank_you_intent(self, message):
        requests.post('http://192.169.1.6/lamp1/on', data={"password":"sezam otvori se"})

    def handle_how_are_you_intent(self, message):
        requests.post('http://10.106.1.211/lamp1/off', data={"password":"sezam otvori se"})

    def handle_hello_world_intent(self, message):
        requests.post('http://10.106.1.211/lamp2/on', data={"password":"sezam otvori se"})
      
    def handle_hello_world_intent2(self, message):
        requests.post('http://10.106.1.211/lamp2/off', data={"password":"sezam otvori se"})


    def stop(self):
        pass


def create_skill():
    return HelloWorldSkill()
