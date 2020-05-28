# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def get_entity_val(entity_type, entities):
    for ent in entities:
        if ent['entity'] == entity_type:
            return ent['value']
    return None    

class ActionAskFilms(Action):

    def name(self) -> Text:
        return "action_ask_films"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        chara = get_entity_val('character', tracker.latest_message['entities'])
        if chara:
            dispatcher.utter_message(text=f"{chara} played in film ABC")
        else:
            dispatcher.utter_message(text="I don't know which character you mean.")
        return []
