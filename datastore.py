class DataStore:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'data_source'):
            self.data_source = {}

    def get(self, key):
        return self.data_source.get(key, None)

    def set(self, key, value):
        self.data_source[key] = value