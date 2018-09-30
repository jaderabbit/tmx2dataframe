# tmx2dataframe

A python package to convert a tmx translation file into a pandas dataframe. Please note that this is very early stages and is certainly not ready for production use.


## Getting Started

### Prerequisites

Python 3

### Installing

Package can be installed using pip.

```
pip install tmx2dataframe
```

## Usage

```
import tmx2dataframe

metadata, df = tmx2dataframe.read("/path/to/tmxfile.tmx")
```

## Running the tests

We use pytest for our tests.
```
pip install pytest
cd navigate/to/project/folder
pytest
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/jaderabbit/tmx2dataframe/tags). 

## Authors

* **Jade Abbott** - *Initial work* - [jaderabbit](https://github.com/jaderabbit)

See also the list of [contributors](https://github.com/jaderabbit/tmx2dataframe/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
