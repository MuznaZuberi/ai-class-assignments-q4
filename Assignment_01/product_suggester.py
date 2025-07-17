import os 
from dotenv import load_dotenv
from agents import Agent , Runner , AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig , function_tool


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")



# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

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
def medicine_suggestion(symptoms: str) -> str:
    symptoms = symptoms.lower()

    if "headache" in symptoms:
        return "You can take Panadol or Ibuprofen for headache relief."
    elif "fever" in symptoms:
        return "Take Paracetamol (e.g., Panadol) and stay hydrated."
    elif "cold" in symptoms:
        return "Try Panadol Cold & Flu and steam inhalation."
    elif "cough" in symptoms:
        return "Use Benylin or Delsym for cough relief."
    elif "sore throat" in symptoms:
        return "Use Strepsils, warm water, or Betadine gargle."
    elif "body pain" in symptoms or "muscle pain" in symptoms:
        return "Try Ibuprofen or Voltaren gel."
    elif "stomach pain" in symptoms:
        return "Use Buscopan or Gaviscon."
    elif "vomiting" in symptoms:
        return "Take Gravinate or Domperidone."
    elif "nausea" in symptoms:
        return "Use Motilium or Emetrol."
    elif "diarrhea" in symptoms:
        return "Take ORS and Loperamide (Imodium)."
    elif "constipation" in symptoms:
        return "Use Duphalac syrup or Isabgol (Psyllium husk)."
    elif "gas" in symptoms or "bloating" in symptoms:
        return "Take Simethicone or Gas-X."
    elif "acidity" in symptoms or "heartburn" in symptoms:
        return "Use Gaviscon or Omeprazole."
    elif "allergy" in symptoms or "sneezing" in symptoms:
        return "Take Cetirizine or Loratadine."
    elif "itching" in symptoms:
        return "Use Cetrizine tablets or Calamine lotion."
    elif "rashes" in symptoms:
        return "Apply Hydrocortisone or Calamine lotion."
    elif "dry skin" in symptoms:
        return "Apply Vaseline or Cetaphil moisturizing lotion."
    elif "burn" in symptoms:
        return "Use Burnol or Silverex cream."
    elif "wound" in symptoms:
        return "Clean with antiseptic and apply Neosporin."
    elif "toothache" in symptoms:
        return "Use painkillers like Ibuprofen and see a dentist."
    elif "eye redness" in symptoms:
        return "Use artificial tears or antihistamine eye drops."
    elif "sleeplessness" in symptoms or "insomnia" in symptoms:
        return "Try taking melatonin supplements or herbal teas."
    else:
        return "Sorry, no matching symptom found. Please consult a doctor for accurate treatment."



store_agent = Agent(
    name="Pharmacy Agent",
    instructions="Assist users by suggesting suitable medicines for their symptoms.",
    tools = [medicine_suggestion]
)



print("🤖 Welcome to CureCompass Pharmacy!")
print("💊 This agent suggests basic medicines for common symptoms like fever, cough, headache, etc.")
print("📋 Please describe your symptom in simple words (e.g., 'I have a headache').")
print("-------------------------------------------------------------")

prompt = input("Enter your symptom: ").strip()




res = Runner.run_sync(
    store_agent,
    prompt,
    run_config = config
)

print(res.final_output)