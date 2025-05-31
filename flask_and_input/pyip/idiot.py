import pyinputplus as pyip
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    
    if response == 'no':
        print('Thank you. Have a nice day, i.e. fuck off')
        break
    elif response == 'yes':
        print('Great!!! Start by answering the question again please...')
