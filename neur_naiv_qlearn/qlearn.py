import random
import numpy as np

class QLearningAgent:
    """
    A Q-learning ügynökünket képviselő osztály
    """
    def __init__(self, n_states_row,  n_states_cols, n_actions, learning_rate):
        self.n_states_row = n_states_row
        self.n_states_cols = n_states_cols
        self.n_actions = n_actions
        self.learning_rate = learning_rate
        
        self.q_table = np.zeros((self.n_states_row, self.n_states_cols, n_actions))
    
    def act(self, state_row, state_col, epsilon):
        # Generáljon véletlen számot a [0, 1] intervallumon
        random_int = random.uniform(0,1)
        action = 0

        """

        Ezt az if, else cuccot kellett megírni csak itten
        """
        # kiválasszuk a legjobbat ha kisebb az epsilon
        if random_int > epsilon:
            action = np.argmax(self.q_table[state_row][state_col])
        else:
            action = random.randint(0, self.n_actions-1)
        return action        
    
    def learn(self, state_row, state_col, action, reward, new_state_row, new_state_col, gamma):
        old_value = self.q_table[state_row][state_col][action]
        new_estimate = reward + gamma * max(self.q_table[new_state_row][new_state_col]) 
        
        self.q_table[state_row][state_col][action] = old_value + self.learning_rate * (new_estimate- old_value)
        
#####################

from tqdm import tqdm
import matplotlib.pyplot as plt

class Maze():
    def __init__(self, epsilon, gamma, environment, aisles):
        self.epsilon = epsilon
        self.gamma = gamma
        self.agent: QLearningAgent = None # type: ignore
        self.aisles = aisles
        self.environment_rows = environment[0]
        self.environment_columns = environment[1]
        self.actions = ['up', 'right', 'down', 'left']
        self.rewards = np.full((self.environment_rows, self.environment_columns), -100.)
        self.rewards[0, 5] = 100.

        # Rewardok beállítása a folyosókhoz
        for row in range(1, self.environment_rows-1):
            for col in self.aisles[row]:
                self.rewards[row, col] = -1.
    
    def set_agent(self, agent):
        self.agent = agent

    def get_rewards(self):
        return self.rewards

    def viz(self, tabel):
        plt.imshow(tabel)
        plt.colorbar()
        plt.show()

    def viz_route(self, start_row, start_col):
        shortest_path = self.get_shortest_path(start_row, start_col)
        table = self.get_rewards().copy()
        for item in shortest_path:
            table[item[0]][item[1]] = 50
        
        self.viz(table)
        
    def is_terminal_state(self, row, col):
        """ Vég állapot vizsgálata"""
        if self.rewards[row, col] == -1.:
            return False
        else:
            return True
            epsilon = min_epsi
    def get_starting_location(self):
        """Nem terminális kezdőpont generálása"""
        row = np.random.randint(self.environment_rows)
        column = np.random.randint(self.environment_columns)

        # Ha terminális állapotot generálunk tovább probálkozunk
        while self.is_terminal_state(row, column):
            row = np.random.randint(self.environment_rows)
            column = np.random.randint(self.environment_columns)
        
        return row, column
    
    # define a function that will get the next location based on the chosen action
    def get_next_location(self, row, col, action):
        """Definiál egy függvényt, amely a következő helyet vissza adja a 
        kiválasztott művelet alapján"""
        new_row = row
        new_column = col
        if self.actions[action] == 'up' and row > 0:
            new_row -= 1
        elif self.actions[action] == 'right' and col < self.environment_columns - 1:
            new_column += 1
        elif self.actions[action] == 'down' and row < self.environment_rows - 1:
            new_row += 1
        elif self.actions[action] == 'left' and col > 0:
            new_column -= 1
        return new_row, new_column
  
    def get_shortest_path(self, start_row, start_column):
        """Vissza adja a legröbidebb utat"""       
        if self.is_terminal_state(start_row, start_column):
            return []
        else: 
            # Ha nem terminális a kezdő pont
            current_row, current_column = start_row, start_column
            shortest_path = []
            shortest_path.append([current_row, current_column])
            # Megyünk amíg terminálisig nem jutunk.
            while not self.is_terminal_state(current_row, current_column):
                action = np.argmax(self.agent.q_table[current_row][current_column])                
                current_row, current_column = self.get_next_location(current_row, current_column, action)
                shortest_path.append([current_row, current_column])
                
            return shortest_path

    def play(self, learning_step):
        """A tanulást végző metódus"""
        print(self.rewards)
        for episode in tqdm(range(learning_step)):
            new_row, new_column = self.get_starting_location()
            while not self.is_terminal_state(new_row, new_column):
                


                """
                Illetve ezeket itten alul
                """
                action = self.agent.act(new_row, new_column,self.epsilon);           
                #megnézzük a kövi lépést hogy melyik sor oszlop lesz,     
                next_row, next_col = self.get_next_location(new_row,new_column,action)

                #kiszedjük az ahhoz tartozó cellához a rewardot, 
                reward = self.rewards[next_row][next_col]

                #tanuljon a hibákból
                self.agent.learn(new_row,new_column,action,reward,next_row,next_col,self.gamma);
                new_row, new_column = next_row, next_col
                
####################

# Folyosók
aisles = {}
aisles[1] = [i for i in range(1, 10)]
aisles[2] = [1, 7, 9]
aisles[3] = [i for i in range(1, 10)]
aisles[3].append(9)
aisles[4] = [1, 3, 7, 9]
aisles[5] = [i for i in range(11)]
aisles[6] = [5]
aisles[7] = [i for i in range(1, 10)]
aisles[8] = [3, 7]
aisles[9] = [i for i in range(8)]

#####################

maze = Maze(epsilon = 0.9, gamma = 0.9, environment=(11,11), aisles = aisles)

maze.viz(maze.get_rewards())

#####################

n_states_row = maze.environment_rows * maze.environment_rows * 2;
n_states_cols = maze.environment_columns * maze.environment_columns * 2;
maze.agent = QLearningAgent(n_states_row,n_states_cols,4,1.0)

maze.play(10000)

#####################

maze.viz_route(6, 5)