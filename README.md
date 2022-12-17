# GAACO-EVRP

# Genetic Algorithm(GA) and Ant Colony Optimization(ACO) to solve vehicle routing problem \*(for my interest)

## How to run GA

```bash
python ga.py
```

Change Path of input data

```bash
    python ga.py --input_path {path_of_data}
example
    python ga.py --input_path .\data\json\homberger_{nodes}_customer_instances\
```

Change Population Size

```bash
    python ga.py --pop_size {number_of_population:int}
```

Change Mutation rate

```bash
    python ga.py --mute_pop {mutation_rate:float}
```

Change Iterations

```bash
    python ga.py --iterations {number_of_iterations:int}
```

Development Stage:

- [x] Simple GA
- [x] Data Transformation (from text to JSON)
- [ ] Ant Colony Optimization (ACO)
- [ ] Combine GA and ACO
- [ ] E-VRP Data Transformation (from text to JSON)

## Reference

- input data, ordered crossover, plotting route codes are borrowed from here. thanks for your work.👍

https://github.com/krishna-praveen/Capacitated-Vehicle-Routing-Problem#assumptions
https://github.com/Henryy-rs/GA-VRP.git
