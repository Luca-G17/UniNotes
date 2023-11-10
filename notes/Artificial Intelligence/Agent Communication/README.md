# Agent Communication
**Speech Acts**

- Declared in declarative form

	- Performative verbs

Informative - “Shipment will arrive on Wednesday”

Directive - “Send me the goods”

Commissive - “I will pay you £5”

<br/>

**Software Engineering Approaches:**

- Sequence Diagrams

- State Transition Diagrams

Evaluation w.r.t multiagent systems:

- Low level abstractions

- Difficult to design and maintain

- Less flexibility at runtime

- Easy compliance checking at the cost of flexibility

<br/>

**Artificial Intelligence Approaches:**

- Knowledge Query and Manipulation Language (KQML)

	- Agents maintain a knowledge base in terms of belief in assertions

	- Assumption: Agents are cooperative

- FIPA - Agent communication language

	- Specify a define syntax for interoperability

	- Specify the semantics of primitives

Evaluation w.r.t multiagent systems:

- High level of abstraction

- Curtailed flexibility

- Verifying agent compliance is impossible

<br/>

**Commitment Life Cycle:**

$$ \text{Detached: } \\C(\text{BookCo}, \text{ Alice}, \text{ £25}, \text{ Book}) \land \text{£25}\implies C(\text{BookCo}, \text{ Alice}, \top, \text{ Book}) \\ {} \\ \text{Satisfy: }\\ \text{Book} \implies \lnot C(\text{BookCo}, \text{ Alice}, \text{ £25}, \text{ Book}) \land \lnot C(\text{BookCo}, \text{ Alice}, \text{ £25}, \text{ Book}) $$

**Commitment Operations:**

- CREATE(SBJ, OBJ, ant, con): Performed by SBJ; causes C(SBJ, OBJ, ant, con) to hold

- CANCEL(SBJ, OBJ, ant, con): Performed by SBJ; causes C(SBJ, OBJ, ant, con) to not hold

- RELEASE(SBJ, OBJ, ant, con): Performed by OBJ; causes C(SBJ, OBJ, ant, con) to not hold

- DELEGATE(SBJ1, OBJ, SBJ2, ant, con): Performed by SBJ1; causes C(SBJ2. OBJ, ant, con) to hold

- ASSIGN(SBJ, OBJ1, OBJ2, ant, con): Performed by OBJ1; causes C(SBJ, OBJ2, ant, con) to hold

<br/>

