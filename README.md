**ONLY CHROME BASED**
For computer 2048 (https://2048game.com/) as it allows key arrows

Tech Stack: 

- Selenium for tracking and moving the website
- Gymnasium environment wraps the Selenium system for training
- PyTorch is where we make the models, that is then trained in the environment
- Numpy uses the 4x4 grids as the 2048


Steps:
1. Browser automation connects to 2048 website
2. Extract game state from DOM/JavaScript
3. Feed state to RL model
4. Model outputs action (up/down/left/right)
5. Send keyboard command to browser
6. Get reward (score increase)
7. Repeat

**RL models** - testing each one to find the best one/performing:
1. Deep Q-Network (DQN) - Q-value function and uses replay buffer to stabilize training

2. Policy Gradient (A2C/PPO) - probability distribution over actions and stable

3. AlphaZero-style (MCTS + Neural Network) - Combines Monte Carlo Tree Search with deep learning



