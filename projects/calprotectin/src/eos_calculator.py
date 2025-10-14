import math

# --- Constants derived from the R code ---

# These values are the numeric constants associated with the incidence rates.
INCIDENCE_MAP = {
    "0.1/1000": 38.952265,
    "0.2/1000": 39.646367,
    "0.3/1000": 40.0528,
    "0.4/1000": 40.3415,
    "0.5/1000": 40.5656,
    "0.6/1000": 40.7489,
    "0.7/1000": 40.903919,
    "0.8/1000": 41.0384,
    "0.9/1000": 41.1571,
    "1.0/1000": 41.263432,
    "2.0/1000": 41.965852,
    "4.0/1000": 42.676976
}

def calculate_eos_pre_risk(
    incidence_rate: float,
    gestational_weeks: int,
    gestational_days: int,
    maternal_temp: float,
    rom_hours: float,
    gbs_status: str,
    abx_type: str
):
    """
    Calculates the Pre-Examination Risk of Early-Onset Sepsis ("Risk at Birth").

    This function uses only perinatal risk factors known at the time of delivery and
    does not require the infant's clinical status.

    Args:
        incidence_rate (float or str): The local incidence of EOS. Can be a pre-defined string
            (e.g., "0.6/1000") or a custom float value from the INCIDENCE_MAP.
        gestational_weeks (int): Gestational age in completed weeks (34-43).
        gestational_days (int): Gestational age in days (0-6).
        maternal_temp (float): Highest intrapartum maternal temperature in °C or °F.
        rom_hours (float): Duration of rupture of membranes in hours (0-240).
        gbs_status (str): Maternal GBS status ("Negative", "Positive", "Unknown").
        abx_type (str): Intrapartum antibiotics ("Broad spectrum >=4 hrs",
            "Broad spectrum 2-4 hrs", "GBS specific >=2 hrs", "None or <2 hrs").

    Returns:
        float: The pre-examination risk per 1000 live births.

    Raises:
        ValueError: If any input parameters are invalid or out of range.
        TypeError: If incidence_rate has an incorrect type.
    """
    # --- 1. Input Validation and Mapping ---
    gbs_map = {"Negative": 1, "Positive": 2, "Unknown": 3}
    abx_map = {
        "Broad spectrum >=4 hrs": 1,
        "Broad spectrum 2-4 hrs": 2,
        "GBS specific >=2 hrs": 3,
        "None or <2 hrs": 0
    }

    if gbs_status not in gbs_map:
        raise ValueError(f"Invalid gbs_status. Must be one of {list(gbs_map.keys())}")
    if abx_type not in abx_map:
        raise ValueError(f"Invalid abx_type. Must be one of {list(abx_map.keys())}")
    
    gbs_code = gbs_map[gbs_status]
    abx_code = abx_map[abx_type]

    if isinstance(incidence_rate, str):
        if incidence_rate in INCIDENCE_MAP:
            incidence = INCIDENCE_MAP[incidence_rate]
        else:
            raise ValueError(f"Invalid incidence_rate string. Must be one of {list(INCIDENCE_MAP.keys())}")
    elif isinstance(incidence_rate, (int, float)):
        incidence = incidence_rate
    else:
        raise TypeError("incidence_rate must be a string key or a numeric value.")

    # Validate numeric ranges
    if not (isinstance(gestational_weeks, int) and 34 <= gestational_weeks <= 43):
        raise ValueError("Gestational age (weeks) must be an integer between 34 and 43.")
    if not (isinstance(gestational_days, int) and 0 <= gestational_days <= 6):
        raise ValueError("Gestational age (days) must be an integer between 0 and 6.")
    if not (((36 <= maternal_temp <= 40) or (96 <= maternal_temp <= 104)) and round(maternal_temp, 1) == maternal_temp):
        raise ValueError("Temperature must be between 36-40°C or 96-104°F, with at most one decimal place.")
    if not (0 <= rom_hours <= 240 and round(rom_hours, 1) == rom_hours):
        raise ValueError("Duration of rupture of membranes (hours) must be between 0-240, with at most one decimal place.")

    # --- 2. Data Preprocessing ---
    gestational_age_rounded = round(gestational_weeks + (gestational_days / 7), 2)
    
    # Convert temperature to Fahrenheit as required by the model's coefficients
    temp_fahrenheit = (maternal_temp * 9 / 5) + 32 if maternal_temp < 50 else maternal_temp
    
    # Create binary flags from categorical codes
    gbs_pos = 1 if gbs_code == 2 else 0
    gbs_unk = 1 if gbs_code == 3 else 0
    intra_abxbr = 1 if abx_code == 1 else 0  # Broad spectrum >=4 hrs
    intra_abxsp = 1 if abx_code > 1 else 0   # Other qualifying antibiotics

    # --- 3. Core Calculation ---
    # Calculate the logit (βx), the linear combination of predictors
    logit = (
        incidence +
        gestational_age_rounded * -6.9325 +
        gestational_age_rounded**2 * 0.0877 +
        temp_fahrenheit * 0.8680 +
        (rom_hours + 0.05)**0.2 * 1.2256 +
        gbs_pos * 0.5771 +
        gbs_unk * 0.0427 +
        intra_abxbr * -1.1861 +
        intra_abxsp * -1.0488
    )
    
    # Calculate pre-examination probability using the logistic function
    pre_prob = 1 / (1 + math.exp(-logit))
    
    # Convert probability to risk per 1000 live births and round
    pre_risk = round(pre_prob * 1000, 2)
    
    return pre_risk

# --- Example Usage ---
if __name__ == "__main__":
    
    # Example 1: A higher-risk scenario
    print("--- Example 1: Higher-risk Infant ---")
    try:
        risk_at_birth = calculate_eos_pre_risk(
            incidence_rate="1.0/1000",
            gestational_weeks=37,
            gestational_days=0,
            maternal_temp=101.5,         # °F
            rom_hours=24,
            gbs_status="Positive",
            abx_type="None or <2 hrs"
        )
        print(f"Calculated pre-examination risk: {risk_at_birth} per 1000 live births.\n")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")

    # Example 2: A lower-risk scenario with antibiotics given
    print("--- Example 2: Lower-risk Infant with IAP ---")
    try:
        risk_at_birth = calculate_eos_pre_risk(
            incidence_rate="0.6/1000",
            gestational_weeks=39,
            gestational_days=3,
            maternal_temp=37.5,         # °C
            rom_hours=12,
            gbs_status="Positive",
            abx_type="GBS specific >=2 hrs"
        )
        print(f"Calculated pre-examination risk: {risk_at_birth} per 1000 live births.\n")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")
        
    # Example 3: Demonstrating an input validation error
    print("--- Example 3: Invalid Input ---")
    try:
        calculate_eos_pre_risk(
            incidence_rate="0.6/1000",
            gestational_weeks=45,  # Invalid, must be <= 43
            gestational_days=0,
            maternal_temp=37.0,
            rom_hours=10,
            gbs_status="Negative",
            abx_type="None or <2 hrs"
        )
    except (ValueError, TypeError) as e:
        print(f"Caught expected error: {e}\n")