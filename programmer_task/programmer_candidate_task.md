# Coding task for developers at SAGA Diagnostics

We are pleased that you are considering SAGA Diagnostics as a potential future employer. Below you will find description of the task and instructions on how to submit the result.

## Objective

The task is to develop web application in Python using Flask framework with one API endpoint and one view and ideally deploy the app on any cloud-services provider (or at least provide docker image for it). The application should accept a text file in a specific format, extract information from the file, add selected entries to internal storage/DB and then show the entries on the view page.


## Specifications
### API endpoint

The application API end-point should be accessible at `yyyy.xxx:pppp/api` (where `yyy.xxx` is IP/hostname/localhost and `pppp` is a port) and it should accept POST requests for uploading a text file. So it is possible to upload `example.bedpe` file via command:

```
curl yyyy.xxx:pppp/api -H "Content-Type: text/xml" --data-binary "@example.bedpe"

curl http://127.0.0.1:5000/api -H "Content-Type: text/xml" --data-binary "file=@example.bedpe"
curl http://127.0.0.1:5000/api -H "Content-Type: text/xml" --data-binary "@example.bedpe"
```


### Backend
* check that file conforms to specifications:
    - tab delimited
    - has #chrom1, start1, end1, chrom2, end2, sample, score columns
* get only top 10 lines per sample (with highest score) and save to a database.
* database should only contain 10 lines per unique sample, if a file with new lines for the sample is uploaded the previous entries should be overwritten.
This also can be achieved by importing all the lines into the database and then outputting only latest top 10 entries per sample in the view.
* database implementation can be anything (SQLite is enough).


### Frontend

* one view accessible at `yyyy.xxx:pppp/view` address, which shows top 10 (based on highest score) lines per unique sample.
* table should be sortable for `sample` and score `column`


### Optional

* add one or more tests
* add authentication to the app


## Deployment and submission

* app source code should be saved in a private repository and shared with Robert (robert.rigo@sagadiagnostics.com) Justin (justin.lanier@sagadiagnositcs.com)and Henrik (henrik.petersson@sagadiagnostics.com).
* the functional app should be containerized and ideally deployed to any of the cloud service providers (AWS, Azure, GoogleCloud) and IP/hostname to access the app shared with Robert and Henrik.
* in case the above is not possible container image is enough or detailed instructions on how to create one should be provided in the repository's README.md.
* instructions should also include how to make a POST request to the app (ideally with curl, and especially if authentication was added)

## Final notes

Feel free to add any other features or improvements to this small app, and leave as many comments as you think is appropriate to communicate your choices of design.

Good luck and have fun solving this non-trivial task!
