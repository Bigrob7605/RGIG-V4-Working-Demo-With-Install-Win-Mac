import argparse
import importlib
import os
import json
import sys
from pathlib import Path
from fields import fieldA, fieldB, fieldC, fieldD, fieldE, fieldF, fieldG

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

FIELDS = [
    ("A", "field_a"),
    ("B", "field_b"),
    ("C", "field_c"),
    ("D", "field_d"),
    ("E", "field_e"),
    ("F", "field_f"),
    ("G", "field_g"),
]

FIELDS_PATH = Path(__file__).parent.parent / "fields"
RUNS_PATH = Path(__file__).parent.parent / "runs"
RUNS_PATH.mkdir(exist_ok=True)

FIELD_MODULES = {
    'A': fieldA,
    'B': fieldB,
    'C': fieldC,
    'D': fieldD,
    'E': fieldE,
    'F': fieldF,
    'G': fieldG,
}

DEMO_RESPONSES = {
    'A': fieldA.DEMO,
    'B': fieldB.DEMO,
    'C': fieldC.DEMO,
    'D': fieldD.DEMO,
    'E': fieldE.DEMO,
    'F': fieldF.DEMO,
    'G': fieldG.DEMO,
}

def list_fields():
    print("Available RGIG Fields:")
    for fid, mod in FIELDS:
        try:
            m = importlib.import_module(f"fields.{mod}")
            field = getattr(m, f"Field{fid}")
            print(f"  {fid}: {field.name}")
        except Exception as e:
            print(f"  {fid}: [Error loading: {e}]")

def run_fields(selected):
    results = {}
    for fid in selected:
        mod = dict(FIELDS).get(fid)
        if not mod:
            print(f"Unknown field: {fid}")
            continue
        try:
            m = importlib.import_module(f"fields.{mod}")
            field = getattr(m, f"Field{fid}")
            test = field.generate_test()
            print(f"\nField {fid}: {field.name}")
            print(f"Prompt: {test['prompt']}")
            # For now, manual entry (Tab Mode)
            response = input(f"Paste response for Field {fid} (as JSON): ")
            try:
                response_obj = json.loads(response)
            except Exception:
                print("Invalid JSON. Skipping.")
                continue
            valid = field.check_response(response_obj)
            print("Valid response:" if valid else "Invalid response!")
            audit_schema = field.audit_schema()
            print("Audit schema:", audit_schema)
            audit = input(f"Paste audit for Field {fid} (as JSON): ")
            try:
                audit_obj = json.loads(audit)
            except Exception:
                print("Invalid audit JSON. Skipping.")
                continue
            score = field.score(audit_obj)
            print(f"Score: {score}")
            results[fid] = {
                "prompt": test["prompt"],
                "response": response_obj,
                "audit": audit_obj,
                "score": score
            }
        except Exception as e:
            print(f"Error running field {fid}: {e}")
    # Export results
    out_path = RUNS_PATH / "rgig_run.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

def batch_run(demo=False):
    results = {}
    for idx, (field, mod) in enumerate(FIELD_MODULES.items(), 1):
        print(f"\n--- Field {field} ({idx}/7) ---")
        if demo:
            result = DEMO_RESPONSES[field]
        else:
            prompt = mod.get_prompt()
            print(f"Prompt:\n{prompt}")
            response = input("Paste LLM response (or leave blank for demo): ")
            if not response:
                result = DEMO_RESPONSES[field]
            else:
                audit = mod.get_audit_schema()
                print(f"Audit schema: {audit}")
                audit_input = input("Paste audit JSON (or leave blank for demo): ")
                if not audit_input:
                    result = DEMO_RESPONSES[field]
                else:
                    try:
                        audit_obj = json.loads(audit_input)
                    except Exception as e:
                        print(f"Invalid JSON: {e}")
                        audit_obj = {}
                    result = {
                        'field': field,
                        'prompt': prompt,
                        'response': response,
                        'audit': audit_obj
                    }
        results[field] = result
    os.makedirs('runs', exist_ok=True)
    with open('runs/rgig_run.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print("\nBatch run complete. Results saved to runs/rgig_run.json")

def main():
    parser = argparse.ArgumentParser(description="RGIG V4 CLI — The one tool to test them all.")
    parser.add_argument("--list-fields", action="store_true", help="List all available fields (A–G)")
    parser.add_argument("--run", type=str, help="Comma-separated list of fields to run (e.g., A,B,F)")
    parser.add_argument('--batch', action='store_true', help='Run all fields A–G in batch mode')
    parser.add_argument('--demo', action='store_true', help='Auto-fill all fields with demo data')
    args = parser.parse_args()

    if args.list_fields:
        list_fields()
    elif args.batch:
        batch_run(demo=args.demo)
    elif args.run:
        selected = [x.strip().upper() for x in args.run.split(",") if x.strip()]
        run_fields(selected)
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 