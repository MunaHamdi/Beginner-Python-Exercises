# Use slices to take outa segment of a long word
# Word:antidisestablishmentarianism
# Slice the word 'establishment' out of the word and store in variable 'answer'

word='antidisestablishmentarianism'
frkey=word.find('establishment')
print(frkey)
enkey=word.find('arianism')
print(enkey)
variable=(word[7:20])
print(variable)