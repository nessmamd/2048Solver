**ONLY CHROME BASED**
For computer 2048 (https://2048game.com/) as it allows key arrows

Selenium for web control and PyTorch for RL model



Steps:
1. Browser automation connects to 2048 website
2. Extract game state from DOM/JavaScript
3. Feed state to RL model
4. Model outputs action (up/down/left/right)
5. Send keyboard command to browser
6. Get reward (score increase)
7. Repeat
