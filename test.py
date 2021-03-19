from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True


board= [["P", "Q", "S", "R", "T"], 
        ["R", "A", "N", "N", "P"], 
        ["C", "A", "T", "H", "B"], 
        ["R", "R", "J", "T", "B"], 
        ["I", "A", "K", "L", "R"]]

class FlaskTests(TestCase):
    def  test_main_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)            
            self.assertIn("<h2>Boggle!</h2>", html)
            self.assertIsNone( session.get("HIGHSCORE"))
            self.assertIn("board", session)


    def test_make_board(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board']=board           
            resp= client.get('/make-board')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code,200)
            self.assertIn("<button id='guess-button'>Check guess</button>", html)
            self.assertIn("board",session)     
    
    
    def test_word_check(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board']=board
            resp=client.get('/check-word?guess=ran')
            resp2=client.get('/check-word?guess=cfdfdt')
            resp3=client.get('/check-word?guess=false')
            self.assertEqual(resp.status_code,200)
            self.assertEqual(session["board"],board)
            self.assertEqual(resp.json['result'], "ok")                    
            self.assertEqual(resp2.json['result'], "not-word")
            self.assertEqual(resp3.json['result'], "not-on-board")

            

                        



    # # TODO -- write tests for every view function / feature!

