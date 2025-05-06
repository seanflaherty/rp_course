class SomeClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # Code to customize the instance here.
        return instance
