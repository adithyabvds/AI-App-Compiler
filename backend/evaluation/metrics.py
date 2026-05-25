import sys
import os

# Allow metrics.py to access compiler.py
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import json
import time

from compiler import compile_app


# --------------------
# Load Dataset
# --------------------

with open("evaluation/dataset.json", "r") as f:
    dataset = json.load(f)


# --------------------
# Metrics Counters
# --------------------

successful = 0
ambiguity_count = 0
contradiction_count = 0
failed = 0

total_latency = 0


# --------------------
# Execute Test Suite
# --------------------

for item in dataset:

    prompt = item["prompt"]

    start = time.perf_counter()

    try:

        result = compile_app(prompt)

        latency = (
            time.perf_counter() - start
        ) * 1000

        total_latency += latency

        status = result.get("status")

        if status == "success":
            successful += 1

        elif status == "needs_clarification":
            ambiguity_count += 1

        elif status == "validation_failed":
            contradiction_count += 1

        else:
            failed += 1

    except Exception as e:

        failed += 1

        print(
            f"ERROR [{item['id']}]: "
            f"{item['prompt']} -> {e}"
        )


# --------------------
# Calculate Metrics
# --------------------

total = len(dataset)

success_rate = round(
    (successful / total) * 100,
    2
)

average_latency = round(
    total_latency / total,
    2
)


# --------------------
# Metrics Report
# --------------------

metrics = {
    "total_tests": total,
    "successful": successful,
    "success_rate": success_rate,
    "average_latency_ms": average_latency,
    "failure_types": {
        "ambiguity": ambiguity_count,
        "contradiction": contradiction_count,
        "exceptions": failed
    }
}


# --------------------
# Output
# --------------------

print("\nMETRICS REPORT")
print("=" * 50)

print(metrics)

print("\nSUMMARY")
print("=" * 50)

print(
    f"Total Tests       : {total}"
)

print(
    f"Successful        : {successful}"
)

print(
    f"Ambiguous Prompts : {ambiguity_count}"
)

print(
    f"Contradictions    : {contradiction_count}"
)

print(
    f"Exceptions        : {failed}"
)

print(
    f"Success Rate      : {success_rate}%"
)

print(
    f"Avg Latency       : {average_latency} ms"
)