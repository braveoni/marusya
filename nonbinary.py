class Skill:
    POSSIBLE_TEAM_VALUE = [
        "не бинарное дерево",
        "небинарное дерево"
    ]

    POSSIBLE_VEZDECODE_VALUE = [
        "везде код",
        "вездекод",
        "везде кот",
        "вездеход"
    ]

    def __init__(self):
        self.categories = {
            "web": 0,
            "cv": 0,
            "game_dev": 0,
            "mobile": 0,
            "data": 0,
            "design": 0,
            "rl": 0,
            "mini_app": 0,
            "backend": 0,
            "marusya": 0
        }

        self.qa = [
            "Если пакетный менеджер, то только\n\npip\nnpm\ngradel\ncomposer",
            "Вызывает ли у тебя смех слово pip?\n\nда/нет",
            "Сколько вкладок хрома можешь открыть одновременно?\n\n1\n2\n3\n4+",
            "Где лучшие тензоры?\n\nу нас в куде\nв гугле\nв одежде\nв датасете",
            "Часто ли вы видите на экране доллар?\n\nда/нет",
            "На сколько частей можно поделить круг?\n\n1\n2\n3\nn",
            "Хук это скилл Пуджа?\n\nда/нет",
            "Что идет после Q?\n\nt\nw\nlearning\nr"
        ]

        self.ans = {
            1: {
                "pip": "backend",
                "npm": "mini_app",
                "gradel": "mobile",
                "composer": "web"
            },
            2: {
                "нет": "backend",
                "да": "design"
            },
            3: {
                "1": "design",
                "2": "mini_app",
                "3": "game_dev",
                "4+": "mobile"
            },
            4: {
                "у нас в куде": "rl",
                "в гугле": "design",
                "в одежде": "design",
                "в датасете": "data"
            },
            5: {
                "да": "web",
                "нет": "cv"
            },
            6: {
                "1": "design",
                "2": "marusya",
                "3": "game_dev",
                "n": "data"
            },
            7: {
                "да": "design",
                "нет": "web"
            },
            8: {
                "t": "mobile",
                "w": "design",
                "learning": "rl",
                "r": "cv"
            }
        }

        self.prof = {
            "web": "Веб разработчик",
            "cv": "Специалист по компьютерному зрению",
            "game_dev": "Разработчик игр",
            "mobile": "Мобильный разработчик",
            "data": "Дата саентист",
            "design": "Дизайнер",
            "rl": "Специалист машинного обучения",
            "mini_app": "Разработчик mini app ВК",
            "backend": "Бэкендер",
            "marusya": "Маруся",
        }

        self.is_test = False

    def check(self, command):
        return any(word in command for word in self.POSSIBLE_TEAM_VALUE) \
               and any(word in command for word in self.POSSIBLE_VEZDECODE_VALUE)

    def add(self, category):
        print("hehe")
        self.categories[category] += 1

    def calc(self, answer, i):
        self.add(self.ans[i][answer])

    def test(self):
        for i, question in enumerate(self.qa[:1], 1):
            yield i, question
