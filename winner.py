
"""The game of billiards involves two players knocking 33 balls around on a green baize table. Well, there is more to it, but for our purposes this is sufficient.
The game consists of several rounds and in each round both players obtain a score, based on how well they played. Once all the rounds have been played, the total score of each player is determined by adding up the scores in all the rounds and the player with the higher total score is declared the winner.
The Siruseri Sports Club organises an annual billiards game where the top two players of Siruseri play against each other. The Manager of Siruseri Sports Club decided to add his own twist to the game by changing the rules for determining the winner. In his version, at the end of each round the leader and her current lead are calculated. Once all the rounds are over the player who had the maximum lead at the end of any round in the game is declared the winner."""
a=0
b=0
for i in range(int(input())):
     c,d=map(int,input().split())
     if c>d:
          m=c-d
     else:
          m=d-c
     if m>a:
          a=m
          b=i+1
print(b,a)
