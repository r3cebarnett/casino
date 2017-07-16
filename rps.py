import random

print("""
Rock, Paper, Scissors written by Maurice Barnett, v1.0
Simply type "r", "p", or "s" to pick, you can keep playing until you keyboard
interrupt or until you enter "q" when prompted. It also keeps score. Leave an
issue on the github for "casino" under r3cebarnett if there are any issues
""")
brk = 'y'
cpuScore = 0
playerScore = 0

while brk != 'n':
    playerInput = input('(R)ock, (P)aper, or (S)cissors?\n').upper()
    cpuInput = random.choice(['R','P','S'])

    if playerInput == 'R':
        if cpuInput == 'S':
            playerScore += 1
        elif cpuInput == 'P':
            cpuScore += 1
    elif playerInput == 'S':
        if cpuInput == 'R':
            cpuScore += 1
        elif cpuInput == 'P':
            playerScore += 1
    else:
        if cpuInput == 'R':
            playerScore += 1
        elif cpuInput == 'S':
            cpuScore += 1

    print('Player used', playerInput, 'and CPU used', cpuInput)
    print('Score: Player', playerScore, '-', cpuScore, 'CPU\n')

    brk = input('Would you like to play again? (y/n): ').lower()
