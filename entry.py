from navis_map_hack.app import get_app

def main():
    get_app().run_server() #Must be at the top-level otherwise it crashes :(, Also `debug=True` breaks it
