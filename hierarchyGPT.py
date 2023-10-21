from dotenv import load_dotenv
import re
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import prompts

load_dotenv()

def get_code_from_string(s):
    if '```python\n' in s:
        s = s.split('```python\n')[1].split('```')[0]
    return s

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
def get_files(llm, project_idea, languages, verbose = False):
    if input("Will this project be contained in one single file? [Y/N]").upper() == "Y":
        file = input("What will the file be called? ")
        return [file]
    prompt = prompts.files_prompt
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    files = llm_chain({'description': project_idea, 'languages': languages, 'file': file})["text"]
    files = files.replace(" ", "").split(",")
    if verbose:
        print(files)
    return files

# Find methods inside files
def get_methods(llm, project_idea, languages, file, verbose = False):
    prompt = prompts.methods_prompt
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    response = llm_chain({'description': project_idea, 'languages': languages, 'file': file})["text"]
    methods = {}
    for resp in response.split("\n"):
        resp = resp.split(":")
        method_name = resp[0].replace(" ", "")
        method_description = resp[1]
        methods[method_name] = method_description
    if verbose:
        print(methods)
    return methods

# Find imports and globals within file
def get_globals(llm, project_idea, languages, file, methods, verbose = False):
    prompt = prompts.globals_prompt
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    globals = llm_chain({'description': project_idea, 'languages': languages, 'file': file, 'methods': methods})["text"]
    if verbose:
        print(globals)
    globals = get_code_from_string(globals)
    with open(file, "a") as f:
        f.write(globals)
    return globals

# Implement methods
def fill_method(llm, project_idea, languages, file, methods, globals, method, explanation, verbose = False):
    prompt = prompts.coding_prompt
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    code = llm_chain({'description': project_idea, 'languages': languages, 'file': file, 'methods': methods, 'globals': globals, 'method': method, 'explanation': explanation})["text"]
    if verbose:
        print(code)
    
    code = get_code_from_string(code)
    with open(file, "a") as f:
        f.write(code)
        f.write("\n")




def main(verbose = False):
    llm = ChatOpenAI()

    #project_idea = input("What project would you like to make? ")
    project_idea = "A simple tik-tak-toe game that a user can play with a command line interface."

    #languages = get_languages(llm, project_idea, verbose)
    languages = ["Python"]

    #files = get_files(llm, project_idea, verbose)
    files = ["tiktaktoe.py"]

    methods = get_methods(llm, project_idea, languages, files[0], verbose)
    #methods = ['start_game', 'print_board', 'make_move', 'check_win', 'switch_player', 'is_board_full', 'is_valid_move']

    globals = get_globals(llm, project_idea, languages, files[0], methods, verbose)
    '''globals = """import random

# Global Variables
board = [' ' for _ in range(9)]
players = ['X', 'O']
current_player = random.choice(players)"""'''

    for method, explanation in methods.items():
        fill_method(llm, project_idea, languages, files[0], methods, globals, method, explanation, verbose)




if __name__ == "__main__":
    main(True)