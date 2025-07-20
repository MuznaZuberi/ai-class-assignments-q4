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




@function_tool
def country_capital(capital: str) -> str:
    cap = capital.lower()
    if "pakistan" in cap:
        return "The capital of Pakistan is Islamabad."
    elif "india" in cap:
        return "The capital of India is New Delhi."
    elif "china" in cap:
        return "The capital of China is Beijing."
    elif "japan" in cap:
        return "The capital of Japan is Tokyo."
    elif "france" in cap:
        return "The capital of France is Paris."
    elif "germany" in cap:
        return "The capital of Germany is Berlin."
    elif "canada" in cap:
        return "The capital of Canada is Ottawa."
    elif "australia" in cap:
        return "The capital of Australia is Canberra."
    elif "saudi arabia" in cap:
        return "The capital of Saudi Arabia is Riyadh."
    elif "united states" in cap or "usa" in cap:
        return "The capital of the United States is Washington, D.C."
    else:
        return "Capital not found for the given country."






@function_tool
def country_language(language: str) -> str:
    lang = language.lower()
    if "pakistan" in lang:
        return "The official language of Pakistan is Urdu."
    elif "india" in lang:
        return "The official language of India is Hindi."
    elif "china" in lang:
        return "The official language of China is Mandarin."
    elif "japan" in lang:
        return "The official language of Japan is Japanese."
    elif "france" in lang:
        return "The official language of France is French."
    elif "germany" in lang:
        return "The official language of Germany is German."
    elif "canada" in lang:
        return "The official languages of Canada are English and French."
    elif "australia" in lang:
        return "The official language of Australia is English."
    elif "saudi arabia" in lang:
        return "The official language of Saudi Arabia is Arabic."
    elif "united states" in lang or "usa" in lang:
        return "The de facto language of the United States is English."
    else:
        return "Language not found for the given country."








@function_tool
def country_population(population: str) -> str:
    pop = population.lower()
    if "pakistan" in pop:
        return "The population of Pakistan is approximately 240 million."
    elif "india" in pop:
        return "The population of India is over 1.4 billion."
    elif "china" in pop:
        return "The population of China is over 1.4 billion."
    elif "japan" in pop:
        return "The population of Japan is approximately 125 million."
    elif "france" in pop:
        return "The population of France is approximately 65 million."
    elif "germany" in pop:
        return "The population of Germany is approximately 83 million."
    elif "canada" in pop:
        return "The population of Canada is approximately 39 million."
    elif "australia" in pop:
        return "The population of Australia is approximately 26 million."
    elif "saudi arabia" in pop:
        return "The population of Saudi Arabia is approximately 36 million."
    elif "united states" in pop or "usa" in pop:
        return "The population of the United States is over 330 million."
    else:
        return "Population data not found for the given country."





Orchestrator = Agent(
    name = "Country Info Agent",
    instructions = "Answer questions about the capital, language, or population of any country. Use the appropriate tool based on the user's query.",
    tools = [country_capital, country_language, country_population]
)




print("🌍Welcome to the Country Info Agent!")
user_input = input("Ask about the capital, language, or population of any country:")


response = Runner.run_sync(
    Orchestrator,
    user_input,
    run_config = config
    )
print(response.final_output)
