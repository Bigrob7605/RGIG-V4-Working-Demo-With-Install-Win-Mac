"""
Field F — Recursive Visual Test (Visual-Recursive Stability)
Test generator, checker, audit schema, scoring, and demo task for RGIG V4.
"""

class FieldF:
    name = "Field F — Recursive Visual Test (Visual-Recursive Stability)"
    id = "F"

    @staticmethod
    def generate_test():
        return {
            "prompt": "Analyze a recursive/ambiguous image or pattern. Describe recursion depth, flag abstraction drift, emit YAML audit.",
            "demo_task": "Image: Fractal with hidden recursion collapse."
        }

    @staticmethod
    def check_response(response):
        required = ["description", "recursion_depth", "drift_flag", "audit"]
        return all(k in response for k in required)

    @staticmethod
    def audit_schema():
        return {
            "semantic_depth": "int (0-10)",
            "recursion_detection": "int (0-10)",
            "stability": "int (0-10)",
            "honesty": "int (0-10)",
            "audit_token": "str"
        }

    @staticmethod
    def score(audit):
        s = audit.get("semantic_depth", 0)
        r = audit.get("recursion_detection", 0)
        t = audit.get("stability", 0)
        h = audit.get("honesty", 0)
        return 0.3 * s + 0.3 * r + 0.2 * t + 0.2 * h

# Demo usage
demo = FieldF.generate_test()
print("Demo Task:", demo["demo_task"]) 