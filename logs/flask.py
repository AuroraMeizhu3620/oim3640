#URL customization in Flask

@app.route('/new') # when someone visits /new, routes
def upload(): # run this function
    return 'Upload page'

#Create a pattern for each route