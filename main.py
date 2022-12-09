import matplotlib.pyplot as plt
import networkx as nx
# Define the players
players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

# Define the chemistry matrix
# This matrix contains the chemistry ratings between each pair of players
# For example, the chemistry between Player 1 and Player 2 is 80
chemistry_matrix = [
  [100, 80, 70, 60, 90],
  [80, 100, 80, 90, 70],
  [70, 80, 100, 80, 60],
  [60, 90, 80, 100, 70],
  [90, 70, 60, 70, 100]
]

def display_team_chemistry(players, chemistry_matrix):
  # Create a new graph
  G = nx.Graph()

  # Loop through all players in the team
  for player in players:
    # Add the player to the graph
    G.add_node(player)

  # Loop through all players in the team
  for i in range(len(players)):
    for j in range(i+1, len(players)):
      # Check if the players have a high chemistry rating
      if chemistry_matrix[i][j] >= HIGH_CHEMISTRY_THRESHOLD:
        # If so, add an edge between the players in the graph
        G.add_edge(players[i], players[j])

  # Draw the graph
  nx.draw(G, with_labels=True)

  # Show the plot
  plt.show()