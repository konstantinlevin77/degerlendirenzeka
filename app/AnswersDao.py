import sqlite3

from .BaseDao import BaseDao
from .Answer import Answer

class AnswersDao(BaseDao):

    def __init__(self):
        super().__init__()
    
    
    def add(self,answer:Answer):
        self.execute_query("INSERT INTO answers(question_id,answer) VALUES (?,?)",[answer.question_id,answer.answer])
    
    
    def delete(self,answer:Answer):
        self.execute_query("DELETE FROM answers WHERE id=?",[answer.id])
    

    def update(self,answer:Answer):
        self.execute_query("UPDATE answers SET answer=? WHERE id=?",[answer.answer,answer.id])
    

    def find_by_id(self,id):

        result = self.execute_query("SELECT * FROM answers WHERE id=?",[id],True)
        if len(result) > 0:
            result = result[0]
        else:
            return None
        return Answer(result[0],result[1],result[2])

    
    def find_by_question_id(self,question_id):

        answer_results = []
        results = self.execute_query("SELECT * FROM answers WHERE question_id=?",[question_id],True)
        for r in results:
            answer_results.append(Answer(r[0],r[1],r[2]))

        return answer_results


    def find_by_answer_text(self,answer_text):
        
        result = self.execute_query("SELECT * FROM answers WHERE answer=?",[answer_text],True)
        if len(result) > 0:
            result = result[0]
        else:
            return None
        return Answer(result[0],result[1],result[2])


    def find_all(self):
        
        answer_results = []
        results = self.execute_query("SELECT * FROM answers",does_return=True)
        for r in results:
            answer_results.append(Answer(r[0],r[1],r[2]))
        return answer_results

