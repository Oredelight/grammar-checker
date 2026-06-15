import json
import time
from collections import defaultdict

from rapidfuzz import fuzz

from services.grammarchecker import check_grammar


PASS_THRESHOLD = 85


def evaluate():

    with open(
        "evaluation/test_cases.json",
        "r",
        encoding="utf-8"
    ) as f:
        test_cases = json.load(f)

    total = len(test_cases)

    passed = 0
    total_time = 0

    category_stats = defaultdict(
        lambda: {
            "passed": 0,
            "total": 0
        }
    )

    failed_cases = []

    for case in test_cases:

        category = case["category"]

        category_stats[category]["total"] += 1

        start = time.time()

        result = check_grammar(
            case["input"]
        )

        prediction = result["corrected"].strip()

        duration = time.time() - start

        total_time += duration

        expected = case["expected"].strip()

        score = fuzz.token_sort_ratio(
            prediction.lower(),
            expected.lower()
        )

        if score >= PASS_THRESHOLD:

            passed += 1

            category_stats[category]["passed"] += 1

        else:

            failed_cases.append({
                "category": category,
                "input": case["input"],
                "expected": expected,
                "predicted": prediction,
                "score": score
            })

    accuracy = (passed / total) * 100

    average_time = total_time / total

    print("\n" + "=" * 50)
    print("DREAMY CHECKER EVALUATION REPORT")
    print("=" * 50)

    print(f"\nTotal Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {accuracy:.2f}%")
    print(f"Average Response Time: {average_time:.2f}s")

    print("\n" + "=" * 50)
    print("CATEGORY REPORT")
    print("=" * 50)

    for category, stats in sorted(category_stats.items()):

        category_accuracy = (
            stats["passed"] /
            stats["total"]
        ) * 100

        print(
            f"{category:<25} "
            f"{stats['passed']}/{stats['total']} "
            f"({category_accuracy:.2f}%)"
        )

    if failed_cases:

        print("\n" + "=" * 50)
        print("FAILED CASES")
        print("=" * 50)

        for case in failed_cases:

            print(f"\nCATEGORY: {case['category']}")

            print("\nINPUT:")
            print(case["input"])

            print("\nEXPECTED:")
            print(case["expected"])

            print("\nPREDICTED:")
            print(case["predicted"])

            print(
                f"\nSIMILARITY: "
                f"{case['score']:.2f}%"
            )

            print("-" * 50)

    print("\nEvaluation Complete.")


if __name__ == "__main__":
    evaluate()