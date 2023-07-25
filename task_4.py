def decorator_json(func):
    import json
    import os

    if os.path.exists(f"/{func.__name__}.json"):
        with open(f"{func.__name__}.json", "r", encoding="UTF-8") as file:
            result_list = file.readlines()
    else:
        result_list = []

    file_name = func.__name__
    
    def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        res_dict = {"args": args,
                    "kwargs": kwargs,
                    "result": result}
        
        result_list.append(res_dict)

        with open(f"{file_name}.json", "w", encoding="UTF-8") as file:
            json.dump(result_list, file)

        return result
    return _wrapper