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
# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
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
        requests.post('http://192.168.0.116/lamp1/on', data={"password":"sezam otvori se"})

    def handle_how_are_you_intent(self, message):
        requests.post('http://192.168.0.116/lamp1/off', data={"password":"sezam otvori se"})

    def handle_hello_world_intent(self, message):
        requests.post('http://192.168.0.116/lamp2/on', data={"password":"sezam otvori se"})
      
    def handle_hello_world_intent2(self, message):
        requests.post('http://192.168.0.116/lamp2/off', data={"password":"sezam otvori se"})


    def stop(self):
        pass


def create_skill():
    return HelloWorldSkill()
