def genetic_algorithm()
    # Initialize population
    population = initialize_population()

    # Evaluate population
    evaluate_population(population)

    # Sort population
    sort_population(population)

    # While termination condition is not met
    while termination_condition_is_not_met():
        # Select parents
        parents = select_parents(population)

        # Apply crossover / mutation operators
        offspring = crossover(parents)
        mutate(offspring)

        # Evaluate offspring
        evaluate_population(offspring)

        # Select survivors
        population = select_survivors(population, offspring)

        # Sort population
        sort_population(population)

    # Return best individual in population
    
# fitness = accuracy of the model 