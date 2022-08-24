from website import create_app # Importing the package file and using that info to run the app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

