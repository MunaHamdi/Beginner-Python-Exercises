# Use slices to take outa segment of a long word
# Word:antidisestablishmentarianism
# Slice the word 'establishment' out of the word and store in variable 'answer'

word='antidisestablishmentarianism'
frkey=word.find('establishment')
enkey=word.find('arianism')
answer=(word[frkey:enkey])
print(answer)

word='antidisestablishmentarianism'
frkey=word.find('establishment')
answer=(word[frkey:frkey+13])
print(answer)