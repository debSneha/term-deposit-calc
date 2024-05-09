# Term Deposit Calculator

### Running the code

##### Requirements
- python version 3
- pip

##### Setup
- create a virtual environment
```
    python -m venv env
```
- activate virtual environment
```
    source env/bin/activate
``` 
- install requirements 
```
    cd termDeposit
    pip install -r requirements.txt
```
- run server
```
    python manage.py runserver
```

Hosting URL -  http://127.0.0.1:8000/calculator

### Assumptions

All the calculations are done assuming that term deposit calculations for interest paid monthly, annually and quarterly use the compounding interest formula : 

$$
 A = P(1 + \frac {r}{n})^{nt} 
$$

and use simple interest formula for interest paid at maturity: 

$$
 A = P.R.T
$$

### Design decisions

- The project follows a simple MVT structure separating concerns into distinct components 

- The view 'TermDepositCalculator' leverages the FormView base class to simplify form handling

- The model TermDeposit model is kept simple with essential fields to represent a term deposit. Additional fields and methods can be added as needed for the specific functionality and extending the application.

