import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter

def execute_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = nbformat.read(notebook_file, as_version=4)

    # Create an ExecutePreprocessor
    execute_processor = ExecutePreprocessor(timeout=None)

    # Execute the notebook
    execute_processor.preprocess(notebook_content, {'metadata': {'path': '.'}})

    # Export the notebook to HTML (optional)
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook_content)

    # Save the executed notebook
    executed_notebook_path = notebook_path.replace('.ipynb', '_executed.ipynb')
    with open(executed_notebook_path, 'w', encoding='utf-8') as executed_notebook_file:
        nbformat.write(notebook_content, executed_notebook_file)

    print(f'Notebook executed and saved at: {executed_notebook_path}')

if __name__ == "__main__":
    # Specify the path to your Colab notebook
    notebook_path = 'fds_fares0211.ipynb'

    # Execute the notebook
    execute_notebook(notebook_path)
