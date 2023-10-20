from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import prompts

load_dotenv()

# Find languages
def get_languages(llm, project_idea, verbose = False):
    if input("Do you know what languages you want to use [Y/N]?").upper() == "Y":
        languages = input("Which languages would you like to use? ")
    else:
        prompt = prompts.languages_prompt
        prompt_template = PromptTemplate.from_template(prompt)
        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt_template
        )
        languages = llm_chain(project_idea)["text"]
        if verbose:
            print(languages)
    languages = languages.replace(" ", "").split(",")
    return languages


# Find files and directories
def get_files(verbose = False):
    pass

# Find methods inside files
def get_methods(verbose = False):
    pass

# Complete methods
def fill_method(verbose = False):
    pass

def main(verbose = False):
    llm = ChatOpenAI()

    #project_idea = input("What project would you like to make? ")
    project_idea = "A simple tik-tak-toe game that a user can play with a command line interface."

    languages = get_languages(llm, project_idea, verbose)



if __name__ == "__main__":
    main(True)