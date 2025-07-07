"""
Field C — Engineering & Tool Orchestration
Test generator, checker, audit schema, scoring, and demo task for RGIG V4.
"""

class FieldC:
    name = "Field C — Engineering & Tool Orchestration"
    id = "C"

    @staticmethod
    def generate_test():
        return {
            "prompt": "Design a system for real-time image recognition with minimal resources. Implement, optimize, analyze failures, and audit.",
            "demo_task": "System: Lightweight CNN for mobile image recognition."
        }

    @staticmethod
    def check_response(response):
        required = ["system_design", "implementation", "optimization", "failure_analysis", "audit"]
        return all(k in response for k in required)

    @staticmethod
    def audit_schema():
        return {
            "accuracy": "int (0-10)",
            "efficiency": "int (0-10)",
            "novelty": "int (0-10)",
            "honesty": "int (0-10)",
            "green_score": "float (0-1)",
            "improvements": "list of str",
            "audit_token": "str"
        }

    @staticmethod
    def score(audit):
        a = audit.get("accuracy", 0)
        e = audit.get("efficiency", 0)
        n = audit.get("novelty", 0)
        h = audit.get("honesty", 0)
        g = audit.get("green_score", 0)
        return 0.35 * a + 0.25 * e + 0.25 * n + 0.1 * h + 0.05 * g

# Demo usage
demo = FieldC.generate_test()
print("Demo Task:", demo["demo_task"]) 