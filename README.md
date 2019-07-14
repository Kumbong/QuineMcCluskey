![](https://img.shields.io/github/release/Kumbong/quine_mccluskey.svg)
 ![](https://img.shields.io/github/issues/Kumbong/quine_mccluskey.svg)
![](https://img.shields.io/github/issues-closed-raw/Kumbong/quine_mccluskey.svg)
![](https://travis-ci.org/Kumbong/quine_mccluskey.svg?branch=master)
[![Requirements Status](https://requires.io/github/Kumbong/quine_mccluskey/requirements.svg?branch=master)](https://requires.io/github/Kumbong/quine_mccluskey/requirements/?branch=master)
![](https://img.shields.io/snyk/vulnerabilities/github/Kumbong/quine_mccluskey.svg)
![](https://img.shields.io/github/languages/top/kumbong/quine_mccluskey.svg)
![](https://img.shields.io/codefactor/grade/github/kumbong/quine_mccluskey/master.svg)



# Quine McCluskey Circuit Minimizer

A robust :hammer:, insanely fast :zap: and stupidly easy to use :sleeping: CLI tool for minimizing sum of products via the Quine Mccluskey minimization technique.

## Features :gem:
   * Written in uncomplicated python :innocent:
   * Supports don't cares and variables for representing expression
   * Display of all steps leading to solution :droplet:
   * Works on Mac, Linux and Windows
   * Provides all other alternative solutions to the minimization problem
   
## Installation :package:
1. Clone the repo
```bash
   git clone https://github.com/Kumbong/quine_mccluskey.git
   cd quine_mccluskey
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```

## Usage :computer:
You can use the following optional arguments according to your needs: 

   * `-d`, `--dcares` (list of numbers): **list of dont't cares (default=[ ])**
   * `-v`, `--variables` (list of chars): **list of characters for representing result (default = [ ])**
   * `-s`, `--show_steps` (yes|no): **show steps leading to solution (default=yes)**
   
Example
```bash
    python -m qmccluskey 0,1,3,7,8,9,11,15 -d 12  -v a,b,c,d
```

## Demo :movie_camera:
   Solution for the the Example above
   
   ![](assets/images/grouping.png)
   ![](assets/images/combining.png)
   ![](assets/images/coverage.png)
   ![](assets/images/solution.png)
   
## Contributing :gift: [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## References :book:
* Petrick's method 
    https://en.wikipedia.org/wiki/Petrick%27s_method
* quine mccluskey also in python
    https://github.com/tpircher/quine-mccluskey
* readme.md
    https://github.com/karan/joe

## Todos :pencil:
 - Automate build
 - Improve code quality to A+
 - Complete GUI module
 - Write tests
 - Include steps for petrick's method


License :key:
----

MIT &copy; Kumbong Hermann

