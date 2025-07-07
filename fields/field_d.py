"""
Field D — Multimodal Creative Synthesis
Test generator, checker, audit schema, scoring, and demo task for RGIG V4.
"""

class FieldD:
    name = "Field D — Multimodal Creative Synthesis"
    id = "D"

    @staticmethod
    def generate_test():
        return {
            "prompt": "Create a multimodal artifact (story, code, music, image) from a theme seed. Audit for quality, coherence, originality, critique, honesty.",
            "demo_task": "Theme: A lost message echoing through time."
        }

    @staticmethod
    def check_response(response):
        required = ["premise", "storyboard", "motif", "code", "audit"]
        return all(k in response for k in required)

    @staticmethod
    def audit_schema():
        return {
            "aesthetic_quality": "int (0-10)",
            "coherence": "int (0-10)",
            "originality": "int (0-10)",
            "critique_depth": "int (0-10)",
            "honesty": "int (0-10)",
            "improvements": "list of str",
            "audit_token": "str"
        }

    @staticmethod
    def score(audit):
        q = audit.get("aesthetic_quality", 0)
        m = audit.get("coherence", 0)
        o = audit.get("originality", 0)
        c = audit.get("critique_depth", 0)
        h = audit.get("honesty", 0)
        return 0.3 * q + 0.25 * m + 0.2 * o + 0.15 * c + 0.1 * h

# Demo usage
demo = FieldD.generate_test()
print("Demo Task:", demo["demo_task"]) 