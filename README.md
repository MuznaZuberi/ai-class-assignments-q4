🤖 AI Agent Projects – Q3 Assignment (Monday 2–5)
-------------
This submission contains three interactive AI agents built using the OpenAI Agents SDK, leveraging tools like @function_tool and handoffs for modular and intelligent responses.


## 📦 Contents

### 1. 🛒 Smart Store Agent (smart_store_agent.py)
##### A virtual assistant designed for an e-commerce store to help users with:
##### Viewing available categories and products
##### Suggesting recommendations
##### Providing prices or availability

### Tech Stack:

##### @function_tool for store functions

##### Orchestrator agent with built-in prompt flow

##### Handles user queries dynamically



## 2. 😊 Mood Detector Agent (mood_response_agent.py)
##### An intelligent agent that detects user mood from input and responds empathetically.

##### Moods: happy, sad, angry, neutral

##### Provides contextual replies and emotional support

##### Uses handoff logic to map moods to the right response tool

### Tools Used:

##### @function_tool for mood-based responses

##### Agent with handoffs for mood routing



## 3. 🌍 Country Info Agent (country_info_toolkit.py)

Provides details about countries using multiple tools:

##### Capital city

##### Official language

##### Current population (with live web search)

### Built With:

##### @function_tool for capital, language, population

##### Central Orchestrator agent with handoffs

##### CLI input for user queries like “Pakistan” or “China population”



## 💡 Technologies Used
##### ✅ OpenAI Agents SDK
##### 🔄 Handoff System
##### 🛠 Function Tools (@function_tool)


> Developed with curiosity and code ✨ by Muzna Amir
