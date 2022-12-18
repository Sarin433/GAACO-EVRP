# GAACO-EVRP

# Genetic Algorithm(GA) and Ant Colony Optimization(ACO) to solve vehicle routing problem \*(for my interest)

## How to run GA

```bash
python ga.py
```

Change input data path

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
    python ga.py --mute_prob {mutation_rate:float}
```

Change Iterations

```bash
    python ga.py --iterations {number_of_iterations:int}
```

Example

- path: .\data\json\homberger_200_customer_instances\c1_2_1.json
- population size: 1000
- mutation rate: 0.4
- iterations: 1000

```bash
    python ga.py --input_path .\data\json\homberger_200_customer_instances\c1_2_1.json --pop_size 1000 --mute_prob 0.4 --iterations 1000
```

## Development Stage:

- [x] Simple GA
- [x] Data Transformation (from text to JSON)
- [ ] Ant Colony Optimization (ACO)
- [ ] Combine GA and ACO
- [ ] E-VRP Data Transformation (from text to JSON)

## Reference

- input data, ordered crossover, plotting route codes are borrowed from here. thanks for your work.👍

https://github.com/krishna-praveen/Capacitated-Vehicle-Routing-Problem#assumptions

https://github.com/Henryy-rs/GA-VRP.git

- Crossover in Genetic Algorithm

https://www.geeksforgeeks.org/crossover-in-genetic-algorithm/
