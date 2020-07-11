# Barbox V3 - CLI

## Installation

```
cd cli/
pip install -r requirements.txt
```

## Usage of the CLI

The barbox CLI permit to manipulate the different pumps of the system in only one command:

`python3 barbox.py --pump <pump_number> <pump_duration>`  

the following command will open the pump 3 during 12 seconds and the pump 1 during 2 secondes:

`python3 barbox.py --pump 3 12 --pump 1 2` 

### Real example

Given the following configuration:

|  Relai    | Boisson               |
|---        |---                    |
| 1         | Vodka                 |
| 2         | Rhum Blanc            |
| 3         | Curaçao Bleu          |
| 4         | Schnaps à la pêche    |
| 5         | Jus d'orange          |
| 6         | Limonade              |
| 7         | Jus de Cranberry      |
| 8         | Jus de Pamplemousse   |

Bluelagoon:

`python3 barbox.py --pump 1 30 --pump 3 30 --pump 3 120` 

Cape cod:

`python3 barbox.py --pump 2 40 --pump 7 160` 

Fuzzy navel:

`python3 barbox.py --pump 4 50 --pump 5 100` 

Gray hound:

`python3 barbox.py --pump 2 50 --pump 8 200` 

Hair Navel:

`python3 barbox.py --pump 1 30 --pump 4 50 --pump 5 70` 

Srewdriver:

`python3 barbox.py --pump 2 50 --pump 5 170` 

Sea Breeze:

`python3 barbox.py --pump 2 40 --pump 7 160 --pump 8 190` 

Sex on the beach:

`python3 barbox.py --pump 1 40 --pump 4 20 --pump 5 40 --pump 7 40 ` 

Woowoo:

`python3 barbox.py --pump 1 60 --pump 4 30 --pump 7 120` 

## Features

- [x] Start / Stop pump
- [ ] Interact with led
- [ ] Detect glass