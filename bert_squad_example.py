from deeppavlov import build_model, configs
from blank import ____

# Define document to ask and question to be asked
# document = ['The rain in Spain falls mainly on the plain.']
# question = ['Where does the rain in Spain fall?']

document = ["A telephone was ringing in the darkness — a tinny, unfamiliar ring. He fumbled for the bedside \
lamp and turned it on. Squinting at his surroundings he saw a plush Renaissance bedroom with \
Louis XVI furniture, hand-frescoed walls, and a colossal mahogany four-poster bed."]
question = ["What happened to the telephone?"]

# Init model
model = build_model(configs.squad.squad, download=False) # set download=True to store model pickle file in ~/.deeppavlov folder
model(document, question)

# Ask question and print result
print(f'question: {question}')
print(f'answer: {model(document, question)}')