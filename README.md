
# Quine McCluskey Circuit Minimizer

A CLI/GUI tool for minimizing sum of products via the Quine McCluskey minimization technique. 


## Usage
Run the circuit minimizer with the minterms
```python
    python quine_mccluskey.py minterms
```
Example
```python
    python quine_mccluskey.py 1,2,3,5,6,7,9,13,15
```
You can also use these optional arguments according to your needs: **-d**,**--dont_cares**  and **-v**,**--variables** 

Example
```python
    python quine_mccluskey.py 1,2,3,5,6,7,9,13,15 -d 0,8,12 -v a,b,c,d
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

### Todos

 - Allow display of steps that lead to solution 
 - Implement GUI component

##References

License
----

MIT

