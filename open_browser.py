import webbrowser

def open_new_tab(url):
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    url = "http://localhost:8888/"
    open_new_tab(url)
    # Add your JavaScript code here
    javascript_code = "alert('Hey')"
    webbrowser.execute_script(javascript_code)
