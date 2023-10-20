languages_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

What languages and software do you think would be best to use to create this project? List only the results separated by commas, do not add any other information or explanation.
"""



files_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following programming languages and software:

{languages}

What files structure and directories do you think I would need to make to implement my ideas and methods into?
"""



methods_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following file structure:

{languages}

Inside of the file "{file}", what methods would need to be implemented to make the project work? List only the method names separated by commas, do not add any other inforamtion or explanation.
"""



globals_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}

It is going to use the following file structure:

{languages}

Implement what the very top of the file 
"""



coding_prompt = """I have an idea for a project that I would like to make. Here is a description of the project:

{description}
"""