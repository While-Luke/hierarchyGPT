languages_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

What programming languages and software do you think would be best to use to implement this project? If there is more than one language that is necessary, list only the results separated by commas, do not add any other information or explanation.
"""



files_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following programming languages and software:

{languages}

What files do you think I would need to make to implement my ideas and methods into? Provide a short explanation as to what each file should achieve. List the results in the following form:

file_name: Explanation
file_name: Explanation
and so on...

Do not add any other information or explanation.
"""



methods_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following languages and software:

{languages}

What methods would need to be implemented to make the project work? Provide a short explanation as to what each method should achieve. List the results in the following form:

method_name: Explanation
method_name: Explanation
and so on...

Don't forget to add a 'main' method to run the whole program. Do not add any other information or explanation.
"""

methods_prompt_extra = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following languages and software:

{languages}

I need to implement the file "{file}" which should achieve the following:

{filedesc}

What methods would need to be implemented inside of this file to make the project work? Provide a short explanation as to what each method should achieve. List the results in the following form:

method_name: Explanation
method_name: Explanation
and so on...

Don't forget to add a 'main' method to run the whole program. Do not add any other information or explanation.
"""



globals_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following languages and software:

{languages}

The program will contain the following methods:

{methods}

Implement what the very top of this file should look like, including the import statements, constants and any global variables if necessary. Do not implement any methods or any other code, and do not add any other information or explanation.
"""

globals_prompt_extra = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following languages and software:

{languages}

I need to implement the file "{file}" which should achieve the following:

{filedesc}

Inside of the {file}, it is going to contain the following methods:

{methods}

Implement what the very top of this file should look like, including the import statements, constants and any global variables if necessary. Do not implement any methods or any other code, and do not add any other information or explanation.
"""



coding_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following languages and software:

{languages}

The program will contain the following methods:

{methods}

This file will also contain the following imports and globals:

{globals}

Implement the method {method}. Here is a description of what this method should do:

{explanation}

Do not give any extra information and explanation about this method, just the code for this one method.
"""

coding_prompt_extra = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following languages and software:

{languages}

Inside of the file "{file}", it is going to contain the following methods:

{methods}

This file will also contain the following imports and globals:

{globals}

Implement the method {method}. Here is a description of what this method should do:

{explanation}

Do not give any extra information and explanation about this method, just the code for this one method.
"""