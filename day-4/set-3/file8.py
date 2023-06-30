def countWords(inputFile, outputFile):
    try:
        with open(inputFile, 'r') as file:
            content = file.read()
            wordCount = len(content.split())

        with open(outputFile, 'w') as file:
            file.write(f"Number of words: {wordCount}")

        print(f"Number of words: {wordCount}")
        print(f"Result has been written to {outputFile}.")

    except FileNotFoundError:
        print(f"File '{inputFile}' not found.")



inputFile = "input.txt"
outputFile = "output.txt"
countWords(inputFile, outputFile)
