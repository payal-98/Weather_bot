from typing import Dict, Text, Any, List, Union
from rasa_core_sdk import Action
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet, UserUttered, Restarted, FollowupAction
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction  
#from apixu.client import ApixuClient
import requests
from apixu.client import ApixuClient

class ActionWeather(Action):
   def name(self): 
    return "action_weather" 
   def run(self, dispatcher, tracker, domain):
    #params = {}
   # params{'access_key'} = "f1843d9dccc578684f39ca3fc8a69b5e"
    #params{'query'} = str(tracker.slots['location'])
    params = {'access_key': 'f1843d9dccc578684f39ca3fc8a69b5e','query': str(tracker.slots['state'])}
    print(params)
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    #print(api_response)
    response ='Current temperature in %s is %d C' % (api_response['location']['name'], api_response['current']['temperature'])
    dispatcher.utter_message(response)
    return[]