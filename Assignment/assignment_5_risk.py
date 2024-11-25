import numpy as np
import matplotlib.pyplot as plt

# First step we need the number of rounds
number_rounds = 1000

# storage the lossess
attacker_losses_total = []
defender_losses_total = []

# Initialize total losses for attacker and defender
attacker_total_losses = 0
defender_total_losses = 0

# Simulate battle for each round
for i in range(number_rounds):
    # Attacker rolls 3 dice, Defender rolls 2 dice. random.randint to get random integers.
    # with below function we will get numbers between 1 and 6, 3 dices attacker, 2 dices defender
    #np.sort to get the the dice results in ascending order and [::-1] to reverst. then the 2 higest results can be compered.
    attacker_dice = np.sort(np.random.randint(1, 7, 3))[::-1]  
    defender_dice = np.sort(np.random.randint(1, 7, 2))[::-1]  

    # Compare the first highest dice 
    if attacker_dice[0] > defender_dice[0]:
        defender_losses = 1
        attacker_losses = 0
    else:
        defender_losses = 0
        attacker_losses = 1

    # Compare the second-highest dice
    if attacker_dice[1] > defender_dice[1]:
        defender_losses += 1
    else:
        attacker_losses += 1

    attacker_total_losses += attacker_losses
    defender_total_losses += defender_losses

    # Append cumulative losses to the lists for plotting
    attacker_losses_total.append(attacker_total_losses)
    defender_losses_total.append(defender_total_losses)

# Plot the total losses over the rounds
plt.plot(attacker_losses_total, label='Attacker Losses', color='orange')
plt.plot(defender_losses_total, label='Defender Losses', color='purple')

# Labels and title
plt.xlabel('Round')
plt.ylabel('Total Losses')
plt.title(f'Attacker vs Defender: Battle simulation {number_rounds} ')
plt.legend()

# Show plot
plt.show()
