# Arctic Masher

This is a clone of the debian game "Monster Masher". This project was started because we couldn't get it to run on our machines.

# Setup

Use pip to install the libraries in requirements.txt
Use python to run arctic-masher.py

# Gameplay

There are two players, and each can move in the 8 cardinal directions, pushing lines of blocks that are in the way. Crush monsters between blocks without getting smished by them yourself. See "pygame.K_w" etc. in arctic-masher.py for the controls. For example, 'pygame.K_e, "ne"' means that the "e" key is used to move "ne" which is north east. "KP" stands for "KeyPad" I believe, so player two uses the numpad. The "p" control, which is the shift keys for each player, allows you to move away from a block to pull it, which only works if there is not a monster adjacent to it.

You have a few respawns, but after that you have to exit the game and start it again to restart.

If you want to change the number of enemies, or check out the "mage" enemy type, edit the numbers on the "spawnEnemy" calls inside of mapgen.py e.g. change "spawnEnemy(Smart, 1)" to "spawnEnemy(Smart, 10)" to make the game miserable.
