import grammar_check

def do_something(val):
    tool = grammar_check.LanguageTool('en-GB')
	texts = val
	matches = tool.check(texts)
	return grammar_check.correct(texts,matches)

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = do_something(arg)