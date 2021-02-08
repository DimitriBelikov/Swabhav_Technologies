#PART-5.2

user_input = 'to be or not to be that is the question'

# unique_tokens = set()
# for tokens in user_input.split():
#     unique_tokens.add(tokens)

#Alternate Approach
unique_tokens = set(words for words in user_input.split())

print(sorted(unique_tokens))