import logging
import json
from sqlalchemy import text, TextClause
from src.python.db.execute_query import ExecuteQuery
from src.python.models.person import Person


class PersonController:

    @classmethod
    def get_person_by_id(cls, person_id: int):
        """
        Get all persons from database.
        :return: list of persons.
        """

        query = "CALL get_select_person(" + str(person_id) + ")"

        return ExecuteQuery.select(query)

    @classmethod
    def insert_person(cls, person: Person):
        """
        Insert person in database.
        :param person: person to insert.
        :return: None.
        """

        data = {
            'first_name': person.first_name,
            'last_name': person.last_name,
            'middle_name': person.middle_name,
            'date_of_birth': person.date_of_birth,
            'gender_id': person.gender_id,
            'nationality': person.nationality,
            'current_occupation': person.current_occupation,
            'current_income': person.current_income,
            'marital_status': person.marital_status,
            'num_children': person.num_children,
            'education_level': person.education_level,
            'email': person.email,
            'phone': person.phone,
            'notes': person.notes
        }

        __query: TextClause = text('CALL post_insert_person (:first_name, :last_name, :middle_name, '
                                   ':date_of_birth, :gender_id, :nationality, :current_occupation, '
                                   ':current_income, :marital_status, :num_children, :education_level, '
                                   ':email, :phone, :notes)')

        ExecuteQuery.insert(__query, data)

    @classmethod
    def update_person(cls, person_id: int, person: Person) -> Person:
        """
            Update person in database.
            :param person_id: person id to update.
            :return: None.
            """

        data_person = {
            'id': person_id,
            'first_name': person.first_name,
            'last_name': person.last_name,
            'middle_name': person.middle_name,
            'date_of_birth': person.date_of_birth,
            'gender_id': person.gender_id,
            'nationality': person.nationality,
            'current_occupation': person.current_occupation,
            'current_income': person.current_income,
            'marital_status': person.marital_status,
            'num_children': person.num_children,
            'education_level': person.education_level,
            'email': person.email,
            'phone': person.phone,
            'notes': person.notes
        }

        __update_query: TextClause = text('CALL put_update_person (:id, :first_name, :last_name, :middle_name, '
                                          ':date_of_birth, :gender_id, :nationality, :current_occupation, '
                                          ':current_income, :marital_status, :num_children, :education_level, '
                                          ':email, :phone, :notes)')

        ExecuteQuery.insert(__update_query, data_person)

    @classmethod
    def delete_person(cls, person_id: int):
        """
        Delete person in database.
        :param person_id: person id to delete.
        :return: None.
        """

        data = {
            'id': int(person_id)
        }

        __query: TextClause = text('CALL put_delete_person(:id)')

        ExecuteQuery.insert(__query, data)
