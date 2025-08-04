from agents import Agent
from tool import calculate_discount , troubleshoot_wifi

billing_agent = Agent(
    name="Billing Agent",
    instructions=(
        "Handle all billing-related queries. "
        "Use the tool to calculate the discount. "
        "If the user doesn't mention a discount, apply a default 20% discount."
    ),
    tools=[calculate_discount]
)



technical_agent = Agent(
    name="Technical Agent",
    instructions=(
        "Resolve user technical issues politely. "
        "When a user describes an issue (e.g., internet not working), "
        "analyze the problem and give a possible reason and solution using the troubleshoot_wifi tool."
    ),
    tools=[troubleshoot_wifi]
)


triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "Identify the type of user query.\n"
        "- If it is a billing query, forward it to Billing Agent.\n"
        "- If it is a technical issue, forward it to Technical Agent."
    ),
    handoffs=[billing_agent, technical_agent]
)
