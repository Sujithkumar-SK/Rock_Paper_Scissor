import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "rockpaperscissors"

def user_input():
  inp = input("Enter your choice [Rock,Paper,Scissor]: ").lower()
  if inp in option:
    return inp
  else:
    print("invalid input...")
    user_input()
def com_inp():
  return random.choice(option)


def res(user_inp,com_inp):
  if user_inp == com_inp:
    return "tie"
  elif (user_inp == 'rock' and com_inp == 'scissor') or (user_inp == 'paper' and com_inp =='rock') or (user_inp == 'scissor' and com_inp == 'paper'):
    return "user"
  else:
    return "computer"

@app.route('/',methods=['GET','POST'])
def index():
  if "user_score" not in session:
    session["user_score"]=0
  if "com_score" not in session:
    session["com_score"]=0
  user_input=None
  com_input=None
  result=None


  if request.method == "POST":
    user_input = request.form["choice"]
    com_input = com_inp()
    result = res(user_input,com_input)
    if result == "user":
      session["user_score"]+=1
    elif result =="computer":
      session["com_score"]+=1
    
  return render_template("index.html", user_input=user_input, com_input=com_input, result = result, user_score=session["user_score"], com_score=session["com_score"])


@app.route("/reset", methods=["GET","POST"])
def reset():
  session['user_score']=0
  session['com_score']=0
  return render_template("index.html", user_score=0, com_score=0)

if __name__ == "__main__":
  option = ['rock','paper','scissor']
  app.run(debug=True)
