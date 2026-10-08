class KnowledgeBase:
    """
    Practical 07: a propositional Knowledge Base of Facts (current percepts)
    and Rules (Horn clauses), with a data-driven Forward Chaining engine.
    """

    def __init__(self):
        self.facts = set()   # unique string facts, e.g. "TargetVisible"
        self.rules = []      # tuples: ([list_of_premises], "conclusion")

    def tell_fact(self, fact):
        self.facts.add(fact)

    def tell_rule(self, premises, conclusion):
        self.rules.append((list(premises), conclusion))

    def clear_facts(self):
        self.facts.clear()

    # ------------------------------------------------------------------
    # Step 2.1 — Forward Chaining: keep firing rules until a full pass over
    # the rule list deduces no new facts (a fixed point is reached).
    # ------------------------------------------------------------------
    def forward_chain(self):
        new_facts_added = True

        while new_facts_added:
            new_facts_added = False

            for premises, conclusion in self.rules:
                if conclusion not in self.facts:
                    # Modus Ponens: (P1 ∧ ... ∧ Pn ⇒ Q) and P1..Pn known ⊢ Q
                    if all(p in self.facts for p in premises):
                        self.facts.add(conclusion)
                        new_facts_added = True

        return self.facts
