import os
import sqlite3
from flask import Flask, send_from_directory

from views.game import game_view
# from views.subjects import subjects_view

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(__file__), 
    'uploads'
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(game_view)
# to download images from the server
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

# @app.route('/api/resource', methods=['GET'])
# def get_resource():
#      # Code to get a specific resource
#      return jsonify({'message': 'Get resource'})
 
# @app.route('/api/resource', methods=['POST'])
# def create_resource():
#          # Code to create a new resource
#     return jsonify({'message': 'Create resource'})

app.secret_key = 'your_secret_key_here'

# A route to test debugger pin functionality
# @app.route('/debugger')
# def debugger_test():
#     # Intentional error to trigger the debugger PIN
#     x = 1 / 0
#     return 'Debugger PIN test'

if __name__ == '__main__':
    app.run(debug=True)