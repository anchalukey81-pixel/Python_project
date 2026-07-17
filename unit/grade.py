def calculate_grade(percentage: float) -> str:
    """
    Percentage score ke basis par absolute student grade return karta hai.
    Input: float ya int (e.g., 85.5)
    Output: str (e.g., 'A')
    """
    # Safety Check: Agar input number galat ya invalid hai
    if percentage is None or percentage < 0:
        return "N/A"
        
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "Fail (F)"
