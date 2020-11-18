# Queue simulation

The goal of this project is to simulate M/M/S/S queuing model [(Erlang B)](https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_B_formula) and construct the blocking probability table. 



## Environment

- Python 3.6



## Usage

```
$ python src.py
```



## Policy

- Generate 100000 customers, both arrival time and service time follow the [Poisson distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
- Blocking probability = number of blocking / number of arrival



## Result

| Erlang ($\lambda / \mu$) | blocking prob. (S = 1) | blocking prob. (S = 5) | blocking prob. (S = 10) |
| ------------------------ | ---------------------- | ---------------------- | ----------------------- |
| 1.0000                   | 0.5012                 | 0.0031                 | 0.0000                  |
| 0.2500                   | 0.1998                 | 0.0000                 | 0.0000                  |
| 0.0625                   | 0.0590                 | 0.0000                 | 0.0000                  |
| 0.0156                   | 0.0154                 | 0.0000                 | 0.0000                  |
| 0.0039                   | 0.0039                 | 0.0000                 | 0.0000                  |
| 0.0010                   | 0.0010                 | 0.0000                 | 0.0000                  |
| 10.0000                  | 0.9093                 | 0.5640                 | 0.2150                  |
| 2.5000                   | 0.7136                 | 0.0696                 | 0.0002                  |
| 0.6250                   | 0.3846                 | 0.0004                 | 0.0000                  |
| 0.1562                   | 0.1352                 | 0.0000                 | 0.0000                  |
| 0.0391                   | 0.0373                 | 0.0000                 | 0.0000                  |
| 0.0098                   | 0.0096                 | 0.0000                 | 0.0000                  |
| 100.0000                 | 0.9900                 | 0.9505                 | 0.9006                  |
| 25.0000                  | 0.9617                 | 0.8084                 | 0.6218                  |
| 6.2500                   | 0.8615                 | 0.3775                 | 0.0505                  |
| 1.5625                   | 0.6096                 | 0.0164                 | 0.0000                  |
| 0.3906                   | 0.2812                 | 0.0001                 | 0.0000                  |
| 0.0977                   | 0.0891                 | 0.0000                 | 0.0000                  |
| 1000.0000                | 0.9990                 | 0.9950                 | 0.9897                  |
| 250.0000                 | 0.9960                 | 0.9799                 | 0.9597                  |
| 62.5000                  | 0.9844                 | 0.9212                 | 0.8431                  |
| 15.6250                  | 0.9397                 | 0.7045                 | 0.4279                  |
| 3.9062                   | 0.7963                 | 0.1914                 | 0.0047                  |
| 0.9766                   | 0.4935                 | 0.0028                 | 0.0000                  |

