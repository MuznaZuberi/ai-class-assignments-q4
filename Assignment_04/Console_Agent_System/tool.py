from agents import Agent , function_tool

@function_tool
def calculate_discount(amount: float, percent: float) -> str:
    discount = amount * percent / 100
    final_amount = amount - discount
    return f"With a {percent}% discount on your ₹{amount} bill, you need to pay ₹{final_amount}."





@function_tool
def troubleshoot_wifi(issue: str) -> str:
    return f"To fix '{issue}', try restarting your router and checking your network settings."
