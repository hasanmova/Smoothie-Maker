# Smoothie-Maker
I created this tool to participate in the diginext entry contest

list of all data : 

| Smoothie Name |	Ingredients |
|----------------|-------------|
| Classic	| strawberry, banana, pineapple, mango, peach, honey, ice, yogurt |
| Forest Berry | strawberry, raspberry, blueberry, honey, ice, yogurt |
| Freezie	| blackberry , blueberry, black currant, grape juice, frozen yogurt |
| Greenie |	green apple, kiwi, lime, avocado, spinach, ice, apple juice |
| Vegan Delite |	strawberry, passion fruit, pineapple, mango, peach, ice, soy milk |
| Just Desserts |	banana, ice cream, chocolate, peanut, cherry |

list of Input and execute on STDOUT : 

| Input	| Expected Output|
|-------|----------------|
| Classic |	banana, honey, ice, mango, peach, pineapple, strawberry, yogurt |
| Classic,-mango |	banana, honey, ice, peach, pineapple, strawberry, yogurt
| Just Desserts |	banana, cherry, chocolate, ice cream, peanut|
| Just Desserts,-ice cream |	banana, cherry, chocolate, peanut|
| Just Desserts,-ice cream,-banana,+peach |	cherry, chocolate, peach, peanut|
| Vegan Delite,+ice cream,-ice |	strawberry, passion fruit, pineapple, mango, peach, soy milk, ice cream|
| Greenie,-apple juice |	green apple, kiwi, lime, avocado, spinach, ice|
| Freezie,+apple juice |	blackberry, blueberry, black currant, grape juice, frozen yogurt, apple juice|
| Forest Berry |	strawberry, raspberry, blueberry, honey, ice, yogurt|

**Through several files, I tried to improve the functionality of the code in Python.**
