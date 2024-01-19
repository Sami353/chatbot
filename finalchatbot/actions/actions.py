# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import psycopg2
import os
import subprocess
import webbrowser


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
    
class ActionFees(Action):

    def name(self) -> Text:
        return "action_provide_fees_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is our college's fee structure pdf document. It'll open automatically")
        pdf_path = 'C:/Clz/FYP/chatbot/IIMS-Fee-Structure-2021-Scholarship.pdf' 

        # Path to Brave browser executable
        # You might need to adjust the path if Brave is installed in a different location
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

        # Use the webbrowser module to get the Brave browser and open the PDF
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
        brave = webbrowser.get('brave')
        brave.open(pdf_path)

        return []

class ActionScholarship(Action):

    def name(self) -> Text:
        return "action_provide_scholarship_info"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the course name from the slot set by user input
        course_name = next(tracker.get_latest_entity_values("course"), None)

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",
            port="5432",
            user="postgres",
            password="vVcikBtONZer9zFw",
            host="db.atbayqaypnhvvabtjyxo.supabase.co"
        )
        
        # Create a cursor object
        cursor = conn.cursor()

        string = 'SELECT * FROM courses WHERE "Courses" = ' + "'" + course_name + "'"

        # Query the database for course information
        cursor.execute(string)
        course_details = cursor.fetchone()
        
        # Close the database connection
        cursor.close()
        conn.close()

        # Check if the course was found and create a response
        if course_details:
            # Assuming the order of course_details follows the schema of your table
            response = (f"To appy scholarship of {course_details[1]} - {course_details[8]} \n \n"
                        f"you can {course_details[7]}\n \n")
        else:
            response = "I'm sorry, I couldn't find details for that course."

        # Send the response to the user
        dispatcher.utter_message(text=response)

        return []
    
class ActionAdmission(Action):
    def name(self) -> Text:
        return "action_provide_admission_info"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the course name from the slot set by user input
        course_name = next(tracker.get_latest_entity_values("course"), None)

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",
            port="5432",
            user="postgres",
            password="vVcikBtONZer9zFw",
            host="db.atbayqaypnhvvabtjyxo.supabase.co"
        )
        
        # Create a cursor object
        cursor = conn.cursor()

        string = 'SELECT * FROM admission_req WHERE "Courses" = ' + "'" + course_name + "'"

        # Query the database for course information
        cursor.execute(string)
        admission_info = cursor.fetchone()
        
        # Close the database connection
        cursor.close()
        conn.close()

        # Check if admission information was found and construct a response
        if admission_info:
            response = (
                f"Admission Information for {admission_info[5]}:\n \n"
                f"The Entry Requirements are : \n {admission_info[1]}\n \n"
                f"Intake takes place in {admission_info[2]}\n \n"
                f"These are the Documents Required: {admission_info[3]}\n \n"
                f"Admission Process: {admission_info[4]}"
            )
        else:
            response = f"I couldn't find admission information for the course {course_name}."

        # Send the response to the user
        dispatcher.utter_message(text=response)

        return []


class ActionFetchCourseDetails(Action):
    def name(self) -> Text:
        return "action_provide_course_info"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the course name from the slot set by user input
        course_name = next(tracker.get_latest_entity_values("course"), None)

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",
            port="5432",
            user="postgres",
            password="vVcikBtONZer9zFw",
            host="db.atbayqaypnhvvabtjyxo.supabase.co"
        )
        
        # Create a cursor object
        cursor = conn.cursor()

        string = 'SELECT * FROM courses WHERE "Courses" = ' + "'" + course_name + "'"

        # Query the database for course information
        cursor.execute(string)
        course_details = cursor.fetchone()
        
        # Close the database connection
        cursor.close()
        conn.close()

        # Check if the course was found and create a response
        if course_details:
            # Assuming the order of course_details follows the schema of your table
            response = (f"{course_details[1]}: {course_details[8]} \n \n"
                        f"This a {course_details[3]} years course \n \n"
                        f"and consists of {course_details[4]} semesters \n \n")
        else:
            response = "I'm sorry, I couldn't find details for that course."

        # Send the response to the user
        dispatcher.utter_message(text=response)

        return []
    
    # this is the schema for courses 
    # response = (f"course_id:{course_details[0]} \n"
    #             f"Course : {course_details[1]}: {course_details[8]} \n"
    #             f"Classification: {course_details[2]} \n"
    #             f"Duration: {course_details[3]} years \n"
    #             f"Semesters: {course_details[4]} \n"
    #             f"Accreditation: {course_details[5]} \n"
    #             f"Fee Structure: {course_details[6]} \n"
    #             f"Scholarship: {course_details[7]}\n")
    
# class ActionProvideCoursesAvailable(Action):
#     def name(self) -> Text:
#         return "action_provide_courses_available"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Connect to the PostgreSQL database using environment variables
#         conn = psycopg2.connect(
#             dbname="postgres",
#             port="5432",
#             user="postgres",
#             password="vVcikBtONZer9zFw",
#             host="db.atbayqaypnhvvabtjyxo.supabase.co"
#         )
        
#         # Create a cursor object
#         cursor = conn.cursor()

#         # Query the database for all course names
#         cursor.execute("SELECT Courses FROM courses")

#         # Fetch all results
#         course_records = cursor.fetchall()

#         # Close the database connection
#         cursor.close()
#         conn.close()

#         # Check if any courses were found and construct a response
#         if course_records:
#             # Extract just the course names from the query results
#             course_names = [record[0] for record in course_records]
#             # Join the course names into a single string to form the response
#             course_list_str = ', '.join(course_names)
#             response = f"The available courses are: {course_list_str}"
#         else:
#             response = "Currently, there are no courses available."

#         # Send the response to the user
#         dispatcher.utter_message(text=response)

#         return []