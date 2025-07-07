"""
Field G — Sensory/Perceptual Acuity (Planned)
Test generator, checker, audit schema, scoring, and demo task for RGIG V4.
"""

class FieldG:
    name = "Field G — Sensory/Perceptual Acuity (Planned)"
    id = "G"

    @staticmethod
    def generate_test():
        return {
            "prompt": "Analyze a micro-text or complex visual for perceptual acuity. Report errors, range, and audit.",
            "demo_task": "Image: Micro-font text with hidden symbol."
        }

    @staticmethod
    def check_response(response):
        required = ["description", "acuity_score", "perceptual_range", "error_detection", "audit"]
        return all(k in response for k in required)

    @staticmethod
    def audit_schema():
        return {
            "acuity_score": "int (0-10)",
            "perceptual_range": "int (0-10)",
            "error_detection": "int (0-10)",
            "honesty": "int (0-10)",
            "audit_token": "str"
        }

    @staticmethod
    def score(audit):
        a = audit.get("acuity_score", 0)
        p = audit.get("perceptual_range", 0)
        e = audit.get("error_detection", 0)
        h = audit.get("honesty", 0)
        return 0.3 * a + 0.3 * p + 0.2 * e + 0.2 * h

# Demo usage
demo = FieldG.generate_test()
print("Demo Task:", demo["demo_task"]) 