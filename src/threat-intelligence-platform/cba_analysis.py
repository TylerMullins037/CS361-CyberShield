def calculate_cba(ale_prior, ale_post, acs):
    """
    Calculate the Cost-Benefit Analysis for risk mitigation.
    """
    return ale_prior - ale_post - acs


def main():
    # Example inputs
    ale_prior = 500000
    ale_post = 100000
    acs = 50000

    # Calculate CBA
    cba = calculate_cba(ale_prior, ale_post, acs)

    # Display formatted result
    print("=== CBA Report ===")
    print(f"ALE Before: ${ale_prior}")
    print(f"ALE After : ${ale_post}")
    print(f"ACS       : ${acs}")
    print(f"CBA Result: ${cba}")

    if cba > 0:
        print("✅ Risk mitigation is cost-effective.")
    else:
        print("❌ Risk mitigation is not cost-effective.")


if name == "main":
    main()
