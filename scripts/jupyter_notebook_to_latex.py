import os

def get_files(path, extension):
    files = []
    for i in os.listdir(path):
        if i.endswith(extension):
            files.append(i)
    return files

def delete_files(file, path):
    os.system("rm -rf " + path + "/" + file)

def convert_jupyter_notebook_to_latex(path):
    os.system("jupyter nbconvert --to latex " + path + "/*.ipynb")

def jupyter_notebook_to_latex(path_to_jupyter_notebooks, path_to_latex_files, path_to_resources):
    convert_jupyter_notebook_to_latex(path_to_jupyter_notebooks)

    resource_folders = get_files(path_to_jupyter_notebooks, "_files")

    if path_to_resources:
        for i in get_files(path_to_jupyter_notebooks, "_files"):
            os.system("cp -r " + path_to_jupyter_notebooks + "/" + i + " " + path_to_resources)
        os.system("cp -r " + path_to_jupyter_notebooks + "/resources" + " " + path_to_resources)

    try:
        os.mkdir(path_to_latex_files)
    except OSError as error:
        print(error) 

    latex_files = get_files(path_to_jupyter_notebooks, ".tex")
    for i in latex_files:
        with open(path_to_jupyter_notebooks + "/" + i, 'r') as file1, open(path_to_latex_files + "/" + i, 'w') as file2:
            flag = False
            for line in file1:
                if line.__contains__("\\begin{document}") or line.__contains__("\\end{document}"):
                    flag = not flag
                    continue
                
                if flag:
                    if line.__contains__("\maketitle"):
                        continue
                    file2.write(line)
    
    for i in resource_folders:
        delete_files(i, path_to_jupyter_notebooks)

    for i in latex_files:
        delete_files(i, path_to_jupyter_notebooks)



project_folders = ["Mathematical_Physics_II", "Quantum_Mechanics", "Statistical_Mechanics"]

for i in range(len(project_folders)):
    path_to_jupyter_notebooks = "projects/undergraduate/" + project_folders[i] +"/JupyterNotebook"
    path_to_latex_files = "projects/undergraduate/" + project_folders[i] +"/LaTeX/input/JupyterNotebook"
    path_to_main_latex_file = "projects/undergraduate/" + project_folders[i] +"/LaTeX"

    jupyter_notebook_to_latex(path_to_jupyter_notebooks, path_to_latex_files, path_to_main_latex_file)
