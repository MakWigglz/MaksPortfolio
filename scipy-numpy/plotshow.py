import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # Creates 100 evenly spaced numbers between 0 and 10
y = np.sin(x)  # Applies the sine function

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

``` 
    (new-matplot-venv) amakki@As-MacBook-Pro scipy-folder % python
Python 3.13.3 | packaged by conda-forge | (main, Apr 14 2025, 20:46:04) [Clang 18.1.8 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> arr = np.array([1, 2, 3, 4, 5])
>>> print(arr)
[1 2 3 4 5]
>>> import matplotlib.pyplot as plt
>>> x = np.linspace(0, 10, 100)
>>> y = np.sin(x)
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x121df6c10>]
>>> plt.title("Sine Wave by Mak the Coder")
Text(0.5, 1.0, 'Sine Wave by Mak the Coder')
>>> plt.xlabel("x values")
Text(0.5, 47.04444444444444, 'x values')
>>> plt.ylabel("y values, bitch")
Text(44.19444444444443, 0.5, 'y values, bitch')
>>> plt.show()


   ```
