# Youtube Basic API

### This is a basic API that allows to search queries for a specific topic with following functionalities : 

1. GET complete list of queries required in tabulated manner.
2. Search Videos based on description and title queries.
3. Tables are updated every 20 seconds using Threading Technique


## Installation 
1. Install any suitable version of python.Python Version 3.8.3 is recommended. Also , ensure that pip is also installed along with it.

2. Run following commands in the same directory as <b>manage.py</b>
(For Windows python keyword may be replaced by py)

<br>

```
pip install < requirements.txt
python manage.py makemigrations
python manage.py migrate
```

3. Set the parameters <b>query</b> and <b>key</b> in the <b>key_query.py</b> file which is inside the API Directory
<ul>
<li>query - Any Query which is to be searched.</li>
<li>key - Key Provided for Youtube V3 API using Google Cloud Console.</li>
</ul>


## Usage 
This API has two basic functionalities : 

1. View List of Videos in paginated format:
Send a <b>GET</b> Request to url: http://localhost:8000/api/videolist/
 without any params.

2. Search for Videos based on a specific query

Send a <b>GET</b> Request to url : 
http://localhost:8000/api/query with no params but body(in JSON format) as follows : 

To search using Title
```
{
    "title" : "Your_title_here"
}
```

To search using description
```
{
    "description" : "Your_description_here" 
}
```

