from agents import Agent, Runner
from configuration import config
from handoffs_agent import triage_agent


prompt = input("User input: ")

res = Runner.run_sync(
    triage_agent,
    prompt,
    run_config=config
)

print(res.final_output)
