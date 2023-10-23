# Coevolution
Organisms in the real world compete with each other and cooperate with other organisms in their environment. Coevolution is the kind of evolution that happens when multiple species interact. 

Coevolution = An automatic fitness function, each organism has to do well in the presence of other species. 

Coevolution = An implicit fitness function its also dynamic.

**Cooperative Coevolution:**

- Each population deals with a separate part of the overall problem

- A solution combines individuals from each population

- Appropriate when the overall problem is highly structured

**Competitive Coevolution:**

- One population of solutions to the problem that we are interested in coevolves against a population of challengers.

- Solutions are fit if they defeat many challengers

- Challengers are fit if they defeat many solutions

	- Reminiscent of natural host-parasite or predator-prey coevolution

<br/>

**Problems with Coevolution:**

- Stagnation - Populations reach a poised state in which there is a turnover of individuals but no phenotypic progress.

- Cycling - Populations repeatedly cycle through the same weak strategies.

- Disengagement - Every host is beaten by every parasite, all selection pressure is extinguished, and coevolution ceases. If being on one side of the problem is significantly easier than the other side then the weaker size can never evolve.

- Measuring Progress - Without a fitness function it can be difficult to assess whether genuine progress is being made by coevolving populations.

These problems arise from a loss of diversity.

<br/>

**Encouraging Diversity:**

- Population Structure - Competition happens in subpopulations, therefore every organism is not interacting with every other organism. 

	- GA’s can do the same by splitting populations into quasi-isolated sub populations called ‘demes’.

	- We can also spread a population over a large space and only allow local interactions

- Fitness Sharing - A more deliberate way of maintaining diversity is to punish solutions that are too similar to other solutions in the population. We assign a lower fitness to individuals with lots of similar neighbours

- Reduced Virulence - We can change our parasite’s fitness function rewarding defeating most hosts over defeating all hosts 

