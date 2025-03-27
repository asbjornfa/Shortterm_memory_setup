from fastapi import APIRouter
from langchain.chains.llm import LLMChain
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


# Initializes the API router for handling endpoint registrations.
router = APIRouter()

# Initialize the desired LLM
llm = ChatOllama(model="gemma2:9b")

# Defines the structure of user input received by the API.
class UserInput(BaseModel):
    prompt: str

# Defines the structure of the bot's response sent back to the user.
class BotOutput(BaseModel):
    prompt_response: str


# Initializes an in-memory conversation buffer to store recent messages.
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

# Function to generate a response from the AI based on the user's input.
def response_func(prompt: str) -> str:
    response = conversation.predict(input=prompt)
    return response.content if hasattr(response, "content") else str(response)


# API endpoint to handle user input and return AI-generated responses.
@router.post("/Communicate", response_model=BotOutput)
async def process_endpoint(request: UserInput):
    response = response_func(request.prompt)
    return BotOutput(prompt_response=response)




