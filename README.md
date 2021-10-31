# life2

This is my attempt at making a more sophisticated 'game of life' game, 99%
inspired by [this blog post](https://build-its.blogspot.com/2011/08/predator-prey-simulation.html).


## Dependencies:
[Random Module](https://pypi.org/project/random2/)
`pip install random2`

[Pygame](https://www.pygame.org/news)
[installation instructions I used](https://www.pygame.org/wiki/MacCompile)

## How to play:

The game is actually a simple simulation meant to display natural selection. 
'predators'(red) and 'prey'(blue) have different sight and movement ranges and reproduction
frequencies. Since predators must eat, they also have a configurable starvation period. 

Every reproduction cycle, the predators and prey generate clones with the possibility of a 
slight mutation (max mutation is configurable). The idea is that successful predators will 
consistently eat food and never starve, producing even stronger children, and successful prey
will run away from them, also producing better-evading children. In this way, natural selection
occurs in the predators and the prey.

Everything you need to configure is in `configuration.py`. Have fun!

MIT License
