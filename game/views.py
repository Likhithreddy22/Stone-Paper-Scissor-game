import random
from django.shortcuts import redirect, render

youDict = {"s": 1, "p": -1, "x": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissor"}

def get_result(computer, younum):
    if(computer == younum):
        return "ITS A DRAW"
    else:

        if(computer == -1 and younum == 0):
            return "YOU WIN!"

        elif(computer == -1 and younum == 1):
            return "YOU LOSE!"

        elif(computer == 1 and younum == 0):
            return "YOU LOSE!"

        elif(computer == 1 and younum == -1):
           return "YOU WIN!"

        elif(computer == 0 and younum == 1):
           return "YOU WIN!"

        elif(computer == 0 and younum == -1):
            return "YOU LOSE!"

        else:
            print("something went wrong")

def game_view(request):

    if "user_score" not in request.session:
        request.session["user_score"] = 0
        request.session["computer_score"] = 0
        

    context = {}

    if request.method == "POST":
        user_choice = request.POST.get("choice")

        # Set target only ONCE
        if request.session.get("target") is None:
            request.session["target"] = int(request.POST.get("target"))

        target_score = request.session["target"]

        computer = random.choice([1, 0, -1])
        younum = youDict[user_choice]

        result = get_result(computer, younum)

        if result == "YOU WIN!":
            request.session["user_score"] += 1
        elif result == "YOU LOSE!":
            request.session["computer_score"] += 1

        winner = None
        if request.session["user_score"] >= target_score:
            winner = "🎉 YOU ARE THE FINAL WINNER!"
        elif request.session["computer_score"] >= target_score:
            winner = "💻 COMPUTER WINS THE GAME!"

        context = {
            "user_choice": reverseDict[younum],
            "computer_choice": reverseDict[computer],
            "result": result,
            "user_score": request.session["user_score"],
            "computer_score": request.session["computer_score"],
            "target": target_score,
            "winner": winner
        }

        # Reset ONLY after winner
        if winner:
            request.session.flush()

    return render(request, "game.html", context)


def reset_game(request):
    request.session["user_score"] = 0
    request.session["computer_score"] = 0
    return redirect("/")