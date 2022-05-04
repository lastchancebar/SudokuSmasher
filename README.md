# Sudoku Smasher

## Table of Contents
-<a href="#about">About Sudoku Smasher</a>
-<a href="#how_to">How to play</a> 
-<a href="#ux">UX Design</a>
    - <a href="#user_stories">User Stories</a>
    - <a href="typography">Typography</a>
    - <a href="#color">Color</a>
- <a href ="#features">Features</a>
  - <a href="#difficulty">Difficulty Settings</a>
  - <a href="#board">Board</a>
  - <a href="#input">Input</a>
  - <a href="#rules">Rules</a>
  - <a href="#val_check">Validation Check</a>
  - <a href="#solution">Solution</a>
  - <a href="#game_exit">Exit from Game</a>
  - <a href="#input_val">Input Validation</a>
  - <a href="#future">Future Features</a>
- <a href="#data_model">Data Model</a>
  - <a href="#attributes">Attributes</a>
  - <a href= "#methods">Methods</a>
- <a href="#logic">Logic Flow</a>
- <a href="#tech_used">Technologies Used</a>
- -<a href="#testing">Testing</a>
  - <a href="#bugs">Bugs</a>
  - <a href="valid_test">Validator Testing</a>
  - <a href="#test_user_stories">Testing User Stories</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>
  - <a href="#tutorials">Tutorials</a>
- <a href="#acknowledgements">Acknowledgements</a>
  
  <section id="about">

  # About Sudoku Smasher
  Sudoku Smasher is a Python terminal game. It is deployed on Heroku and uses a mock terminal made by Code Institute.

  Users can play the classic game of Sudoku popularised in modern times by the Nokoli puzzle company in Japan. Studies have shown that Sudoku exercises the brain's working memory and doing the puzzle has been found to improve the memory of older people.(source-Wikipedia)

  Users can select an easy, medium or hard Sudoku puzzle to solve, are alerted if they make an incorrect selection on a square, and after finishing the puzzle users can see the correct solution.

  [The deployed site is here!]()

  <img src="#"amiresponsive>

  </swction>
  <section id = "how_to">

  # How to play

  Sudoku Smasher is based on the classic puzzle Sudoku, found in most newspapers and puzzle books. You can learn more about Sudoku [here](https://en.wikipedia.org/wiki/Sudoku).

  The rules for Sudoku are simple
  - There is a 9 x 9 grid which must be filled with numbers
- The game starts with some squares already filled in
- only the numbers 1 - 9 can be used 
- Every square must contain one number 
- Each 3×3 box can only contain each number from 1 to 9 once
- Each vertical column can only contain each number from 1 to 9 once
- Each horizontal row can only contain each number from 1 to 9 once

</section>

<section id="ux">

# UX Design

## <p id="user_stories"> User Stories</p>
- As a user I want a digital version of sudoku to avoid paper waste.
- As a user I want varying levels of difficulty to suit the mood I am in or to train myself to get better at sudoku. 
- As a user I want the option to get hints to the correct solution whenever I need it. 
- As a user I want to know if my solution is correct or not.
- As a user I want to be able to pencil in numbers that can be edited later.
- As a user, I want to know how long it takes me to complete a puzzle.

All user needs are met by the program. 

  - It is fully digital. 

  - It has 3 levels of difficulty to choose from. 
