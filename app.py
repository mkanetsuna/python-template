from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)

reload_needed = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reload')
def reload():
    global reload_needed
    return jsonify(reload=reload_needed)

def set_reload_flag():
    global reload_needed
    reload_needed = True

def clear_reload_flag():
    global reload_needed
    reload_needed = False

if __name__ == '__main__':
    from watcher import start_watcher
    watcher_thread = threading.Thread(target=start_watcher, args=(set_reload_flag,))
    watcher_thread.daemon = True
    watcher_thread.start()
    app.run(debug=True, use_reloader=False)
