# find-OS
You can control  which OS  is running?  and which you prefer?  just with one code 


## How we can use?
(Example)

### findOS.get()
```python
import findOS

print(findOS.get())

```
>console: MacOS 


```python
import findOS

print(findOS.get(1,1))

```
>console: MacOS19.6.0

### findOS.control("OS")
```python
import findOS

print(findOS.control("macos"))

```
>console: True

```python
import findOS

print(findOS.control("linux"))

```
![False](false.png)

```python
import findOS

print(findOS.control("macos18.06"))

```

![False](falsewithversion.png)
