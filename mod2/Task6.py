from flask import Flask
import os

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)

    try:
        with open(abs_path, 'r', encoding='utf-8') as file:
            content = file.read(size)
            result_size = len(content)
            return (f"<b>{abs_path}</b> {result_size}<br>\n"
                    f"{content}")
    except FileNotFoundError:
        return "File not found", 404
    except IsADirectoryError:
        return "Path is a directory", 400


if __name__ == '__main__':
    app.run(debug=True)