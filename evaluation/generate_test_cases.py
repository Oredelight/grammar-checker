import json
import random

random.seed(42)

def make(category, inputs):
    return [{"category": category, **item} for item in inputs]

tense = make("tense", [
    {"input": "Yesterday I goes to school.", "expected": "Yesterday I went to school."},
    {"input": "She eat breakfast early.", "expected": "She ate breakfast early."},
    {"input": "They was playing football.", "expected": "They were playing football."},
    {"input": "I seen him yesterday.", "expected": "I saw him yesterday."},
    {"input": "We was late for class.", "expected": "We were late for class."},
])

subject_verb = make("subject_verb_agreement", [
    {"input": "She go to school daily.", "expected": "She goes to school daily."},
    {"input": "They plays football.", "expected": "They play football."},
    {"input": "He do his work.", "expected": "He does his work."},
    {"input": "The dogs runs fast.", "expected": "The dogs run fast."},
    {"input": "My friend and I is happy.", "expected": "My friend and I are happy."},
])

pronouns = make("pronouns", [
    {"input": "Me and him went there.", "expected": "He and I went there."},
    {"input": "Her is my friend.", "expected": "She is my friend."},
    {"input": "Them are coming.", "expected": "They are coming."},
    {"input": "Him and me is late.", "expected": "He and I are late."},
    {"input": "I gave it to she.", "expected": "I gave it to her."},
])

articles = make("articles", [
    {"input": "I saw elephant in zoo.", "expected": "I saw an elephant in the zoo."},
    {"input": "She is best student.", "expected": "She is the best student."},
    {"input": "He bought car.", "expected": "He bought a car."},
    {"input": "We went to hospital.", "expected": "We went to the hospital."},
    {"input": "She is engineer.", "expected": "She is an engineer."},
])

prepositions = make("prepositions", [
    {"input": "She is good in math.", "expected": "She is good at math."},
    {"input": "He depends of me.", "expected": "He depends on me."},
    {"input": "We arrived to school.", "expected": "We arrived at school."},
    {"input": "She married with him.", "expected": "She is married to him."},
    {"input": "They discussed about it.", "expected": "They discussed it."},
])

punctuation = make("punctuation", [
    {"input": "Wow this is crazy I love it", "expected": "Wow, this is crazy! I love it."},
    {"input": "He said hello how are you", "expected": "He said, \"Hello, how are you?\""},
    {"input": "Wait what is this", "expected": "Wait, what is this?"},
    {"input": "I like apples bananas oranges", "expected": "I like apples, bananas, and oranges."},
    {"input": "No way thats true", "expected": "No way, that's true!"},
])

spelling = make("spelling", [
    {"input": "I recieved your mesage.", "expected": "I received your message."},
    {"input": "She beleives in me.", "expected": "She believes in me."},
    {"input": "He commited mistake.", "expected": "He committed mistake."},
    {"input": "They definetly won.", "expected": "They definitely won."},
    {"input": "I alwasy forget.", "expected": "I always forget."},
])

mixed = make("mixed", [
    {"input": "i seen him he was go market", "expected": "I saw him. He was going to the market."},
    {"input": "me and him was late", "expected": "He and I were late."},
    {"input": "she dont like apples", "expected": "She doesn't like apples."},
    {"input": "they is playing football", "expected": "They are playing football."},
    {"input": "we was happy we wins", "expected": "We were happy we won."},
])

dataset = (
    tense + subject_verb + pronouns +
    articles + prepositions + punctuation +
    spelling + mixed
)

while len(dataset) < 100:
    item = random.choice(dataset).copy()
    item["input"] += " "  
    dataset.append(item)

random.shuffle(dataset)

with open("evaluation/test_cases.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2)

print("Generated", len(dataset), "test cases")