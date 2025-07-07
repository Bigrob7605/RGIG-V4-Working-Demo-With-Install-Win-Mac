"""
Field B — Scientific Hypothesis & Simulation
Test generator, checker, audit schema, scoring, and demo task for RGIG V4.
"""

class FieldB:
    name = "Field B — Scientific Hypothesis & Simulation"
    id = "B"

    @staticmethod
    def generate_test():
        """Generate a scientific hypothesis and simulation task."""
        return {
            "prompt": "Given a noisy dataset of atmospheric CO2 and temperature, formulate a hypothesis, create a simulation, validate, refine, and audit.",
            "demo_task": "Hypothesis: Rising CO2 causes nonlinear temperature acceleration."
        }

    @staticmethod
    def check_response(response):
        required = ["hypothesis", "simulation", "validation", "refinement", "audit"]
        return all(k in response for k in required)

    @staticmethod
    def audit_schema():
        return {
            "accuracy": "int (0-10)",
            "creativity": "int (0-10)",
            "novelty": "int (0-10)",
            "honesty": "int (0-10)",
            "green_score": "float (0-1)",
            "improvements": "list of str",
            "audit_token": "str"
        }

    @staticmethod
    def score(audit):
        a = audit.get("accuracy", 0)
        c = audit.get("creativity", 0)
        n = audit.get("novelty", 0)
        h = audit.get("honesty", 0)
        g = audit.get("green_score", 0)
        return 0.35 * a + 0.25 * c + 0.25 * n + 0.1 * h + 0.05 * g

# Demo usage
demo = FieldB.generate_test()
print("Demo Task:", demo["demo_task"]) 