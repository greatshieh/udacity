import random
import math
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator
import pandas as pd
import os
from visuals import plot_trials
import ast


class LearningAgent(Agent):
    """ An agent that learns to drive in the Smartcab world.
        This is the object you will be modifying. """

    def __init__(self,
                 env,
                 learning=False,
                 epsilon=1.0,
                 alpha=0.5,
                 constant=0.1):
        super(LearningAgent,
              self).__init__(env)  # Set the agent in the evironment
        self.planner = RoutePlanner(self.env, self)  # Create a route planner
        self.valid_actions = self.env.valid_actions  # The set of valid actions

        # Set parameters of the learning agent
        self.learning = learning  # Whether the agent is expected to learn
        self.Q = dict(
        )  # Create a Q-table which will be a dictionary of tuples
        self.epsilon = epsilon  # Random exploration factor
        self.alpha = alpha  # Learning factor
        self.counter = 0
        self.constant = constant

        ###########
        ## TO DO ##
        ###########
        # Set any additional class parameters as needed

    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)

        ###########
        ## TO DO ##
        ###########
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0
        if testing:
            self.alpha = 0
            self.epsilon = 0
        else:
            self.counter += 1
            # self.epsilon = self.constant**self.counter
            # self.alpha = 0.5 * self.constant**self.counter
            self.epsilon = math.fabs(math.cos(self.constant * self.counter))
            # self.epsilon -= 0.05

        return None

    def build_state(self):
        """ The build_state function is called when the agent requests data from the 
            environment. The next waypoint, the intersection inputs, and the deadline 
            are all features available to the agent. """

        # Collect data about the environment
        waypoint = self.planner.next_waypoint()  # The next waypoint
        inputs = self.env.sense(
            self)  # Visual input - intersection light and traffic
        deadline = self.env.get_deadline(self)  # Remaining deadline

        ###########
        ## TO DO ##
        ###########
        # Set 'state' as a tuple of relevant data for the agent
        state = (waypoint, inputs['light'], inputs['left'], inputs['right'],
                 inputs['oncoming'])

        return state

    def get_maxQ(self, state):
        """ The get_max_Q function is called when the agent is asked to find the
            maximum Q-value of all actions based on the 'state' the smartcab is in. """

        ###########
        ## TO DO ##
        ###########
        # Calculate the maximum Q-value of all actions for a given state

        maxQ = max(self.Q[state].values())

        return maxQ

    def createQ(self, state):
        """ The createQ function is called when a state is generated by the agent. """

        ###########
        ## TO DO ##
        ###########
        # When learning, check if the 'state' is not in the Q-table
        # If it is not, create a new dictionary for that state
        #   Then, for each action available, set the initial Q-value to 0.0
        if self.learning:
            self.Q.setdefault(state, {key: 0.0 for key in self.valid_actions})

        return

    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
            which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = None

        ###########
        ## TO DO ##
        ###########
        # When not learning, choose a random action
        # When learning, choose a random action with 'epsilon' probability
        #   Otherwise, choose an action with the highest Q-value for the current state
        if not self.learning:
            action = random.choice(self.valid_actions)  # None
        else:
            if self.epsilon > random.random() and self.epsilon > 0.1:
                action = random.choice(self.valid_actions)
            else:
                optional_action = []
                maxQ = self.get_maxQ(state)
                for key, value in self.Q[state].iteritems():
                    if value == maxQ:
                        optional_action.append(key)
                action = random.choice(optional_action)

        return action

    def learn(self, state, action, reward):
        """ The learn function is called after the agent completes an action and
            receives an award. This function does not consider future rewards 
            when conducting learning. """

        ###########
        ## TO DO ##
        ###########
        # When learning, implement the value iteration update rule
        #   Use only the learning rate 'alpha' (do not use the discount factor 'gamma')
        if self.learning:
            self.Q[state][action] += self.alpha * (
                reward - self.Q[state][action])

        return

    def update(self):
        """ The update function is called when a time step is completed in the 
            environment for a given trial. This function will build the agent
            state, choose an action, receive a reward, and learn if enabled. """

        state = self.build_state()  # Get current state
        self.createQ(state)  # Create 'state' in Q-table
        action = self.choose_action(state)  # Choose an action
        reward = self.env.act(self, action)  # Receive a reward
        self.learn(state, action, reward)  # Q-learn

        return


def run():
    """ Driving function for running the simulation. 
        Press ESC to close the simulation, or [SPACE] to pause the simulation. """
    # constant = 0.9957
    # alpha = 0.2
    tolerance = 0.01

    for constant in [
            0.0078, 0.0052, 0.0039, 0.0031, 0.0026, 0.0022, 0.0019, 0.0017
    ]:
        for alpha in [0.2, 0.5, 0.8]:
            good_counter = 0
            for n in range(20):
                ##############
                # Create the environment
                # Flags:
                #   verbose     - set to True to display additional output from the simulation
                #   num_dummies - discrete number of dummy agents in the environment, default is 100
                #   grid_size   - discrete number of intersections (columns, rows), default is (8, 6)
                env = Environment(verbose=True)
                ##############
                # Create the driving agent
                # Flags:
                #   learning   - set to True to force the driving agent to use Q-learning
                #    * epsilon - continuous value for the exploration factor, default is 1
                #    * alpha   - continuous value for the learning rate, default is 0.5
                agent = env.create_agent(
                    LearningAgent,
                    learning=True,
                    alpha=alpha,
                    constant=constant)
                ##############
                # Follow the driving agent
                # Flags:
                #   enforce_deadline - set to True to enforce a deadline metric
                env.set_primary_agent(agent, enforce_deadline=True)
                ##############
                # Create the simulation
                # Flags:
                #   update_delay - continuous time (in seconds) between actions, default is 2.0 seconds
                #   display      - set to False to disable the GUI if PyGame is enabled
                #   log_metrics  - set to True to log trial and simulation results to /logs
                #   optimized    - set to True to change the default log file name
                sim = Simulator(
                    env,
                    update_delay=0,
                    log_metrics=True,
                    display=False,
                    optimized=True)
                ##############
                # Run the simulator
                # Flags:
                #   tolerance  - epsilon tolerance before beginning testing, default is 0.05
                #   n_test     - discrete number of testing trials to perform, default is 0
                sim.run(n_test=100, tolerance=tolerance)

                safety_rating, reliability_rating = plot_trials(
                    'sim_improved-learning.csv')

                if safety_rating in ['A+', 'A'
                                     ] and reliability_rating in ['A', 'A+']:
                    good_counter += 1
                else:
                    break

            f = open('result.txt', 'a+')
            f.write('{}, {}, {}, {}\n'.format(constant, alpha, agent.counter,
                                              good_counter))
            f.close()


if __name__ == '__main__':
    run()