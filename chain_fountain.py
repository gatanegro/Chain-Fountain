import math

def calculate_chain_fountain_ratio():
    # LOGOS exact LZ-HQS constants
    lz_values = [
        0.8934663922421224,  # lz0
        1.1884835867122727,  # lz1  
        1.2324872492906604,  # lz2
        1.2348836948610768,  # lz3
        1.2349784610451732,  # lz4
        1.2349821314710578,  # lz5
        1.2349822735137316,  # lz6
        1.2349822790104976,  # lz7
        1.2349822792232112,  # lz8
        1.2349822792314428,  # lz9
        1.2349822792317612,  # lz10
        1.2349822792317737,  # lz11
        1.2349822792317741   # LZ∞
    ]
    
    hqs_values = [
        0.4580303486913581,  # hqs0
        0.2563627656259622,  # hqs1
        0.2365675399187783,  # hqs2  
        0.2355433075380717,  # hqs3
        0.2355029143309773,  # hqs4
        0.2355013500132297,  # hqs5
        0.2355012894755802,  # hqs6
        0.2355012871328953,  # hqs7
        0.2355012870422381,  # hqs8
        0.2355012870387299,  # hqs9
        0.2355012870385942,  # hqs10
        0.2355012870385889,  # hqs11
        0.2355012870385887   # HQS∞
    ]
    
    total_transfer = 0.0
    
    # Calculate cascade transfer for each level transition
    for n in range(1, len(lz_values)):
        lz_prev = lz_values[n-1]
        lz_current = lz_values[n]
        hqs_prev = hqs_values[n-1]  # ← USE PREVIOUS HQS!
        
        # Resonance transfer formula
        transfer = (hqs_prev / lz_prev) * (1 - math.exp(-(lz_current - lz_prev)))
        total_transfer += transfer
        
        print(f"Level {n-1}→{n}: HQS_{n-1}/LZ_{n-1} = {hqs_prev/lz_prev:.6f}, ΔLZ = {lz_current - lz_prev:.6f}, Transfer = {transfer:.6f}")
    
    return total_transfer

# Run the calculation
result = calculate_chain_fountain_ratio()
print(f"\nFinal h₂/h₁ ratio = {result:.5f}")
print(f"Experimental value = 0.14000")
print(f"Difference = {abs(result - 0.14):.5f}")
