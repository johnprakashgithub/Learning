from random import choice

questions = ["Whu the sky is blue?:","why is there a face on the moon?:", "where are the dinousures?:"]

question = choice(questions)
answer = input(question).strip()
expected = "Just because"
while answer.lower() != expected.lower():
    answer = input("Why?:").strip()

print("Oh ...Ok")