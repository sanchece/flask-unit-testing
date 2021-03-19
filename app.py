from flask import Flask, render_template, session, request, jsonify
from boggle import Boggle
app=Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

boggle_game = Boggle()


@app.route('/')
def main_page():
    board=boggle_game.make_board()
    session["board"]=board
    highscore = session.get("HIGHSCORE", None)
    return render_template('base.html', board=board)

@app.route('/make-board')
def make_board():
    board= session["board"]  
    return render_template("board.html", board=board)
 
@app.route('/check-word', methods=["GET"])
def check_word():
    guess=request.args["guess"]
    
    board=session["board"]
    result= boggle_game.check_valid_word(board,guess) 
    return jsonify({"result":result})

@app.route('/save-score', methods=["POST"])
def save_score():
    score=request.json["score"] 
        
    
    HIGHSCORE=session.get("HIGHSCORE", 0) 
    highscore= max(score,HIGHSCORE)
    session["HIGHSCORE"]=highscore

    return jsonify({"score":highscore})

