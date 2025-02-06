# Credit
A CS application the ensure that creditcards is valid. Using Luhn alogrithm.

The application was implemented as a optional assignment at xCS50
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.<br>
A demo of the application can be watched at [CS50 HomePage](https://cs50.harvard.edu/x/2024/psets/6/credit/)

## Installation
1. Clone the repository:
```sh
#  Using HTTPS
git clone https://github.com/krigjo25/console-credit-py.git

##  Using SSH
ssh git@github.com:krigjo25/console-credit-py.git

#  Using Github CLI
gh repo clone console-credit-py.git
```

2. Navigate to the project directory
```sh
cd console-Credit-py
```

3. Run the file
```sh
python app.py
```

##  Usage
To use the application, run the following command in your terminal

```sh
Usage : type in the terminal python app.py, wait for the prompted message
then type in some numbers.
python app.py
```

## Example
```sh
python app.py

Credit Card Number : <1234567890>

expected output:
Invalid
```
Replace `<1234567890>` with the desired desired number, to authenticate the number as valid or Invalid

##  Testing framework / Testing data
By using pytest to test the datasets below you'll get the desired result. Due to the modulo algorithm, and IIN Number.
Results can be watched in [Index.html](tests/index.html)

| AMEX  | MASTERCARD  | VISA  | INVALID  | |
|---|---|---|---|---|
| 378282246310005  |  5555555555554444 |  4111111111111111 |  1234567890 | 
|  71449635398431 | 5105105105105100  | 4012888888881881  |  4062901840 |
|   |   |   | 4222222222223  |
|   |   |   | 369421438430814  |
|   |   |   | 5673598276138003  |
|   |   |   | 4111111111111113  |

###  Usage
To test the application, run the following command in your terminal

```sh
Usage : type in the terminal pytest app.py
pytest -k test_app.py
pytest test_app.py
pytest --html=index.html
```

## LICENCE
The application is under [GNU General Public License v3.0](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25
