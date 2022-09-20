from executive import Executive

def main():
    file_name = "gibbons-collection.tsv"
    my_exec =  Executive(file_name)
    my_exec.run()
    
if __name__ == "__main__":
    main()