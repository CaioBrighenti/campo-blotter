import markovify
import os
#os.getcwd()
#os.chdir("C:/Users/Caio Laptop/Documents/Repositories/campo-blotter")

# Get raw text as string.
with open("blotter.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(660))
