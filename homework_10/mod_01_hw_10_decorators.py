def input_error(func):
    
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
            
        except IndexError:
            return "Not enough parameters"
            
        except KeyError:
            return "Contact doesn't exist"
            
    return inner