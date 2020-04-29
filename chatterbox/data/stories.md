## very happy path
* greet
  - utter_greet
* pizzas
  - utter_pizzas
* prices
  - utter_prices
* drinks
  - utter_drinks
* promotions
  - utter_promotions
* request
  - sales_pizza
  - form{"name": "sales_pizza"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path
* greet
  - utter_greet
* request
  - sales_pizza
  - form{"name": "sales_pizza"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## unhappy path pizza
* request
  - sales_pizza
  - form{"name": "sales_pizza"}
* deny
  - utter_pizzas
  - sales_pizza
  - form{"name": null}


## unhappy path drink
* request
  - sales_pizza
  - form{"name": "sales_pizza"}
* deny
  - utter_drinks
  - sales_pizza
  - form{"name": null}
 

## unhappy path pizza and drink
* request
  - sales_pizza
  - form{"name": "sales_pizza"}
* deny
  - utter_pizzas
  - sales_pizza
  - form{"name": "sales_pizza"}
* deny 
  - utter_drinks
  - sales_pizza
  - form{"name": null}
 

## very unhappy path 
* greet
  - utter_greet
* chichat 
  - utter_chichat
* request
   - sales_pizza
   - form{"name": "sales_pizza"}
   - form{"name": null}
 
* challenge 
  - utter_challenge
* goodbye
  - utter_goodbye


## challenge path 
* greet
  - utter_greet
* request
  - sales_pizza
  - form{"name":"sales_pizza"}
* challenge 
  - utter_challenge
  - sales_pizza
  - form{"name": null}
 
* goodbye
  - utter_goodbye

## chichat path
* chichat
  - utter_chichat
  