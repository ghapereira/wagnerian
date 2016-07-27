# wagnerian
Simple Google Maps [Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/) project

This project aims to find the better path for traveling salesmen by using Google Distance API. Since finding
shortest Hamiltonian Paths is a classic problem, we'll use NetworkX instead of implementing our own solution.
The objective here is to test the API most than anything.

## Requirements

The requirements for the Virtualenv were saved as stated [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/#other-notes).
To use them, you need to use [the following command](http://stackoverflow.com/questions/7225900/how-to-pip-install-packages-according-to-requirements-txt-from-a-local-directory):

```
pip install -r requirements.txt
```

## API key
You need to [obtain an API key from Google](https://developers.google.com/maps/documentation/distance-matrix/get-api-key)
and then put it into a JSON file named confs.json with the following structure:
```
{
  "apidata":{
      "apikey": "AIzaXXXXXX"
    }
}
```

