## A3C for CartPole

This code implements the Asynchronous Advantage Actor-Critic (A3C) algorithm for training an agent to play the CartPole environment in OpenAI Gym.

### Installation

This code requires the following dependencies:

* gym
* torch

You can install them using pip:

```bash
pip install gym torch
Use code with caution.

Usage
Run the code with the following command:

Bash
python A3C.py
Use code with caution.

This will start training multiple agents in parallel using A3C. The agents will learn to play CartPole and print the episode reward periodically.

Hyperparameters
The code uses the following default hyperparameters:

Learning rate: 1e-4
Environment: CartPole-v0
Number of actions: 2
Input dimensions: 4
Discount factor (gamma): 0.99
Number of steps per update (T_MAX): 5
These can be modified in the main.py script.


