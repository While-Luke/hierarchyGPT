from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import prompts

load_dotenv()

def get_code_from_string(s):
    if '```python\n' in s:
        s = s.split('```python\n')[1].split('```')[0]
    elif 'def' in s:
        s = s[s.find('def'):]
    return s

# Find languages
def get_languages(llm, info, verbose = False):
    if input("Do you know what languages you want to use [Y/N]?").upper() == "Y":
        languages = input("Which languages would you like to use? ")
    else:
        prompt = prompts.languages_prompt
        prompt_template = PromptTemplate.from_template(prompt)
        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt_template
        )
        if verbose > 1:
            print("Languages prompt: ")
            print(prompt.format(**info))

        languages = llm_chain(info)["text"]
        if verbose:
            print(languages)

    languages = languages.replace(" ", "").split(",")
    return languages


# Find files and directories
def get_files(llm, info, verbose = False):
    if input("Will this project be contained in one single file? [Y/N]").upper() == "Y":
        file = input("What will the file be called? ")
        return [file], True
    prompt = prompts.files_prompt
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    if verbose > 1:
        print("Files prompt: ")
        print(prompt.format(**info))

    response = llm_chain(info)["text"]

    files = {}
    for resp in response.split("\n"):
        if resp == '': #Somethimes uses double newlines
            continue
        resp = resp.split(":")
        file_name = resp[0].replace(" ", "")
        file_description = resp[1]
        files[file_name] = file_description
    if verbose:
        print(files)
    return files, False

# Find methods inside files
def get_methods(llm, info, singlefile, verbose = False):
    if singlefile:
        prompt = prompts.methods_prompt
    else:
        prompt = prompts.methods_prompt_extra
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    if verbose > 1:
        print("Methods prompt: ")
        print(prompt.format(**info))

    response = llm_chain(info)["text"]
    methods = {}
    for resp in response.split("\n"):
        if resp == '': #Somethimes uses double newlines
            continue
        resp = resp.split(":")
        method_name = resp[0].replace(" ", "")
        method_description = resp[1]
        methods[method_name] = method_description
    if verbose:
        print(methods)
    return methods

# Find imports and globals within file
def get_globals(llm, info, singlefile, verbose = False):
    if singlefile:
        prompt = prompts.globals_prompt
    else:
        prompt = prompts.globals_prompt_extra
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    if verbose > 1:
        print("Globals prompt: ")
        print(prompt.format(**info))

    globals = llm_chain(info)["text"]
    if verbose:
        print(globals)
    globals = get_code_from_string(globals)
    with open(info['file'], "a") as f:
        f.write(globals)
        f.write("\n")
    return globals

# Implement methods
def fill_method(llm, info, singlefile, verbose = False):
    if singlefile:
        prompt = prompts.coding_prompt
    else:
        prompt = prompts.coding_prompt_extra
    prompt_template = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )
    if verbose > 1:
        print("Coding prompt: ")
        print(prompt.format(**info))

    code = llm_chain(info)["text"]
    if verbose:
        print(code)
    
    code = get_code_from_string(code)

    with open(info['file'], "a") as f:
        f.write(code)
        f.write("\n")




def main(verbose = False):
    llm = ChatOpenAI()
    info = {}

    project_idea = input("What project would you like to make? ")
    #project_idea = "A simple tik-tak-toe game that a user can play with a command line interface."
    info["description"] = project_idea

    languages = get_languages(llm, info, verbose)
    info["languages"] = languages

    files, singlefile = get_files(llm, info, verbose)

    if singlefile:
        info["file"] = files[0]

        methods = get_methods(llm, info, singlefile, verbose)
        info["methods"] = methods

        globals = get_globals(llm, info, singlefile, verbose)
        info["globals"] = globals

        for method, explanation in methods.items():
            info["method"] = method
            info["explanation"] = explanation
            fill_method(llm, info, singlefile, verbose)

    else:
        for file, filedesc in files.items():
            info["file"] = file
            info["filedesc"] = filedesc

            methods = get_methods(llm, info, singlefile, verbose)
            info["methods"] = methods

            globals = get_globals(llm, info, singlefile, verbose)
            info["globals"] = globals

            for method, explanation in methods.items():
                info["method"] = method
                info["explanation"] = explanation
                fill_method(llm, info, singlefile, verbose)




if __name__ == "__main__":
    main(True)