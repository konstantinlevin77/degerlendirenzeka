import sqlite3
import os

from .BaseDao import BaseDao 
from .Question import Question


class QuestionsDao(BaseDao):

    def __init__(self):
        super().__init__()

    
    def add(self,question:Question):
        self.execute_query("INSERT INTO questions(question_text) VALUES(?)",[question.question_text])


    def delete(self,question:Question):
        self.execute_query("DELETE FROM questions WHERE id=?",[question.id])


    def update(self,question:Question):
        self.execute_query("UPDATE questions SET question_text=? WHERE id=?",[question.question_text,question.id])


    def find_by_question_text(self,question_text):
        result = self.execute_query("SELECT * FROM questions WHERE question_text=?",[question_text],True)
        if len(result) > 0:
            result = result[0]
        else:
            return None
        return Question(id=result[0],question_text=result[1])


    def find_by_id(self,question_id):
        result = self.execute_query("SELECT * FROM questions WHERE id=?",[question_id],True)
        if len(result) > 0:
            result = result[0]
        else:
            return None
        return Question(id=result[0],question_text=result[1])


    def find_all(self):
        questions_list = []
        results = self.execute_query("SELECT * FROM questions",does_return=True)
        for r in results:
            questions_list.append(Question(r[0],r[1]))
        
        return questions_list

