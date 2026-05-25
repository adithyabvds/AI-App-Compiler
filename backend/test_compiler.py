from compiler import compile_app

prompts = [
    # Normal Prompts
    "Build a CRM with login and dashboard",
    "Build a hospital management system",
    "Build an ecommerce app with payments",
    "Build a food delivery application",

    # Ambiguous Prompts
    "Build something",
    "Build something for doctors",

    # Contradictory Prompts
    "Create payment system without customers",
    "Build CRM without users",
    "Create orders system without products",
    "Build hospital system without patients"
]

for prompt in prompts:

    result = compile_app(prompt)

    print("\n" + "=" * 70)
    print(f"PROMPT: {prompt}")

    # --------------------
    # Ambiguity Handling
    # --------------------

    if result.get("status") == "needs_clarification":

        print("\nNEEDS CLARIFICATION")
        print(result["intent"])

        print("\n" + "=" * 70)
        continue

    # --------------------
    # Contradiction Handling
    # --------------------

    if result.get("status") == "validation_failed":

        print("\nVALIDATION FAILED")
        print(result["validation_errors"])

        print("\n" + "=" * 70)
        continue

    # --------------------
    # Successful Generation
    # --------------------

    print("\nINTENT")
    print(result["intent"])

    print("\nARCHITECTURE")
    print(result["architecture"])

    print("\nUI")
    print(result["ui"])

    print("\nAPI")
    print(result["api"])

    print("\nDATABASE")
    print(result["database"])

    print("\nAUTH")
    print(result["auth"])

    print("\nVALIDATION")
    print(result["validation"])

    print("\nSIMULATION")
    print(result["simulation"])

    print("\nSTATUS")
    print(result["status"])

    print("\n" + "=" * 70)