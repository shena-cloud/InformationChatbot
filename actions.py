# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
import mysql.connector



class ActionContactSearch(Action):

    def name(self) -> Text:
         return "action_contact_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        db = mysql.connector.connect(host = "localhost",
        user = "root",
        passwd = "rasachatbot123",
        database = "faculty",
        auth_plugin="mysql_native_password")
        fname = tracker.get_slot("faculty_name")
        email = tracker.get_slot("contact")
        mycursor = db.cursor()
        q = "SELECT email_id FROM faculties WHERE (name = '%s');" % fname
        mycursor.execute(q)
        results = mycursor.fetchone()
        if results != None:
            reply = results[0]
            response = "The email id is {}".format(reply)
            dispatcher.utter_message(text = 'Sure')
            dispatcher.utter_message(text = response)
        else:
            dispatcher.utter_message(text = 'Sorry, could you please rephrase?')
        db.close()
        return[AllSlotsReset()]

class ActionQualificationSearch(Action):

    def name(self) -> Text:
        return "action_qualification_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        db = mysql.connector.connect(host = "localhost",
        user = "root",
        passwd = "rasachatbot123",
        database = "faculty",
        auth_plugin="mysql_native_password")
        fname = tracker.get_slot("faculty_name")
        mycursor = db.cursor()
        q = "SELECT qualification FROM faculties WHERE (name = '%s');" % fname
        mycursor.execute(q)
        results = mycursor.fetchone()
        if results != None:
            reply = results[0]
            response = "The qualification of {} is {}.".format(fname, reply)
            dispatcher.utter_message(text = 'I am on it.')
            dispatcher.utter_message(text = response)
        else:
            dispatcher.utter_message(text = 'Sorry, could you please rephrase?')
        db.close()
        return[AllSlotsReset()]    

class ActionSpecialisationSearch(Action):

    def name(self) -> Text:
        return"action_specialisation_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        db = mysql.connector.connect(host = "localhost",
            user = "root",
            passwd = "rasachatbot123",
            database = "faculty",
            auth_plugin = "mysql_native_password")
        fname = tracker.get_slot("faculty_name")
        mycursor = db.cursor()
        q = "SELECT specialisation FROM faculties WHERE (name = '%s');" % fname
        mycursor.execute(q)
        results = mycursor.fetchone()
        if results != None:
            reply = results[0]
            response = "{} is specialised in {}.".format(fname, reply)
            dispatcher.utter_message(text = "Sure!")
            dispatcher.utter_message(text = response)
        else:
            dispatcher.utter_message(text = 'Sorry, could you please rephrase?')
        db.close()
        return[AllSlotsReset()]

class ActionJoiningYear(Action):

    def name(self) -> Text:
        return"action_joining_year_search"

    def run(self , dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domian: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        db = mysql.connector.connect(host = "localhost",
            user = "root",
            passwd = "rasachatbot123",
            database = "faculty",
            auth_plugin = "mysql_native_password")
        fname = tracker.get_slot("faculty_name")
        mycursor = db.cursor()
        q = "SELECT joining_year FROM faculties WHERE (name = '%s');" % fname
        mycursor.execute(q)
        results = mycursor.fetchone()
        if results != None:
            reply = results[0]
            response = "{} joined on {}.".format(fname, reply)
            dispatcher.utter_message(text = "Hmm..Let me check")
            dispatcher.utter_message(text =response)
        else:
            dispatcher.utter_message(text = 'Sorry, could you please rephrase?')
        db.close()
        return[AllSlotsReset()]

        