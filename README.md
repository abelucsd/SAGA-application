# Sample App

### Instructions 
Access through http://3.16.11.28:5000/

Use the default command for a post:
curl http://3.16.11.28:5000/api -H "Content-Type: text/xml" --data-binary "@example.bedpe"

Display the table view at:
http://3.16.11.28:5000/view

### Design

#### Models

I chose to create a Sample object because each data entry is a sample entity. All of the fields are required. From observing the sample file, the score of each sample should be within the range 0 to 10.

#### Post

- Chose to return json messages in case it is required to pass them in json format.
- Receives a sample data file and inserts only the top 10 of each sample into the database
- Fail checks:
    - Check if there is a file input.
    - The file is checked to have the correct format.
    - The data is checked to be tab delimited.
    - Check the data if it has the required column attributes.

#### Get

- Renders json sample data into template.

#### Testing

- test_routes.py
    - Home page:
        - status code
    - View page:
        - status code
- test_api.py
    - api get endpoint:
        - response.get_json() — matches recently posted data
        - status code
    - api post endpoint:
        - Uses various sample data to post into the api.
        - response.get_json() — matches posted data
        - status code
- test_sample.py
    - Sample creation
    - All Sample fields
    - Sample score:
        - Assertion Error message
    - Sample score within range 0 to 10
        - Assertion Error message
>>>>>>> 3fcca8140861a0903eeb3f7db1f629787bacc22c
