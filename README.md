# Puzzle [![Build Status][travis-image]][travis-url] [![Test Coverage][coveralls-img]][coveralls-url]

Variant Caller GUI and genetic disease analysis tool.

```bash
$ git clone https://github.com/robinandeer/puzzle.git
$ cd puzzle
$ pip install --editable .
$ puzzle view tests/fixtures/
# open webbrowser on port 5000
$ open http://localhost:5000
```

## Using Puzzle
Puzzle will look for variant calling resources such as VCF files and [GEMINI][gemini] databases and visualize their content. It lets you inspect, annotate, and analyze variant calls.

Puzzle is not primarily meant to be run as a persistant server but think of it more as an webinterface to quickly spin to visualize your variant calls.

We set out to make `Puzzle` both very simple to install as well as intuitive to use. You can be up and running in minutes with minimal prerequisites.

## Developing Puzzle
Puzzle is a Python Flask app with a command line interface. It can work with multiple backends using plugins; raw VCFs, GEMINI, MongoDB.

Anyone can help make this project better - read [CONTRIBUTING](CONTRIBUTING.md) to get started!

### Install for development
I decided to try out [Otto][otto] for this project so make sure you have it installed :smile:

```bash
$ git clone https://github.com/robinandeer/puzzle.git
$ cd puzzle
$ otto dev
$ otto dev ssh
> npm install
> sudo apt-get install vim python-pip git
> pip install --user --editable .
> puzzle /vagrant/tests/
# open webbrowser on port 5000
```

## Testing Puzzle
To run the tests, you need [pytest](pytest) installed in your system. You can install `pytest` together
with the other development libraries by running `pip install -r requirements-dev.txt`.

You will also need to download the database used for testing, which you can do by executing this command:

```
wget https://s3-us-west-2.amazonaws.com/robinandeer/HapMapFew.db -O tests/fixtures/HapMapFew.db
```

Then, just run `py.test tests/`

## Use a gemini database ##

Make sure you have gemini installed in your local environment

```
puzzle --mode gemini view -i path/to/gemini_database.db
```

## Use ped info ##

Puzzle uses the ped file to show more information in family view and in variant calls:

```
puzzle view -i tests/fixtures/hapmap.vcf --family_file/-f tests/fixtures/hapmap.vcf
```

## Credits
Puzzle Piece by Creative Stall from the Noun Project

## License
MIT. See the [LICENSE](LICENSE) file for more details.


[travis-url]: https://travis-ci.org/robinandeer/puzzle?branch=master
[travis-image]: https://img.shields.io/travis/robinandeer/puzzle/master.svg?style=flat-square
[coveralls-url]: https://coveralls.io/github/robinandeer/puzzle
[coveralls-img]: https://img.shields.io/coveralls/robinandeer/puzzle.svg?style=flat-square
[otto]: https://ottoproject.io/
[gemini]: https://github.com/arq5x/gemini
[pytest]: http://pytest.org/latest/
