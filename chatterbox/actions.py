# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class SalesPizza(FormAction):

    def name(self) -> Text:
        return "sales_pizza"

    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return [
            "u_name",
            "u_location",
            "u_flavor",
            "u_size",
            "u_drink"
        ]


    def slot_mappings(self):
        return {
            "u_name": self.from_entity(entity="name", intent="inform"),
            "u_location": self.from_entity(entity="location", intent="inform"),
            "u_flavor": self.from_entity(entity="flavor", intent="inform"),
            "u_size": self.from_entity(entity="size", intent="inform"),
            "u_drink": self.from_entity(entity="drink", intent="inform")
        }


    def submit(
        self,
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any],
        ) -> List[Dict]:
        dispatcher.utter_message(template="utter_goodbye")
        return []
