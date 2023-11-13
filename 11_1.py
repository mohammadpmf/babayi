from random import choice
answers = {
    'hello': ['hi', 'hello', 'gom sho'],
    'how are you': ['Im good', 'Im bad', 'Shut up'],
    'goodbye': ['bye', 'goodbye', '?'],
    'how is the weather tomorrow': ['cloudy', 'sunny', 'storm', 'windy'],
}
a = ''
while a not in ['end', 'exit']:
    a = input("Tell something").strip()
    print(choice(answers.get(a, ["I cant answer", 'cant understand'])))

