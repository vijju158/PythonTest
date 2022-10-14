print("Hello")
from matplotlib import pyplot as plt
players = ['Vijay', 'Ranjit']
score = [10, 20]
plt.bar(players,score,color='red')
plt.title('Score Card')
plt.xlable('Players')
plt.ylable('Runs')
plt.show()