# Tower_defence_Golear_Karpenko
[![build status](
  http://img.shields.io/travis/Disadvantaged/Tower_defence_Golear_Karpenko/master.svg?style=flat)](
 https://travis-ci.com/Disadvantaged/Tower_defence_Golear_Karpenko)


Tower defence
(Paired project)


Short info: This is a strategy game, where the goal is to protect player territory. There is a road on the map leading to your city. You should protect it at all costs. Near the road, you can put some defensive mechanisms. 

Installation:
    pip3 install Tower_defence_Golear_Karpenko

Launch:
    tower_defence
Or:
    python3 -m Tower_defence_Golear_Karpenko

How to play:
Play - New game. Launches a wave of enemies. You should put towers on the grass, that would kill the monsters. 
On your account you have money for purchasing towers.
You can buy towers of different cost.
Every enemy robbs your territories and takes 200 coins.

New wave - starts new wave of enemies, gives you 500 coins.
There is 3 waves of enemies. If after some enemies breach and you have <= 0 coins, than you lose.
If you have protected your kingdom from all 3 waves, than you win.

Each tower has a different price/range/power. 


----
About game architecture
- Implemented various Design patterns and made the game scalable.
- Different maps, enemies, towers, etc could be easily added.
- Launched my code in public repository of packages
- Set the project so that before release it is being tested
