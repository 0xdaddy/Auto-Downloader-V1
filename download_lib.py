def install():
    import os
    try:
        import requests
    except ImportError:
        os.system("pip install requests")