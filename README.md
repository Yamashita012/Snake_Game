# ReadMe - Snake Game

This code is a simple implementation of the classic Snake Game using the Turtle graphics library in Python.

## How to Play
1. Run the Python script.
2. The game window will open with a black background and a snake.
3. Use the arrow keys (Up, Down, Left, Right) to control the snake's movement.
4. The snake's goal is to eat the food that appears on the screen.
5. Each time the snake eats the food, it grows longer and the score increases.
6. The game ends if the snake collides with the wall or its own body.
7. After the game ends, the final score is displayed.
8. Close the game window by clicking on it.

## Game Components
The code consists of the following components:

### 1. Snake
The `Snake` class handles the snake's movement and behavior. It contains methods to control the snake's direction and update its position.

### 2. Food
The `Food` class represents the food that the snake needs to eat. It is randomly generated on the screen, and when the snake collides with it, the score increases and the snake grows longer.

### 3. Scoreboard
The `Scoreboard` class keeps track of the player's score and displays it on the screen. It also handles the game over condition and displays the final score when the game ends.

### 4. Main Game Loop
The main game loop runs continuously until the game ends. It performs the following tasks:
- Updates the screen to display any changes.
- Controls the speed of the game by introducing a small delay using `time.sleep(0.1)`.
- Moves the snake forward one step in its current direction.
- Checks for collisions with the food, walls, or the snake's own tail.
- If a collision occurs, the game ends, and the appropriate actions are taken.

## Dependencies
The code relies on the following Python libraries:
- `turtle`: Used for creating the game window and graphics.

## Compatibility
The code is compatible with Python 3.x versions.

## Acknowledgments
This implementation of the Snake Game is inspired by the classic arcade game. The code is developed for educational purposes to demonstrate basic game development concepts using Python and the Turtle graphics library.
