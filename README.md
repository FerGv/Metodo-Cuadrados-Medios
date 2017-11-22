# random-numbers
Methods to generate random numbers.

### `middle_square(seed, numbers)`
  - **seed** -- type: string => Seed to generate random numbers
  - **numbers** -- type: int => Numbers to generate

  Return a list.
  
### `mixed_congruential(initial_seed, multiplicative_constant, additive_constant, module)`
  - **initial_seed** -- type: float => Initial seed to generate random numbers
  - **multiplicative_constant** -- type: float => Number to multiply by the seed
  - **additive_constant** -- type: float => Number to add to the seed
  - **module** -- type: float

  Return a list.

### `montecarlo(frequencies, numbers)`
  - **frequencies** -- type: list => [(value_1, frequency_1), ..., (value_n, frequency_n)]
  - **numbers** -- type: list => [number_1, ..., number_n]

  Return a list.
   
### `normal_distribution(mean, deviation, numbers)`
  - **mean** -- type: float => Mean of distribution
  - **deviation** -- type: float => Standard deviation of distribution
  - **numbers** -- type: int => Numbers to generate

  Return a list.
