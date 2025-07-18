import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel , function_tool
from agents.run import RunConfig


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


mood_response_agent = Agent(
    name = "Mood Detector Agent",
    instructions = """
    You are a Mood Response Agent. Respond based on the user's mood from handoff.

    Moods:
    - Happy: Celebrate with the user.
    - Sad: Offer comfort and emotional support.
    - Angry: Stay calm and help the user de-stress.
    - Excited: Share the excitement with enthusiasm.
    - Confused: Offer clear guidance.
    - Nervous: Reassure and calm them.
    - Lonely: Provide warmth and connection.
    - Loved: Acknowledge their joy.
    - Bored: Suggest fun or creative ideas.
    - Grateful: Acknowledge and celebrate with them.
    - Tired: Encourage and uplift. Give them strength and motivation to keep going.
    - Motivated: Boost their energy even further.
    - Anxious: Help them feel safe and grounded.
    - Hopeful: Reinforce their optimism.
    - Frustrated: Help them find a solution calmly.
    - Shocked: Respond gently and supportively.
    - Proud: Celebrate their achievement.
    - Embarrassed: Reassure with empathy.

    Always match your tone to the mood. Don't ask the user their mood—it's already provided via handoff.
    """
)


mood_activity_suggestion_agent = Agent(
    name = "Mood Observed Agent",
    instructions = "Reply supportively based on the user's given mood—no need to ask it."
)



mood_routing_agent = Agent(
    name = "Mood Trigger Agent",
    instructions = "This agent routes user mood inputs to appropriate agents for reaction and activity.",
    handoffs = [mood_response_agent , mood_activity_suggestion_agent]
)


prompt = "I'm so confused about my next step in career."

response = Runner.run_sync(
    mood_routing_agent,
    prompt,
    run_config = config
)

print(response.final_output)