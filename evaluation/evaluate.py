import json
import time
from services.aicorrector import ai_corrector


def evaluate():

    with open(
        "evaluation/test_cases.json",
        "r",
        encoding="utf-8"
    ) as f:

        test_cases = json.load(f)

    passed = 0
    total_time = 0

    for case in test_cases:

        start = time.time()

        prediction = ai_corrector(
            case["input"]
        ).strip()

        duration = time.time() - start

        total_time += duration

        expected = case["expected"].strip()

        if prediction == expected:
            passed += 1

        else:
            print("\nFAILED")
            print("INPUT:")
            print(case["input"])

            print("\nEXPECTED:")
            print(expected)

            print("\nPREDICTED:")
            print(prediction)

            print("-" * 50)

    total = len(test_cases)

    accuracy = (
        passed / total
    ) * 100

    average_time = (
        total_time / total
    )

    print("\n========== REPORT ==========")

    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {accuracy:.2f}%")
    print(f"Average Response Time: {average_time:.2f}s")


if __name__ == "__main__":
    evaluate()