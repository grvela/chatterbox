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


