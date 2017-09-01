def returnVerifier(f):
    def inner(*args, **kwargs):
        keys = [
                "question_index", 
                "question_name", 
                "problem_statement", 
                "correct_answer", 
                "solution",
               ]
        s_keys = set(keys)
        ret = f(*args, **kwargs)
        if(s_keys != set(ret.keys())):
            print(f()["question_name"])
        assert( set(ret.keys()) == s_keys )
        return ret
    return inner
