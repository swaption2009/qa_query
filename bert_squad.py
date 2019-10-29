from deeppavlov import build_model, configs

class BertSquad:
    def __init__(self, config=configs.squad.squad, download=False):
        self.model = build_model(config, download=download)

    def ask_question(self, document, question):
        answer = self.model(document, question)