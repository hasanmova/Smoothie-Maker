# Smoothie Maker

This tool was developed as an entry for the Diginext contest, allowing users to create and customize smoothie recipes based on available ingredients.


## Features

- **Predefined Smoothie Recipes:** Offers a selection of classic smoothie recipes with specific ingredients.
- **Customization Options:** Enables users to modify existing recipes by adding or removing ingredients.
- **Ingredient Management:** Provides functionality to handle ingredients efficiently.



## Predefined Smoothie Recipes

| Smoothie Name   | Ingredients                                           |
|-----------------|-------------------------------------------------------|
| Classic         | strawberry, banana, pineapple, mango, peach, honey, ice, yogurt |
| Forest Berry    | strawberry, raspberry, blueberry, honey, ice, yogurt |
| Freezie         | blackberry, blueberry, black currant, grape juice, frozen yogurt |
| Greenie         | green apple, kiwi, lime, avocado, spinach, ice, apple juice |
| Vegan Delite    | strawberry, passion fruit, pineapple, mango, peach, ice, soy milk |
| Just Desserts   | banana, ice cream, chocolate, peanut, cherry         |



## Usage

The program accepts input in the following format:


SmoothieName,[+ingredient1,-ingredient2,...]


- **SmoothieName:** The name of the predefined smoothie (e.g., `Classic`).
- **+ingredient:** Ingredient to add to the smoothie.
- **-ingredient:** Ingredient to remove from the smoothie.

**Examples:**

| Input                          | Expected Output                                      |
|--------------------------------|------------------------------------------------------|
| `Classic`                      | banana, honey, ice, mango, peach, pineapple, strawberry, yogurt |
| `Classic,-mango`               | banana, honey, ice, peach, pineapple, strawberry, yogurt |
| `Just Desserts`                | banana, cherry, chocolate, ice cream, peanut         |
| `Just Desserts,-ice cream`     | banana, cherry, chocolate, peanut                    |
| `Just Desserts,-ice cream,-banana,+peach` | cherry, chocolate, peach, peanut          |
| `Vegan Delite,+ice cream,-ice` | strawberry, passion fruit, pineapple, mango, peach, soy milk, ice cream |

---

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hasanmova/Smoothie-Maker.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Smoothie-Maker
   ```

3. **Run the Program:**

   ```bash
   python smoothie_maker.py
   ```



## Requirements

- **Python 3.x**



## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

For any questions or suggestions, feel free to open an issue or contact me directly.

