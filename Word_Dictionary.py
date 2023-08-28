# We are going to build a Word Dictionary using Python

# Have a python dictionary that has a key/value pair that represents a word and it's definition.
# Collect input from the user, input is a word.
# Check if the word is in the dictionary.
# Print the definition.

def main():
    word_dictionary = {
        "Accomplish": "achieve or complete successfully",
        "Attain": "succeed in achieving",
        "Balance": "an even distribution of weight enabling someone or something to remain upright and steady",
        "Detect": "discover or identify the presence or existence of",
        "Enormous": "very large in size quantity or extent",
        "Enigmatic": "difficult to interpret or understand",
        "Fabulous": "extraordinary",
        "Gratitude": "the quality of being thankful",
        "Hallucination": "an experience involving the apparent perception of something not present",
        "Impactful": "having a major effect",
        "Jolly": "happy and cheerful",
        "Knowledge": "the theoretical or practical understanding of a subject",
        "Lavish": "spending or using things that are more than necessary",
        "Neighbour": "a person living near or next door",
        "Optimistic": "hopeful and confident about the future",
        "Practical": "concerned with the actual doing or use of something rather than with theory and ideas",
        "Ultimately": "in the end",
        "Victory": "an act of defeating an enemy or opponent in a battle",
    }

    word = input("Enter a word:")
    if word in word_dictionary:
        print(word,":",word_dictionary[word])

main()
