#!/usr/bin/env python3
from flask.templating import render_template_string
import SquareCrosswordGenerator as square_gen
from re import search as f
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "QSKMALKMKMASDOIWDJ898*&SD*A&H"

def export_to_json(square_crossword):
    json_dictionary = {}
    json_dictionary['rows'] = [[len(regex.text_sequence), regex.regex_sequence] for regex in square_crossword['rows_regexes']]
    json_dictionary['cols'] = [[len(regex.text_sequence), regex.regex_sequence] for regex in square_crossword['cols_regexes']]
    return(json_dictionary)

def values():
        try:
                mass = export_to_json(square_gen.random_square_crossword(2))
        except:
                mass = export_to_json(square_gen.random_square_crossword(2))
        return mass

@app.route('/', methods=["GET", "POST"])
def simple():
        if not session:
                session['count'] = 0
        if not session.get('mass'):
                session['mass'] = values()

        pr1 = session['mass']['rows'][0][1]
        pc1 = session['mass']['cols'][0][1]
        pr2 = session['mass']['rows'][1][1]
        pc2 = session['mass']['cols'][1][1]

        if request.method == "POST":
                answer = request.form.get('answer').strip().rstrip().split()
                try:
                        user_pr1 = str(answer[0] + answer[1])
                        user_pr2 = str(answer[2] + answer[3])
                        user_pc1 = str(answer[0] + answer[2])
                        user_pc2 = str(answer[1] + answer[3])
                except:
                        session.clear()
                        return render_template("index.html", message="Not all fields are filled, try again", button='<a href="/" class="button">New Game</a>')
                if f(pc1, user_pc1) and f(pc2, user_pc2) and f(pr2, user_pr2) and f(pr1, user_pr1):
                        session['count'] = int(session['count'])+1
                        session['mass'].clear()
                        return render_template('index.html', message="correct", count=int(session['count']), button='<a href="/" class="button">Next</a>')
                else:   
                        session.clear()
                        return render_template("index.html", message="Wrong! Try again.", button='<a href="/" class="button">New Game</a>')
        count = int(session['count'])
        if count == 200:
                return render_template_string("yetiCTF{[c]+o{2}[l]+_R3}")
        return render_template("index.html", count=count, pr1=pr1, pr2=pr2, pc1=pc1, pc2=pc2)

@app.route('/help')
def help():
    return render_template("help.html")
