def install():
    import os
    try:
        import requests
    except ImportError:
        os.system("pip install requests")
    try:
        import colorama
    except ImportError:
        os.system("pip install colorama")
    try:
            import re
    except ImportError:
        os.system("pip install re")