"""
Field A — Abstract Reasoning & Mathematics
Test generator, checker, audit schema, scoring, and demo task for RGIG V4.
"""

class FieldA:
    name = "Field A — Abstract Reasoning & Mathematics"
    id = "A"

    @staticmethod
    def generate_test():
        """Generate a novel math conjecture and proof task."""
        return {
            "prompt": "Generate a non-trivial conjecture for a finite, simple cubic graph on 2n vertices. Proceed to proof, counterexample, and audit as outlined.",
            "demo_task": "Conjecture: Every connected cubic graph on 2n vertices has a perfect matching."
        }

    @staticmethod
    def check_response(response):
        """Check if the response includes conjecture, proof, counterexample, and audit."""
        required = ["conjecture", "proof", "counterexample", "compression", "audit"]
        return all(k in response for k in required)

    @staticmethod
    def audit_schema():
        """Return YAML/JSON audit schema for Field A."""
        return {
            "accuracy": "int (0-10)",
            "novelty": "int (0-10)",
            "honesty": "int (0-10)",
            "green_score": "float (0-1)",
            "improvements": "list of str",
            "audit_token": "str"
        }

    @staticmethod
    def score(audit):
        """Compute score from audit dict."""
        a = audit.get("accuracy", 0)
        n = audit.get("novelty", 0)
        h = audit.get("honesty", 0)
        g = audit.get("green_score", 0)
        return 0.4 * a + 0.3 * n + 0.2 * h + 0.1 * g

# Demo usage
demo = FieldA.generate_test()
print("Demo Task:", demo["demo_task"]) 