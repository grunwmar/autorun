from python_autorun import autorun, src


@autorun(var_source=[src.ENV, src.JSON, src.ARGS], json_filename='sample.json')
def main(HELLO_WORLD, hello_world_cs, name):
    """Prints Hello World! ..."""
    
    print(HELLO_WORLD)
    print(hello_world_cs)
    print(name)
