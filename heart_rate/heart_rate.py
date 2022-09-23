print('Lets see at what rate your heart need to beat to strength your heart?')

age=int(input('Please set your age: '))

slowest=(((220-age)/100)*65)
faster=(((220-age)/100)*85)

print(f'When you exercise to strengthen your heart, you should keep your heart rate between {round(slowest,0)} and {round(faster,0)} beats per minute')