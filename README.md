# Golf-Course-Strategy-Simulator



-The Golf Course Strategy Simulator is a decision making tool that will use probabilities to find an expected number of strokes required to complete a golf hole from a certain situation.

-The simulator will compare different club choices by modeling each shot and accounting for some factors like:
  -Distance
  -Average club carry
  -Distance dispersion
  -Left/right dispersion
  -Shape of the shot
  -Spin
  -Wind direction and speed
  -Pin position
  -Lie of golf ball
  -Green firmness
  -Bunkers and water hazards
  -Course/green layout

-The model will generate a bunch of possible shot outcomes and find the expected number of strokes required to get the ball in the hole. After finding the club with the lowest expected shots it will recommend said club.

-Maths Approach:
  -Probability Distributions
    Model uncertainty with many different factors. 
  -Correlation models
    Find relationships between variables such has distance and lateral dispersion.
  -Geometric models
    Simulate the layout of the golf hole mathematically and determine where shots finish.
  -Probabilities estimation
    Probabilities of hitting green, losing it in water, rough, buncker.
  -Expected value
    Calculate the expected strokes based on the previous probabilities.
  -Club comparison
    Calculate expected strokes with different clubs and see which is lowest.
  -Monte Carlo simulation
    Simulate as many shots as possible and use the results to estimate the performance of each strategy.
  -Optimization
    Select the optimal strategy with all the data. 

-Long term Goal:
Given this situation on the golf course, which strategy and club give me the best expected score.

