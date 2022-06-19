from collections import OrderedDict

from flask import Flask, request, jsonify
from flask_cors import CORS
from nonbinary import Skill


app = Flask(__name__)
CORS(app)

skill = Skill()
test = skill.test()


@app.route("/webhook", methods=["GET", "POST"])
def index():
    global test
    req = request.get_json()

    response = {
            "version": req["version"],
            "session": req["session"],
            "response": {
                "text": "Не знаю такой команды",
                "end_session": False,
            }
        }

    command = req["request"]["command"].lower()

    if skill.check(command):
        response["response"]["text"] = "Привет Вездекодерам!"
        response["response"]["tts"] = "Привет ^Вездек`одерам^!"
        return jsonify(response)

    if any([skill.is_test, "тест" in command]):
        skill.is_test = True
        try:
            i, response["response"]["text"] = next(test)
            if i != 1:
                if command in skill.ans[i - 1].keys():
                    skill.calc(command, i - 1)
        except StopIteration:
            skill.is_test = False
            class_ = list(OrderedDict(skill.categories).items())
            class_ = class_[0][0]
            test = skill.test()
            return jsonify(
                {
                    "version": req["version"],
                    "session": req["session"],
                    "response": {
                        "text": f"{class_.capitalize()}",
                        "tts": f"Поздравляю! <speaker audio=marusia-sounds/game-win-1> Вы {skill.prof[class_]}! "
                               f"Не хотите подготовиться к Вездек`оду?",
                        "end_session": False,
#                         "commands": [
#                             {
#                                 "type": "BigImage",
#                                 "image_id": 457239018,
#                             },
#                             {
#                                 "type": "MiniApp",
#                                 "url": "[https://vk.com/app7923597]"
#                             }
#                         ]
                    }
                }
            )

        return jsonify(response)

    return response


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
