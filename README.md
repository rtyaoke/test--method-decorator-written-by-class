# memo

This is my learning code for developing a python decorator having some features like this ↓.

## features

- having globally-shared-property

```python

@call_count_decorator
def methodA():
    pass

@call_count_decorator
def methodB():
    pass

methodA()
methodB()

print(call_count_decorator.call_count) # keeping total call count

```

- can be used before class method line.

```python
class C:
    @sample_decorator
    def method(self):
        pass
```
